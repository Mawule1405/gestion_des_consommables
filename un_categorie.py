#les bibliothèques de python
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from tkinter import messagebox

#Modules de constructes
import setting as set
import graphi_print as gp

def update_categorie(idcat, entry):
    """
    Procéduire de mise à jour des information des champs 
    """
    nom = gp.get_one_categories(idcat)
    entry.configure(state = tk.NORMAL)
    nom = nom[0][0]
    entry.delete(0, tk.END)
    entry.insert(0, nom)
    entry.configure(state = "disable")

def activation_champ(checkin,liste_entry):
    """
    Procéduire d'activation des champs de saisir
    @param: intVar, liste de champs
    @return: None
    """

    valeur = checkin.get()

    if valeur:
        
        liste_entry[1].configure(state=tk.NORMAL)
    else:
    
        liste_entry[1].configure(state="disable")

def modifier(chekin, entrys):
    """
    Procéduire de modification des données
    """
    valeur = chekin.get()
    if valeur:
        id_e = entrys[0]
        id_e.configure(state= tk.NORMAL)
        id= id_e.get()
        id_e.configure(state= "disable")
        nom_e= entrys[1]
        nom = nom_e.get()
        
        if nom:
            categorie = (nom,id)
            reponse = gp.modifier_categories(categorie)
            if reponse:
                update_categorie(id,nom_e)
                chekin.set(0)
                messagebox.showinfo("Modification de catégorie", "La modification a été effectuée avec succès")
            else:
                messagebox.showerror("Modification de catégorie", "Impossible d'effectué cette modification")
    else:
        messagebox.showerror("Modification d'un consommable", "Pour modifier cette consommable, veuillez activer le champs du nom en cliquant sur cochant la case")

def supprimer(id_e, frame ):
    id_e.configure(state= tk.NORMAL)
    id= id_e.get()
    id=int(id)

    reponse = messagebox.askquestion("Supprssion de catégorie", "Êtes vous sûr de vouloir supprimer cette catégorie de consommable")
    if reponse:
        answer = gp.supprimer_categories(id)
        answer = gp.get_one_categories(id)

        if not answer:
            frame.destroy()
            messagebox.showinfo("Suppression de catégorie de consommable", "Suppression effectuée avec succès")
        else:
            messagebox.showerror("Supprision de la catégorie de consommable", "Impossible de supprimer cette catégorie de consommable")
        



def categorie(idcat, formulaire):        
    
    categorie = gp.get_one_categories(idcat)
    categorie = categorie[0]


    id_cat_l = ctk.CTkLabel(formulaire, text= "Identifiant", fg_color=set.col_blanc_1, font = ('Montsérrat', 15,"bold"), text_color=set.col_noir_1, bg_color= "transparent")
    id_cat_l.place(x= 20, y=40)

    id_cat_e = ctk.CTkEntry(formulaire,placeholder_text='0',justify='right' ,fg_color=set.col_blanc_1, width=150,height=40,
                            font = ('Montsérrat', 15),corner_radius=10, placeholder_text_color=set.col_placeholder,bg_color= "transparent",
                            text_color=set.col_noir_1)
    id_cat_e.place(x= 20, y=100)
    id_cat_e.insert(0, idcat)
    id_cat_e.configure(state = "disable")
    
    #Identifiant
    nom_cat_l = ctk.CTkLabel(formulaire, text= "Nom", fg_color=set.col_blanc_1, font = ('Montsérrat', 15, "bold") , text_color= set.col_noir_1)
    nom_cat_l.place(x= 250, y=40)
    nom_cat_e = ctk.CTkEntry(formulaire,placeholder_text='Catégorie name',justify='left' ,fg_color=set.col_blanc_4, width=250,height=40,
                            font = ('Montsérrat', 15),  placeholder_text_color=set.col_placeholder, corner_radius=10, bg_color= "transparent",
                            text_color=set.col_noir_1)
    nom_cat_e.place(x= 250, y=100)
    nom_cat_e.insert(0, categorie[0])
    nom_cat_e.configure(state = "disable")
    
    #liste des entry
    liste_entry = [id_cat_e, nom_cat_e]

    #Les bouttons
    active_number = tk.IntVar()
    active_champs = ctk.CTkCheckBox(formulaire, text="", variable=active_number, bg_color= "transparent" ,command= lambda: activation_champ(active_number, liste_entry))
    active_champs.place(x= 575, y=45)

    modifier_cat = ctk.CTkButton(formulaire, text = "Modifier",width=100,height=40, command=lambda :  modifier(active_number, liste_entry),
                                 fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    modifier_cat.place(x=600, y=40)

    supprimer_cat = ctk.CTkButton(formulaire, text = "Supprimer",width=100,height=40, command = lambda: supprimer(id_cat_e, formulaire),
                                  fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    supprimer_cat.place(x=600, y=100)



def build_categorie(idcat, framescroll):
    
    cat = gp.get_one_categories(idcat)
    cat = cat[0]

    cons_frame = ctk.CTkFrame(framescroll ,width=790, height= 180, fg_color=set.col_blanc_1,border_color=set.col_noir_1, border_width=1 )
    cons_frame.pack(padx=10, pady=5)
    
    fond_image_path =  "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(770,170))

    fond = ctk.CTkLabel(cons_frame,text=0,image=image)
    fond.place(x=2, y=2)
    

    categorie(idcat,cons_frame)


