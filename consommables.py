import customtkinter as ctk
from tkinter import ttk
import tkinter as tk

import setting as set
import graphi_print as gp

def consommables(framescrol):
    """ """
    #Définition des consommables
    
    #zone
    conso = ctk.CTkFrame(framescrol, width=1150, height=650, fg_color=set.col_fg, bg_color=set.col_bg,
                         border_color=set.col_border, border_width=1)
    conso.place(x= 0 , y=0)

    """Formulaire"""
    #Le formulaire
    formulaire = ctk.CTkFrame(conso, width=960, height=210, bg_color=set.col_bg,fg_color=set.col_fg,border_color=set.col_border,
                         border_width=1)
    formulaire.place(x=20, y=15)

    liste_conso = ctk.CTkLabel(conso, text= "FORMULAIRE", fg_color =set.col_fg,font = ('Montsérrat', 20),
                             text_color =set.col_text)
    liste_conso.place(x=25, y=5 )

    

    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(formulaire, text='Identifiant :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    id.place(x=5, y=35)
    id_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=100, height=30, corner_radius=0,
                        font= ("Montsérrat",20))
    id_e.place(x=150, y= 35)
    
    #Nom du produit
    nom = ctk.CTkLabel(formulaire, text='Nom :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    nom.place(x=260, y=35)
    nom_e = ctk.CTkEntry(formulaire, placeholder_text="Nom du consommable",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=300, height=30, corner_radius=0,
                        font= ("Montsérrat",20))
    nom_e.place(x=370, y= 35)

    #Prix unitaire
    prix_unitaire = ctk.CTkLabel(formulaire, text='Prix unitaire :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    prix_unitaire.place(x=675, y=35)
    prix_unitaire_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=150, height=30, corner_radius=0,
                        font= ("Montsérrat",20))
    prix_unitaire_e.place(x=800, y= 35)


    #Quantité en stock du produit
    qtestock = ctk.CTkLabel(formulaire, text='Qte en stock :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    qtestock.place(x=5, y=90)
    qtestock_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=100, height=30, corner_radius=0,
                        font= ("Montsérrat",20))
    qtestock_e.place(x=150, y= 90)

    #Quantité seuil du produit a respecter
    qteseuil = ctk.CTkLabel(formulaire, text='Qte seuil :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    qteseuil.place(x=260, y=90)
    qteseuil_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=100, height=30, corner_radius=0,
                        font= ("Montsérrat",20))
    qteseuil_e.place(x=370, y= 90)


    #Categories
    option = gp.get_categories()
    options = ["Choisir une catégorie"]+[str(i[0])+' '+i[1] for i in option]
    categorie = ctk.CTkLabel(formulaire, text='Catégorie :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    categorie.place(x=550, y=90)
    categorie_e= ctk.CTkComboBox(master=formulaire, width=250, height=30, fg_color=set.col_fg, border_width=1, 
                            border_color=set.col_border, values=options, button_color=set.col_border,button_hover_color=set.col_hover,
                            font=('Montsérrat', 12,),dropdown_font=('Montsérrat',15), text_color= set.col_text, dropdown_text_color= set.col_text,
                            dropdown_fg_color= set.col_fg, dropdown_hover_color=set.col_hover, corner_radius=0,
                            )
   
    categorie_e.place(x=700, y=90)

    #Les boutons
    rechercher_cons = ctk.CTkButton(formulaire, text = "Rechercher",width=200,height=30,command= "#",font=('Montsérrat', 25),
                                   fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    rechercher_cons.place(x=5, y=150)
    
    enregistrer_cons = ctk.CTkButton(formulaire, text = "Enregistrer",width=200,height=30,command= "#",font=('Montsérrat', 25),
                                    fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    enregistrer_cons.place(x=270, y=150)

    modifier_cons = ctk.CTkButton(formulaire, text = "Modifier",width=200,height=30,command="#",font=('Montsérrat', 25),
                                 fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    modifier_cons.place(x=500, y=150)

    supprimer_cons = ctk.CTkButton(formulaire, text = "Supprimer",width=200,height=30, command = "#",font=('Montsérrat', 25),
                                  fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    supprimer_cons.place(x=750, y=150)

    #Affichage des consommables

    listes_cons = gp.get_consommables()

    liste_cons = ctk.CTkLabel(framescrol, text= "Liste de des consommables".upper(), fg_color=set.col_fg,
                             font = ('Montsérrat', 20), text_color= set.col_text , bg_color=set.col_bg)
    liste_cons.place(x=15, y=250)

    frame_cons = ctk.CTkScrollableFrame(framescrol, width=940, height=320, border_color=set.col_border, border_width=1,
                                             fg_color=set.col_fg, bg_color= set.col_bg, orientation='vertical',
                                             scrollbar_fg_color=set.col_fg)
    frame_cons.place(x=15 , y=290)

    style_cons = ttk.Style()
    style_cons.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'), rowheight=20, foreground=set.col_fg)
    style_cons.configure("Treeview", font=('Helvetica', 13, 'bold'), rowheight=50,)
    tree_cons = ttk.Treeview(frame_cons, columns=('id_cons', 'nom_cons',"qtestock_cons", 'qteseuil_cons', 'prix_unitaire_cons', 'categorie'), 
                             show='headings', height=20)

    # Définir les en-têtes
    tree_cons.column('nom_cons', width=400)
    tree_cons.column('id_cons', width=75) 
    tree_cons.column("qtestock_cons", width=100)
    tree_cons.column("qteseuil_cons", width=100)
    tree_cons.column("prix_unitaire_cons", width=300)
    tree_cons.heading('id_cons', text='ID')
    tree_cons.heading('nom_cons', text='Nom ')
    tree_cons.heading('qtestock_cons', text='Q S')
    tree_cons.heading('qteseuil_cons', text='Q s')
    tree_cons.heading('prix_unitaire_cons', text='PU')
    tree_cons.heading('categorie', text='Categorie')
    for ligne in listes_cons:
        tree_cons.insert('', tk.END, values=ligne)
    tree_cons.pack()