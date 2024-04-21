import customtkinter  as ctk
from tkinter import ttk
import tkinter as tk
from PIL import Image


import setting as set
import graphi_print as gp


def employe_utilisateur_conso(information,scrolframe):
    """
    Procédure pour présenter un employé qui à effectuer une commande
    paramètre: information est un tuple 
    """
    frame = ctk.CTkFrame(scrolframe, fg_color= set.col_blanc_4, border_width=2, border_color= set.col_noir_1,
                         height=450)
    frame.pack(fill= 'both', pady= 10)

    try:
        image_path = information[-1]
        if image_path != None:
            image_pil = Image.open(image_path)
            image_ctk = ctk.CTkImage(image_pil, size=(150, 150))
            label_photo = ctk.CTkLabel(master=frame,text='', image=image_ctk)
            label_photo.place(x=65, y=5)
    except:
        label_photo = ctk.CTkLabel(master=frame,text='', fg_color=set.col_noir_5, width=150, height=150,
                                   )
        label_photo.place(x=65, y=5)

    
    nom = ctk.CTkLabel(frame,text= f"{information[1]+" "+information[2]}", fg_color= set.col_blanc_4, text_color=set.col_noir_1,
                        font=("Montsérrat", 13, 'bold'))
    nom.place(x=230,y=3)

    date_nais = ctk.CTkLabel(frame,text= f"Né le : {information[3]}", fg_color= set.col_blanc_4, text_color=set.col_noir_1,
                        font=("Montsérrat", 13, 'bold'))
    date_nais.place(x=230,y=28)

    sate_emb = ctk.CTkLabel(frame,text= f"Embauché le : {information[4]}", fg_color= set.col_blanc_4, text_color=set.col_noir_1,
                        font=("Montsérrat", 13, 'bold'))
    sate_emb.place(x=230,y=53)

    lieu_resid = ctk.CTkLabel(frame,text= f"Réside à : {information[5]}", fg_color= set.col_blanc_4, text_color=set.col_noir_1,
                        font=("Montsérrat", 13, 'bold'))
    lieu_resid.place(x=230,y=78)

    email = ctk.CTkLabel(frame,text= f"Email : {information[6]} ", fg_color= set.col_blanc_4, text_color=set.col_noir_1,
                        font=("Montsérrat", 13, 'bold'))
    email.place(x=230,y=102)

    telephone = ctk.CTkLabel(frame,text= f"Téléphone : {information[7]}", fg_color= set.col_blanc_4, text_color=set.col_noir_1,
                        font=("Montsérrat", 13, 'bold'))
    telephone.place(x=230,y=128)

    #=====Liste des commandes
    liste_frame = ctk.CTkScrollableFrame(frame, width=600,height=250, fg_color= set.col_blanc_4)
    liste_frame.place(x=5, y=175)

    style_com = ttk.Style()
    style_com.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), rowheight=5, foreground=set.col_fg)
    style_com.configure("Treeview", font=('Helvetica', 12, 'bold'), rowheight=30,)
    tree_com = ttk.Treeview(liste_frame, columns=('id_com', 'date_com',"nombre_com","montant_com"),
                             show='headings', height=50)

    # Définir les en-têtes
    tree_com.column('id_com', width=75) 
    tree_com.heading('id_com', text='ID')
    tree_com.heading('date_com', text='Date')
    tree_com.heading('nombre_com', text='Nombre Conso')
    tree_com.heading('montant_com', text='Montant (FCFA)')
   
    liste_com = gp.get_commande_of_emp(information[0]) #liste des commandes effectuees par l'employes
    data_1 = []
    data_2 = []
    for ligne in liste_com:
        data_1.append((str(ligne[0]), ligne[3]))
        data_2.append((ligne[2], ligne[3]))
        tree_com.insert('', tk.END, values=ligne)

    tree_com.pack()

    










def liste_emp_utilisateur():
    """
    Procédure permet de lister l'ensemble des employés ayant effectuées de commande
    avec la liste des commandes effectués
    """
    top = ctk.CTkToplevel()
    top.title('Liste des employés ayant effectués de commandes')
    top.geometry('700x600+0+0')
    top.resizable(width=False, height=False)
    top.configure(fg_color = set.col_blanc_4)
    top.attributes('-topmost', True)

    zone_affichage = ctk.CTkScrollableFrame(top, width=650, height=550,corner_radius=5,fg_color=set.col_blanc_4)
    zone_affichage.place(x=25, y=25)

    les_employes = gp.get_emp_commande_conso()

   
    for employe in les_employes:
        employe_utilisateur_conso(employe, zone_affichage)




    top.mainloop()