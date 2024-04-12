import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
from datetime import datetime
import re 

import graphi_print as gp
import setting as set

image_path = ""

def enregistrement(frame):
    #choisir une photo
    def choisir_photo():
        """Procedure qui permet de choisir une photo"""
        app = ctk.CTk()
        app.withdraw()
        types_de_photos=[("Images JPG","*.jpg"),("Images JPEG","*.jpeg"),("Images PNG","*.png"),]
        chemin_de_photos = ctk.filedialog.askopenfilename(title="Choisissez une photo", filetypes=types_de_photos)
        try:
                image_path = chemin_de_photos
                photo_emp.delete(0,tk.END)
                photo_emp.insert(0,image_path)
                image_pil = Image.open(image_path)
                image_ctk = ctk.CTkImage(image_pil, size=(200, 270))
                label_photo = ctk.CTkLabel(master=frame,text='', image=image_ctk)
                label_photo.place(x=10, y=20)
                app.destroy()
        except:
            app.destroy()
            

    
    #Soumettre une modification
    def enregistrer():
        """Une procedure qui sert a modifier les attributs d'un employe"""
        
        nom_e = nom.get()                           ; nom_is_val = False
        prenom_e = prenom.get()                     ; prenom_is_val = False
        date_nais_e = date_nais.get()               ; date_nais_is_val = False
        date_emb_e = date_emb.get()                 ; date_emb_is_val = False
        nationalite_e = nationalite.get()           ; nationalite_is_val = False
        niveau_e = niveau.get()                     ; niveau_is_val = False
        salaire_e = salaire.get()                   ; salaire_is_val = False
        residence_e = residence.get()               ; residence_is_val = False
        email_e = email.get()                       ; email_is_val= False
        telephone_e = telephone.get()               ; telephone_is_val = False
        sexe_e = sexe.get()                         ; sexe_is_val = False
        service_e = service.get().split()[0]        ; service_is_val = False
        photo_e = photo_emp.get()   
        photo_e= photo_e.replace('/','\\')
        photo_emp.delete(0, tk.END)
        photo_emp.insert(0,"RECUPERE VAL")                
        
        tousValides = False
        
        
        #verification du nom
        if nom_e !='':
            nom_is_val= True
            nom.configure(border_color = '#fff')
        else:
            nom_is_val= False
            nom.configure(border_color = 'red')

        #verification du prenom
        if prenom_e !='':
            prenom_is_val= True
            prenom.configure(border_color = '#fff')
        else:
            prenom_is_val= False
            prenom.configure(border_color = 'red')

        #verification de la date de naissance
        try:
            date_nais_is_val= True
            date_nais_e = datetime.strptime(date_nais_e, '%Y-%m-%d').date()
            date_nais.configure(border_color = '#fff')
        except:
            date_nais_is_val= False
            date_nais.configure(border_color = 'red')
        
        #verification de la date d'embauche
        try:
            date_emb_is_val = True
            date_emb_e = datetime.strptime(date_emb_e, '%Y-%m-%d').date()
            date_emb.configure(border_color = '#fff')
        except:
            date_emb_is_val = False
            date_emb.configure(border_color = 'red')
        
        #Verification de la nationalite
        if nationalite_e !='':
            nationalite_is_val= True
            nationalite.configure(border_color = '#fff')
        else:
            nationalite_is_val= False
            nationalite.configure(border_color = 'red')

        #Verification de la niveau
        if niveau_e !='':
            niveau_is_val= True
            niveau.configure(border_color = '#fff')
        else:
            niveau_is_val= False
            niveau.configure(border_color = 'red')

        #Verification de la residence
        if residence_e !='':
            residence_is_val= True
            residence.configure(border_color = '#fff')
        else:
            residence_is_val= False
            residence.configure(border_color = 'red')

        #Verification de la email
        regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        if re.search(regex, email_e):
            email_is_val= True
            email.configure(border_color = '#fff')
        else:
            email_is_val= False
            email.configure(border_color = 'red')

        #Verification de la telephone
        regrex1 = r"^(?:\+|00)[0-9]{11,}"

        if re.search(regrex1, telephone_e):
            telephone_is_val= True
            telephone.configure(border_color = '#fff')
        else:
            telephone_is_val= False
            telephone.configure(border_color = 'red')


        #Verification de la telephone
        regrex2 = r"^[1-9][0-9]{5,10}$"

        if re.search(regrex2, salaire_e):
            salaire_e = int(salaire_e)
            salaire_is_val= True
            salaire.configure(border_color = '#fff')
        else:
            salaire_is_val= False
            salaire.configure(border_color = 'red')

        #Verification de la sexe
        if sexe_e !='':
            sexe_is_val= True
            sexe.configure(border_color = '#fff')
        else:
            sexe_is_val= False
            sexe.configure(border_color = 'red')

        #Verification de la service
        try:
            service_is_val= True
            service_e = int(service_e)
            service.configure(border_color = '#fff')
        except:
            service_is_val= False
            service.configure(border_color = 'red')

        
        tousValides = all([nom_is_val, prenom_is_val, date_nais_is_val, date_emb_is_val, 
                           nationalite_is_val, niveau_is_val, salaire_is_val, residence_is_val, 
                           email_is_val, telephone_is_val, sexe_is_val, service_is_val])

        if tousValides:
            tuples_attributs = (
                 nom_e, prenom_e, date_nais_e, date_emb_e,
                nationalite_e, niveau_e, salaire_e, residence_e,
                email_e, telephone_e,photo_e,  service_e, sexe_e
            )
            
            resultat = gp.inserer_employe(information=tuples_attributs)

            if resultat:
                messagebox.showwarning("Résultat de la soumission","Enregistrement effectué avec succès")

            else:
                messagebox.showwarning("Résultat de la soumission","L'enregistrement a échoué")
        else:
            messagebox.showwarning("Valeurs invalides","Veuillez vérifier les champs.\nUn champs de bordure rouge signifie que la valeur est invalide.")


    # Créer une boîte de sélection
    options = ["Choisir un nom"]
    try:
        noms_emp = gp.get_employes()
        for ligne in noms_emp:
            options.append(str(ligne[0])+' '+ligne[1]+' '+ligne[2])
    except :
        messagebox.showwarning('Connexion échoué', """La tentative de connexion à la base de données a échoué.\nVeuillez vérifier le serveur de la base de données ou réessayer plutard!""")
    

    
    #photo
    photo_emp = ctk.CTkEntry(frame,width=5,text_color="#000", bg_color="#000",fg_color="#000")
    if image_path != "" and image_path !=None:
        photo_emp.insert(0,image_path)
        image_pil = Image.open(image_path)
        image_ctk = ctk.CTkImage(image_pil, size=(200, 270))
        label_photo = ctk.CTkLabel(master=frame,text='', image=image_ctk)
        label_photo.place(x=10, y=20)
    else:
        photo_emp.insert(0,image_path)

        label_photo = ctk.CTkLabel(master=frame,text=image_path, width=200, height=270, fg_color='#fff',
                                   corner_radius=10)
        label_photo.place(x=10, y=20)

    #Bouton pour changer l'image
    changer_photo = ctk.CTkButton(frame, text="Choisir une image", width=200, height=35, fg_color=set.col_btn_bg,
                                  hover_color=set.col_hover, command= lambda: choisir_photo(), corner_radius=0,
                                  font=("Montsérrat", 20))
    changer_photo.place(x=10, y=305)    

    #nom
    nom_lb =ctk.CTkLabel(frame, text="Nom",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                         text_color="#ff0",corner_radius=0)
    nom_lb.place(x=250, y=20)
    nom = ctk.CTkEntry(frame, placeholder_text="Nom", width=350, height=35, font=("Montsérrat", 18),
                       border_color=set.col_border,border_width=1,fg_color=set.col_fg,corner_radius=0,
                       text_color=set.col_text, placeholder_text_color=set.col_placeholder)
    nom.place(x=250, y=50)

    #prenom
    prenom_lb =ctk.CTkLabel(frame, text="Prénoms",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                            text_color="#ff0",corner_radius=0)
    prenom_lb.place(x=620, y=20)
    prenom = ctk.CTkEntry(frame, placeholder_text="Prénoms", width=350, height=35, font=("Montsérrat", 18),
                          border_color=set.col_border,border_width=1,fg_color = set.col_fg,corner_radius=0,
                          text_color=set.col_text, placeholder_text_color=set.col_placeholder)
    prenom.place(x=620, y=50)

    #sexe
    sexe_lb =ctk.CTkLabel(frame, text="Sexe",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                          text_color='#ff0',corner_radius=5)
    sexe_lb.place(x=250, y=120)
    sexe = ctk.CTkComboBox(master=frame, width=350, height=35, fg_color = set.col_fg, border_width=1, 
                            border_color=set.col_border, values=["","Féminin", "Masculin"], button_color=set.col_border,
                            button_hover_color=set.col_hover,font=('Montsérrat', 15),
                            dropdown_font=('Montsérrat',15),text_color= set.col_text, dropdown_text_color= set.col_text,
                            dropdown_fg_color= set.col_fg, dropdown_hover_color=set.col_hover, corner_radius=0,)
    sexe.place(x=250, y=150)

    #nationalité
    nationalite_lb =ctk.CTkLabel(frame, text="Nationalité",height=20, font = ('Montsérrat', 18), 
                                 text_color='#ff0',fg_color = set.col_fg,corner_radius=5)
    nationalite_lb.place(x=620, y=120)
    nationalite = ctk.CTkEntry(frame, placeholder_text="Nationalités", width=350, height=35, font=("Montsérrat", 18),
                               border_color=set.col_border,border_width=1,fg_color = set.col_fg, corner_radius=0,
                               placeholder_text_color=set.col_placeholder,text_color=set.col_text)
    nationalite.place(x=620, y=150)

    #Lieu de residence
    residence_lb =ctk.CTkLabel(frame, text="Lieu de résidence",height=20, font = ('Montsérrat', 18), 
                               text_color='#ff0',fg_color = set.col_fg,corner_radius=5)
    residence_lb.place(x=250, y=210)
    residence = ctk.CTkEntry(frame, placeholder_text="Lieu de résidence", width=350, height=35, font=("Montsérrat", 18),
                               border_color=set.col_border,border_width=1,fg_color = set.col_fg, corner_radius=0,
                               placeholder_text_color=set.col_placeholder, text_color=set.col_text)
    residence.place(x=250, y=240)

    #salaire
    salaire_lb =ctk.CTkLabel(frame, text="Salaire en FCFA",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                             text_color='#ff0',corner_radius=5)
    salaire_lb.place(x=620, y=210)
    salaire = ctk.CTkEntry(frame, placeholder_text="Salaire en FCFA", width=350, height=35, font=("Montsérrat", 18),
                               border_color=set.col_border,border_width=1,fg_color = set.col_fg, corner_radius=0,
                               placeholder_text_color=set.col_placeholder, text_color=set.col_text)
    salaire.place(x=620, y=240)

    #email
    email_lb =ctk.CTkLabel(frame, text="Email",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                           text_color='#ff0',corner_radius=5)
    email_lb.place(x=250, y=300)
    email = ctk.CTkEntry(frame, placeholder_text="Email@exemple.gp", width=350, height=35, font=("Montsérrat", 18),
                               border_color=set.col_border, text_color=set.col_text,border_width=1,fg_color = set.col_fg, corner_radius=0,
                               placeholder_text_color=set.col_placeholder)
    email.place(x=250, y=330)

    #telephone
    telephone_lb =ctk.CTkLabel(frame, text="Téléphone",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                               text_color='#ff0',corner_radius=5)
    telephone_lb.place(x=620, y=300)
    telephone = ctk.CTkEntry(frame, placeholder_text="Téléphone", width=350, height=35, font=("Montsérrat", 18),
                               border_color=set.col_border, text_color=set.col_text,border_width=1,fg_color = set.col_fg, corner_radius=0,
                               placeholder_text_color=set.col_placeholder)
    telephone.place(x=620, y=330)

    #date_nais
    date_nais_lb =ctk.CTkLabel(frame, text="Date de naissance ",height=20, font = ('Montsérrat', 18), 
                               text_color='#ff0',fg_color = set.col_fg,corner_radius=5)
    date_nais_lb.place(x=250, y=395)
    date_nais = ctk.CTkEntry(frame, placeholder_text="AAAA-MM-JJ", width=180, height=35, font=("Montsérrat", 18),
                               border_color=set.col_border, text_color=set.col_text,border_width=1,fg_color = set.col_fg, corner_radius=0,
                               placeholder_text_color=set.col_placeholder)
    date_nais.place(x=420, y=390)

    #date_emb
    date_emb_lb =ctk.CTkLabel(frame, text="Date d'embauche",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                              text_color='#ff0',corner_radius=5)
    date_emb_lb.place(x=620, y=395)
    date_emb = ctk.CTkEntry(frame, placeholder_text="AAAA-MM-JJ", width=180, height=35, font=("Montsérrat", 18),
                               border_color=set.col_border, text_color=set.col_text,border_width=1,fg_color = set.col_fg, corner_radius=0,
                               placeholder_text_color=set.col_placeholder)
    date_emb.place(x=780, y=390)


    #service
    services_lb =ctk.CTkLabel(frame, text="Service",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                              text_color='#ff0',corner_radius=5)
    services_lb.place(x=250, y=440)

    services=["Choisir un service"]
    try:
        
        noms_serv = gp.get_services()
        for ligne in noms_serv:
            services.append(str(ligne[0])+' '+ligne[1])
    except :
        messagebox.showwarning('Connexion échoué', """La tentative de connexion à la base de données a échoué.\nVeuillez vérifier le serveur de la base de données ou réessayer plutard!""")
    
    service = ctk.CTkComboBox(master=frame, width=350, height=35, fg_color = set.col_fg, border_width=1, 
                            border_color='#fff', values=services, button_color='#fff',
                            button_hover_color='#000',font=('Montsérrat', 15),
                            dropdown_font=('Montsérrat',15),text_color= set.col_text, dropdown_text_color= set.col_text,
                            dropdown_fg_color= set.col_fg, dropdown_hover_color=set.col_hover, corner_radius=0,)
    service.place(x=250, y=470)

    #niveau
    niveau_lb =ctk.CTkLabel(frame, text="Niveau d'étude",height=20, font = ('Montsérrat', 18), fg_color = set.col_fg,
                           text_color='#ff0',corner_radius=5)
    niveau_lb.place(x=620, y=440)
    niveau = ctk.CTkEntry(frame, placeholder_text="Niveau d'étude", width=350, height=35, font=("Montsérrat", 18),
                               border_color=set.col_border, text_color=set.col_text,border_width=1,fg_color = set.col_fg, corner_radius=0,
                               placeholder_text_color=set.col_placeholder)
    niveau.place(x=620, y=470)




    #bouton de soumission
    soumettre = ctk.CTkButton(frame, text="Soumettre",width=200, height=40, fg_color = set.col_btn_bg,
                              hover_color=set.col_hover, font=('Montsérrat', 20), command= lambda : enregistrer())
    soumettre.place(x=10 , y=470)



    