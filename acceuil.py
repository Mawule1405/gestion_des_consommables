"""
Implimentation de la page d'acceuil de l'application
"""
import customtkinter as ctk
import employe 
import ressources as res
import setting as set
import statistique  as stat
import construire_accueil as ca
from datetime import datetime
import graphi_print as gp
from tkinter import messagebox


#fonction pour switcher entre les options
def switch(indicator_lb,page):
    for child in bar_menu.winfo_children():
        if isinstance(child, ctk.CTkLabel):
            child.configure(fg_color=set.col_noir_1)

    indicator_lb.configure(fg_color=set.col_blanc_4)

    
    for frame in zone.winfo_children():
        frame.destroy()
        root.update()
    page()

def update_time():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y   %H:%M:%S")
    horaire.configure(text=date_time)
    root.after(1000, update_time)  


connexion = gp.connexion_database()
if connexion:

    root = ctk.CTk()
    root._set_appearance_mode(set.col_blanc_4)

    root.geometry("1200x700+0+0")
    root.title('Application de gestion de consommables')
    root.resizable(width=False, height=False)

    root.iconbitmap("images/images_app/logo.ico")


    #Définiton de la barre de menu
    bar_menu = ctk.CTkFrame(root, width=1200, height=50, fg_color=set.col_noir_1, corner_radius=0)
    bar_menu.place(x=0, y=0)

    horaire = ctk.CTkLabel(bar_menu,text = "", width=150, font=("Montsérrat" , 30), fg_color=set.col_noir_1,
                        text_color=set.col_blanc_4)
    horaire.place(x=875, y= 5)
    update_time()
    #Définition des onglets de la barre de menu
    #onglet 1
    onglet1_lb = ctk.CTkLabel(bar_menu,text='', fg_color=set.col_blanc_1, width=150,height=1)
    onglet1_lb.place(x=0, y=28)
    onglet1 = ctk.CTkButton(bar_menu,text = "Acceuil", font= ('Montsérrat', 15),width=150, height=35,
                            fg_color=set.col_noir_1, corner_radius=0,
                            command=lambda: switch(indicator_lb=onglet1_lb, page =page_acceuil))
    onglet1.place(x=0, y=2)


    #onglet 2
    onglet2_lb = ctk.CTkLabel(bar_menu,text='', width=150,height=1)
    onglet2_lb.place(x=150, y=28)
    onglet2 = ctk.CTkButton(bar_menu,text = "Employés", font= ('Montsérrat', 15),width=150, height=35,
                            fg_color=set.col_noir_1, corner_radius=0,
                            command=lambda: switch(indicator_lb=onglet2_lb, page = page_employe))
    onglet2.place(x=150, y=2)


    #onglet 3
    onglet3_lb = ctk.CTkLabel(bar_menu,text='', width=150,height=1)
    onglet3_lb.place(x=300, y=28)
    onglet3 = ctk.CTkButton(bar_menu,text = "Ressources", font= ('Montsérrat', 15),width=150, height=35,
                            fg_color=set.col_noir_1, corner_radius=0,
                            command=lambda: switch(indicator_lb=onglet3_lb, page = page_ressources))
    onglet3.place(x=300, y=2)


    #onglet 4
    onglet4_lb = ctk.CTkLabel(bar_menu,text='' , width=150,height=1)
    onglet4_lb.place(x=450, y=28)
    onglet4 = ctk.CTkButton(bar_menu,text = "Statistiques", font= ('Montsérrat', 15),width=150, 
                            height=35,fg_color=set.col_noir_1 , corner_radius=0,
                            command=lambda: switch(indicator_lb=onglet4_lb, page = page_statistique))
    onglet4.place(x=450, y=2)



    #Définition de la zone de widgets
    zone = ctk.CTkFrame(root, width=1190, height=645, fg_color=set.col_blanc_4)
    zone.place(x=5, y=50)



    #Definition des pages
    #Définition de la page d'acceuil
    def page_acceuil():
        home = ctk.CTkFrame(root, width=1200, height=645, fg_color=set.col_blanc_4,
                                    border_width=0)
        home.place(x=5,y=50)
        ca.build_accueil(home)
    page_acceuil()

    #definition de la page ressource
    def page_ressources():
        home = ctk.CTkFrame(root, width=1200, height=645, fg_color=set.col_blanc_4,
                                    border_color=set.col_border,border_width=0)
        home.place(x=5,y=50)
        res.build_home(home)
        


    #Définition de la page de gestion des employés
    def page_employe():
        emp = ctk.CTkFrame(root, width=1200, height=645, fg_color=set.col_blanc_4)
        employe.build_employee(emp)
        emp.place(x=5,y=50)


    #Définition de la page de statistique
    def page_statistique():
        statistique = ctk.CTkFrame(root, width=1200, height=645, fg_color=set.col_blanc_4)
        stat.build_statistique(statistique)
        statistique.place(x=5,y=50)

    root.mainloop()
else:
    messagebox.showinfo("Connesion impossible", "Erreur de connexion, veuillez contacter le service informatique! Merci")