import customtkinter as ctk
from tkinter import ttk , messagebox
import tkinter as tk

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



    #Définition des Services
    #zone
    service = ctk.CTkFrame(framescrol, width=1200, height=640, fg_color=set.col_fg, bg_color=set.col_bg,
                         border_color=set.col_border, border_width=0)
    service.pack(pady = 0, padx=0)


     #Le formulaire
    formulaire = ctk.CTkFrame(service, width=970, height=350, bg_color=set.col_bg,fg_color=set.col_fg,border_color=set.col_border,
                         border_width=1)
    formulaire.place(x=5, y=15)

    liste_conso = ctk.CTkLabel(service, text= "FORMULAIRE", fg_color =set.col_fg,font = ('Montsérrat', 20),
                             text_color =set.col_text)
    liste_conso.place(x=10, y=5 )

    

    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(formulaire, text='Identifiant :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    id.place(x=5, y=35)
    id_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=100, height=30, corner_radius=0,
                        font= ("Montsérrat",20))
    id_e.place(x=150, y= 35)
    
    #Nom du produit
    nom = ctk.CTkLabel(formulaire, text='Nom :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    nom.place(x=410, y=35)
    nom_e = ctk.CTkEntry(formulaire, placeholder_text="Nom du service",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=300, height=30, corner_radius=0,
                        font= ("Montsérrat",20))
    nom_e.place(x=520, y= 35)

    #Prix unitaire
    description = ctk.CTkLabel(formulaire, text='Description :', font= ("Montsérrat",18), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    description.place(x=5, y=190)
    description_e = ctk.CTkTextbox(formulaire,text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                         width=670, height=70, corner_radius=0, border_width=1, border_color=set.col_border, 
                        font= ("Montsérrat",15))
    description_e.place(x=150, y= 190)
   
    #Date de création du service
    date_creation = ctk.CTkLabel(formulaire, text='Date de créaion :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    date_creation.place(x=5, y=110)
    date_creation_e = ctk.CTkEntry(formulaire, placeholder_text="AAAA-MM-JJ",text_color=set.col_text, bg_color=set.col_bg, fg_color= set.col_fg,
                        placeholder_text_color=set.col_placeholder, justify = 'left', width=200, height=30, corner_radius=0,
                        font= ("Montsérrat",20))
    date_creation_e.place(x=200, y= 110)

    #Quantité seuil du produit a respecter
    option = gp.get_employes()
    options = ["Choisir un service"]+[str(i[0])+' '+i[1]+' '+i[2] for i in option]
    responsable = ctk.CTkLabel(formulaire, text='Responsable :', font= ("Montsérrat",20), text_color=set.col_tx, bg_color=set.col_bg, fg_color= set.col_fg)
    responsable.place(x=410, y=110)
    responsable_e= ctk.CTkComboBox(master=formulaire, width=250, height=30, fg_color=set.col_fg, border_width=1, 
                            border_color=set.col_border, values=options, button_color=set.col_border,button_hover_color=set.col_hover,
                            font=('Montsérrat', 12,),dropdown_font=('Montsérrat',15), text_color= set.col_text, dropdown_text_color= set.col_text,
                            dropdown_fg_color= set.col_fg, dropdown_hover_color=set.col_hover, corner_radius=0,
                            )
   
    responsable_e.place(x=570, y= 110)


    #Les boutons
    rechercher_cons = ctk.CTkButton(formulaire, text = "Rechercher",width=200,height=30,command= recherche,font=('Montsérrat', 25),
                                   fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    rechercher_cons.place(x=5, y=300)
    
    enregistrer_cons = ctk.CTkButton(formulaire, text = "Enregistrer",width=200,height=30,command= "#",font=('Montsérrat', 25),
                                    fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    enregistrer_cons.place(x=270, y=300)

    modifier_cons = ctk.CTkButton(formulaire, text = "Modifier",width=200,height=30,command="#",font=('Montsérrat', 25),
                                 fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    modifier_cons.place(x=500, y=300)

    supprimer_cons = ctk.CTkButton(formulaire, text = "Supprimer",width=200,height=30, command = "#",font=('Montsérrat', 25),
                                  fg_color= set.col_btn_bg, hover_color= set.col_hover, corner_radius=0)
    supprimer_cons.place(x=750, y=300)


    #Listes des services
    listes_serv = gp.get_services()

    liste_serv = ctk.CTkLabel(framescrol, text= "Liste de des consommables".upper(), fg_color=set.col_fg,
                             font = ('Montsérrat', 20), text_color= set.col_text , bg_color=set.col_bg)
    liste_serv.place(x=5, y=380)

    frame_serv = ctk.CTkScrollableFrame(framescrol, width=950, height=200, border_color=set.col_border, border_width=1,
                                             fg_color=set.col_fg, bg_color= set.col_bg, orientation='vertical',
                                             scrollbar_fg_color=set.col_fg)
    frame_serv.place(x=5 , y=420)

    style_serv = ttk.Style()
    style_serv.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'), rowheight=20, foreground=set.col_fg)
    style_serv.configure("Treeview", font=('Helvetica', 13, 'bold'), rowheight=50,)
    tree_serv = ttk.Treeview(frame_serv, columns=('id_serv', 'nom_serv',"description_serv", 'date_creation_serv', 'nom_emp', 'prenom_emp'), 
                             show='headings', height=20)
    
    # Définir les en-têtes
    tree_serv.column('nom_serv', width=200)
    tree_serv.column('id_serv', width=100) 
    tree_serv.column('prenom_emp', width=300)
    tree_serv.heading('id_serv', text='ID')
    tree_serv.heading('nom_serv', text='Nom ')
    tree_serv.heading('description_serv', text='Description')
    tree_serv.heading('date_creation_serv', text='date de création')
    tree_serv.heading('nom_emp', text='Nom resp')
    tree_serv.heading('prenom_emp', text='Prénom resp')
 
    for ligne in listes_serv:
        tree_serv.insert('', tk.END, values=ligne)
    tree_serv.pack()
