import customtkinter as ctk
from tkinter import ttk , messagebox

import tkinter as tk
from datetime import datetime

import setting as set
import graphi_print as gp

les_consommables_selectionnes = dict()


def confirmation_de_la_selectionne(id_employe, les_produits_selectionnes):
    reponse = messagebox.askquestion("Enrégisrement", "Désirevous enrégistrer les produits sélectionnés ?")

    if reponse == "yes":
        les_demandes = []
        for consommable in les_produits_selectionnes:
            les_demandes.append((id_employe,consommable[0], consommable[2], datetime.now().date()))
        print(les_demandes)

def recuperation_des_champs_selectionner():
    """
    Une fonction qui recupere parcour la liste des consommables et recuperer ceux qui ont été sémectionner
    paramètre: Neant
    Return: Dictionnaire de lignes sélectionnées
    """
    les_champs_selectionne = dict()

    for id,valeurs in les_consommables_selectionnes.items():
        select = valeurs[4].get()
        
        if select:
            les_champs_selectionne[id] = valeurs
    
    return les_champs_selectionne



def apercu_des_consommables_selectionner(employe_entry):
    """Une procéduire qui permet voir la liste des lignes selectionner
    
    """
    
    consommables = recuperation_des_champs_selectionner()
    employe = employe_entry.get()
    id_emp = employe.split()[0]
    try:
        id_emp = int(id_emp)
        nom_prenom_emp = " ".join(employe[1:])


        #construction d'un toplevel
        apercu_fen = ctk.CTkToplevel()
        apercu_fen.geometry("600x650+200+0")
        apercu_fen.title(f"Liste des consommables à fournir à l'employé {nom_prenom_emp}")
        apercu_fen.resizable(width=False, height=False)
        apercu_fen.configure(fg_color= set.col_white)
        apercu_fen.attributes('-topmost', True)

        #titre
        titre = ctk.CTkLabel(apercu_fen, text= f'LISTE DES CONSOMMABLES DE: {nom_prenom_emp}', text_color= set.col_text)
        titre.place(x=200,y=5)
        #zone tableau
        tableau_consommables = ctk.CTkScrollableFrame(apercu_fen, width=500, height=530,fg_color= set.col_white,
                                                    border_width=1, border_color= set.col_border)
        tableau_consommables.place(x=40, y= 40)

        

        les_conso_selectionnees = []
        
        for id,ligne in consommables.items():
            try:
                qte_demander = int(ligne[3].get())
                if qte_demander and qte_demander < int(ligne[2].get()):
                    les_conso_selectionnees.append((int(id),ligne[1].get(),qte_demander))
                    ligne[3].configure(border_color= set.col_border, state= tk.NORMAL)
                else:
                    ligne[3].configure(border_color= set.col_rouge, state = "disable")
                    ligne[4]._variable.set(0)
                
            except:
                
                ligne[3].delete(0, tk.END)
                ligne[3].insert(0,0)
                ligne[3].configure(border_color= set.col_rouge, state = "disable")
                ligne[4]._variable.set(0)
        

        


        #bouton fermer
        fermer_btn = ctk.CTkButton(apercu_fen, text= 'Fermer', width=110,height=30,font=("Montsérrat",14), border_color=set.col_border,
                                border_width=1, hover_color= set.col_hover, corner_radius=5,fg_color=set.col_rouge, command= apercu_fen.destroy)
        fermer_btn.place(x=450,y=600)

        #bouton confirmer
        confirmation_btn = ctk.CTkButton(apercu_fen, text= 'COnfirmer', width=110,height=30,font=("Montsérrat",14), border_color=set.col_border,
                                border_width=1, hover_color= set.col_hover, corner_radius=5,fg_color=set.col_green,
                                  command= lambda :confirmation_de_la_selectionne(id_emp, les_conso_selectionnees))
        confirmation_btn.place(x=40,y=600)

        apercu_fen.mainloop()

    except:

        messagebox.showinfo("Information importante", "Veuillez sélectionner l'employé à qui est destineé les pproduits sélectionnés")

