import customtkinter as ctk
from tkinter import ttk , messagebox

import tkinter as tk
from datetime import datetime

import setting as set
import graphi_print as gp

les_consommables_selectionnes = dict()

def update_fenetre(frame):
    """
    Une procédure pour mettre à jour l'interface après chaque enrégistrement
    parametre: frame
    
    """
    for widget in frame.winfo_children():
        widget.destroy()
    approvisionner(frame)



def enregistrer_la_selectionne(frame, toplevel,id_employe,date_commande, les_produits_selectionnes):
    """
    Procédure permettant d'en régistre les consommables sélectionner dans la table demander
    paramètres: id_employe : identifiant de l'employé qui à demander les consommables
                date_commande: date à laquelle la commande a été effectué
                les_produits_selectionnes: la liste des produits commandés: id_cons, qte_com
    """
    confirme = messagebox.askquestion("Confirmation de l'enrégistrement", "Etes vous sur d'enrégistrer les données qui vous aient été présenté.\n Une fois enrégistrer vous n'aurez plus le droit de les supprimées.\n Au besoins veillez vous contacter votre administrateur.")
    les_demandes = []
    
    
    if confirme:
        #insertion de la commande
        id_com = gp.get_last_commande_id()
        id_com+=1
        reponse_insertion_commande = gp.inserer_commande((id_com, date_commande, id_employe))
        if reponse_insertion_commande:

            for consommable in les_produits_selectionnes:
                les_demandes.append((id_com, consommable[0], consommable[2]))
            
            print(les_demandes)
            if les_demandes :
                resulat = gp.inserer_appartenir(les_demandes)
                if resulat:
                    messagebox.showinfo("Enrégistrement", "Succès")
                    update_fenetre(frame)
                    toplevel.destroy()
                else:
                    messagebox.showinfo("Enrégistrement", "Echec")
        else:
            messagebox.showerror("Insertion commande", "Echéc de l'opération !")

def recuperation_des_champs_selectionner():
    """
    Une fonction qui recupere parcour la liste des consommables et recuperer ceux qui ont été sémectionner
    paramètre: Neant
    Return: Dictionnaire de lignes sélectionnées
    """
    les_champs_selectionne = dict()

    for id,valeurs in les_consommables_selectionnes.items():
        select = valeurs[3].get()
        
        if select:
            les_champs_selectionne[id] = valeurs
    
    return les_champs_selectionne



