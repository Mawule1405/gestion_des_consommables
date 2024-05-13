import customtkinter as ctk
from tkinter import messagebox
from PIL import Image


import graphi_print as gp
import employe_modifier as em
import employe_enregistrer as ee
import employe_supprimer as es
import exportation as ex
import setting as set

def build_empoye(el, listeFrame):
    frame_emp = ctk.CTkFrame(listeFrame, width=750, height= 300, border_width=1,fg_color=set.col_blanc_4)
    frame_emp.pack(pady=10, padx=5)

    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(750,300))

    fond = ctk.CTkLabel(frame_emp,text=0,image=image)
    fond.place(x=0, y=0)
    #Numero
    label_emp =ctk.CTkLabel(frame_emp,text="Information de l'employé N° :"+str(el[0]), font=('Montsérrat', 15,  "bold", 'underline'), text_color=set.col_noir_1)
    label_emp.place(x=10,y=10)

    #Photo
    image_path = el[11]
    try:
        if image_path != None:
            image_pil = Image.open(image_path)
            image_ctk = ctk.CTkImage(image_pil, size=(150, 150))
            label_photo = ctk.CTkLabel(master=frame_emp,text='', image=image_ctk)
            label_photo.place(x=10, y=40)
    except:
        label_photo = ctk.CTkLabel(master=frame_emp,text='', fg_color=set.col_noir_5, width=150, height=150,
                                   )
        label_photo.place(x=10, y=40)
    
    #Nom
    label_nom =ctk.CTkLabel(frame_emp,text="Nom  : "+el[1], font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_nom.place(x=180,y=40)

    #Prenom
    label_prenom =ctk.CTkLabel(frame_emp,text="Prénoms  : "+el[2],font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_prenom.place(x=400,y=40)

    #Date de naissance
    label_date_nais =ctk.CTkLabel(frame_emp,text="Né(e) le : "+str(el[3]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_date_nais.place(x=180,y=80)

    #Date de naissance
    label_date_emb =ctk.CTkLabel(frame_emp,text="Date d'embauche  : "+str(el[4]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_date_emb.place(x=400,y=80)

    #Nationalité
    label_nationalite =ctk.CTkLabel(frame_emp,text="Nationalité  : "+str(el[5]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_nationalite.place(x=180,y=120)

    #Niveau d'étude
    label_niveau =ctk.CTkLabel(frame_emp,text="Niveau d'étude  : "+str(el[6]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_niveau.place(x=400,y=120)

    #Salaire
    label_salaire =ctk.CTkLabel(frame_emp,text="Salaire  : "+str(el[7])[:-3]+' FCFA',font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_salaire.place(x=180,y=160)

    #Lieu de résidence
    label_lieu_res =ctk.CTkLabel(frame_emp,text="Lieu de résidence  : "+str(el[8]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_lieu_res.place(x=400,y=160)

    #email
    label_email =ctk.CTkLabel(frame_emp,text="Email  : "+str(el[9]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_email.place(x=10,y=200)

    #contact
    label_contact =ctk.CTkLabel(frame_emp,text="Téléphone  : "+str(el[10]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_contact.place(x=400,y=200)

    #service
    label_service =ctk.CTkLabel(frame_emp,text="Service  : "+str(el[12]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_service.place(x=10,y=240)

    #sexe
    label_sexe =ctk.CTkLabel(frame_emp,text="Sexe  : "+str(el[13]),font=('Montsérrat', 15),text_color=set.col_noir_1)
    label_sexe.place(x=400,y=240)

    #Bouton detail
    detail = ctk.CTkButton(frame_emp, text="Exporter",width=150, height=30, fg_color = set.col_noir_5,
                        hover_color='blue', font=('Montsérrat', 20),command= lambda: ex.export_employe_information(el) )
    detail.place(x=575,y=10)