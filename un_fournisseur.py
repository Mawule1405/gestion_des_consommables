"""
    But: construire un consommable
"""

#importation des bibliothèques de python
import customtkinter as ctk
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image
from datetime import datetime
import shutil
import os
import re

#import des modules
import graphi_print as gp
import setting as set



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
            destination = "C://wamp64/www/DEV/image/image_consommable"
            deplacer_fichier(chemin_de_photos, destination)
            chemin_de_photos = destination+"/"+nom_image
        except:
            pass
        
        entry_photo.insert(0, chemin_de_photos)
        label_photo.configure(image = place_image(chemin_de_photos))
    
    
    app.destroy()



def update_page(liste_entry):
    """
    Procéduire de mise à jour des champs après modificvtion des données dans la base de données
    @param: la liste des champs de saisie
    """
    for element in liste_entry:
        element.configure(state = tk.NORMAL)

    id= int(liste_entry[0].get())
   
    
    fourn = gp.get_one_fournisseur(id)[0]
    
    
    for  element in liste_entry:
        
        element.delete(0,tk.END)

       
    liste_entry[0].insert(0, fourn[0])
    liste_entry[1].insert(0, fourn[1])
    liste_entry[2].insert(0,fourn[2])
    liste_entry[3].insert(0,fourn[3])
    
   

    if fourn[-1]!=None:
        liste_entry[4].insert(0, fourn[-1])
    else: 
        liste_entry[4].insert(0, "images/images_app/bg_page_connexion.png")
    
    for element in liste_entry:
        element.configure(state ="disable")



def activation_des_champs(checking, liste_entry):
    """
    Procéduire d'activation des champs permettant la modification des informations du consommables
    @param: les des champs de saisi
    @return : None
    """
    valeur = checking.get()
    if valeur:
        for element in liste_entry[1:]:
            element.configure(state= tk.NORMAL)
    else:
        for element in liste_entry[1:]:
            element.configure(state= "disable")
        update_page(liste_entry)


def enregistre(liste_de_entry):
    """
        Une procédure qui permet d'enrégistrer une nouvelle consommable
        Paramètre: liste des entrys => ID, Nom, Qte S, Qte s, Prix, cat
    """
  
    nom_cons = liste_de_entry[1].get(); nom_cons_val = False
    prix_u_cons= liste_de_entry[2].get(); prix_u_cons_val = False
    qte_stock_cons = liste_de_entry[3].get(); qte_stock_cons_val = False
    qte_seuil_cons = liste_de_entry[4].get(); qte_seuil_cons_val = False
    categorie_cons = liste_de_entry[5].get().split()[0]; categorie_cons_val = False
    
    
    
    #Verification du nom
    if nom_cons != "":
        nom_cons_val = True
        liste_de_entry[1].configure(border_color = set.col_noir_1)
    else:
        nom_cons_val = False
        liste_de_entry[1].configure(border_color = set.col_rouge)
    

    #Verification du prix unitaire
    try:
        prix_u_cons = int(prix_u_cons)
        assert prix_u_cons >= 0
        prix_u_cons_val = True
        liste_de_entry[2].configure(border_color = set.col_noir_1)
    except:
        prix_u_cons_val = False
        liste_de_entry[2].configure(border_color = set.col_rouge)

    #verification de la quantité en stock
    try:
        qte_stock_cons = int(qte_stock_cons)
        assert qte_stock_cons >= 0
        qte_stock_cons_val = True
        liste_de_entry[3].configure(border_color = set.col_noir_1)
    except:
        qte_stock_cons_val = False
        liste_de_entry[3].configure(border_color = set.col_rouge)

    #Verification de la quantité seuil
    try:
    
        qte_seuil_cons = int(qte_seuil_cons)
        assert qte_seuil_cons >= 0
        qte_seuil_cons_val = True
        liste_de_entry[4].configure(border_color = set.col_noir_1)
    except:
        qte_seuil_cons_val = False
        liste_de_entry[4].configure(border_color = set.col_rouge)



    #verification de l'id du categorie de consommable à laquelle elle appartient
    try:
        categorie_cons = int(categorie_cons)
        categorie_cons_val = True
        liste_de_entry[5].configure(border_color = set.col_noir_1)
    except:
        categorie_cons_val = False
        liste_de_entry[5].configure(border_color = set.col_rouge)

    validation = all([ nom_cons_val, prix_u_cons_val, qte_seuil_cons_val, qte_stock_cons_val, categorie_cons_val])


    if validation:
        image = liste_de_entry[-1].get()
        consommable   = (nom_cons, qte_stock_cons, qte_seuil_cons, categorie_cons, prix_u_cons,image)

        reponse = gp.inserer_consommable(consommable)
        if reponse :
            messagebox.showinfo("Enrégistrement","Enrégistrement du consommable a été effectué avec succès" )
           
            liste_de_entry[1].delete(0, tk.END)
            liste_de_entry[2].delete(0, tk.END)
            liste_de_entry[3].delete(0, tk.END)
            liste_de_entry[4].delete(0, tk.END)
            liste_de_entry[5].set("Choisir une catégorie")
            liste_de_entry[-1].delete(0, tk.END)
            
        else:
            
            messagebox.showerror("Enregistrement", "Echec de l'opération !\nID consommable déjà existant")

    else:
        messagebox.showerror("Enregistrement", "Echec de l'opération !\nLes donées de certains champs sont invalides")



