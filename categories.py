import customtkinter as ctk
from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image


import graphi_print as gp
import setting as set
import un_categorie as uncat

def enregistrer(entry, frame, page, frame2):
    """
    Procéduire d'enrégistrement d'une nouvelle catégorie
    @param: entry de nom, frame (zone de widget), page (la page à mettre jour)
    @return: none
    """
    nom = entry.get()
    if nom:
        entry.configure(border_color = "black")
        reponse = messagebox.askquestion("Ajout d'une nouvelle catégorie", "Veuillez confirmez l'ajout de la nouvelle catégorie")
        if reponse == "yes":
            answer = gp.inserer_categorie(nom)
            if answer:
                frame.destroy()
                page(frame2)
                messagebox.showinfo("Ajout d'une nouvelle catégorie", "Ajout de consommable effectuée avec succès")
            else:
                messagebox.showinfo("Ajout d'une nouvelle catégorie", "Ajout de catégorie échoué. Veuillez réessayer!")
    else:
        entry.configure(border_color = "red")

 
def ajouter_categorie(frame, page,frame2):
    """
    Procéduire de gestion d'ajout d'une nouvelle catégrie
    @param: frame (zone des widgets) et page (la page à mettre à jour)
    @return: none
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("520x200")
    toplevel.title("Ajout d'une nouvelle catégorie")
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.resizable(width=False, height=False)
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.attributes('-topmost', True)
    
    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(500,200))

    fond = ctk.CTkLabel(toplevel,text=0,image=image)
    fond.place(x=0, y=0)

    
    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(toplevel, text="Formulaire d'enrégistrement d'un nouveau catégorie".upper(), font= ("Montsérrat",12,'bold'), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    id.place(x=50, y=5)
    

    #Nom du produit
    nom = ctk.CTkLabel(toplevel, text='Nom :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    nom.place(x=50, y=45)
    nom_e = ctk.CTkEntry(toplevel, placeholder_text="Nom du catégorie",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=300, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    nom_e.place(x=200, y= 45)
 


    annulation = ctk.CTkButton(toplevel, text = "Annuler",width=100,height=40, command = lambda: toplevel.destroy()
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    annulation.place(x=50, y=130)

    enregistrement = ctk.CTkButton(toplevel, text = "Enrégistrer",width=100,height=40, command = lambda : enregistrer(nom_e, frame, page, frame2)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    enregistrement.place(x=350, y=130)

    toplevel.mainloop()


def categories(framescrol):
    fond_image_path =  "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(993,645))
    fond = ctk.CTkLabel(framescrol,text=0,image=image)
    fond.place(x=0, y=0)

    
    catframe = ctk.CTkScrollableFrame(framescrol, width=800, height=500, fg_color=set.col_blanc_4, 
                         border_color=set.col_noir_1, border_width=0,corner_radius=0)
    catframe.place(x=100, y=30)

    cats = gp.get_categories()

    for element in cats:
        uncat.build_categorie(element[0], catframe)
    
    ajouter = ctk.CTkButton(framescrol, text = "Ajouter une nouvelle catégorie".upper(),width=300,height=40, 
                                  command = lambda : ajouter_categorie(catframe, categories,framescrol)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    ajouter.place(x=600, y= 570)