def apercu_des_consommables_selectionner(frame, employe_entry, date_entry):
    """Une procéduire qui permet voir la liste des lignes selectionner
    
    """
    
    consommables = recuperation_des_champs_selectionner()
    employe = employe_entry.get()
    date_commande = date_entry.get() ; date_is_val = False
    id_emp = employe.split()[0] ; id_is_val = False
    

    #verification de l'id de l'employé qui a effectué la commande
    try:
        id_emp = int(id_emp)
        id_is_val = True
    except:
        id_is_val = False
    
    #verification de la date ou la commande a été effectué
    try:
        date_commande = datetime.strptime(date_commande,"%Y-%m-%d").date()
        date_is_val = True
    except:
        date_is_val = False
       
    if id_is_val and not date_is_val:
        messagebox.showinfo("Information importante", "Veuillez préciser la date où la commande a été effectué")
    elif not id_is_val and date_is_val:
        messagebox.showinfo("Information importante", "Veuillez préciser l'employé à qui a effectuée la commande")
    elif not id_is_val and not date_is_val:
        messagebox.showinfo("Information importante", "Veuillez préciser l'employé à qui a effectuée la commande \net la date où la commande a été effectué")
    else:
        
        nom_prenom_emp = " ".join(employe[1:])


        #construction d'un toplevel
        apercu_fen = ctk.CTkToplevel()
        apercu_fen.geometry("600x650+0+0")
        apercu_fen.title(f"Liste des consommables à fournir à l'employé {nom_prenom_emp}")
        apercu_fen.resizable(width=False, height=False)
        apercu_fen.configure(fg_color= set.col_blanc_4)
        apercu_fen.attributes('-topmost', True)

        #titre
        titre = ctk.CTkLabel(apercu_fen, text= f'LISTE DES CONSOMMABLES DE: {nom_prenom_emp}', text_color= set.col_noir_1)
        titre.place(x=40,y=5)
        #zone tableau
        tableau_consommables = ctk.CTkScrollableFrame(apercu_fen, width=500, height=530,fg_color= set.col_blanc_4,
                                                    border_width=1, border_color= set.col_border)
        tableau_consommables.place(x=40, y= 40)

        

        les_conso_selectionnees = [] # (id_consommables, Nom du consommable ,quantité demande)
        #Récupération des lignes selectionner et dont la valeur est raisonnable
        for id,ligne in consommables.items():
            try:
                qte_demander = int(ligne[2].get())
                if qte_demander > 0:
                    les_conso_selectionnees.append((int(id),ligne[1].get(),qte_demander))
                   
                    ligne[2].configure(border_color= set.col_noir_4, state= tk.NORMAL)
                    
                else:
                    ligne[2].configure(border_color= set.col_rouge, state = "disable")
                    ligne[3]._variable.set(0)
                  
                
            except:
                
                ligne[2].delete(0, tk.END)
                ligne[2].insert(0,0)
                ligne[2].configure(border_color= set.col_rouge, state = "disable")
                ligne[3]._variable.set(0)
        
        #Construction du tableau d'affichage
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'), rowheight=10, foreground=set.col_fg)
        style.configure("Treeview", font=('Helvetica', 13, 'bold'), rowheight=30,)
        tree_cat = ttk.Treeview(tableau_consommables, columns=('id', 'nom', "qte_commande"), show='headings', height=20)

        # Définir les en-têtes
        tree_cat.column('nom', width=550)
        tree_cat.column('id', width=100) 
        tree_cat.heading('id', text='ID')
        tree_cat.heading('nom', text='Nom du consommable')
        tree_cat.heading('qte_commande', text="Qté Com")
        for ligne in les_conso_selectionnees:
            tree_cat.insert('', tk.END, values=ligne)
        tree_cat.pack()
        


        #bouton fermer
        fermer_btn = ctk.CTkButton(apercu_fen, text= 'Fermer', width=110,height=30,font=("Montsérrat",14), border_color=set.col_noir_1,
                                border_width=1, hover_color= set.col_hover, corner_radius=5,fg_color=set.col_noir_5, command= apercu_fen.destroy)
        fermer_btn.place(x=450,y=600)

        #bouton confirmer
        confirmation_btn = ctk.CTkButton(apercu_fen, text= 'Enrégistrer', width=110,height=30,font=("Montsérrat",14), border_color=set.col_noir_1,
                                border_width=1, hover_color= set.col_hover, corner_radius=5,fg_color=set.col_noir_5,
                                  command= lambda :enregistrer_la_selectionne(frame,apercu_fen,id_emp,date_commande, les_conso_selectionnees))
        confirmation_btn.place(x=40,y=600)

        apercu_fen.mainloop()

   
    

def inserer_entry_disable(element, entry):
    """
        Une procédure utilisé pour insérer un élément dans un CTkEntry et la rendre inaccessible
        parametre: element = élément à insérer dans le CTkEntry
                   entry = le CTkEntry
    """
    entry.insert(0,element)
    entry.configure(state="disable")

def build_ligne(cons, formulaire,fonction):
    """
    Fonction pour dessiner une ligne de consommable avec les widgets
    paramètres: id_cons =id du consommable
                CTKFrame = la zone dans laquelle la ligne sera représenté
                Fonction = la fonction a executer par le CTkCheckBox
    return : un tuple (4 x CTkEntry, IntVar, CTkChecBox)
    """

    #ligne de consommables
    conso_frame = ctk.CTkFrame(formulaire,fg_color=set.col_blanc_4, height=40, corner_radius=0)
    conso_frame.pack(fill="both",padx=10, pady=0)
    
    
    #id conommable
    id_l = ctk.CTkEntry(conso_frame,fg_color=set.col_blanc_4, corner_radius=0, height=30,
                         text_color= set.col_noir_1, width=75)
    id_l.place(x=5, y=5)
    inserer_entry_disable(cons[0], id_l)

    #nom de la consommable
    nom_l = ctk.CTkEntry(conso_frame,fg_color=set.col_blanc_4, width=500, text_color= set.col_noir_1,corner_radius=0, height=30,)
    nom_l.place(x=75, y=5)
    inserer_entry_disable(cons[1], nom_l)

    
    #quantité à de consommable a founir à l'employé
    qtedonne_l = ctk.CTkEntry(conso_frame,fg_color=set.col_blanc_4, width=95, text_color= set.col_noir_1,corner_radius=0, height=30,)
    qtedonne_l.place(x=500, y=5)
    inserer_entry_disable(0, qtedonne_l)
    #checkbox de selection du consommable à fournir à l'employé
    select_var = tk.IntVar()
    select_l = ctk.CTkCheckBox(conso_frame,variable=select_var, text= "",fg_color=set.col_noir_1, width=50, text_color= set.col_noir_1,
                               corner_radius=0,hover_color= set.col_hover , border_width= 1,
                                height=30,command= lambda: fonction(qtedonne_l,select_l))
    select_l.place(x=600, y=5)

    les_consommables_selectionnes[id_l.get()] = (id_l, nom_l, qtedonne_l, select_l)

    return  (id_l, nom_l, qtedonne_l, select_var, select_l)