def ajouter_consonmmable(root):
    root.destroy()

    toplevel = ctk.CTkToplevel()
    toplevel.geometry("720x300+0+0")
    toplevel.title("Ajout d'un nouveau consommable")
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.resizable(width=False, height=False)
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.attributes('-topmost', True)
    
    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(800,300))

    fond = ctk.CTkLabel(toplevel,text=0,image=image)
    fond.place(x=0, y=0)

    #image du consommable
    image_label = ctk.CTkLabel(toplevel,text="", width=200, height=220,fg_color=set.col_noir_3 )
    image_label.place(x=20,y=20)

    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(toplevel, text="Formulaire d'enrégistrement d'un nouveau consommable".upper(), font= ("Montsérrat",12,'bold'), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    id.place(x=250, y=5)
    

    
    #Nom du produit
    nom = ctk.CTkLabel(toplevel, text='Nom :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    nom.place(x=250, y=45)
    nom_e = ctk.CTkEntry(toplevel, placeholder_text="Nom du consommable",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    nom_e.place(x=450, y= 45)
 

    #Prix unitaire
    prix_unitaire = ctk.CTkLabel(toplevel, text='Prix unitaire (FCFA) :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    prix_unitaire.place(x=250, y=85)
    prix_unitaire_e = ctk.CTkEntry(toplevel, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    prix_unitaire_e.place(x=450, y= 85)



    #Quantité en stock du produit
    qtestock = ctk.CTkLabel(toplevel, text='Qte en stock :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    qtestock.place(x=250, y=125)
    qtestock_e = ctk.CTkEntry(toplevel, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    qtestock_e.place(x=450, y= 125)
  

    #Quantité seuil du produit a respecter
    qteseuil = ctk.CTkLabel(toplevel, text='Qte seuil :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    qteseuil.place(x=250, y=165)
    qteseuil_e = ctk.CTkEntry(toplevel, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    qteseuil_e.place(x=450, y= 165)
 


    #Categories
    option = gp.get_categories()
   
    options = ["Choisir une catégorie"]+[str(i[0])+' '+i[1] for i in option]
    categorie = ctk.CTkLabel(toplevel, text='Catégorie :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    categorie.place(x=250, y=205)
    categorie_e= ctk.CTkComboBox(master=toplevel, width=250, height=30, fg_color=set.col_blanc_4, border_width=1, 
                            border_color=set.col_noir_1, values=options,
                            font=('Montsérrat', 12,), text_color= set.col_noir_1, corner_radius=5,
                            )
    categorie_e.place(x=450, y=205)
   
    

    image_e = ctk.CTkEntry(toplevel)
    

    #Les boutons
    liste_entry = [[], nom_e, prix_unitaire_e, qtestock_e, qteseuil_e, categorie_e, image_e] #liste des entry
    
    
    changer_image_cons = ctk.CTkButton(toplevel, text = "Changer image".upper(),width=200,height=40, command = lambda :choisir_photo(image_e, image_label)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    changer_image_cons.place(x=20, y=245)

    
    
    annulation = ctk.CTkButton(toplevel, text = "Annuler",width=100,height=40, command = lambda: toplevel.destroy()
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    annulation.place(x=255, y=245)

    enregistrement = ctk.CTkButton(toplevel, text = "Enrégistrer",width=100,height=40, command = lambda : enregistre(liste_entry)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    enregistrement.place(x=600, y=245)

    toplevel.mainloop()





def modifie(checking, liste_de_entry):
    """
        Une procédure qui permet d'enrégistrer une nouvelle consommable
        Paramètre: liste des entrys => ID, Nom, Qte S, Qte s, Prix, cat
    """
    valeur = checking.get()

    if valeur:
        #Recuperation des données
        id_fourn = liste_de_entry[0].get()
        nom_fourn = liste_de_entry[1].get(); nom_fourn_val = False
        adresse_fourn= liste_de_entry[2].get(); adresse_fourn_val = False
        contact_fourn = liste_de_entry[3].get(); contact_fourn_val = False
      
        
        
        #Verification du nom
        if nom_fourn != "":
            nom_fourn_val = True
            liste_de_entry[1].configure(border_color = set.col_noir_1)
        else:
            nom_fourn_val = False
            liste_de_entry[1].configure(border_color = "red")
        

        #Verification du prix unitaire
        if adresse_fourn:
            adresse_fourn_val = True
            liste_de_entry[2].configure(border_color= set.col_noir_1)
        else:
            adresse_fourn_val = False
            liste_de_entry[2].configure(border_color= "red")
        
        
        #Verification de la telephone
        regrex1 = r"^(?:\+|00)[0-9]{11,}"

        if re.search(regrex1, contact_fourn):
            contact_fourn_val= True
            liste_de_entry[3].configure(border_color = '#fff')
        else:
            contact_fourn_val= False
            liste_de_entry[3].configure(border_color = 'red')

        image_chemin = liste_de_entry[-1].get()
        if not image_chemin:
            image_chemin = "images/images_app/bg_page_connexion.png"

        validation = all([ nom_fourn_val,adresse_fourn_val, contact_fourn_val])


        if validation:
            image_chemin = liste_de_entry[-1].get()
            fournisseur   = (nom_fourn, adresse_fourn ,contact_fourn ,image_chemin, id_fourn)
          

            reponse = gp.update_fournisseur(fournisseur)
            if reponse :
                checking.set(0)
                messagebox.showinfo("Modification des informations du fournisseur","Modification effectuée avec succès")
                update_page(liste_de_entry)
            else: 
                
                messagebox.showerror("Modification des informations du fournisseur", "Echec de l'opération ! ID inexistant.")

        else:
            messagebox.showerror("Modification des informatins du fournisseur", "Echec de l'opération !\nLes données de certains champs sont invalides")
    else:
        messagebox.showinfo("Modification des informations du fournisseur", "Pour effectuer une modification, veuillez activer les champs en cochant la case")



def fournisseur(fourn, formulaire):
    """ 
        procédure fondamentale de gestion des fournisseurs:
        elle permet l'enregistrement, la recherche, le sauvegarde
    """
   
    #image 
    image_label = ctk.CTkLabel(formulaire,text="", width=200, height=230, image = place_image(fourn[-1]))
    image_label.place(x=20,y=10)

    #Identifier Verification de l'ID
    id = ctk.CTkLabel(formulaire, text='Fournisseur N°: ', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    id.place(x=250, y=10)
    id_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    id_e.place(x=450, y= 10)
    id_e.insert(0, fourn[0])
    id_e.configure(state = "disable")
    
    #Nom du produit
    nom = ctk.CTkLabel(formulaire, text='Nom :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    nom.place(x=250, y=50)
    nom_e = ctk.CTkEntry(formulaire, placeholder_text="Nom du fournisseur",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    nom_e.place(x=450, y= 50)
    nom_e.insert(0, fourn[1])
    nom_e.configure(state = "disable")

    #Prix unitaire
    adresse = ctk.CTkLabel(formulaire, text='Adresse :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    adresse.place(x=250, y=90)
    adresse_e = ctk.CTkEntry(formulaire, placeholder_text="Adresse",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    adresse_e.place(x=450, y= 90)
    adresse_e.insert(0,fourn[2])
    adresse_e.configure(state = "disable")


    #Quantité en stock du produit
    contact = ctk.CTkLabel(formulaire, text='Contact :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    contact.place(x=250, y=130)
    contact_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    contact_e.place(x=450, y= 130)
    contact_e.insert(0, fourn[3])
    contact_e.configure(state = "disable")

    
    image_e = ctk.CTkEntry(formulaire)
    if fourn[-1]!=None:
        image_e.insert(0, fourn[-1])
    else: 
        image_e.insert(0, "C:/wamp64/www/DEV/image/image_consommable/defaut.jpeg")

    #Les boutons
    liste_entry = [id_e, nom_e, adresse_e, contact_e, image_e] #liste des entry
    
    
    changer_image = ctk.CTkButton(formulaire, text = "Changer image".upper(),width=200,height=40, command = lambda :choisir_photo(image_e, image_label)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    changer_image.place(x=20, y=250)

    

    suppression = ctk.CTkButton(formulaire, text = "Supprimer".upper(),width=100,height=40, command = lambda : supprimer(id_e, formulaire)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    suppression.place(x=370, y=250)


    rendre_modifiable_value = tk.IntVar()
    rendre_modifiable = ctk.CTkCheckBox(formulaire, text="",variable=rendre_modifiable_value,
                                         command=lambda:activation_des_champs(rendre_modifiable_value, liste_entry))
    rendre_modifiable.place(x=470, y=255)


    modifier_fourn = ctk.CTkButton(formulaire, text = "Modifier".upper(),width=100,height=40, 
                                  command = lambda : modifie(rendre_modifiable_value, liste_entry)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    modifier_fourn.place(x=495, y=250)




def supprimer(idfour_e, formulaire):
    """
    Procéduire permettant de supprimer unfourniseur de la base
    @param: entry de id du fournisseur, ctkFrame formulaire
    @return: None
    """
    idfour_e.configure(state = tk.NORMAL)
    id = idfour_e.get()
    idfour_e.configure(state = "disable")
   
    
    idfour = int(id)

    if idfour :
         reponse = messagebox.askquestion("Suppression d'un fournisseur", "Validez vous la suppression de ce fournisseur")
         if reponse == "yes":
            answer = gp.supprimer_fournisseur(idfour)
            answer = gp.get_one_fournisseur(idfour)
            if not answer :
                formulaire.destroy()
                messagebox.showinfo("Suppression d'un fournisseur", "Suppression du fournisseur avec succès")
                 
            else:
                messagebox.showerror("Suppression d'un fournisseur", "Impossible de supprimer ce fournisseur")
    




def build_fournisseur(idfournisseur,framescroll):
    consommable = gp.get_one_fournisseur(idfournisseur)
    consommable = consommable[0]

    four_frame = ctk.CTkFrame(framescroll , height= 300, fg_color=set.col_blanc_4 )
    four_frame.pack(fill = "both", padx=10, pady=5)
    
    fond_image_path =  "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(800,300))

    fond = ctk.CTkLabel(four_frame,text=0,image=image)
    fond.place(x=0, y=0)
    

    fournisseur(consommable,four_frame)
