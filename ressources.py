import customtkinter as ctk
from PIL import Image

import categories as cat
import consommables as cons
import services as serv
import setting as set
import attribution as attr
import approvisionnement as app

def build_home(framescrol):
    
    def switch(label,aff_frame_x,page):

        for widget in slide_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                widget.configure(fg_color =set.col_noir_1)
        
        label.configure(fg_color = set.col_blanc_4)

        for iframe in aff_frame_x.winfo_children():
            iframe.destroy()
        
        aff_frame_x.update()
        page()

    #zone de lien
    slide_frame = ctk.CTkFrame(framescrol, width=200, height= 650, border_color= set.col_border, border_width=1,
                                fg_color=set.col_noir_1, corner_radius=0)
    slide_frame.place(x=0, y=0)

    #zone d'affichage
    aff_frame = ctk.CTkFrame(framescrol, width=993, height= 645, border_color= set.col_border, border_width=1,
                                fg_color=set.col_blanc_4, corner_radius=0)
    aff_frame.place(x=200, y=0)

    


    #Les boutons
    categorie = ctk.CTkButton(slide_frame,text='categories de consommables'.upper(),width=190, height=40, fg_color=set.col_noir_1
                              ,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch(cat_l,aff_frame,page_categories))
    categorie.place(x=2,y=1)
    cat_l = ctk.CTkLabel(slide_frame,text="", width=15,height=40, fg_color=set.col_blanc_4)
    cat_l.place(x=192,y=1)



    consommable = ctk.CTkButton(slide_frame,text="Les consommables".upper(), width=190, height=40, fg_color=set.col_noir_1,
                                corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch(cons_l,aff_frame, page_consommable))
    consommable.place(x=2,y=42)
    cons_l = ctk.CTkLabel(slide_frame,text="", width=15,height=40)
    cons_l.place(x=192,y=42)


    distribuer = ctk.CTkButton(slide_frame,text="Attribution de consommables".upper(), width=190, height=40, fg_color=set.col_noir_1,
                               corner_radius=0, 
                               hover_color=set.col_hover,font= ('Montsérrat',11),  
                           command= lambda : switch(distribuer_l,aff_frame,  page_attribution))
    distribuer.place(x=2,y=84)
    distribuer_l = ctk.CTkLabel(slide_frame,text="", width=15,height=40, )
    distribuer_l.place(x=192,y=84)


    approvisionner = ctk.CTkButton(slide_frame,text="Approvisionnement".upper(), width=190, height=40, fg_color=set.col_noir_1,
                                   corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : switch(approvisionner_l,aff_frame, page_approvisionnement))
    approvisionner.place(x=2,y=126)
    approvisionner_l = ctk.CTkLabel(slide_frame,text="", width=15,height=40)
    approvisionner_l.place(x=192,y=126)


    #Les fonctions
    def page_categories():
         cat.categories(aff_frame)
    page_categories()

    def page_consommable():
        cons.consommable(aff_frame)

    def page_attribution():
        attr.attribuer(aff_frame)

    def page_approvisionnement():
        app.approvisionner(aff_frame)
        
 




























    """cat.categories(framescrol)
    cons.consommables(framescrol)
    serv.services(framescrol)    """



    



    

    