def on_entry_change(value):
    # Perform your validation or control logic here
    # For example, check if the value is an integer
    if value.isdigit():
        # Value is an integer, proceed as needed
        print(value)
    else:
        # Value is not an integer, handle error or provide feedback
        print('Mauvaise valeur ', value)

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
    conso_frame = ctk.CTkFrame(formulaire,fg_color=set.col_fg, height=40, corner_radius=0)
    conso_frame.pack(fill="both",padx=10, pady=0)
    
    
    #id conommable
    id_l = ctk.CTkEntry(conso_frame,fg_color=set.col_fg, corner_radius=0, height=30,
                         text_color= set.col_text, width=60)
    id_l.place(x=5, y=5)
    inserer_entry_disable(cons[0], id_l)

    #nom de la consommable
    nom_l = ctk.CTkEntry(conso_frame,fg_color=set.col_fg, width=320, text_color= set.col_text,corner_radius=0, height=30,)
    nom_l.place(x=75, y=5)
    inserer_entry_disable(cons[1], nom_l)

    #quantité en stock du consommable
    qtestock_l = ctk.CTkEntry(conso_frame,fg_color=set.col_fg, width=95, text_color= set.col_text,corner_radius=0, height=30,
                              justify="center" )
    qtestock_l.place(x=400, y=5)
    inserer_entry_disable(cons[2], qtestock_l)

    #quantité à de consommable a founir à l'employé
    qtedonne_l = ctk.CTkEntry(conso_frame,fg_color=set.col_fg, width=95, text_color= set.col_text,corner_radius=0, height=30,)
    qtedonne_l.place(x=500, y=5)
    inserer_entry_disable(0, qtedonne_l)
    #checkbox de selection du consommable à fournir à l'employé
    select_var = tk.IntVar()
    select_l = ctk.CTkCheckBox(conso_frame,variable=select_var, text= "",fg_color=set.col_rouge, width=50, text_color= set.col_text,
                               corner_radius=0,border_color=set.col_border,hover_color= set.col_hover , border_width= 1,
                                height=30,command= lambda: fonction(qtedonne_l,select_l))
    select_l.place(x=600, y=5)

    les_consommables_selectionnes[id_l.get()] = (id_l, nom_l, qtestock_l, qtedonne_l, select_l)

    return  (id_l, nom_l, qtestock_l, qtedonne_l, select_var, select_l)

