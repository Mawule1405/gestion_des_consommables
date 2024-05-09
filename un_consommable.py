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
   
    print(gp.get_consommables_by_id_cons(id))
    conso = gp.get_consommables_by_id_cons(id)[0]
    
    
    for  element in liste_entry:
        if not isinstance(element, ctk.CTkComboBox):
            element.delete(0,tk.END)

       
    liste_entry[0].insert(0, conso[0])
    liste_entry[1].insert(0, conso[1])
    liste_entry[2].insert(0,conso[4])
    liste_entry[3].insert(0,conso[2])
    liste_entry[4].insert(0,conso[3])

    if conso[-1]!=None:
        liste_entry[6].insert(0, conso[-1])
    else: 
        liste_entry[6].insert(0, "C:/wamp64/www/DEV/image/image_consommable/defaut.jpeg")
    
    liste_entry[5].set(str(conso[5])+' '+conso[6])

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



def attributtion(root, consommable, employe: ctk.CTkComboBox, qte: ctk.CTkEntry, liste_entry):
    """
    Fonction permettant d'enrégistrer les attributions de consommables dans la base de données
    @param:tuple de consommable, Combobox emplopye, Entry quantitedemande, page à mettre à jour
    @return : None
    """

    id_cons = consommable[0]
    qtestock = consommable[2]
    qtedemande = qte.get()
    employe_info= employe.get().split() 
    
    try:
        qtedemande = int(qtedemande)
        qte.configure(border_color = "black")

        try :
            
            id_emp = int(employe_info[0])
            

            if qtestock < qtedemande:
                messagebox.showinfo("Attribution de consommable", "La quantité en stock du consommable est insuffisante")
            else:
                date = datetime.now().date()
                reponse = gp.inserer_one_demande((id_emp,id_cons, qtedemande, date))

                if reponse:
                    messagebox.showinfo("Attribution de consommable", f"{qtedemande} de {consommable[1]} ont été attribuer avec succès à {" ".join(employe_info[1:])} le {date}")
                    root.destroy()
                    update_page(liste_entry) #Mise à jour de la page
                else:
                    messagebox.showerror("Erreur d'attribution de cnsommable", "Une erreur s'est souvenue lors des opérations. Veillez réessayer!")
        except Exception as e:
            messagebox.showinfo("Alerte", f"Veuillez sélectionner l'employé qui demande le consommable {e}")
    except:
        qte.configure(border_color = "red")
  


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



def lister_les_consommable():
    #Affichage des consommables
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("700x500")
    toplevel.title("Liste des consommables")
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.resizable(width=False, height=False)
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.attributes('-topmost', True)


    framescrol = ctk.CTkScrollableFrame(toplevel, width=620, height=400, fg_color=set.col_blanc_4, border_color= set.col_noir_1,
                                         border_width=1)
    framescrol.place(x=20,y=30)


    listes_cons = gp.get_consommables()

    liste_cons = ctk.CTkLabel(toplevel, text= "Liste de des consommables".upper(), fg_color=set.col_blanc_4,
                             font = ('Montsérrat', 15), text_color= set.col_noir_1 )
    liste_cons.place(x=20, y=2)

    
    enregistre_button = ctk.CTkButton(toplevel, text = "Ajouter un nouveau consommable".upper(),width=200,height=35, fg_color=set.col_noir_5,
                                     corner_radius=5, hover_color= set.col_hover,font=('Montsérrat', 10),
                                     command= lambda: ajouter_consonmmable(toplevel))
    enregistre_button.place(x=20 ,y=460)
    

    fermer_button = ctk.CTkButton(toplevel, text = "FERMER".upper(),width=80,height=35, fg_color=set.col_noir_5,
                                     corner_radius=5, hover_color= set.col_hover,font=('Montsérrat', 10),
                                     command= lambda: toplevel.destroy() )
    fermer_button.place(x=580 ,y=460)

    style_cons = ttk.Style()
    style_cons.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'), rowheight=20, foreground=set.col_fg)
    style_cons.configure("Treeview", font=('Helvetica', 13, 'bold'), rowheight=50,)
    tree_cons = ttk.Treeview(framescrol, columns=('id_cons', 'nom_cons',"qtestock_cons", 'qteseuil_cons', 'prix_unitaire_cons', 'categorie'), 
                             show='headings', height=100)

    # Définir les en-têtes
    tree_cons.column('nom_cons', width=400)
    tree_cons.column('id_cons', width=75) 
    tree_cons.column("qtestock_cons", width=100)
    tree_cons.column("qteseuil_cons", width=100)
    tree_cons.column("prix_unitaire_cons", width=150)
    tree_cons.heading('id_cons', text='ID')
    tree_cons.heading('nom_cons', text='Nom ')
    tree_cons.heading('qtestock_cons', text='Q S')
    tree_cons.heading('qteseuil_cons', text='Q s')
    tree_cons.heading('prix_unitaire_cons', text='PU')
    tree_cons.heading('categorie', text='Categorie')
    for ligne in listes_cons:
        tree_cons.insert('', tk.END, values=ligne)
    tree_cons.pack()

    toplevel.mainloop()



