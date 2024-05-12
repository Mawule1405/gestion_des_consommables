import customtkinter as ctk
from tkinter import  messagebox
import tkinter as tk
from PIL import Image
import shutil, re


import setting as set
import graphi_print as gp
import un_fournisseur as unfr


def ajouter(framescrol, page, zone, liste_de_entry):
    """
    Procéduire d'ajout d'un service 
    @param: framescoll (zone des widget), page (fonction de reconstruction), zone (la zane à reconstruire)n dictionnaire des champs de saisis
    @return None
    """

   
   
    nom_fourn = liste_de_entry[0].get(); nom_fourn_val = False
    adresse_fourn= liste_de_entry[1].get(); adresse_fourn_val = False
    contact_fourn = liste_de_entry[2].get(); contact_fourn_val = False
    
  
    #Verification du nom
    if nom_fourn != "":
        nom_fourn_val = True
        liste_de_entry[0].configure(border_color = set.col_noir_1)
    else:
        nom_fourn_val = False
        liste_de_entry[0].configure(border_color = "red")
    

    #Verification du prix unitaire
    if adresse_fourn:
        adresse_fourn_val = True
        liste_de_entry[1].configure(border_color= set.col_noir_1)
    else:
        adresse_fourn_val = False
        liste_de_entry[1].configure(border_color= "red")
    
    
    #Verification de la telephone
    regrex1 = r"^(?:\+|00)[0-9]{11,}"

    if re.search(regrex1, contact_fourn):
        contact_fourn_val= True
        liste_de_entry[2].configure(border_color = set.col_noir_1)
    else:
        contact_fourn_val= False
        liste_de_entry[2].configure(border_color = 'red')

    image_chemin = liste_de_entry[-1].get()
    if not image_chemin:
        image_chemin = "images/images_app/bg_page_connexion.png"

    validation = all([nom_fourn_val,adresse_fourn_val, contact_fourn_val])


    if validation:
        image_chemin = liste_de_entry[-1].get()
        fournisseur   = (nom_fourn, adresse_fourn ,contact_fourn ,image_chemin)

        answer = messagebox.askquestion("Ajout d'un nouveau fournisseur", "Validez-vous l'ajout d'un nouveau fournisseur?")
        if answer == "yes":
            reponse = gp.inserer_fournisseur(fournisseur)

            if reponse :
                framescrol.destroy()
                for el in liste_de_entry:
                    el.delete(0, tk.END)
                
                page(zone)
                messagebox.showinfo("Ajout d'un nouveau fournisseur","Le fournisseur a été bien ajouté")
                    
            else: 
                    
                messagebox.showerror("Ajout d'un nouveau fournisseur", "Echec de l'opération!")
    else:
        messagebox.showinfo("Ajout d'un nouveau fournisseur", "Valeur(s) invalide")


def deplacer_fichier(source, destination):
    """
    Procédure permettant de copier un fichier d'un dossier source vers un dossier destination
    @param: source (file), destination (direction)
    @return : None
    """
    try:
        shutil.copy(source, destination)
        
    except PermissionError:
        messagebox.showerror("Alerte", "Permission non accordée")
    


def choisir_photo(entry_photo, label_photo):
    """
        Procéduire pour choisir une image se trouvant dans le lieu du disque
        @param: entry concervant le entry, label
        @return : None 
    """
    app = ctk.CTk()
    app.withdraw()
    app.attributes('-topmost', True)
    types_de_photos=[("Images JPG","*.jpg"),("Images JPEG","*.jpeg"),("Images PNG","*.png"),]
    chemin_de_photos = ctk.filedialog.askopenfilename(title="Choisissez une photo", filetypes=types_de_photos)

    if chemin_de_photos:
        entry_photo.delete(0, tk.END)
        
        try:
            nom_image = chemin_de_photos.split('/')[-1]
            destination = "C://wamp64/www/DEV/image/image_fournisseur"
            deplacer_fichier(chemin_de_photos, destination)
            chemin_de_photos = destination+"/"+nom_image
        except:
            pass
        
        entry_photo.insert(0, chemin_de_photos)
        label_photo.configure(image = place_image(chemin_de_photos))
    
    
    app.destroy()



