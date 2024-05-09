import customtkinter as ctk


import setting as set
import graphi_print as gp
import un_consommable as uncons



def consommable(framescrol):
    liste_cons = ctk.CTkScrollableFrame(framescrol, height=630,width=970)
    liste_cons.pack(fill = 'both')
    
    
    liste_des_consommables = gp.get_consommables()
    for cons in liste_des_consommables:
        uncons.build_consommable(cons[0] ,liste_cons)
    
   
    