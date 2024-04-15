import customtkinter as ctk

import categories as cat
import consommables as cons
import services as serv
import setting as set
import attribution as attr
import approvisionnement as app

def build_home(framescrol):
    
    def switch(liste_button,aff_frame_x,page):
        for widget in slide_frame.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.configure(fg_color = "#f00",hover_color= "#f00")
        
        for widget in liste_button:
            if isinstance(widget, ctk.CTkButton):
                widget.configure(fg_color = set.col_fg, hover_color = set.col_hover)

        for iframe in aff_frame_x.winfo_children():
            iframe.destroy()
        
        aff_frame_x.update()
        page()

    #zone de lien
    slide_frame = ctk.CTkFrame(framescrol, width=200, height= 650, border_color= set.col_border, border_width=1,
                                fg_color=set.col_fg, corner_radius=0)
    slide_frame.place(x=0, y=0)

    #zone d'affichage
    aff_frame = ctk.CTkFrame(framescrol, width=993, height= 645, border_color= set.col_border, border_width=1,
                                fg_color="#f00", corner_radius=0)
    aff_frame.place(x=200, y=0)

    #Les boutons
    categorie = ctk.CTkButton(slide_frame,text='categories de consommables'.upper(),width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch([consommable, distribuer, approvisionner],aff_frame,page_categories))
    categorie.place(x=2,y=1)

    consommable = ctk.CTkButton(slide_frame,text="Les consommables".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch([categorie, distribuer, approvisionner],aff_frame, page_consommable))
    consommable.place(x=2,y=42)

    distribuer = ctk.CTkButton(slide_frame,text="Attribution de consommables".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, 
                               hover_color=set.col_hover,font= ('Montsérrat',11),  
                           command= lambda : switch([categorie,consommable,  approvisionner],aff_frame,  page_attribution))
    distribuer.place(x=2,y=84)

    approvisionner = ctk.CTkButton(slide_frame,text="Approvisionnement".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : switch([consommable, distribuer, categorie],aff_frame, page_approvisionnement))
    approvisionner.place(x=2,y=126),


    #Les fonctions
    def page_categories():
         cat.categories(aff_frame)

    def page_consommable():
        cons.consommables(aff_frame)

    def page_attribution():
        attr.attribuer(aff_frame)

    def page_approvisionnement():
        app.approvisionner(aff_frame)
        
    def page_vide():
        attr.attribuer(aff_frame)




























    """cat.categories(framescrol)
    cons.consommables(framescrol)
    serv.services(framescrol)    """



    



    

    