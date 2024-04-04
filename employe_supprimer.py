import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
from datetime import datetime
import re 

import graphi_print as gp


image_path = ""

def supprimer(frame):
        

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
                image_ctk = ctk.CTkImage(image_pil, size=(200, 270))
                label_photo = ctk.CTkLabel(master=frame,text='', image=image_ctk)
                label_photo.place(x=75, y=120)
            except:
                label_photo = ctk.CTkLabel(master=frame,text="", width=200, height=270, fg_color='#fff',
                                   corner_radius=10)
                label_photo.place(x=75, y=120)
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
            id_is_val=True
            option_de_recherche.configure(border_color = '#fff')
        except:
            id_is_val=False
            option_de_recherche.configure(border_color = 'red')
        
        
        

        if id_is_val:
            
            resultat = messagebox.askquestion("Suppression d'un employe","Confirmez-vous la suppression de l'employe?")
            

            if resultat:
                answer = gp.delete_employe(id_e)
                if answer :
                    messagebox.showwarning("Suppression","Employé(e) supprimé(e)")
                else:
                    messagebox.showwarning("Suppression",".\nImpossible de supprimer l'employé.")


    # Créer une boîte de sélection
    options = ["Choisir un nom"]
    try:
        noms_emp = gp.get_employes()
        for ligne in noms_emp:
            options.append(str(ligne[0])+' '+ligne[1]+' '+ligne[2])
    except :
        messagebox.showwarning('Connexion échoué', """La tentative de connexion à la base de données a échoué.\nVeuillez vérifier le serveur de la base de données ou réessayer plutard!""")
    
    
    
    option_de_recherche = ctk.CTkComboBox(master=frame, width=200, height=30, fg_color="#000", border_width=1, 
                            border_color='#fff', values=options, button_color='#fff',button_hover_color='#000',
                            font=('Montsérrat', 12,),dropdown_font=('Montsérrat',15),
                            dropdown_fg_color= "#000", dropdown_hover_color="#f00", corner_radius=20,
                            )
   
    option_de_recherche.place(x=75, y=20)

    #Bouton recherche
    rechercher = ctk.CTkButton(frame, text="Rechercher", width=200, height=30, fg_color='dark green',
                                  hover_color='blue', command= rechercher_employer,
                                  font=("Montsérrat", 20), corner_radius=20, )
    rechercher.place(x=75, y=60)

    #photo
    photo_emp = ctk.CTkEntry(frame,width=5,text_color="#000", bg_color="#000",fg_color="#000")
    if image_path != "" and image_path !=None:
        photo_emp.insert(0,image_path)
        image_pil = Image.open(image_path)
        image_ctk = ctk.CTkImage(image_pil, size=(200, 270))
        label_photo = ctk.CTkLabel(master=frame,text='', image=image_ctk)
        label_photo.place(x=75, y=120)
    else:
        photo_emp.insert(0,image_path)

        label_photo = ctk.CTkLabel(master=frame,text=image_path, width=200, height=270, fg_color='#fff',
                                   corner_radius=10)
        label_photo.place(x=75, y=120)

        

    #nom
    nom_lb =ctk.CTkLabel(frame, text="Nom",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                         text_color='#ff0',corner_radius=5)
    nom_lb.place(x=320, y=20)
    nom = ctk.CTkEntry(frame, placeholder_text="Nom", width=350, height=35, font=("Montsérrat", 18),
                       border_color='#fff',border_width=1,fg_color="#000",corner_radius=5)
    nom.place(x=320, y=50)

    #prenom
    prenom_lb =ctk.CTkLabel(frame, text="Prénoms",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                            text_color='#ff0',corner_radius=5)
    prenom_lb.place(x=720, y=20)
    prenom = ctk.CTkEntry(frame, placeholder_text="Prénoms", width=350, height=35, font=("Montsérrat", 18),
                          border_color='#fff',border_width=1,fg_color="#000",corner_radius=5)
    prenom.place(x=720, y=50)

    #sexe
    sexe_lb =ctk.CTkLabel(frame, text="Sexe",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                          text_color='#ff0',corner_radius=5)
    sexe_lb.place(x=320, y=120)
    sexe = ctk.CTkComboBox(master=frame, width=350, height=35, fg_color="#000", border_width=1, 
                            border_color='#fff', values=["","Féminin", "Masculin"], button_color='#fff',
                            button_hover_color='#000',font=('Montsérrat', 15),
                            dropdown_font=('Montsérrat',15),
                            dropdown_fg_color= "#000", dropdown_hover_color="#f00", corner_radius=5)
    sexe.place(x=320, y=150)

    #nationalité
    nationalite_lb =ctk.CTkLabel(frame, text="Nationalité",height=20, font = ('Montsérrat', 18), 
                                 text_color='#ff0',fg_color = '#000',corner_radius=5)
    nationalite_lb.place(x=720, y=120)
    nationalite = ctk.CTkEntry(frame, placeholder_text="Nationalités", width=350, height=35, font=("Montsérrat", 18),
                               border_color='#fff',border_width=1,fg_color="#000", corner_radius=5)
    nationalite.place(x=720, y=150)

    #Lieu de residence
    residence_lb =ctk.CTkLabel(frame, text="Lieu de résidence",height=20, font = ('Montsérrat', 18), 
                               text_color='#ff0',fg_color = '#000',corner_radius=5)
    residence_lb.place(x=320, y=210)
    residence = ctk.CTkEntry(frame, placeholder_text="Lieu de résidence", width=350, height=35, font=("Montsérrat", 18),
                               border_color='#fff',border_width=1,fg_color="#000", corner_radius=5)
    residence.place(x=320, y=240)

    #salaire
    salaire_lb =ctk.CTkLabel(frame, text="Salaire en FCFA",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                             text_color='#ff0',corner_radius=5)
    salaire_lb.place(x=720, y=210)
    salaire = ctk.CTkEntry(frame, placeholder_text="Salaire en FCFA", width=350, height=35, font=("Montsérrat", 18),
                               border_color='#fff',border_width=1,fg_color="#000", corner_radius=5)
    salaire.place(x=720, y=240)

    #email
    email_lb =ctk.CTkLabel(frame, text="Email",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                           text_color='#ff0',corner_radius=5)
    email_lb.place(x=320, y=300)
    email = ctk.CTkEntry(frame, placeholder_text="Email@exemple.gp", width=350, height=35, font=("Montsérrat", 18),
                               border_color='#fff',border_width=1,fg_color="#000", corner_radius=5)
    email.place(x=320, y=330)

    #telephone
    telephone_lb =ctk.CTkLabel(frame, text="Téléphone",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                               text_color='#ff0',corner_radius=5)
    telephone_lb.place(x=720, y=300)
    telephone = ctk.CTkEntry(frame, placeholder_text="Téléphone", width=350, height=35, font=("Montsérrat", 18),
                               border_color='#fff',border_width=1,fg_color="#000", corner_radius=5)
    telephone.place(x=720, y=330)

    #date_nais
    date_nais_lb =ctk.CTkLabel(frame, text="Date de naissance ",height=20, font = ('Montsérrat', 18), 
                               text_color='#ff0',fg_color = '#000',corner_radius=5)
    date_nais_lb.place(x=320, y=395)
    date_nais = ctk.CTkEntry(frame, placeholder_text="AAAA-MM-JJ", width=180, height=35, font=("Montsérrat", 18),
                               border_color='#fff',border_width=1,fg_color="#000", corner_radius=5)
    date_nais.place(x=490, y=390)

    #date_emb
    date_emb_lb =ctk.CTkLabel(frame, text="Date d'embauche",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                              text_color='#ff0',corner_radius=5)
    date_emb_lb.place(x=720, y=395)
    date_emb = ctk.CTkEntry(frame, placeholder_text="AAAA-MM-JJ", width=180, height=35, font=("Montsérrat", 18),
                               border_color='#fff',border_width=1,fg_color="#000", corner_radius=5)
    date_emb.place(x=890, y=390)


    #service
    services_lb =ctk.CTkLabel(frame, text="Service",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                              text_color='#ff0',corner_radius=5)
    services_lb.place(x=320, y=440)

    services=["Choisir un service"]
    try:
        
        noms_serv = gp.get_services()
        for ligne in noms_serv:
            services.append(str(ligne[0])+' '+ligne[1])
    except :
        messagebox.showwarning('Connexion échoué', """La tentative de connexion à la base de données a échoué.\nVeuillez vérifier le serveur de la base de données ou réessayer plutard!""")
    
    service = ctk.CTkComboBox(master=frame, width=350, height=35, fg_color="#000", border_width=1, 
                            border_color='#fff', values=services, button_color='#fff',
                            button_hover_color='#000',font=('Montsérrat', 15),
                            dropdown_font=('Montsérrat',15),
                            dropdown_fg_color= "#000", dropdown_hover_color="#f00", corner_radius=5)
    service.place(x=320, y=470)

    #niveau
    niveau_lb =ctk.CTkLabel(frame, text="Niveau d'étude",height=20, font = ('Montsérrat', 18), fg_color = '#000',
                           text_color='#ff0',corner_radius=5)
    niveau_lb.place(x=720, y=440)
    niveau = ctk.CTkEntry(frame, placeholder_text="Niveau d'étude", width=350, height=35, font=("Montsérrat", 18),
                               border_color='#fff',border_width=1,fg_color="#000", corner_radius=5)
    niveau.place(x=720, y=470)


    #bouton de soumission
    soumettre = ctk.CTkButton(frame, text="Supprimer",width=200, height=40, fg_color = 'dark green',
                              hover_color='blue', font=('Montsérrat', 20), command= lambda : suppression())
    soumettre.place(x=75 , y=470)



    