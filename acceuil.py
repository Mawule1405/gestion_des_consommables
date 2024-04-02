"""
Implimentation de la page d'acceuil de l'application
"""
import customtkinter as ctk
import employe 

#fonction pour switcher entre les options
def switch(indicator_lb,page):
    for child in bar_menu.winfo_children():
        if isinstance(child, ctk.CTkLabel):
            child.configure(bg_color='#000')
    indicator_lb.configure(bg_color="#fff")

    
    for frame in zone.winfo_children():
        frame.destroy()
        root.update()
    page()





root = ctk.CTk()
root.geometry("1200x700+0+0")
root.title('Application de gestion de consommable')
root.resizable(width=False, height=False)




#Définiton de la barre de menu
bar_menu = ctk.CTkFrame(root, width=1200, height=30, fg_color='#000')
bar_menu.place(x=0, y=0)

#Définition des onglets de la barre de menu
#onglet 1
onglet1 = ctk.CTkButton(bar_menu,text = "Acceuil", font= ('Montsérrat', 15),width=150, height=25,
                        hover_color='#f00',fg_color='#000', corner_radius=0,
                        command=lambda: switch(indicator_lb=onglet1_lb, page = page_d_aide))
onglet1.place(x=0, y=2)
onglet1_lb = ctk.CTkLabel(bar_menu, bg_color='#fff', width=150,height=2)
onglet1_lb.place(x=0, y=28)

#onglet 2
onglet2 = ctk.CTkButton(bar_menu,text = "Employés", font= ('Montsérrat', 15),width=150, height=25,
                        hover_color='#f00',fg_color='#000', corner_radius=0,
                        command=lambda: switch(indicator_lb=onglet2_lb, page = page_employe))
onglet2.place(x=150, y=2)
onglet2_lb = ctk.CTkLabel(bar_menu, width=150,height=2)
onglet2_lb.place(x=150, y=28)

#onglet 3
onglet3 = ctk.CTkButton(bar_menu,text = "Ressources", font= ('Montsérrat', 15),width=150, height=25,
                        hover_color='#f00',fg_color='#000', corner_radius=0,
                        command=lambda: switch(indicator_lb=onglet3_lb, page = page_d_aide))
onglet3.place(x=300, y=2)
onglet3_lb = ctk.CTkLabel(bar_menu,text='', width=150,height=2)
onglet3_lb.place(x=300, y=28)

#onglet 4
onglet4 = ctk.CTkButton(bar_menu,text = "Approvisionnement", font= ('Montsérrat', 15),width=150, 
                        height=25,hover_color='#f00',fg_color='#000', corner_radius=0,
                        command=lambda: switch(indicator_lb=onglet4_lb, page = page_d_aide))
onglet4.place(x=450, y=2)
onglet4_lb = ctk.CTkLabel(bar_menu,text='' , width=150,height=2)
onglet4_lb.place(x=450, y=28)

#onglet 5
onglet5 = ctk.CTkButton(bar_menu,text = "Distributions", font= ('Montsérrat', 15),width=150, height=25,
                        hover_color='#f00',fg_color='#000', corner_radius=0,
                        command=lambda: switch(indicator_lb=onglet5_lb, page = page_d_aide))
onglet5.place(x=600, y=2)
onglet5_lb = ctk.CTkLabel(bar_menu,text='', width=150,height=2)
onglet5_lb.place(x=600, y=28)

#onglet 6
onglet6 = ctk.CTkButton(bar_menu,text = "Aides", font= ('Montsérrat', 15),width=150, height=25,
                        hover_color='#f00',fg_color='#000', corner_radius=0,
                        command=lambda: switch(indicator_lb=onglet6_lb, page = page_d_aide))
onglet6.place(x=750, y=2)
onglet6_lb = ctk.CTkLabel(bar_menu,text='', width=150)
onglet6_lb.place(x=750, y=28)

#Définition de la zone de widgets
zone = ctk.CTkFrame(root, width=1190, height=660, fg_color="#000")
zone.place(x=5, y=35)



#Definition des pages
def page_d_aide():
    for i in range(9):
        print(i)

def page_employe():
    emp = ctk.CTkFrame(root, width=1190, height=660, fg_color="#000")
    employe.build_employe(emp)
    emp.place(x=0,y=35)

root.mainloop()