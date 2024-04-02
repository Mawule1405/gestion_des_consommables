import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox 
from PIL import Image, ImageTk

import graphi_print as gp




def modifier(frame):
    #choisir une photo
    def choisir_photo():
        """Procedure qui permet de choisir une photo"""
        app = ctk.CTk()
        app.withdraw()
        types_de_photos=[("Images PNG","*.png"),("Images JPG","*.jpg"),("Images JPEG","*.jpeg")]
        chemin_de_photos = ctk.filedialog.askopenfilename(title="Choisissez une photo", filetypes=types_de_photos)
        try:
                image_pil = Image.open(chemin_de_photos)
                image_ctk = ctk.CTkImage(image_pil, size=(200, 270))
                label_photo = ctk.CTkLabel(master=frame,text='', image=image_ctk)
                label_photo.place(x=75, y=120)
        except:
            pass
        

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
            

            #Insertion des inforamations
            nom.insert(0,employe[0][1])
            prenom.insert(0,employe[0][2])
            nationalite.insert(0,employe[0][5])
            residence.insert(0,employe[0][8])
            salaire.insert(0,int(employe[0][7]))
            email.insert(0,employe[0][9])
            date_nais.insert(0,employe[0][3])
            date_emb.insert(0,employe[0][4])
            telephone.insert(0,employe[0][10])
            
            sex1 = employe[0][13]
            if sex1 != None:
                sex2 = "Masculin" if sex1 == "Féminin" else "Féminin"
                sexe.configure(values=[sex1, sex2 ])

            try:
                image_pil = Image.open(employe[0][11])
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
            
      #  

    
    #Soumettre une modification
    def soumettre():
        pass

    # Créer une boîte de sélection
    options = ["Choisir un nom"]
    try:
        noms_emp = gp.get_employe()
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
    image_path = ""
    if image_path != "" and image_path !=None:
        image_pil = Image.open(image_path)
        image_ctk = ctk.CTkImage(image_pil, size=(200, 270))
        label_photo = ctk.CTkLabel(master=frame,text='', image=image_ctk)
        label_photo.place(x=75, y=120)
    else:
        label_photo = ctk.CTkLabel(master=frame,text=image_path, width=200, height=270, fg_color='#fff',
                                   corner_radius=10)
        label_photo.place(x=75, y=120)

    #Bouton pour changer l'image
    changer_photo = ctk.CTkButton(frame, text="Choisir une image", width=200, height=35, fg_color='dark green',
                                  hover_color='blue', command= lambda: choisir_photo(),
                                  font=("Montsérrat", 20))
    changer_photo.place(x=75, y=405)    

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
    salaire_lb =ctk.CTkLabel(frame, text="Salaire",height=20, font = ('Montsérrat', 18), fg_color = '#000',
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
                              text_color='#fff',corner_radius=5)
    services_lb.place(x=320, y=455)
    services =["Choisir un service", "Service 1", "Service 2", "Service 3", "service 4"]
    service = ctk.CTkComboBox(master=frame, width=650, height=35, fg_color="#000", border_width=1, 
                            border_color='#fff', values=services, button_color='#fff',
                            button_hover_color='#000',font=('Montsérrat', 15),
                            dropdown_font=('Montsérrat',15),
                            dropdown_fg_color= "#000", dropdown_hover_color="#f00", corner_radius=5)
    service.place(x=420, y=450)

    #bouton de soumission
    soumettre = ctk.CTkButton(frame, text="Soumettre",width=200, height=40, fg_color = 'dark green',
                              hover_color='blue', font=('Montsérrat', 20))
    soumettre.place(x=75 , y=470)



    