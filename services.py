import customtkinter as ctk
from tkinter import ttk


def services(framescrol):
    #Définition des Services
    #titre
    titre_service = ctk.CTkLabel(framescrol,text="LES SERVICES", font = ('Montsérrat', 25), 
                               fg_color ='#000')
    titre_service.pack(padx=5, pady=10)
    #zone
    service = ctk.CTkFrame(framescrol, width=1150, height=500, fg_color="#000", bg_color="#000",
                         border_color="#fff", border_width=1)
    service.pack(pady = 10)