def modifie(checking, liste_de_entry):
    """
        Une procédure qui permet d'enrégistrer une nouvelle consommable
        Paramètre: liste des entrys => ID, Nom, Qte S, Qte s, Prix, cat
    """
    valeur = checking.get()

    if valeur:
        #Recuperation des données
        id_cons = liste_de_entry[0].get() ; id_cons_val = False
        nom_cons = liste_de_entry[1].get(); nom_cons_val = False
        prix_u_cons= liste_de_entry[2].get(); prix_u_cons_val = False
        categorie_cons = liste_de_entry[5].get().split()[0]; categorie_cons_val = False
      
        #Verification de l'identité 
        try:
            id_cons = int(id_cons)
            id_cons_val = True
            liste_de_entry[0].configure(border_color = set.col_noir_1)
        except:
            id_cons_val = False
            liste_de_entry[0].configure(border_color = "red")
        
        #Verification du nom
        if nom_cons != "":
            nom_cons_val = True
            liste_de_entry[1].configure(border_color = set.col_noir_1)
        else:
            nom_cons_val = False
            liste_de_entry[1].configure(border_color = "red")
        

        #Verification du prix unitaire
        try:
            prix_u_cons = int(prix_u_cons)
            assert prix_u_cons >= 0
            prix_u_cons_val = True
            liste_de_entry[2].configure(border_color = set.col_noir_1)
        except:
            prix_u_cons_val = False
            liste_de_entry[2].configure(border_color = "red")

        try:
            categorie_cons = int(categorie_cons)
           
            categorie_cons_val = True
            liste_de_entry[5].configure(border_color = set.col_noir_1)
        except:
            categorie_cons_val = False
            liste_de_entry[5].configure(border_color = "red")


        validation = all([id_cons_val, nom_cons_val,categorie_cons_val, prix_u_cons_val])


        if validation:
            image_chemin = liste_de_entry[-1].get()
            consommable   = (nom_cons, prix_u_cons,categorie_cons,image_chemin, id_cons)
          

            reponse = gp.update_consommable(consommable)
            if reponse :
                checking.set(0)
                messagebox.showinfo("Modification","Mocation des données effectués avec succès.\nVous ne pouvez pas changer la quantité en stock ni la quantité seuil")
                update_page(liste_de_entry)
            else: 
                
                messagebox.showerror("Modification", "Echec de l'opération ! ID inexistant.")

        else:
            messagebox.showerror("Modification", "Echec de l'opération !\nLes données de certains champs sont invalides")
    else:
        messagebox.showinfo("Modification", "Pour effectuer une modification, veuillez activer les champs en cochant la case")



def recherche(liste_de_entry):
    """
       Procéduire permettant de rechercher un consommable et envoyé
       les résulats dans les autres entry ou checkbox
       parametre: identifiant du consommable à rechercher"""
    id_cons = liste_de_entry[0].get()
    
    try:
        id_cons = int(id_cons)
        resultat = gp.get_consommables_by_id_cons(id_cons)
        res = resultat[0]
        liste_de_entry[1].delete(0,tk.END); liste_de_entry[1].insert(0,res[1])
        liste_de_entry[2].delete(0,tk.END); liste_de_entry[2].insert(0,res[4])
        liste_de_entry[3].delete(0,tk.END); liste_de_entry[3].insert(0,res[2])
        liste_de_entry[4].delete(0,tk.END); liste_de_entry[4].insert(0,res[3])
        liste_de_entry[5].set(str(res[5])+' '+res[6])
    
    except IndexError:
           messagebox.showinfo("Recherche", "Identifiant non trouvé !")
    
    except Exception as e  :
        
        messagebox.showinfo("Recherche", "Veuillez préciser l'identifiant du consommable recherché")



