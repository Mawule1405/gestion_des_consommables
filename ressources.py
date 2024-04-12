import customtkinter as ctk

import categories as cat
import consommables as cons
import services as serv
import setting as set

def build_home(framescrol):
    
    def switch(aff_frame_x,page):
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
                           font= ('Montsérrat',11), command= lambda : switch(aff_frame,page_categories))
    categorie.place(x=2,y=1)

    consommable = ctk.CTkButton(slide_frame,text="Les consommables".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch(aff_frame, page_consommable))
    consommable.place(x=2,y=42)

    distribuer = ctk.CTkButton(slide_frame,text="Attributions".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : switch(aff_frame,  page_vide))
    distribuer.place(x=2,y=84)

    approvisionner = ctk.CTkButton(slide_frame,text="Approvisionnement".upper(), width=196, height=40, fg_color=set.col_fg,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : switch(aff_frame, page_vide))
    approvisionner.place(x=2,y=126),


    #Les fonctions
    def page_categories():
         cat.categories(aff_frame)

    def page_consommable():
        cons.consommables(aff_frame)

    def page_vide():
        titre = "aaaaaaaaaaaaaaaaaaaa".upper()
        print(titre)
        titrel= ctk.CTkLabel(aff_frame, text= titre, font=('Arial', 30))
        titrel.place(x=200, y=200)





























    """cat.categories(framescrol)
    cons.consommables(framescrol)
    serv.services(framescrol)    """



    



    

    