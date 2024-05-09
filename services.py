import customtkinter as ctk
from tkinter import ttk , messagebox
import tkinter as tk
from datetime import datetime
from PIL import Image

import setting as set
import graphi_print as gp
import un_service as unserv


def ajouter(framescrol, page, zone, dictionnaire):
    """
    Procéduire d'ajout d'un service 
    @param: framescoll (zone des widget), page (fonction de reconstruction), zone (la zane à reconstruire)n dictionnaire des champs de saisis
    @return None
    """

   
    nom= dictionnaire['nomx'].get()  ; nom_val = False
    date = dictionnaire['datex'].get() ; date_val = False
    responsable = dictionnaire['responsablex'].get() ; responsable_val = False
    description = dictionnaire['descriptionx'].get("1.0", "end-1c") ; description_val = False

    
    if nom:
        nom_val = True
        dictionnaire["nomx"].configure(border_color = "black")
    else:
        nom_val = False
        dictionnaire["nomx"].configure(border_color = "red")

    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        date_val = True
        dictionnaire["datex"].configure(border_color = "black")
    except:
        date_val = False
        dictionnaire["datex"].configure(border_color = "red")

    try:
        responsable = int(responsable.split()[0])
        responsable_val = True
        dictionnaire["responsablex"].configure(border_color = "black")
    except:
        responsable_val = False
        dictionnaire["responsablex"].configure(border_color = "red")

    validation = all([ nom_val, date_val, responsable_val])

    if validation:
        reponse = messagebox.askquestion("Ajout d'un nouveau service", f"Validez vous l'ajout du nouveau service {nom}?")

        if reponse == "yes":
            service = (nom, description, date, responsable)
            answer = gp.inserer_service(service)
            if answer :
                
               
                dictionnaire["nomx"].delete(0, tk.END)
                dictionnaire["descriptionx"].delete("1.0", "end")
                dictionnaire["datex"].delete(0, tk.END)
                dictionnaire["responsablex"].set("Choisir un responsable")
                framescrol.destroy()
                page(zone)
                messagebox.showinfo("Ajout d'un nouveau service", f"Bravo! Le service {nom} est créé le {date}")
            else:
                messagebox.showinfo("Ajout d'un nouveau service", f"Désolé! Le service {nom} ne peut être créer. Veuillez réessayer")



def ajouter_service(framescrol, page, zone):

    toplevel = ctk.CTkToplevel()
    toplevel.geometry("800x300")
    toplevel.title("Ajout d'une nouvelle service")
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.resizable(width=False, height=False)
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.attributes('-topmost', True)
    
    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(800,300))

    fond = ctk.CTkLabel(toplevel,text=0,image=image)
    fond.place(x=0, y=0)

    
    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(toplevel, text="Formulaire d'enrégistrement d'un nouveau service".upper(), font= ("Montsérrat",12,'bold'), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    id.place(x=50, y=5)
    
    nom = ctk.CTkLabel(toplevel, text='Nom :', font= ("Montsérrat",15,"bold"), text_color=set.col_noir_1, fg_color= set.col_blanc_4)
    nom.place(x=50, y=25)
    nom_e = ctk.CTkEntry(toplevel, placeholder_text="Nom du service",text_color=set.col_noir_1,fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=270, height=30, corner_radius=5,
                        font= ("Montsérrat",13))
    
    nom_e.place(x=50, y= 70)


    #Date de création du service
    date_creation = ctk.CTkLabel(toplevel, text='Date de créaion :', font= ("Montsérrat",15, "bold"), text_color=set.col_noir_1,
                                  fg_color= set.col_blanc_4)
    date_creation.place(x=400, y=25)
    date_creation_e = ctk.CTkEntry(toplevel, placeholder_text="AAAA-MM-JJ",text_color=set.col_noir_1, 
                                    fg_color= set.col_blanc_4, placeholder_text_color=set.col_placeholder, 
                                    justify = 'left', width=200, height=30, corner_radius=5,
                        font= ("Montsérrat",12, "bold"))
    date_creation_e.place(x=530, y= 25)


    #Quantité seuil du produit a respecter
    option = gp.get_employes()
    options = ["Choisir un service"]+[str(i[0])+' '+i[1]+' '+i[2] for i in option]
    responsable = ctk.CTkLabel(toplevel, text='Responsable :', font= ("Montsérrat",15, "bold"), text_color=set.col_noir_1,
                               fg_color= set.col_blanc_4)
    responsable.place(x=400, y=70)
    responsable_e= ctk.CTkComboBox(master=toplevel, width=200, height=30, fg_color=set.col_blanc_4, border_width=1, 
                            values=options, font=('Montsérrat', 12, "bold"), text_color= set.col_noir_1,  corner_radius=5)
    responsable_e.place(x=530, y= 70)
   


    
    description = ctk.CTkLabel(toplevel, text='Description:', font= ("Montsérrat",15, "bold"), text_color=set.col_noir_1, 
                               fg_color= set.col_blanc_4)
    description.place(x=50, y= 120)

    description_e = ctk.CTkTextbox(toplevel,text_color=set.col_noir_1, fg_color= set.col_blanc_4,
                         width=685, height=50, corner_radius=5, border_width=1, font= ("Montsérrat",16, "bold"))
    description_e.place(x=50, y= 150)
  

    #dictionnaires des éléments
    dictionnaires = {"nomx": nom_e, "datex": date_creation_e, "responsablex":responsable_e, "descriptionx": description_e}

    
    annuler = ctk.CTkButton(toplevel, text = "Annuler",width=150, height=40,font=('Montsérrat', 15),
                                    fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=5,
                                    command = lambda: toplevel.destroy())
    annuler.place(x=95, y=230)

    

    enregistrement = ctk.CTkButton(toplevel, text = "Enrégistrer",width=150, height=40, command = lambda: ajouter(framescrol,page, zone, dictionnaires),
                                  fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=5)
    enregistrement.place(x=525, y=230)




def des_services(framescrol):
    fond_image_path =  "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(993,645))
    fond = ctk.CTkLabel(framescrol,text=0,image=image)
    fond.place(x=0, y=0)

    
    servframe = ctk.CTkScrollableFrame(framescrol, width=800, height=500, fg_color=set.col_blanc_4, 
                         border_color=set.col_noir_1, border_width=0,corner_radius=0)
    servframe.place(x=100, y=30)

    serv = gp.get_services()

    for sev in serv:

        unserv.build_service(sev[0], servframe)


    ajouter = ctk.CTkButton(framescrol, text = "Ajouter une nouvelle catégorie".upper(),width=300,height=40, 
                                  command = lambda : ajouter_service(servframe, des_services,framescrol)
                               ,font=('Montsérrat', 11), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    ajouter.place(x=600, y= 570)
