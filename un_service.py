#Bibliothèque natif de python
import customtkinter as ctk
from PIL import Image
from datetime import datetime
import tkinter as tk
from tkinter import messagebox


#Mes modules
import graphi_print as gp
import setting as set



def activer_champ(checking, dictionnaire):
    valeur = checking.get()

    if valeur:
        for  val in dictionnaire.values():
            val.configure(state = tk.NORMAL)
    else:
        for  val in dictionnaire.values():
            val.configure(state = "disable")

def supprimer(idserv_e, formulaire):

    reponse = messagebox.askquestion("Suppression du service", "Êtes vous sûr de supprimer ce service")

    if reponse == "yes":
        idserv_e.configure(state = "disable")
        id = int(idserv_e.get())

        supprime =gp.supprimer_service(id)
        serv =gp.get_one_service(id)

        if not serv:
            formulaire.destroy()
            messagebox.showinfo("Suppression du service", "Suppression effectuée avec succès")
        else:
            messagebox.showerror("Suppression du service", "Impossible de supprimer ce service. Il y a des employés qui y travailles")
        


def modifier(cheking, dictionnaire):
    valeur = cheking.get()

    if valeur:
        id = dictionnaire["idx"].get() ; id_val = False
        nom= dictionnaire['nomx'].get()  ; nom_val = False
        date = dictionnaire['datex'].get() ; date_val = False
        responsable = dictionnaire['responsablex'].get() ; responsable_val = False
        description = dictionnaire['descriptionx'].get("1.0", "end-1c") ; description_val = False

        try:
            id = int(id)
            id_val = True
            dictionnaire["idx"].configure(border_color = "black")
        except:
            dictionnaire["idx"].configure(border_color = "red")
            id_val = False

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

        validation = all([id_val, nom_val, date_val, responsable_val])

        if validation:
            servic = (nom,  description, date,responsable, id)
            answer = gp.update_service(servic)
            service = gp.get_one_service(id)[0]
       
            if answer:

                dictionnaire["idx"].delete(0, tk.END)
                dictionnaire["nomx"].delete(0, tk.END)
                dictionnaire["descriptionx"].delete("1.0", "end")
                dictionnaire["datex"].delete(0, tk.END)
                
                dictionnaire["idx"].insert(0,service[0])
                dictionnaire["nomx"].insert(0,service[1])
                if service[2]:
                    dictionnaire["descriptionx"].insert("1.0", service[2])

                dictionnaire["datex"].insert(0, datetime.strftime(service[3], "%Y-%m-%d"))
                dictionnaire["responsablex"].set(str(service[4])+" "+service[5]+" "+service[6])
                cheking.set(0)

                for val in dictionnaire.values():
                    val.configure(state = "disable")

                messagebox.showinfo("Modification des informations d'un service", "Modification effectuée avec succès")
            else:
                messagebox.showinfo("Modification des informations d'un service", "Impossible d'effectuer la modification")

        
        





    else:
        messagebox.showinfo("Modification des informations d'un service", "Pour faire une modification, veuillez cocher la case")


