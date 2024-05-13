
import customtkinter as ctk

#--------
import setting as set
import un_employe as unemp
def presenter_employer(employees, framescroll):
        listeFrame= ctk.CTkScrollableFrame(framescroll, width=800, height=600,fg_color=set.col_blanc_4, 
                                           border_color=set.col_noir_1, border_width=0)
        listeFrame.place(x=125,y=20)
        
        
        for  el in employees:
            unemp.build_empoye(el,listeFrame)
            