def attribuer(aff_frame):
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
                        widget[1]._variable.set(1)
                else:
                    for widget in donnee_select:
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

                    
                else :
                    
                    checkbox._variable.set(0)
                    entry.delete(0, tk.END)
                    entry.configure(state = "disable")
                

            #Définition des entetes il ne seront que des labels
            conso_ente = ctk.CTkFrame(formulaire,fg_color="#f00",height=35,corner_radius=0)
            conso_ente.pack(fill="both",padx=30, pady=1)
            conso_ligne = ctk.CTkFrame(formulaire,fg_color=set.col_fg,height=40,corner_radius=0)
            conso_ligne.pack(fill="both",padx=15, pady=0)

            
            #Entete de chaque categories
            id = ctk.CTkLabel(conso_ente,text=cat, text_color=set.col_text, font=('Montsérrat', 20))
            id.place(x=15, y=5)

            nom = ctk.CTkLabel(conso_ente,text=categorie[0][0], text_color=set.col_text, font=('Montsérrat', 20))
            nom.place(x=90, y=5)
            
            lignes  = [ ]
            
            all_click = tk.IntVar()
            select_all_label = ctk.CTkLabel(conso_ente,text="All", text_color=set.col_text, font=('Montsérrat', 20))
            select_all_label.place(x=530, y=5)
            all_select = ctk.CTkCheckBox(conso_ente,variable= all_click,text="", text_color=set.col_text, font=('Montsérrat', 20),
                                        corner_radius=0,border_color=set.col_border,hover_color= set.col_hover, border_width= 1,
                                        fg_color= set.col_fg,command=lambda: selectionne_all(lignes))
            all_select.place(x=595, y=5)
            
            for cons in les_conso:
                les_lignes[cons[0]] = build_ligne(cons, conso_ligne, selection)
            
            lignes  = [ ]
            for num, val in les_lignes.items() :
                lignes.append((val[3], val[5]))


            

            
    """
        Un methode qui permet de gérer les attributs de commables à un employé
    """
    titre = ctk.CTkLabel(aff_frame, text="Formulaire d'attribution de consommable au employé".upper(), font= ("Montsérrat", 20,"bold"),
                         fg_color="#f00", text_color= set.col_text)
    titre.place(x=150, y=10)
    formulaire = ctk.CTkScrollableFrame(aff_frame, width=700, height=550, fg_color=set.col_fg, corner_radius=0)
    formulaire.place(x=150,y=50)



    #employé
    emp_frame = ctk.CTkFrame(formulaire, fg_color= set.col_fg)
    emp_frame.pack(fill = "both", padx =15, pady = 15)
    les_employes = gp.get_employes()
    options = ["Choisir un employé"]
    for employe in les_employes:
        
       options.append(" ".join([str(employe[0]), employe[1], employe[2]]))

    employe = ctk.CTkLabel(emp_frame, text="Employé :", text_color=set.col_text, font= ("Montsérrat", 15))
    employe.pack(side="left",padx=20,)

    employe_c = ctk.CTkComboBox(emp_frame,width=300, values= options,fg_color=set.col_fg, text_color=set.col_text, font= ("Montsérrat", 15))
    employe_c.pack(side="left",padx=20,)


    #btn ajouter et supprimer consommable a enregistrer dans  le compte de employé
    apercu_des_choix = ctk.CTkButton(emp_frame, text = "Voir tous les choix".upper(),width=100,height=30, fg_color=set.col_green,
                                     corner_radius=10, hover_color= set.col_hover,
                                     command= lambda: apercu_des_consommables_selectionner(employe_c) )
    apercu_des_choix.pack(side= "right", padx =10, pady = 10)


    #Affiches tous les catégories
    cat_frame = ctk.CTkFrame(formulaire, fg_color= set.col_fg)
    cat_frame.pack(fill = "both", padx =10, pady = 15)
   
    #Entete du tableau 
    entete_tableau = ctk.CTkFrame(cat_frame,fg_color= set.col_fg,height=30)
    entete_tableau.pack(fill = "both", padx =10, pady = 0)

    id = ctk.CTkLabel(entete_tableau,text="ID", text_color=set.col_text, font=('Montsérrat', 15))
    id.place(x=5, y=3)

    nom = ctk.CTkLabel(entete_tableau,text="Nom", text_color=set.col_text, font=('Montsérrat', 15))
    nom.place(x=75, y=3)

    qtestock = ctk.CTkLabel(entete_tableau,text="Qté S", text_color=set.col_text, font=('Montsérrat', 15))
    qtestock.place(x=400, y=3)

    qtedonne = ctk.CTkLabel(entete_tableau,text="Qté D", text_color=set.col_text, font=('Montsérrat', 15))
    qtedonne.place(x=500, y=3)

    select = ctk.CTkLabel(entete_tableau,text="Select", text_color=set.col_text, font=('Montsérrat', 15))
    select.place(x=600, y=3)

    les_categories = gp.get_categories()
    for one_catetogie in les_categories:
        id=one_catetogie[0]
        tableau_dist(id)
        

    pied_page = ctk.CTkFrame(formulaire,fg_color= set.col_fg,height=30)
    pied_page.pack(fill = "both", padx =10, pady = 0)

