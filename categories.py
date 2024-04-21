import customtkinter as ctk
from tkinter import ttk, messagebox
import tkinter as tk


import graphi_print as gp
import setting as set



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
                id_cat_e.delete(0,tk.END)
                nom_cat_e.delete(0,tk.END)
                tree_cat.insert('', tk.END, values=(id_x,nom_x))
                tree_cat.update()
                framescrol.update()

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
            res = gp.modifier_categories((nom_x,id_x))
            
            if res:
                listes = gp.get_categories()
                nom_cat_e.delete(0,tk.END)
                tree_cat.delete(*tree_cat.get_children())
                for i in listes:
                    tree_cat.insert('',tk.END, values=i)
                tree_cat.update()
                framescrol.update()
            else:
                messagebox.showerror('Information',"L'identifiant existe déjà.\nVeillez regarder la liste")
        else:
            messagebox.showerror('Alert', 'Valeur incorrecte dans au moins un champs')

    def supprimer():
        """Une procédure pour supprimer une catégories de consommables"""
        id_x = id_cat_e.get(); id_is_val = False
        
        
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
        

        if id_is_val :
            resultat = messagebox.askquestion('Suppression',"Confirmez-vous la suppression ?")
            if resultat == 'yes':
                res = gp.supprimer_categories(id_x)
                
                if res:
                    listes = gp.get_categories()
                    tree_cat.delete(*tree_cat.get_children())
                    for i in listes:
                        tree_cat.insert('',tk.END, values=i)
                    tree_cat.update()
                    framescrol.update()

                else:
                    messagebox.showerror('Information'," Désolé Suppression impossible !")
        else:
            messagebox.showerror('Alert', 'Valeur incorrecte dans au moins un champs')

    
    """CATEGORIES DE CONSOMMANBLES"""
    #Définition des catégories de consommables
    #zone
    cat = ctk.CTkFrame(framescrol, width=990, height=650, fg_color=set.col_blanc_4, 
                         border_color=set.col_border, border_width=1,corner_radius=0)
    cat.place(x= 0, y= 0)

    #zone du formulaire
    zone_forme = ctk.CTkFrame(cat,width=350, height=360, fg_color=set.col_blanc_4, corner_radius=5,
                         border_color=set.col_noir_1, border_width=1)
    zone_forme.place(x=15,y=50)

    #Définition des éléments
    #Formulaire
    liste_cat = ctk.CTkLabel(cat, text= "FORMULAIRE", fg_color=set.col_blanc_4,font = ('Montsérrat', 20),
                             text_color = set.col_noir_1)
    liste_cat.place(x=30, y=35 )

    

    id_cat_l = ctk.CTkLabel(zone_forme, text= "ID :", fg_color=set.col_blanc_4, font = ('Montsérrat', 15), text_color=set.col_noir_1)
    id_cat_l.place(x= 10, y=50)

    id_cat_e = ctk.CTkEntry(zone_forme,placeholder_text='0',justify='right' ,fg_color=set.col_blanc_4, width=250,height=30,
                            font = ('Montsérrat', 15),corner_radius=5, placeholder_text_color=set.col_placeholder,
                            text_color=set.col_noir_1)
    id_cat_e.place(x= 80, y=50)
    
    #Identifiant
    nom_cat_l = ctk.CTkLabel(zone_forme, text= "Nom :", fg_color=set.col_blanc_4, font = ('Montsérrat', 15) , text_color= set.col_noir_1)
    nom_cat_l.place(x= 10, y=150)
    nom_cat_e = ctk.CTkEntry(zone_forme,placeholder_text='Catégorie name',justify='left' ,fg_color=set.col_blanc_4, width=250,height=30,
                            font = ('Montsérrat', 15),  placeholder_text_color=set.col_placeholder, corner_radius=5, 
                            text_color=set.col_noir_1)
    nom_cat_e.place(x= 80, y=150)

    #Les bouttons
    rechercher_cat = ctk.CTkButton(zone_forme, text = "Rechercher",width=160,height=40,command= recherche,
                                   fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    rechercher_cat.place(x=10, y=250)
    
    enregistrer_cat = ctk.CTkButton(zone_forme, text = "Enregistrer",width=160,height=40,command= enregistrer,
                                    fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    enregistrer_cat.place(x=180, y=250)

    modifier_cat = ctk.CTkButton(zone_forme, text = "Modifier",width=160,height=40,command= modifier,
                                 fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    modifier_cat.place(x=10, y=310)

    supprimer_cat = ctk.CTkButton(zone_forme, text = "Supprimer",width=160,height=40, command = supprimer,
                                  fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    supprimer_cat.place(x=180, y=310)

    #Affichage des categories
    listes_cat = gp.get_categories()


    frame_categorie = ctk.CTkScrollableFrame(cat, width=500, height=350, border_width=1,
                                             fg_color=set.col_blanc_4, orientation='vertical')
    frame_categorie.place(x=400 , y=50)

    liste_cat = ctk.CTkLabel(cat, text= "Liste de catégories de consommables".upper(), fg_color=set.col_blanc_4,
                             font = ('Montsérrat', 20), text_color= set.col_noir_1 )
    liste_cat.place(x=430, y=35)



    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 18, 'bold'), rowheight=10, foreground=set.col_fg)
    style.configure("Treeview", font=('Helvetica', 13, 'bold'), rowheight=30,)
    tree_cat = ttk.Treeview(frame_categorie, columns=('id_cat', 'nom_cat'), show='headings', height=20)

    # Définir les en-têtes
    tree_cat.column('nom_cat', width=500)
    tree_cat.column('id_cat', width=100) 
    tree_cat.heading('id_cat', text='ID')
    tree_cat.heading('nom_cat', text='Nom de la catégorie')
    for ligne in listes_cat:
        tree_cat.insert('', tk.END, values=ligne)
    tree_cat.pack(pady=20)