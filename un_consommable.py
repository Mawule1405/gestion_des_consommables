"""
    But: construire un consommable
"""

#importation des bibliothèques de python
import customtkinter as ctk
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image
from datetime import datetime


#import des modules
import graphi_print as gp
import setting as set


def place_image(chemin):
    try:
    
        image= Image.open(chemin.replace("\\",'/'))

    except:
        image= Image.open("C:/wamp64/www/DEV/image/image_consommable/defaut.jpeg")

    photo = ctk.CTkImage(image, size=(200,230))
    return photo


def choisir_photo(entry_photo, label_photo):
    app = ctk.CTk()
    app.withdraw()
    types_de_photos=[("Images JPG","*.jpg"),("Images JPEG","*.jpeg"),("Images PNG","*.png"),]
    chemin_de_photos = ctk.filedialog.askopenfilename(title="Choisissez une photo", filetypes=types_de_photos)

    if chemin_de_photos:
        entry_photo.delete(0, tk.END)
        entry_photo.insert(0, chemin_de_photos)
        label_photo.configure(image = place_image(chemin_de_photos))
        
    
    app.destroy()

def update_page(liste_entry):
    for element in liste_entry:
        element.configure(state = tk.NORMAL)

    id= int(liste_entry[0].get())
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
  

def lister_les_consommable():
    #Affichage des consommables
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("700x750+0+0")
    toplevel.title("Liste des consommables")
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.resizable(width=False, height=False)
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.attributes('-topmost', True)


    framescrol = ctk.CTkScrollableFrame(toplevel, width=600, height=620, fg_color=set.col_blanc_4, border_color= set.col_noir_1,
                                         border_width=1)
    framescrol.place(x=50,y=30)


    listes_cons = gp.get_consommables()

    liste_cons = ctk.CTkLabel(toplevel, text= "Liste de des consommables".upper(), fg_color=set.col_blanc_4,
                             font = ('Montsérrat', 15), text_color= set.col_noir_1 )
    liste_cons.place(x=50, y=2)

    

    fermer_button = ctk.CTkButton(toplevel, text = "FERMER".upper(),width=80,height=35, fg_color=set.col_noir_5,
                                     corner_radius=5, hover_color= set.col_hover,font=('Montsérrat', 10),
                                     command= lambda: toplevel.destroy() )
    fermer_button.place(x=580 ,y=690)

    style_cons = ttk.Style()
    style_cons.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'), rowheight=20, foreground=set.col_fg)
    style_cons.configure("Treeview", font=('Helvetica', 13, 'bold'), rowheight=50,)
    tree_cons = ttk.Treeview(framescrol, columns=('id_cons', 'nom_cons',"qtestock_cons", 'qteseuil_cons', 'prix_unitaire_cons', 'categorie'), 
                             show='headings', height=20)

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


def modifie(liste_de_entry):
    """
        Une procédure qui permet d'enrégistrer une nouvelle consommable
        Paramètre: liste des entrys => ID, Nom, Qte S, Qte s, Prix, cat
    """
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
        liste_de_entry[0].configure(border_color = set.col_rouge)
    
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

    



    

    validation = all([id_cons_val, nom_cons_val, prix_u_cons_val])


    if validation:
        consommable   = ( nom_cons, prix_u_cons, id_cons)

        reponse = gp.update_consommable(consommable)
        if reponse :
            messagebox.showinfo("Modification","Modification des données effectués avec succès.\nVous ne pouvez pas changer la quantité en stock ni la quantité seuil")
            
        else: 
            
            messagebox.showerror("Modification", "Echec de l'opération ! ID inexistant.")

    else:
        messagebox.showerror("Modification", "Echec de l'opération !\nLes données de certains champs sont invalides")

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

    """rechercher_cons = ctk.CTkButton(formulaire, text = "Rechercher".upper(),width=100,height=40, command = lambda :recherche(liste_entry)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    rechercher_cons.place(x=255, y=245)"""
    
    
    attribuer_cons = ctk.CTkButton(formulaire, text = "Attribuer".upper(),width=100,height=40, command = lambda: attribuer(conso, liste_entry)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    attribuer_cons.place(x=370, y=245)

    modifier_cons = ctk.CTkButton(formulaire, text = "Modifier".upper(),width=100,height=40, command = lambda : modifie(liste_entry)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    modifier_cons.place(x=495, y=245)


    voir_liste = ctk.CTkButton(formulaire, text = "Supprimer".upper(),width=100,height=40, command = lambda : lister_les_consommable()
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    voir_liste.place(x=600, y=245)


def build_consommable(idconsommable,framescroll):
    consommable = gp.get_consommables_by_id_cons(idconsommable)
    consommable = consommable[0]

    cons_frame = ctk.CTkFrame(framescroll , height= 300, fg_color=set.col_blanc_4 )
    cons_frame.pack(fill = "both", padx=100, pady=5)

    consommables(consommable,cons_frame)