#====================================================================
#======================FONCTION PRINCIPALE===========================
def approvisionner(aff_frame):
    """
    Procédure de gestion des attributions de consommables à un employé
    paramètres: aff_frame = la zone représentant l'interface
    """

    def tableau_dist(cat):
        """
            Une procédure pour dessiner la un tableau d'une catégorie 
            de produit consommable donnée
            -- parametre: id du produit onsommable
        """
        les_conso = gp.get_consommables_by_cat(cat)
        categorie = gp.get_one_categories(cat)
        
        if les_conso :
            les_lignes = dict()
    
            #fonction pour selectionner tous les checkbox
            def selectionne_all(donnee_select=[]):
                """
                Une procédure pour sélectionner tous les produits d'une catégorie donnée
                -- parametre: liste de tuple (CTkEntry, CTkCheckBox)
                """
                number = all_click.get()
                
                if number:
                    for widget in donnee_select:
                        widget[0].configure(state = tk.NORMAL)
                        widget[0].delete(0, tk.END)
                        widget[1]._variable.set(1)
                else:
                    for widget in donnee_select:
                        widget[0].insert(0,0)
                        widget[0].configure(state = "disable")
                        widget[1]._variable.set(0)
                        

            #fonction de controle des chekbox
            def selection(entry, checkbox):
                """
                    Une procédure pour sélectonner une consommanble dans une catégorie
                    afin de permettre la saisir de la quantité à demander
                    -- parametre: CTkEntry et CTkCheckBox
                """
                var = checkbox._variable
                number  = var.get()
                
                
                if number :

                    checkbox._variable.set(1)
                    entry.configure(state = tk.NORMAL)
                    entry.delete(0, tk.END)

                    
                else :
                    
                    checkbox._variable.set(0)
                    entry.insert(0, 0)
                    entry.configure(state = "disable")
     
                

            #Définition des entetes il ne seront que des labels
            conso_ente = ctk.CTkFrame(formulaire,fg_color=set.col_blanc_4,height=35,corner_radius=0)
            conso_ente.pack(fill="both",padx=30, pady=1)
            conso_ligne = ctk.CTkFrame(formulaire,fg_color=set.col_blanc_4,height=40,corner_radius=0)
            conso_ligne.pack(fill="both",padx=15, pady=0)

            
            #Entete de chaque categories
            id = ctk.CTkLabel(conso_ente,text=cat, text_color=set.col_noir_1, font=('Montsérrat', 20))
            id.place(x=15, y=5)

            nom = ctk.CTkLabel(conso_ente,text=categorie[0][0], text_color=set.col_noir_1, font=('Montsérrat', 20))
            nom.place(x=90, y=5)
            
            lignes  = [ ]
            
            all_click = tk.IntVar()
            select_all_label = ctk.CTkLabel(conso_ente,text="All", text_color=set.col_noir_1, font=('Montsérrat', 20))
            select_all_label.place(x=530, y=5)
            all_select = ctk.CTkCheckBox(conso_ente,variable= all_click,text="", font=('Montsérrat', 20),
                                        corner_radius=0,border_color=set.col_noir_1,hover_color= set.col_hover, border_width= 1,
                                        fg_color= set.col_noir_1,command=lambda: selectionne_all(lignes))
            all_select.place(x=595, y=5)
            
            for cons in les_conso:
                les_lignes[cons[0]] = build_ligne(cons, conso_ligne, selection)
            
            lignes  = [ ]
            for num, val in les_lignes.items() :
                lignes.append((val[2], val[4]))


            

            
    """
        Un methode qui permet de gérer les attributs de commables à un employé
    """
    titre = ctk.CTkLabel(aff_frame, text="Formulaire d'enregistrement de commandes".upper(), font= ("Montsérrat", 15,"bold"),
                         fg_color=set.col_blanc_4, text_color= set.col_noir_1)
    titre.place(x=150, y=10)
    formulaire = ctk.CTkScrollableFrame(aff_frame, width=700, height=500, fg_color=set.col_blanc_4, corner_radius=5,
                                        border_width=1)
    formulaire.place(x=150,y=50)



    #employé
    information_frame = ctk.CTkFrame(formulaire , height=50, fg_color= set.col_blanc_4)
    information_frame.pack(fill = "both", padx =15, pady = 15)
    les_employes = gp.get_employes()
    options = ["Choisir un employé"]
    for employe in les_employes:
        
       options.append(" ".join([str(employe[0]), employe[1], employe[2]]))


    employe_c = ctk.CTkComboBox(information_frame,width=300,height=30, values= options, text_color=set.col_noir_1, 
                                font= ("Montsérrat", 15), border_width=1)
    employe_c.place(x=10, y=5)

    #Les numeros de la commandes
    
    numero_label = ctk.CTkLabel(information_frame, text="Commande N° :",width=100, height=30,fg_color= set.col_blanc_4, justify="left",
                                font=("MOntsérrat", 15))
    numero_label.place(x=360, y=5)
    numero_de_la_commande = ctk.CTkEntry(information_frame, width=10,height=30, text_color=set.col_noir_1, 
                                font= ("Montsérrat", 15), border_width=0, corner_radius=0, fg_color=set.col_blanc_4)
    numero_de_la_commande.place(x=470, y=5)
    numero=gp.get_last_commande_id()+1
    inserer_entry_disable(numero, numero_de_la_commande)

    #Date
    date_de_la_commande = ctk.CTkEntry(information_frame, width=150,height=30, text_color=set.col_noir_1, placeholder_text="Date: 2024-01-01",
                                font= ("Montsérrat", 15), border_width=1, corner_radius=5, fg_color=set.col_blanc_4)
    date_de_la_commande.place(x=520, y=5)

    #btn ajouter et supprimer consommable a enregistrer dans  le compte de employé
    apercu_des_choix = ctk.CTkButton(aff_frame, text = "Voir tous les choix".upper(),width=30,height=40, fg_color=set.col_noir_5,
                                     corner_radius=5, hover_color= set.col_hover,font=('Montsérrat', 10),
                                     command= lambda: apercu_des_consommables_selectionner(aff_frame,employe_c,date_de_la_commande) )
    apercu_des_choix.place(x=750, y= 580)


    #Affiches tous les catégories
    cat_frame = ctk.CTkFrame(formulaire, fg_color= set.col_blanc_4)
    cat_frame.pack(fill = "both", padx =10, pady = 15)
   
    #Entete du tableau 
    entete_tableau = ctk.CTkFrame(cat_frame,fg_color= set.col_blanc_4,height=30)
    entete_tableau.pack(fill = "both", padx =10, pady = 0)

    id = ctk.CTkLabel(entete_tableau,text="ID", text_color=set.col_noir_1, font=('Montsérrat', 15))
    id.place(x=5, y=3)

    nom = ctk.CTkLabel(entete_tableau,text="Nom", text_color=set.col_noir_1, font=('Montsérrat', 15))
    nom.place(x=75, y=3)

    

    qtedonne = ctk.CTkLabel(entete_tableau,text="Qté D", text_color=set.col_noir_1, font=('Montsérrat', 15))
    qtedonne.place(x=500, y=3)

    select = ctk.CTkLabel(entete_tableau,text="Select", text_color=set.col_noir_1, font=('Montsérrat', 15))
    select.place(x=600, y=3)

    les_categories = gp.get_categories()
    for one_catetogie in les_categories:
        id=one_catetogie[0]
        tableau_dist(id)
        

    pied_page = ctk.CTkFrame(formulaire,fg_color= set.col_blanc_4,height=30)
    pied_page.pack(fill = "both", padx =10, pady = 0)

