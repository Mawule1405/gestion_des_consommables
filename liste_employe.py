
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
#--------
import graphi_print as gp
import employe_modifier as em
import employe_enregistrer as ee
import employe_supprimer as es
import exportation as ex
import setting as set

def presenter_employer(employees, framescroll):
    
        for el in employees:
            frame_emp = ctk.CTkFrame(framescroll, width=990, height= 300, border_width=1, border_color= "#fff",
                                    fg_color=set.col_fg)
            frame_emp.pack(pady=10, padx=5)
            #Numero
            label_emp =ctk.CTkLabel(frame_emp,text="Employé "+str(el[0]), font=('Montsérrat', 20), text_color=set.col_text)
            label_emp.place(x=10,y=10)

            #Photo
            image_path = el[11]
            try:
                if image_path != None:
                    image_pil = Image.open(image_path)
                    image_ctk = ctk.CTkImage(image_pil, size=(180, 250))
                    label_photo = ctk.CTkLabel(master=frame_emp,text='', image=image_ctk)
                    label_photo.place(x=10, y=40)
            except:
                pass
            
            #Nom
            label_nom =ctk.CTkLabel(frame_emp,text="Nom  : "+el[1], font=('Montsérrat', 15),text_color=set.col_text)
            label_nom.place(x=250,y=40)

            #Prenom
            label_prenom =ctk.CTkLabel(frame_emp,text="Prénoms  : "+el[2],font=('Montsérrat', 15),text_color=set.col_text)
            label_prenom.place(x=600,y=40)

            #Date de naissance
            label_date_nais =ctk.CTkLabel(frame_emp,text="Date de naissance  : "+str(el[3]),font=('Montsérrat', 15),text_color=set.col_text)
            label_date_nais.place(x=250,y=80)

            #Date de naissance
            label_date_emb =ctk.CTkLabel(frame_emp,text="Date d'embauche  : "+str(el[4]),font=('Montsérrat', 15),text_color=set.col_text)
            label_date_emb.place(x=600,y=80)

            #Nationalité
            label_nationalite =ctk.CTkLabel(frame_emp,text="Nationalité  : "+str(el[5]),font=('Montsérrat', 15),text_color=set.col_text)
            label_nationalite.place(x=250,y=120)

            #Niveau d'étude
            label_niveau =ctk.CTkLabel(frame_emp,text="Niveau d'étude  : "+str(el[6]),font=('Montsérrat', 15),text_color=set.col_text)
            label_niveau.place(x=600,y=120)

            #Salaire
            label_salaire =ctk.CTkLabel(frame_emp,text="Salaire  : "+str(el[7])[:-3]+' FCFA',font=('Montsérrat', 15),text_color=set.col_text)
            label_salaire.place(x=250,y=160)

            #Lieu de résidence
            label_lieu_res =ctk.CTkLabel(frame_emp,text="Lieu de résidence  : "+str(el[8]),font=('Montsérrat', 15),text_color=set.col_text)
            label_lieu_res.place(x=600,y=160)

            #email
            label_email =ctk.CTkLabel(frame_emp,text="Email  : "+str(el[9]),font=('Montsérrat', 15),text_color=set.col_text)
            label_email.place(x=250,y=200)

            #contact
            label_contact =ctk.CTkLabel(frame_emp,text="Téléphone  : "+str(el[10]),font=('Montsérrat', 15),text_color=set.col_text)
            label_contact.place(x=600,y=200)

            #service
            label_service =ctk.CTkLabel(frame_emp,text="Service  : "+str(el[12]),font=('Montsérrat', 15),text_color=set.col_text)
            label_service.place(x=250,y=240)

            #sexe
            label_sexe =ctk.CTkLabel(frame_emp,text="Sexe  : "+str(el[13]),font=('Montsérrat', 15),text_color=set.col_text)
            label_sexe.place(x=600,y=240)

            #Bouton detail
            detail = ctk.CTkButton(frame_emp, text="Exporter",width=200, height=40, fg_color = 'dark green',
                                hover_color='blue', font=('Montsérrat', 20),command= lambda: ex.export_employe_information([]) )
            detail.place(x=755,y=243)