def service(idserv, formulaire):
    """
    Procéduire d'affichage du service. Placer les widgets dans la zone formulaire
    @param: service, formulaire
    @return: none
    """
    
    serv = gp.get_one_service(idserv)[0]

   
    id = ctk.CTkLabel(formulaire, text='ID :', font= ("Montsérrat",15,"bold"), text_color=set.col_noir_1, fg_color= set.col_blanc_4)
    id.place(x=50, y=25)
    id_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1, fg_color= set.col_blanc_4, 
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=200, height=30, corner_radius=5,
                        font= ("Montsérrat",13))
    id_e.place(x=120, y= 25)
    id_e.insert(0, serv[0])
    id_e.configure(state = "disable")
    
    #Nom du produit
    nom = ctk.CTkLabel(formulaire, text='Nom :', font= ("Montsérrat",15,"bold"), text_color=set.col_noir_1, fg_color= set.col_blanc_4)
    nom.place(x=50, y=70)
    nom_e = ctk.CTkEntry(formulaire, placeholder_text="Nom du service",text_color=set.col_noir_1,fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=200, height=30, corner_radius=5,
                        font= ("Montsérrat",13))
    
    nom_e.place(x=120, y= 70)
    nom_e.insert(0, serv[1])
    nom_e.configure(state = "disable")

   
    #Date de création du service
    date_creation = ctk.CTkLabel(formulaire, text='Date de créaion :', font= ("Montsérrat",15, "bold"), text_color=set.col_noir_1,
                                  fg_color= set.col_blanc_4)
    date_creation.place(x=400, y=25)
    date_creation_e = ctk.CTkEntry(formulaire, placeholder_text="AAAA-MM-JJ",text_color=set.col_noir_1, 
                                    fg_color= set.col_blanc_4, placeholder_text_color=set.col_placeholder, 
                                    justify = 'left', width=200, height=30, corner_radius=5,
                        font= ("Montsérrat",15, "bold"))
    date_creation_e.place(x=530, y= 25)
    date = datetime.strftime(serv[3], "%Y-%m-%d")
    date_creation_e.insert(0, date)
    date_creation_e.configure(state = "disable")

    #Quantité seuil du produit a respecter
    option = gp.get_employes()
    options = ["Choisir un service"]+[str(i[0])+' '+i[1]+' '+i[2] for i in option]
    responsable = ctk.CTkLabel(formulaire, text='Responsable :', font= ("Montsérrat",15, "bold"), text_color=set.col_noir_1,
                               fg_color= set.col_blanc_4)
    responsable.place(x=400, y=70)
    responsable_e= ctk.CTkComboBox(master=formulaire, width=200, height=30, fg_color=set.col_blanc_4, border_width=1, 
                            values=options, font=('Montsérrat', 12, "bold"), text_color= set.col_noir_1,  corner_radius=5)
    responsable_e.place(x=530, y= 70)
    responsable_e.set(str(serv[4])+' '+serv[5]+' '+serv[6])
    responsable_e.configure(state = "disable")


    
    description = ctk.CTkLabel(formulaire, text='Description:', font= ("Montsérrat",15, "bold"), text_color=set.col_noir_1, 
                               fg_color= set.col_blanc_4)
    description.place(x=50, y= 120)

    description_e = ctk.CTkTextbox(formulaire,text_color=set.col_noir_1, fg_color= set.col_blanc_4,
                         width=685, height=50, corner_radius=5, border_width=1, font= ("Montsérrat",16, "bold"))
    description_e.place(x=50, y= 150)
    if serv[2]:
        description_e.insert("end", serv[2])
    description_e.configure(state = "disable")

    #dictionnaires des éléments
    dictionnaires = {"idx":id_e, "nomx": nom_e, "datex": date_creation_e, "responsablex":responsable_e, "descriptionx": description_e}
    active_number = tk.IntVar()
    active_champ = ctk.CTkCheckBox(formulaire,text ="", variable= active_number, command = lambda: activer_champ(active_number, dictionnaires) )
    active_champ.place(x=95, y=240) 

    
    modification = ctk.CTkButton(formulaire, text = "Modifier",width=150, height=40,font=('Montsérrat', 15),
                                    fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=5,
                                    command = lambda: modifier(active_number, dictionnaires))
    modification.place(x=120, y=230)

    

    supprimer_cons = ctk.CTkButton(formulaire, text = "Supprimer",width=150, height=40, command = lambda: supprimer(id_e, formulaire),font=('Montsérrat', 15),
                                  fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=5)
    supprimer_cons.place(x=525, y=230)



def build_service(idserv, frame):
    """
    Procéduire permettant de construire un service
    @param: le service , frame
    @return: none
    """
    
    cons_frame = ctk.CTkFrame(frame ,width=790, height= 300, fg_color=set.col_blanc_1,border_color=set.col_noir_1, border_width=1 )
    cons_frame.pack(padx=10, pady=5)
    
    fond_image_path =  "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(770, 295))

    fond = ctk.CTkLabel(cons_frame,text=0,image=image)
    fond.place(x=2, y=2)

    service(idserv,cons_frame)



