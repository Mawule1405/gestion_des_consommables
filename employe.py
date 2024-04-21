
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
#--------
import graphi_print as gp
import employe_modifier as em
import employe_enregistrer as ee
import employe_supprimer as es
import exportation as ex
import services as ser
import setting as set

import liste_employe as le

#fonction pour switcher entre les options

def build_employee(frame):

    def switch(aff_frame_x,page):
        for iframe in aff_frame_x.winfo_children():
            iframe.destroy()
        
        aff_frame_x.update()
        page()


    #zone de lien
    slide_frame = ctk.CTkFrame(frame, width=200, height= 680, border_color= set.col_border, border_width=1,
                                fg_color=set.col_fg, corner_radius=0)
    slide_frame.place(x=0, y=0)

    #zone d'affichage
    aff_frame = ctk.CTkFrame(frame, width=975, height= 680,border_width=1,
                                fg_color=set.col_blanc_4, corner_radius=0)
    aff_frame.place(x=200, y=0)

    #Les boutons
    apercu = ctk.CTkButton(slide_frame,text='Liste des employés'.upper(),width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch(aff_frame,page_liste))
    apercu.place(x=2,y=1)

    recherche = ctk.CTkButton(slide_frame,text="Modification d'informations".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch(aff_frame, page_modification))
    recherche.place(x=2,y=42)

    modification = ctk.CTkButton(slide_frame,text="Enregistrement d'un employé".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : switch(aff_frame,  page_enregistrer))
    modification.place(x=2,y=84)

    suppression = ctk.CTkButton(slide_frame,text="Suppression d'un employé".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : switch(aff_frame, page_suppression))
    suppression.place(x=2,y=126), 

    service = ctk.CTkButton(slide_frame,text="Gestion des services".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : switch(aff_frame, page_service))
    service.place(x=2,y=168),

    

    #premier page d'affichage d'employe
    liste_emp = gp.get_employes()
    le.presenter_employer(liste_emp, aff_frame)
    
    #Les ecrans
    def page_liste():
        liste_emp = gp.get_employes()
        le.presenter_employer(liste_emp, aff_frame)
        
    def page_modification():
        em.modifier(aff_frame)

    def page_suppression():
        es.supprimer(aff_frame)

    def page_enregistrer():
        ee.enregistrement(aff_frame)

    def page_service():
        ser.services(aff_frame)
    
    def page_vide():
        print("toto")




    
       








































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