def attribuer(consommable,liste_entry):
    """
        Une procédure qui permet d'enrégistrer une nouvelle consommable
        Paramètre: liste des entrys => ID, Nom, Qte S, Qte s, Prix, cat
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("400x250")
    toplevel.title("Attribuer consommable")
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.resizable(width=False, height=False)
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.attributes('-topmost', True)

    titre_l = ctk.CTkLabel(toplevel, text="Attribution de consommable", font=('Montsérrat', 15,"bold"), text_color= set.col_noir_1)
    titre_l.place(x=30, y=0)

    
    employe_l = ctk.CTkLabel(toplevel, text="Employé")
    employe_l.place(x=30, y=30)
    option = gp.get_employes()
    options = ["Choisir une catégorie"]+[str(i[0])+' '+i[1]+' '+i[2] for i in option]
    employe_e= ctk.CTkComboBox(master= toplevel, width=340, height=40, fg_color=set.col_blanc_4, border_width=1, 
                            border_color=set.col_noir_1, values=options,
                            font=('Montsérrat', 13,), text_color= set.col_noir_1, corner_radius=5,
                            )
    employe_e.place(x=30, y=60)

    qte_l = ctk.CTkLabel(toplevel, text="Quantité attribuer")
    qte_l.place(x= 30 , y= 110)
    qte_e= ctk.CTkEntry(master= toplevel, width=340, height=40, fg_color=set.col_blanc_4, border_width=1, 
                            border_color=set.col_noir_1,
                            font=('Montsérrat', 13,), text_color= set.col_noir_1, corner_radius=5,
                            )
    qte_e.place(x=30, y=140)

    annuler = ctk.CTkButton(toplevel, text="Annuler", width=100, height=40, command= lambda: toplevel.destroy())
    annuler.place(x=30, y= 200)

    enregistrer = ctk.CTkButton(toplevel, text="Enrégistrer", width=100, height=40, command= lambda: attributtion(toplevel, consommable, employe_e, qte_e, liste_entry))
    enregistrer.place(x=270, y= 200)


    


    toplevel.mainloop()



def consommables(conso, formulaire):
    """ 
        procédure fondamentale de gestion des consommables:
        elle permet l'enregistrement, la recherche, le sauvegarde
    """
    #Définition des consommables

    
   
    #image du consommable
    image_label = ctk.CTkLabel(formulaire,text="", width=200, height=230, image = place_image(conso[-1]))
    image_label.place(x=20,y=5)

    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(formulaire, text='Consommable N°: ', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    id.place(x=250, y=5)
    id_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=20, corner_radius=5,
                        font= ("Montsérrat",15))
    id_e.place(x=450, y= 5)
    id_e.insert(0, conso[0])
    id_e.configure(state = "disable")
    
    #Nom du produit
    nom = ctk.CTkLabel(formulaire, text='Nom :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    nom.place(x=250, y=45)
    nom_e = ctk.CTkEntry(formulaire, placeholder_text="Nom du consommable",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    nom_e.place(x=450, y= 45)
    nom_e.insert(0, conso[1])
    nom_e.configure(state = "disable")

    #Prix unitaire
    prix_unitaire = ctk.CTkLabel(formulaire, text='Prix unitaire (FCFA) :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    prix_unitaire.place(x=250, y=85)
    prix_unitaire_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    prix_unitaire_e.place(x=450, y= 85)
    prix_unitaire_e.insert(0,conso[4])
    prix_unitaire_e.configure(state = "disable")


    #Quantité en stock du produit
    qtestock = ctk.CTkLabel(formulaire, text='Qte en stock :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    qtestock.place(x=250, y=125)
    qtestock_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    qtestock_e.place(x=450, y= 125)
    qtestock_e.insert(0, conso[2])
    qtestock_e.configure(state = "disable")

    #Quantité seuil du produit a respecter
    qteseuil = ctk.CTkLabel(formulaire, text='Qte seuil :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    qteseuil.place(x=250, y=165)
    qteseuil_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=250, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    qteseuil_e.place(x=450, y= 165)
    qteseuil_e.insert(0, conso[3])
    qteseuil_e.configure(state = "disable")


    #Categories
    option = gp.get_categories()
   
    options = ["Choisir une catégorie"]+[str(i[0])+' '+i[1] for i in option]
    categorie = ctk.CTkLabel(formulaire, text='Catégorie :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    categorie.place(x=250, y=205)
    categorie_e= ctk.CTkComboBox(master=formulaire, width=250, height=30, fg_color=set.col_blanc_4, border_width=1, 
                            border_color=set.col_noir_1, values=options,
                            font=('Montsérrat', 12,), text_color= set.col_noir_1, corner_radius=5,
                            )
    categorie_e.place(x=450, y=205)
    categorie_e.set(str(conso[5])+' '+conso[6])
    categorie_e.configure(state ="disable")
    

    image_e = ctk.CTkEntry(formulaire)
    if conso[-1]!=None:
        image_e.insert(0, conso[-1])
    else: 
        image_e.insert(0, "C:/wamp64/www/DEV/image/image_consommable/defaut.jpeg")

    #Les boutons
    liste_entry = [id_e, nom_e, prix_unitaire_e, qtestock_e, qteseuil_e, categorie_e, image_e] #liste des entry
    
    
    changer_image_cons = ctk.CTkButton(formulaire, text = "Changer image".upper(),width=200,height=40, command = lambda :choisir_photo(image_e, image_label)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    changer_image_cons.place(x=20, y=245)

    
    
    attribuer_cons = ctk.CTkButton(formulaire, text = "Attribuer".upper(),width=100,height=40, command = lambda: attribuer(conso, liste_entry)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    attribuer_cons.place(x=255, y=245)

    suppression = ctk.CTkButton(formulaire, text = "Supprimer".upper(),width=100,height=40, command = lambda : supprimer(id_e, formulaire)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    suppression.place(x=370, y=245)


    rendre_modifiable_value = tk.IntVar()
    rendre_modifiable = ctk.CTkCheckBox(formulaire, text="",variable=rendre_modifiable_value,
                                         command=lambda:activation_des_champs(rendre_modifiable_value, liste_entry))
    rendre_modifiable.place(x=470, y=250)


    modifier_cons = ctk.CTkButton(formulaire, text = "Modifier".upper(),width=100,height=40, 
                                  command = lambda : modifie(rendre_modifiable_value, liste_entry)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    modifier_cons.place(x=495, y=245)

    plus_info = ctk.CTkButton(formulaire, text = "Liste simple".upper(),width=100,height=40, 
                              command = lambda :lister_les_consommable()
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    plus_info.place(x=600, y=245)



def supprimer(idcons_e, formulaire):
    """
    Procéduire permettant de supprimer un consommable
    @param: entry de consommable, ctkFrame formulaire
    @return: None
    """
    idcons_e.configure(state = tk.NORMAL)
    id = idcons_e.get()
    idcons_e.configure(state = "disable")
   
    
    idcons = int(id)

    if idcons :
         reponse = messagebox.askquestion("Suppression d'un consommable", "Validez vous la suppression de ce consommable")
         print(reponse)
         if reponse == "yes":
            answer = gp.supprimer_consommable(idcons)
            answer = gp.get_consommables_by_id_cons(idcons)
            if not answer :
                formulaire.destroy()
                messagebox.showinfo("Suppression d'un consommable", "Suppression du consommable avec succès")
                 
            else:
                messagebox.showerror("Suppression d'un consommable", "Impossible de supprimer ce consommable")
    




def build_consommable(idconsommable,framescroll):
    consommable = gp.get_consommables_by_id_cons(idconsommable)
    consommable = consommable[0]

    cons_frame = ctk.CTkFrame(framescroll , height= 300, fg_color=set.col_blanc_4 )
    cons_frame.pack(fill = "both", padx=100, pady=5)
    
    fond_image_path =  "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(600,300))

    fond = ctk.CTkLabel(cons_frame,text=0,image=image)
    fond.place(x=0, y=0)
    

    consommables(consommable,cons_frame)
