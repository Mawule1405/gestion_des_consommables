import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
from datetime import datetime
import re 

import graphi_print as gp
import setting as set


image_path = ""

def supprimer(frame):
        
    frame_c = ctk.CTkFrame(frame, fg_color=set.col_blanc_4, border_width=1, corner_radius=5, 
                           width=600 , height=600)
    frame_c.place(x=200,y=20)

    # fonction de recherche
    def rechercher_employer():
        """Procedure qui permet de rechercher un employe"""
        option= option_de_recherche.get()
        option_x = option.split(' ')[0]
        id=0
        try:
            id = int(option_x)
        except:
            id=0
        
        employe = gp.get_one_employe(id_emp=id)

        if employe != []:
            #Nettoyage des chams
            nom.delete(0,tk.END)
            prenom.delete(0,tk.END)
            nationalite.delete(0,tk.END)
            residence.delete(0,tk.END)
            salaire.delete(0,tk.END)
            email.delete(0,tk.END)
            telephone.delete(0,tk.END)
            date_emb.delete(0,tk.END)
            date_nais.delete(0,tk.END)
            niveau.delete(0,tk.END)

            #Insertion des inforamations
            nom.insert(0,employe[0][1])
            prenom.insert(0,employe[0][2])
            date_nais.insert(0,employe[0][3])
            date_emb.insert(0,employe[0][4])
            nationalite.insert(0,employe[0][5])
            niveau.insert(0,employe[0][6])
            salaire.insert(0,int(employe[0][7]))
            residence.insert(0,employe[0][8])
            email.insert(0,employe[0][9])
            telephone.insert(0,employe[0][10])
            sexe.set(employe[0][13])
            service.set(str(employe[0][12])+' '+employe[0][14])

                

            try:
                image_path = employe[0][11]
                photo_emp.delete(0,tk.END)
                photo_emp.insert(0,image_path)
                image_pil = Image.open(image_path)
                image_ctk = ctk.CTkImage(image_pil, size=(150,150))
                label_photo = ctk.CTkLabel(master=frame_c,text='', image=image_ctk)
                label_photo.place(x=10, y=120)
            except:
                label_photo = ctk.CTkLabel(master=frame_c,text="", width=150, height=150, fg_color=set.col_noir_5,
                                   corner_radius=10)
                label_photo.place(x=10, y=120)
        else:
            #Nettoyage des chams
            nom.delete(0,tk.END)
            prenom.delete(0,tk.END)
            nationalite.delete(0,tk.END)
            residence.delete(0,tk.END)
            salaire.delete(0,tk.END)
            email.delete(0,tk.END)
            telephone.delete(0,tk.END)
            date_emb.delete(0,tk.END)
            date_nais.delete(0,tk.END)
            niveau.delete(0,tk.END)
            photo_emp.delete(0,tk.END)
            
      #  

    
    #Soumettre une modification
    def suppression():
        """Une procedure qui sert a modifier les attributs d'un employe"""
        id_e = option_de_recherche.get().split()[0] ; id_is_val = False
        
        #Verification de l'identifiant
        try: 
            id_e = int(id_e)
            option_de_recherche.configure(border_color = '#fff')
            id_is_val=True
        except:
            id_is_val=False
            option_de_recherche.configure(border_color = 'red')
        
        
        if id_is_val:
            
            resultat = messagebox.askquestion("Suppression d'un employe","Confirmez-vous la suppression de l'employe?")

            if resultat == "yes":
                answer = gp.delete_employe(id_e)
                if answer :
                    messagebox.showwarning("Suppression","Employé(e) supprimé(e)")
                    frame.update()
                else:
                    messagebox.showwarning("Suppression",".\nImpossible de supprimer l'employé.")
            
                
        else:
            messagebox.showwarning("Suppression","Identifiant incorrect")
                


    # Créer une boîte de sélection
    options = ["Choisir un nom"]
    try:
        noms_emp = gp.get_employes()
        for ligne in noms_emp:
            options.append(str(ligne[0])+' '+ligne[1]+' '+ligne[2])
    except :
        messagebox.showwarning('Connexion échoué', """La tentative de connexion à la base de données a échoué.\nVeuillez vérifier le serveur de la base de données ou réessayer plutard!""")
    
    
    
    option_de_recherche = ctk.CTkComboBox(master=frame_c, width=150, height=30, fg_color=set.col_blanc_4, border_width=1, 
                            values=options,
                            font=('Montsérrat', 13),dropdown_font=('Montsérrat',15), text_color= set.col_noir_5, corner_radius=5,
                            )
   
    option_de_recherche.place(x=10, y=20)

    #Bouton recherche
    rechercher = ctk.CTkButton(frame_c, text="Rechercher", width=150, height=30, fg_color = set.col_noir_5, command= rechercher_employer,
                                  font=("Montsérrat", 15), corner_radius=5, )
    rechercher.place(x=10, y=60)

    #photo
    photo_emp = ctk.CTkEntry(frame,width=5,text_color="#000", bg_color="#000",fg_color = set.col_fg)
    if image_path != "" and image_path !=None:
        photo_emp.insert(0,image_path)
        image_pil = Image.open(image_path)
        image_ctk = ctk.CTkImage(image_pil, size=(150,150))
        label_photo = ctk.CTkLabel(master=frame,text='', image=image_ctk, corner_radius=10)
        label_photo.place(x=10, y=120)
    else:
        photo_emp.insert(0,image_path)

        label_photo = ctk.CTkLabel(master=frame,text=image_path, width=150, height=150, fg_color = set.col_blanc_5,
                                   corner_radius=10)
        label_photo.place(x=10, y=120)

    

     

    #nom
    nom_lb =ctk.CTkLabel(frame_c, text="Nom :", height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                         text_color=set.col_noir_1, corner_radius=0)
    nom_lb.place(x=170, y=20)
    nom = ctk.CTkEntry(frame_c, placeholder_text="Nom", width=300, height=30, font=("Montsérrat", 13),
                       border_width=1,fg_color=set.col_blanc_4, corner_radius=5,
                       text_color=set.col_noir_1, placeholder_text_color=set.col_placeholder)
    nom.place(x=270, y=20)

    #prenom
    prenom_lb =ctk.CTkLabel(frame_c, text="Prénoms :",height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                            text_color=set.col_noir_1)
    prenom_lb.place(x=170, y=70)
    prenom = ctk.CTkEntry(frame_c, placeholder_text="Prénoms", width=300, height=30, font=("Montsérrat", 13),
                          border_width=1 ,fg_color = set.col_blanc_4 ,corner_radius=5,
                          text_color=set.col_noir_1, placeholder_text_color=set.col_placeholder)
    prenom.place(x=270, y=70)

    #sexe
    sexe_lb =ctk.CTkLabel(frame_c, text="Sexe :",height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                          text_color=set.col_noir_1)
    sexe_lb.place(x=170, y=120)
    sexe = ctk.CTkComboBox(master=frame_c, width=300, height=30, fg_color = set.col_blanc_4, border_width=1, 
                            values=["","Féminin", "Masculin"],font=('Montsérrat', 13), corner_radius=5,)
    sexe.place(x=270, y=120)

    #nationalité
    nationalite_lb =ctk.CTkLabel(frame_c, text="Nationalité :",height=20, font = ('Montsérrat', 15), 
                                 text_color=set.col_noir_1,fg_color = set.col_blanc_4 )
    nationalite_lb.place(x=170, y=170)
    nationalite = ctk.CTkEntry(frame_c, placeholder_text="Nationalité", width=300, height=30, font=("Montsérrat", 13)
                               ,text_color=set.col_noir_1)
    nationalite.place(x=270, y=170)

    #Lieu de residence
    residence_lb =ctk.CTkLabel(frame_c, text="Lieu de résidence :",height=20, font = ('Montsérrat', 15), 
                               text_color=set.col_noir_1, fg_color = set.col_blanc_4, corner_radius=5)
    residence_lb.place(x=170, y=220)
    residence = ctk.CTkEntry(frame_c, placeholder_text="Lieu de résidence", width=270, height=30, font=("Montsérrat", 13),
                               border_width=1,fg_color = set.col_blanc_4, corner_radius=5,
                               placeholder_text_color=set.col_placeholder, text_color=set.col_noir_1)
    residence.place(x=300, y=220)

    #salaire
    salaire_lb =ctk.CTkLabel(frame_c, text="Salaire en FCFA :",height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                             text_color=set.col_noir_1,corner_radius=5)
    salaire_lb.place(x=170, y=270)
    salaire = ctk.CTkEntry(frame_c, placeholder_text="Salaire en FCFA", width=270, height=30, font=("Montsérrat", 13),
                               border_width=1, fg_color = set.col_blanc_4, corner_radius=5,
                               placeholder_text_color=set.col_placeholder, text_color=set.col_noir_1)
    salaire.place(x=300, y=270)

    #email
    email_lb =ctk.CTkLabel(frame_c, text="Email :",height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                           text_color=set.col_noir_1 ,corner_radius=5)
    email_lb.place(x=170, y=320)
    email = ctk.CTkEntry(frame_c, placeholder_text="Email@exemple.gp", width=300, height=30, font=("Montsérrat", 13),
                                text_color=set.col_noir_1,border_width=1,fg_color = set.col_blanc_4, corner_radius=5,
                               placeholder_text_color=set.col_placeholder)
    email.place(x=270, y=320)

    #telephone
    telephone_lb =ctk.CTkLabel(frame_c, text="Téléphone :",height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                               text_color=set.col_noir_1, corner_radius=5)
    telephone_lb.place(x=170, y=370)
    telephone = ctk.CTkEntry(frame_c, placeholder_text="Téléphone", width=270, height=30, font=("Montsérrat", 13),
                            text_color=set.col_noir_1,border_width=1,fg_color = set.col_blanc_4, corner_radius=5,
                            placeholder_text_color=set.col_placeholder)
    telephone.place(x=300, y=370)

    #date_nais
    date_nais_lb =ctk.CTkLabel(frame_c, text="Date de naissance ",height=20, font = ('Montsérrat', 15), 
                               text_color=set.col_noir_1, fg_color = set.col_blanc_4,corner_radius=5)
    date_nais_lb.place(x=170, y=425)
    date_nais = ctk.CTkEntry(frame_c, placeholder_text="AAAA-MM-JJ", width=180, height=30, font=("Montsérrat", 13),
                               text_color=set.col_noir_1,border_width=1,fg_color = set.col_blanc_4, corner_radius=5,
                               placeholder_text_color=set.col_placeholder)
    date_nais.place(x=170, y=450)

    #date_emb
    date_emb_lb =ctk.CTkLabel(frame_c, text="Date d'embauche",height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                              text_color=set.col_noir_1,corner_radius=5)
    date_emb_lb.place(x=390, y=425)
    date_emb = ctk.CTkEntry(frame_c, placeholder_text="AAAA-MM-JJ", width=180, height=30, font=("Montsérrat", 13),
                               text_color=set.col_noir_1 ,border_width=1,fg_color = set.col_blanc_4, corner_radius=5,
                               placeholder_text_color=set.col_placeholder)
    date_emb.place(x=390, y=450)


    #service
    services_lb =ctk.CTkLabel(frame_c, text="Service :",height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                              text_color=set.col_noir_1,corner_radius=5)
    services_lb.place(x=170, y=500)

    services=["Choisir un service"]
    try:
        
        noms_serv = gp.get_services()
        for ligne in noms_serv:
            services.append(str(ligne[0])+' '+ligne[1])
    except :
        messagebox.showwarning('Connexion échoué', """La tentative de connexion à la base de données a échoué.\nVeuillez vérifier le serveur de la base de données ou réessayer plutard!""")
    
    service = ctk.CTkComboBox(master=frame_c, width=300, height=30, fg_color = set.col_blanc_4, border_width=1, 
                             values=services ,font=('Montsérrat', 13),
                            text_color= set.col_noir_1, corner_radius=5)
    service.place(x=270, y=500)

    #niveau
    niveau_lb =ctk.CTkLabel(frame_c, text="Niveau d'étude :",height=20, font = ('Montsérrat', 15), fg_color = set.col_blanc_4,
                           text_color=set.col_noir_1,corner_radius=5)
    niveau_lb.place(x=170, y=550)
    niveau = ctk.CTkEntry(frame_c, placeholder_text="Niveau d'étude", width=270, height=30, font=("Montsérrat", 13),
                                text_color=set.col_noir_1, border_width=1,fg_color = set.col_blanc_4,
                                corner_radius=5, placeholder_text_color=set.col_placeholder)
    niveau.place(x=300, y=550)



    #bouton de soumission
    soumettre = ctk.CTkButton(frame_c, text="Supprimer",width=150, height=30, fg_color = set.col_noir_5, corner_radius=5,
                              hover_color=set.col_hover, font=('Montsérrat', 15), command= lambda : suppression())
    soumettre.place(x=10 , y=550)



    