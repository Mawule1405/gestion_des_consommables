import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk
from datetime import datetime
import re , shutil

import graphi_print as gp
import setting as set


def deplacer_fichier(source, destination):
    """
    Procédure permettant de copier un fichier d'un dossier source vers un dossier destination
    @param: source (file), destination (direction)
    @return : None
    """
    try:
        shutil.copy(source, destination)
        
    except PermissionError:
        messagebox.showerror("Alerte", "Permission non accordée")
    



def modifier(frame):

    frame_c = ctk.CTkFrame(frame, fg_color=set.col_blanc_4, border_width=1, corner_radius=5, 
                           width=600 , height=600)
    frame_c.place(x=200,y=20)

    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(600,600))

    fond = ctk.CTkLabel(frame_c,text=0,image=image)
    fond.place(x=0, y=0)

    image_path = ""
    #choisir une photo
    def choisir_photo():
        """Procedure qui permet de choisir une photo"""
        app = ctk.CTk()
        app.withdraw()
        types_de_photos=[("Images JPG","*.jpg"),("Images JPEG","*.jpeg"),("Images PNG","*.png"),]
        chemin_de_photos = ctk.filedialog.askopenfilename(title="Choisissez une photo", filetypes=types_de_photos)
        try:
            nom_image = chemin_de_photos.split('/')[-1]
            destination = "C://wamp64/www/DEV/image/photo_employe"
            deplacer_fichier(chemin_de_photos, destination)
            chemin_de_photos = destination+"/"+nom_image

            image_path = chemin_de_photos
            photo_emp.delete(0,tk.END)
            photo_emp.insert(0,image_path)
            image_pil = Image.open(image_path)
            image_ctk = ctk.CTkImage(image_pil, size=(150, 150))
            label_photo = ctk.CTkLabel(master=frame_c,text='', image=image_ctk)
            label_photo.place(x=10, y=20)
            app.destroy()
        except:
            nom_image = "photo_de_profile.jpeg"
            destination = "C://wamp64/www/DEV/image/photo_employe"
            deplacer_fichier(chemin_de_photos, destination)
            chemin_de_photos = destination+"/"+nom_image

            image_path = chemin_de_photos
            photo_emp.delete(0,tk.END)
            photo_emp.insert(0,image_path)
            image_pil = Image.open(image_path)
            image_ctk = ctk.CTkImage(image_pil, size=(150, 150))
            label_photo = ctk.CTkLabel(master=frame_c,text='', image=image_ctk)
            label_photo.place(x=10, y=20)
            app.destroy()
            
        

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
                image_path = employe[0][11].replace('\\', '/')
                photo_emp.delete(0,tk.END)
                photo_emp.insert(0,image_path)
                image_pil = Image.open(image_path)
                image_ctk = ctk.CTkImage(image_pil, size=(150, 150))
                label_photo = ctk.CTkLabel(master=frame_c,text='', image=image_ctk, )
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
    def modification():
        """Une procedure qui sert a modifier les attributs d'un employe"""
        id_e = option_de_recherche.get().split()[0] ; id_is_val = False
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
        
        #Verification de l'identifiant
        try: 
            id_e = int(id_e)
            id_is_val=True
            option_de_recherche.configure(border_color =set.col_noir_1)
        except:
            id_is_val=False
            option_de_recherche.configure(border_color = 'red')
        
        #verification du nom
        if nom_e !='':
            nom_is_val= True
            nom.configure(border_color =set.col_noir_1)
        else:
            nom_is_val= False
            nom.configure(border_color = 'red')

        #verification du prenom
        if prenom_e !='':
            prenom_is_val= True
            prenom.configure(border_color =set.col_noir_1)
        else:
            prenom_is_val= False
            prenom.configure(border_color = 'red')

        #verification de la date de naissance
        try:
            date_nais_is_val= True
            date_nais_e = datetime.strptime(date_nais_e, '%Y-%m-%d').date()
            date_nais.configure(border_color = set.col_noir_1)
        except:
            date_nais_is_val= False
            date_nais.configure(border_color ='red' )
        
        #verification de la date d'embauche
        try:
            date_emb_is_val = True
            date_emb_e = datetime.strptime(date_emb_e, '%Y-%m-%d').date()
            date_emb.configure(border_color = set.col_noir_1)
        except:
            date_emb_is_val = False
            date_emb.configure(border_color = 'red')
        
        #Verification de la nationalite
        if nationalite_e !='':
            nationalite_is_val= True
            nationalite.configure(border_color =set.col_noir_1)
        else:
            nationalite_is_val= False
            nationalite.configure(border_color = 'red')

        #Verification de la niveau
        if niveau_e !='':
            niveau_is_val= True
            niveau.configure(border_color = set.col_noir_1)
        else:
            niveau_is_val= False
            niveau.configure(border_color = 'red')

        #Verification de la residence
        if residence_e !='':
            residence_is_val= True
            residence.configure(border_color = set.col_noir_1)
        else:
            residence_is_val= False
            residence.configure(border_color = 'red')

        #Verification de la email
        regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        if re.search(regex, email_e):
            email_is_val= True
            email.configure(border_color = set.col_noir_1)
        else:
            email_is_val= False
            email.configure(border_color = 'red')

        #Verification de la telephone
        regrex1 = r"^(?:\+|00)[0-9]{11,}"

        if re.search(regrex1, telephone_e):
            telephone_is_val= True
            telephone.configure(border_color = set.col_noir_1)
        else:
            telephone_is_val= False
            telephone.configure(border_color = 'red')


        #Verification de la telephone
        regrex2 = r"^[1-9][0-9]{5,10}$"

        if re.search(regrex2, salaire_e):
            salaire_e = int(salaire_e)
            salaire_is_val= True
            salaire.configure(border_color = set.col_noir_1)
        else:
            salaire_is_val= False
            salaire.configure(border_color = 'red')

        #Verification de la sexe
        if sexe_e !='':
            sexe_is_val= True
            sexe.configure(border_color = set.col_noir_1)
        else:
            sexe_is_val= False
            sexe.configure(border_color = 'red')

        #Verification de la service
        try:
            service_is_val= True
            service_e = int(service_e)
            service.configure(border_color = set.col_noir_1)
        except:
            service_is_val= False
            service.configure(border_color = 'red')

        
        tousValides = all([id_is_val, nom_is_val, prenom_is_val, date_nais_is_val, date_emb_is_val, 
                           nationalite_is_val, niveau_is_val, salaire_is_val, residence_is_val, 
                           email_is_val, telephone_is_val, sexe_is_val, service_is_val])

        if tousValides:
            liste_attributs = (
                 nom_e, prenom_e, date_nais_e, date_emb_e,
                nationalite_e, niveau_e, salaire_e, residence_e,
                email_e, telephone_e,photo_e,  service_e, sexe_e,id_e
            )
            
            resultat = gp.modifier_employe(information=liste_attributs)

            if resultat:
                messagebox.showwarning("Résultat de la soumission","La modification a été effectué avec succès")

            else:
                messagebox.showwarning("Résultat de la soumission","La modification a échoué")
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
        image_ctk = ctk.CTkImage(image_pil, size=(150, 150))
        label_photo = ctk.CTkLabel(master=frame_c,text='', image=image_ctk,corner_radius=10)
        label_photo.place(x=10, y=120)
    else:
        photo_emp.insert(0,image_path)

        label_photo = ctk.CTkLabel(master=frame_c,text=image_path, width=150, height=150, fg_color = set.col_noir_5,
                                   corner_radius=10)
        label_photo.place(x=10, y=120)

    #Bouton pour changer l'image
    changer_photo = ctk.CTkButton(frame_c, text="Choisir une image", width=150, height=30, fg_color=set.col_noir_5,
                                  command= lambda: choisir_photo(),
                                  font=("Montsérrat", 15), corner_radius = 5)
    changer_photo.place(x=10, y=305)    

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
    soumettre = ctk.CTkButton(frame_c, text="Soumettre",width=150, height=30, fg_color = set.col_noir_5,
                              corner_radius=5,
                              font=('Montsérrat', 15), command= lambda : modification())
    soumettre.place(x=10 , y=550)



    