import customtkinter as ctk
from tkinter import ttk , messagebox
import tkinter as tk
from datetime import datetime

import setting as set
import graphi_print as gp

def services(framescrol):

    #Fonctions des boutons
    def recherche():
        """La commande du bouton rechercher permettant de rechercher un service par son identifiant"""
        id = id_e.get() ; id_is_val = False

        try:
            id = int(id)
            id_is_val = True
        except:
            id_is_val = False

        if id_is_val:
            service = gp.get_one_service(id)
            nom_e.delete(0, tk.END)
            description_e.delete("1.0", "end")
            date_creation_e.delete(0,tk.END)

            if service ==[]:
                messagebox.showinfo("Resultat de la recherche", "Identifiant inexistant.\tVeillez vérifier la liste des services!")
            else:
                service = service[0]
                
                nom_e.insert(0,service[1])
                
                description_e.insert("0.0",str(service[2])+"")

                date_creation_e.insert(0,service[3])

                responsable_e.set(str(service[0])+' '+service[4]+' '+service[5])
        else:
            messagebox.showerror("Confirmation de l'identifiant", "Identifiant incorrecte !")

    def enregistrer():
        id = id_e.get()                                ; id_is_val = False
        nom = nom_e.get()                              ; nom_is_val = False
        descr = description_e.get("0.0","end")        ; descrp_is_val = False
        date = date_creation_e.get()                     ; date_is_val =  False
        respon = responsable_e.get()                   ;  resp_is_val = False
       
        #verification de l'id
        try:
            id = int(id)
            id_is_val = True
            id_e.configure(border_color = set.col_border)
        except:
            id_is_val = False
            id_e.configure(border_color = "#f00")
        #verification du nom

        if nom !="":
            nom_is_val =  True
            nom_e.configure(border_color = set.col_border)
        else:
            nom_is_val = False
            nom_e.configure(border_color = "#f00")
            
        #verification du responsable
        try:
            respon_x = int(respon.split()[0])
            resp_is_val = True
            responsable_e.configure(border_color = set.col_border)

        except:
            resp_is_val = False
            responsable_e.configure(border_color = "#f00")



        #verification de la date de creation du service
        
        try:
            date_is_val = True
            date = datetime.strptime(date, '%Y-%m-%d').date()
            date_creation_e.configure(border_color = set.col_border)
        except:
            date_is_val = False
            date_creation_e.configure(border_color = 'red')
    

        tous_valide = id_is_val and nom_is_val and resp_is_val and date_is_val

        if tous_valide:
            serv =(id,nom, descr, date,respon_x)
            
            confirme = messagebox.askquestion("Confirmation", f"Confirmez-vous la création du service: {id} \nNom: {nom} \nResponsable: {respon} \n Date de création: {date} \n Description: {descr}")

            if confirme =='yes':
                res = gp.inserer_service(serv)

                if res :
                    tree_serv.delete(*tree_serv.get_children())
                    listes = gp.get_services()
                    for i in listes:
                        tree_serv.insert('',tk.END, values=i)
                    tree_serv.update()
                    messagebox.showinfo("Réponse de l'enregistrement", "En registrement effectue avec succès")
                else:
                    messagebox.showerror("Réponse de l'enregistrement", f"Un autre identifiant à pour identifiant id= {id}")
                
            else:
                messagebox.showinfo("Réponse de l'enregistrement", "En registrement effectue avec succès")

        else:
            messagebox.showerror("Réponse de l'enregistrement", "Echec d'enrégistrement.\nDonnées incorrctes ou insuffisantes")


    def modifier():
        id = id_e.get()                                ; id_is_val = False
        nom = nom_e.get()                              ; nom_is_val = False
        descr = description_e.get("0.0","end")        ; descrp_is_val = False
        date = date_creation_e.get()                     ; date_is_val =  False
        respon = responsable_e.get()                   ;  resp_is_val = False
       
        #verification de l'id
        try:
            id = int(id)
            id_is_val = True
            id_e.configure(border_color = set.col_border)
        except:
            id_is_val = False
            id_e.configure(border_color = "#f00")
        #verification du nom

        if nom !="":
            nom_is_val =  True
            nom_e.configure(border_color = set.col_border)
        else:
            nom_is_val = False
            nom_e.configure(border_color = "#f00")
            
        #verification du responsable
        try:
            respon_x = int(respon.split()[0])
            resp_is_val = True
            responsable_e.configure(border_color = set.col_border)

        except:
            resp_is_val = False
            responsable_e.configure(border_color = "#f00")



        #verification de la date de creation du service
        
        try:
            date_is_val = True
            date = datetime.strptime(date, '%Y-%m-%d').date()
            date_creation_e.configure(border_color = set.col_border)
        except:
            date_is_val = False
            date_creation_e.configure(border_color = 'red')
    

        tous_valide = id_is_val and nom_is_val and resp_is_val and date_is_val

        if tous_valide:
            serv =(nom, descr, date,respon_x,id)
            
            confirme = messagebox.askquestion("Confirmation", f"Confirmez-vous les nouvelles informations du service: {id} \nNom: {nom} \nResponsable: {respon} \n Date de création: {date} \n Description: {descr}")

            if confirme =='yes':
                res = gp.update_service(serv)

                if res :
                    tree_serv.delete(*tree_serv.get_children())
                    listes = gp.get_services()
                    for i in listes:
                        tree_serv.insert('',tk.END, values=i)
                    tree_serv.update()
                    messagebox.showinfo("Réponse de la modification", "Modification effectuée avec succès")
                else:
                    messagebox.showerror("Réponse de la modification", f"Un autre service a déja pour identifiant id = {id}")
                
            else:
                messagebox.showinfo("Réponse de la modification", "Modification effectuée avec succès")

        else:
            messagebox.showerror("Réponse de la modification", "Echec de la modification .\nDonnées incorrctes ou insuffisantes")

    def supprimer():
        id = id_e.get(); is_val_id = False

        try:
            id = int(id)
            
            is_val_id = True
            id_e.configure(border_color = set.col_border)
        except:
            is_val_id = False
            id_e.configure(border_color = "#f00")
        

        if is_val_id:
            confirme = messagebox.askquestion("Suppression d'un service", "Confirmez vous la suppression d'un service ?")
            if confirme =='yes':
                reponse = gp.supprimer_service(id = id)
                if reponse:
                    messagebox.showinfo("Suppression","Suppression effectuée avec succès")
                    tree_serv.delete(*tree_serv.get_children())
                    listes = gp.get_services()
                    for i in listes:
                        tree_serv.insert('',tk.END, values=i)
                    tree_serv.update()
                else:
                    messagebox.showinfo("Suppression","Suppression échouée. Il se peut que l'identifiant n'existe pas !")
            
    
        else:
            messagebox.showerror("Suppression","Veillez préciser l'identifiant du service à supprimer!")


    #Définition des Services
    #zone
    service = ctk.CTkFrame(framescrol, width=1200, height=640, fg_color=set.col_fg, bg_color=set.col_bg,
                         border_color=set.col_border, border_width=0)
    service.pack(pady = 0, padx=0)


     #Le formulaire
    formulaire = ctk.CTkFrame(service, width=830, height=300, bg_color=set.col_bg,fg_color=set.col_fg ,border_color=set.col_border,
                         border_width=1)
    formulaire.place(x=75, y=25)

    liste_conso = ctk.CTkLabel(service, text= "FORMULAIRE", fg_color =set.col_fg,font = ('Montsérrat', 15),
                             text_color =set.col_text)
    liste_conso.place(x=85, y=10 )

    

    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(formulaire, text='Identifiant :', font= ("Montsérrat",18), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    id.place(x=5, y=35)
    id_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=100, height=30, corner_radius=0,
                        font= ("Montsérrat",16))
    id_e.place(x=150, y= 35)
    
    #Nom du produit
    nom = ctk.CTkLabel(formulaire, text='Nom :', font= ("Montsérrat",18), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    nom.place(x=410, y=35)
    nom_e = ctk.CTkEntry(formulaire, placeholder_text="Nom du service",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=300, height=30, corner_radius=0,
                        font= ("Montsérrat",16))
    nom_e.place(x=520, y= 35)

    #Prix unitaire
    description = ctk.CTkLabel(formulaire, text='Description :', font= ("Montsérrat",18), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    description.place(x=5, y=150)
    description_e = ctk.CTkTextbox(formulaire,text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                         width=670, height=70, corner_radius=0, border_width=1, border_color=set.col_border, 
                        font= ("Montsérrat",16))
    description_e.place(x=150, y= 150)
   
    #Date de création du service
    date_creation = ctk.CTkLabel(formulaire, text='Date de créaion :', font= ("Montsérrat",18), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    date_creation.place(x=5, y=90)
    date_creation_e = ctk.CTkEntry(formulaire, placeholder_text="AAAA-MM-JJ",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'left', width=200, height=30, corner_radius=0,
                        font= ("Montsérrat",16))
    date_creation_e.place(x=150, y= 90)

    #Quantité seuil du produit a respecter
    option = gp.get_employes()
    options = ["Choisir un service"]+[str(i[0])+' '+i[1]+' '+i[2] for i in option]
    responsable = ctk.CTkLabel(formulaire, text='Responsable :', font= ("Montsérrat",18), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    responsable.place(x=410, y=90)
    responsable_e= ctk.CTkComboBox(master=formulaire, width=250, height=30, fg_color=set.col_fg, border_width=1, 
                            border_color=set.col_border, values=options, button_color=set.col_border,button_hover_color=set.col_hover,
                            font=('Montsérrat', 12,),dropdown_font=('Montsérrat',15), text_color= set.col_text, dropdown_text_color= set.col_text,
                            dropdown_fg_color= set.col_fg, dropdown_hover_color=set.col_hover, corner_radius=0,
                            )
   
    responsable_e.place(x=570, y= 90)


    #Les boutons
    rechercher_cons = ctk.CTkButton(formulaire, text = "Rechercher",width=175,height=25,command= recherche,font=('Montsérrat', 20),
                                   fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    rechercher_cons.place(x=5, y=250)
    
    enregistrer_cons = ctk.CTkButton(formulaire, text = "Enregistrer",width=175,height=25,command= enregistrer,font=('Montsérrat', 20),
                                    fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    enregistrer_cons.place(x=215, y=250)

    modifier_cons = ctk.CTkButton(formulaire, text = "Modifier",width=175,height=25,command= modifier,font=('Montsérrat', 20),
                                 fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    modifier_cons.place(x=435, y=250)

    supprimer_cons = ctk.CTkButton(formulaire, text = "Supprimer",width=175,height=25, command = supprimer,font=('Montsérrat', 20),
                                  fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    supprimer_cons.place(x=650, y=250)


    #Listes des services
    listes_serv = gp.get_services()

    liste_serv = ctk.CTkLabel(framescrol, text= "Liste des services".upper(), fg_color=set.col_fg,
                             font = ('Montsérrat', 20), text_color= set.col_text , bg_color=set.col_bg)
    liste_serv.place(x=75, y=350)

    frame_serv = ctk.CTkScrollableFrame(framescrol, width=800, height=220, border_color=set.col_border, border_width=1,
                                             fg_color=set.col_fg, bg_color= set.col_bg, orientation='vertical',
                                             scrollbar_fg_color=set.col_fg)
    frame_serv.place(x=75 , y=400)

    style_serv = ttk.Style()
    style_serv.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'), rowheight=20, foreground=set.col_fg)
    style_serv.configure("Treeview", font=('Helvetica', 13, 'bold'), rowheight=50,)
    tree_serv = ttk.Treeview(frame_serv, columns=('id_serv', 'nom_serv',"description_serv", 'date_creation_serv', 'nom_emp', 'prenom_emp'), 
                             show='headings', height=20)
    
    # Définir les en-têtes
    tree_serv.column('nom_serv', width=200)
    tree_serv.column('id_serv', width=50) 
    tree_serv.column('prenom_emp', width=250)
    tree_serv.heading('id_serv', text='ID')
    tree_serv.heading('nom_serv', text='Nom ')
    tree_serv.heading('description_serv', text='Description')
    tree_serv.heading('date_creation_serv', text='Date')
    tree_serv.heading('nom_emp', text='Nom resp')
    tree_serv.heading('prenom_emp', text='Prénom resp')
 
    for ligne in listes_serv:
        tree_serv.insert('', tk.END, values=ligne)
    tree_serv.pack()