def place_image(chemin):
    """
    Procéduire permettant de préparer une image à placer sur l'interface. Au cas où le chemin
    n'est pas reconnu elle utilise un chemin par défaut
    @param: Chemin de l'image
    @return: photo
    """
    try:
    
        image= Image.open(chemin.replace("\\",'/'))

    except:
        image= Image.open("C:/wamp64/www/DEV/image/image_consommable/defaut.jpeg")

    photo = ctk.CTkImage(image, size=(200,230))
    return photo



def ajouter_fournisseur(framescrol, page, zone):

    toplevel = ctk.CTkToplevel()
    toplevel.geometry("800x320")
    toplevel.title("Ajout d'un nouveau fournisseur")
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.resizable(width=False, height=False)
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.attributes('-topmost', True)
    
    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(800,300))

    fond = ctk.CTkLabel(toplevel,text=0,image=image)
    fond.place(x=0, y=0)

 
    
    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(toplevel, text="Formulaire d'enrégistrement d'un fournisseur".upper(), font= ("Montsérrat",12,'bold'), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    id.place(x=250, y=5)

    image_label = ctk.CTkLabel(toplevel,text="", width=200, height=230, image = place_image("images/images_app/bg_page_connexion.png"))
    image_label.place(x=20,y=10)
    
    #Nom du produit
    nom = ctk.CTkLabel(toplevel, text='Nom :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    nom.place(x=250, y=50)
    nom_e = ctk.CTkEntry(toplevel, placeholder_text="Nom du fournisseur",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    nom_e.place(x=450, y= 50)
    

    #Prix unitaire
    adresse = ctk.CTkLabel(toplevel, text='Adresse du fournisseur :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    adresse.place(x=250, y=90)
    adresse_e = ctk.CTkEntry(toplevel, placeholder_text="Adresse",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    adresse_e.place(x=450, y= 90)
  


    #Quantité en stock du produit
    contact = ctk.CTkLabel(toplevel, text='Contact du fournisseur:', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    contact.place(x=250, y=130)
    contact_e = ctk.CTkEntry(toplevel, placeholder_text="00000000000000",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    contact_e.place(x=450, y= 130)

    #dictionnaires des éléments
    image_e = ctk.CTkEntry(toplevel)
    liste_entry = [nom_e, adresse_e, contact_e, image_e]

    changer_image = ctk.CTkButton(toplevel, text = "Changer image".upper(),width=200,height=40, command = lambda :choisir_photo(image_e, image_label)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    changer_image.place(x=20, y=250)

    
    annuler = ctk.CTkButton(toplevel, text = "Annuler",width=150, height=40,font=('Montsérrat', 15),
                                    fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=5,
                                    command = lambda: toplevel.destroy())
    annuler.place(x=250, y=230)

    

    enregistrement = ctk.CTkButton(toplevel, text = "Enrégistrer",width=150, height=40, command = lambda: ajouter(framescrol,page, zone, liste_entry),
                                  fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=5)
    enregistrement.place(x=525, y=230)



def des_fournisseurs(framescrol):
    fond_image_path =  "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(993,645))
    fond = ctk.CTkLabel(framescrol,text=0,image=image)
    fond.place(x=0, y=0)

    
    fourframe = ctk.CTkScrollableFrame(framescrol, width=800, height=500, fg_color=set.col_blanc_4, 
                         border_color=set.col_noir_1, border_width=0,corner_radius=0)
    fourframe.place(x=100, y=30)

    fourn = gp.get_fournisseurs()

    for four in fourn:

        unfr.build_fournisseur(four[0], fourframe)


    ajouter = ctk.CTkButton(framescrol, text = "Ajouter un nouveau fournisseur".upper(),width=300,height=40, 
                                  command = lambda : ajouter_fournisseur(fourframe, des_fournisseurs,framescrol)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    ajouter.place(x=600, y= 570)

    