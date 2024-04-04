import customtkinter as ctk
from tkinter import ttk

def consommables(framescrol):
    """ """
    #Définition des consommables
    #titre
    titre_conso = ctk.CTkLabel(framescrol,text="LES CONSOMMABLES", font = ('Montsérrat', 25), 
                               fg_color ='#000')
    titre_conso.pack(padx=5, pady=10)
    #zone
    conso = ctk.CTkFrame(framescrol, width=1150, height=500, fg_color="#000", bg_color="#000",
                         border_color="#fff", border_width=1)
    conso.pack(pady = 10)

    """Formulaire"""
    liste_conso = ctk.CTkLabel(conso, text= "FORMULAIRE", fg_color = "#000",font = ('Montsérrat', 25,'underline'),
                             text_color = "#fff")
    liste_conso.place(x=10, y=5 )

    #Le formulaire
    frame = ctk.CTkFrame(conso, width=400, height=440, bg_color='#000',fg_color='#000',border_color='#fff',
                         border_width=1)
    frame.place(x=10, y=45)

    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(frame, text='ID', font= ("Montsérrat",20))
    id.place(x=5, y=10)

