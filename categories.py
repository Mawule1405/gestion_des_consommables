import customtkinter as ctk
from tkinter import ttk, messagebox
import tkinter as tk


import graphi_print as gp

def categories(framescrol):


    def enregistrer():
        """Une procédure pour enrégistrer de nouvelle catégories de consommables"""
        id_x = id_cat_e.get(); id_is_val = False
        nom_x = nom_cat_e.get(); nom_is_val = False
        
        #Vérification de l'ID
        try:
            id_x = int(id_x)
            if id_x > 0:
                id_is_val = True
                id_cat_e.configure(border_color = '#fff')
            else:
                id_is_val = False
                id_cat_e.configure(border_color = 'red')
        except:
            id_is_val = False
            id_cat_e.configure(border_color = 'red')
        
        #Vérification du nom
        if nom_x != "":
            nom_is_val = True
            nom_cat_e.configure(border_color = '#fff')
        else:
            nom_is_val = False
            nom_cat_e.configure(border_color = 'red')
        
        if id_is_val and nom_is_val:
            res = gp.inserer_categorie((id_x,nom_x))
            if res:
                tree_cat.insert('', tk.END, values=(id_x,nom_x))
                tree_cat.update()
            else:
                messagebox.showerror('Information',"L'identifiant existe déjà.\nVeillez regarder la liste")
        else:
            messagebox.showerror('Alert', 'Valeur incorrecte dans au moins un champs')


    def recherche():
        """Une procédure pour enrégistrer de nouvelle catégories de consommables"""
        id_x = id_cat_e.get()

        try:
            id_x = int(id_x)
            res = gp.get_one_categories(id_cat= id_x)
            if res:
                nom_cat_e.delete(0,tk.END)
                nom_cat_e.insert(0,res[0][0])
            else:
                messagebox.showinfo("Résulat de la recherche", "Identifiant inexistant")
        except:
            messagebox.showerror('Alert', 'Identifiant incorrect')


    def modifier():
        """Une procédure pour enrégistrer de nouvelle catégories de consommables"""
        id_x = id_cat_e.get(); id_is_val = False
        nom_x = nom_cat_e.get(); nom_is_val = False
        
        #Vérification de l'ID
        try:
            id_x = int(id_x)
            if id_x > 0:
                id_is_val = True
                id_cat_e.configure(border_color = '#fff')
            else:
                id_is_val = False
                id_cat_e.configure(border_color = 'red')
        except:
            id_is_val = False
            id_cat_e.configure(border_color = 'red')
        
        #Vérification du nom
        if nom_x != "":
            nom_is_val = True
            nom_cat_e.configure(border_color = '#fff')
        else:
            nom_is_val = False
            nom_cat_e.configure(border_color = 'red')
        
        if id_is_val and nom_is_val:
            res = gp.modifier_categories((id_x,nom_x))
            if res:
                listes = gp.get_categories()
                tree_cat.insert('', tk.END, values=(id_x,nom_x))
                tree_cat.update()
            else:
                messagebox.showerror('Information',"L'identifiant existe déjà.\nVeillez regarder la liste")
        else:
            messagebox.showerror('Alert', 'Valeur incorrecte dans au moins un champs')



    """CATEGORIES DE CONSOMMANBLES"""
    #Définition des catégories de consommables
    #titre
    titre_cat = ctk.CTkLabel(framescrol,text="CATEGORIES DE CONSOMMABLES", font = ('Montsérrat', 30), 
                               fg_color ='#000')
    titre_cat.pack(padx=5, pady=10)
    #zone
    cat = ctk.CTkFrame(framescrol, width=1150, height=400, fg_color="#000", bg_color="#000",
                         border_color="#fff", border_width=1)
    cat.pack(pady = 10)

    #Définition des éléments
    #Identifiant
    liste_cat = ctk.CTkLabel(cat, text= "FORMULAIRE", fg_color = "#000",font = ('Montsérrat', 25,'underline'),
                             text_color = "#fff")
    liste_cat.place(x=10, y=5 )

    id_cat_l = ctk.CTkLabel(cat, text= "Identifiant", fg_color = "#000",font = ('Montsérrat', 20) )
    id_cat_l.place(x= 10, y=50)

    id_cat_e = ctk.CTkEntry(cat,placeholder_text='0',justify='right' ,fg_color = "#000", width=200,height=30,
                            font = ('Montsérrat', 20))
    id_cat_e.place(x= 125, y=50)
    
    #Identifiant
    nom_cat_l = ctk.CTkLabel(cat, text= "Nom", fg_color = "#000",font = ('Montsérrat', 20) )
    nom_cat_l.place(x= 10, y=100)
    nom_cat_e = ctk.CTkEntry(cat,placeholder_text='Catégorie name',justify='left' ,fg_color = "#000", width=250,height=30,
                            font = ('Montsérrat', 15))
    nom_cat_e.place(x= 75, y=100)

    #Les bouttons
    rechercher_cat = ctk.CTkButton(cat, text = "Rechercher",width=150,height=35,command= recherche)
    rechercher_cat.place(x=10, y=160)
    
    enregistrer_cat = ctk.CTkButton(cat, text = "Enregistrer",width=150,height=35,
                                    command= enregistrer)
    enregistrer_cat.place(x=175, y=160)

    modifier_cat = ctk.CTkButton(cat, text = "Modifier",width=150,height=35)
    modifier_cat.place(x=10, y=210)

    supprimer_cat = ctk.CTkButton(cat, text = "Supprimer",width=150,height=35)
    supprimer_cat.place(x=175, y=210)

    #Affichage des categories
    listes_cat = gp.get_categories()

    liste_cat = ctk.CTkLabel(cat, text= "Liste de catégories de consommables", fg_color = "#000",font = ('Montsérrat', 20) )
    liste_cat.place(x=360, y=15)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 30, 'bold'), rowheight=20, foreground='blue')
    style.configure("Treeview", font=('Helvetica', 30, 'bold'), rowheight=50,)
    tree_cat = ttk.Treeview(cat, columns=('id_cat', 'nom_cat'), show='headings', height=15)

    # Définir les en-têtes
    tree_cat.column('nom_cat', width=1500) 
    tree_cat.heading('id_cat', text='Numéro')
    tree_cat.heading('nom_cat', text='Nom de la catégorie')
    for ligne in listes_cat:
        tree_cat.insert('', tk.END, values=ligne)
    tree_cat.place(x=900 , y=150,width=1950)