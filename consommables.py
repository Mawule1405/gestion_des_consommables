import customtkinter as ctk
from tkinter import ttk, messagebox
import tkinter as tk

import setting as set
import graphi_print as gp
import un_consommable as uncons




def lister_les_consommable():
    #Affichage des consommables
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("700x750+0+0")
    toplevel.title("Liste des consommables")
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.resizable(width=False, height=False)
    toplevel.configure(fg_color= set.col_blanc_4)
    toplevel.attributes('-topmost', True)


    framescrol = ctk.CTkScrollableFrame(toplevel, width=600, height=620, fg_color=set.col_blanc_4, border_color= set.col_noir_1,
                                         border_width=1)
    framescrol.place(x=50,y=30)


    listes_cons = gp.get_consommables()

    liste_cons = ctk.CTkLabel(toplevel, text= "Liste de des consommables".upper(), fg_color=set.col_blanc_4,
                             font = ('Montsérrat', 15), text_color= set.col_noir_1 )
    liste_cons.place(x=50, y=2)

    

    fermer_button = ctk.CTkButton(toplevel, text = "FERMER".upper(),width=80,height=35, fg_color=set.col_noir_5,
                                     corner_radius=5, hover_color= set.col_hover,font=('Montsérrat', 10),
                                     command= lambda: toplevel.destroy() )
    fermer_button.place(x=580 ,y=690)

    style_cons = ttk.Style()
    style_cons.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'), rowheight=20, foreground=set.col_fg)
    style_cons.configure("Treeview", font=('Helvetica', 13, 'bold'), rowheight=50,)
    tree_cons = ttk.Treeview(framescrol, columns=('id_cons', 'nom_cons',"qtestock_cons", 'qteseuil_cons', 'prix_unitaire_cons', 'categorie'), 
                             show='headings', height=20)

    # Définir les en-têtes
    tree_cons.column('nom_cons', width=400)
    tree_cons.column('id_cons', width=75) 
    tree_cons.column("qtestock_cons", width=100)
    tree_cons.column("qteseuil_cons", width=100)
    tree_cons.column("prix_unitaire_cons", width=150)
    tree_cons.heading('id_cons', text='ID')
    tree_cons.heading('nom_cons', text='Nom ')
    tree_cons.heading('qtestock_cons', text='Q S')
    tree_cons.heading('qteseuil_cons', text='Q s')
    tree_cons.heading('prix_unitaire_cons', text='PU')
    tree_cons.heading('categorie', text='Categorie')
    for ligne in listes_cons:
        tree_cons.insert('', tk.END, values=ligne)
    tree_cons.pack()

    toplevel.mainloop()


def modifie(liste_de_entry):
    """
        Une procédure qui permet d'enrégistrer une nouvelle consommable
        Paramètre: liste des entrys => ID, Nom, Qte S, Qte s, Prix, cat
    """
    #Recuperation des données
    id_cons = liste_de_entry[0].get() ; id_cons_val = False
    nom_cons = liste_de_entry[1].get(); nom_cons_val = False
    prix_u_cons= liste_de_entry[2].get(); prix_u_cons_val = False
    categorie_cons = liste_de_entry[5].get().split()[0]; categorie_cons_val = False
    
    #Verification de l'identité 
    try:
        id_cons = int(id_cons)
        id_cons_val = True
        liste_de_entry[0].configure(border_color = set.col_noir_1)
    except:
        id_cons_val = False
        liste_de_entry[0].configure(border_color = set.col_rouge)
    
    #Verification du nom
    if nom_cons != "":
        nom_cons_val = True
        liste_de_entry[1].configure(border_color = set.col_noir_1)
    else:
        nom_cons_val = False
        liste_de_entry[1].configure(border_color = set.col_rouge)
    

    #Verification du prix unitaire
    try:
        prix_u_cons = int(prix_u_cons)
        assert prix_u_cons >= 0
        prix_u_cons_val = True
        liste_de_entry[2].configure(border_color = set.col_noir_1)
    except:
        prix_u_cons_val = False
        liste_de_entry[2].configure(border_color = set.col_rouge)

    



    

    validation = all([id_cons_val, nom_cons_val, prix_u_cons_val])


    if validation:
        consommable   = ( nom_cons, prix_u_cons, id_cons)

        reponse = gp.update_consommable(consommable)
        if reponse :
            messagebox.showinfo("Modification","Modification des données effectués avec succès.\nVous ne pouvez pas changer la quantité en stock ni la quantité seuil")
            
        else: 
            
            messagebox.showerror("Modification", "Echec de l'opération ! ID inexistant.")

    else:
        messagebox.showerror("Modification", "Echec de l'opération !\nLes données de certains champs sont invalides")

def recherche(liste_de_entry):
    """
       Procéduire permettant de rechercher un consommable et envoyé
       les résulats dans les autres entry ou checkbox
       parametre: identifiant du consommable à rechercher"""
    id_cons = liste_de_entry[0].get()
    
    try:
        id_cons = int(id_cons)
        resultat = gp.get_consommables_by_id_cons(id_cons)
        res = resultat[0]
        liste_de_entry[1].delete(0,tk.END); liste_de_entry[1].insert(0,res[1])
        liste_de_entry[2].delete(0,tk.END); liste_de_entry[2].insert(0,res[4])
        liste_de_entry[3].delete(0,tk.END); liste_de_entry[3].insert(0,res[2])
        liste_de_entry[4].delete(0,tk.END); liste_de_entry[4].insert(0,res[3])
        liste_de_entry[5].set(str(res[5])+' '+res[6])
    
    except IndexError:
           messagebox.showinfo("Recherche", "Identifiant non trouvé !")
    
    except Exception as e  :
        
        messagebox.showinfo("Recherche", "Veuillez préciser l'identifiant du consommable recherché")


def enregistre(liste_de_entry):
    """
        Une procédure qui permet d'enrégistrer une nouvelle consommable
        Paramètre: liste des entrys => ID, Nom, Qte S, Qte s, Prix, cat
    """
    #Recuperation des données
    id_cons = liste_de_entry[0].get() ; id_cons_val = False
    nom_cons = liste_de_entry[1].get(); nom_cons_val = False
    prix_u_cons= liste_de_entry[2].get(); prix_u_cons_val = False
    qte_stock_cons = liste_de_entry[3].get(); qte_stock_cons_val = False
    qte_seuil_cons = liste_de_entry[4].get(); qte_seuil_cons_val = False
    categorie_cons = liste_de_entry[5].get().split()[0]; categorie_cons_val = False
    
    #Verification de l'identité 
    try:
        id_cons = int(id_cons)
        id_cons_val = True
        liste_de_entry[0].configure(border_color = set.col_noir_1)
    except:
        id_cons_val = False
        liste_de_entry[0].configure(border_color = set.col_rouge)
    
    #Verification du nom
    if nom_cons != "":
        nom_cons_val = True
        liste_de_entry[1].configure(border_color = set.col_noir_1)
    else:
        nom_cons_val = False
        liste_de_entry[1].configure(border_color = set.col_rouge)
    

    #Verification du prix unitaire
    try:
        prix_u_cons = int(prix_u_cons)
        assert prix_u_cons >= 0
        prix_u_cons_val = True
        liste_de_entry[2].configure(border_color = set.col_noir_1)
    except:
        prix_u_cons_val = False
        liste_de_entry[2].configure(border_color = set.col_rouge)

    #verification de la quantité en stock
    try:
        qte_stock_cons = int(qte_stock_cons)
        assert qte_stock_cons >= 0
        qte_stock_cons_val = True
        liste_de_entry[3].configure(border_color = set.col_noir_1)
    except:
        qte_stock_cons_val = False
        liste_de_entry[3].configure(border_color = set.col_rouge)

    #Verification de la quantité seuil
    try:
    
        qte_seuil_cons = int(qte_seuil_cons)
        assert qte_seuil_cons >= 0
        qte_seuil_cons_val = True
        liste_de_entry[4].configure(border_color = set.col_noir_1)
    except:
        qte_seuil_cons_val = False
        liste_de_entry[4].configure(border_color = set.col_rouge)



    #verification de l'id du categorie de consommable à laquelle elle appartient
    try:
        categorie_cons = int(categorie_cons)
        categorie_cons_val = True
        liste_de_entry[5].configure(border_color = set.col_noir_1)
    except:
        categorie_cons_val = False
        liste_de_entry[5].configure(border_color = set.col_rouge)

    validation = all([id_cons_val, nom_cons_val, prix_u_cons_val, qte_seuil_cons_val, qte_stock_cons_val, categorie_cons_val])


    if validation:
        consommable   = (id_cons, nom_cons, qte_stock_cons, qte_seuil_cons, categorie_cons, prix_u_cons)

        reponse = gp.inserer_consommable(consommable)
        if reponse :
            messagebox.showinfo("Enrégistrement","Enrégistrement du consommable a été effectué avec succès" )
            liste_de_entry[0].delete(0, tk.END)
            liste_de_entry[1].delete(0, tk.END)
            liste_de_entry[2].delete(0, tk.END)
            liste_de_entry[3].delete(0, tk.END)
            liste_de_entry[4].delete(0, tk.END)
            liste_de_entry[5].set("Choisir une catégorie")
        else:
            
            messagebox.showerror("Enregistrement", "Echec de l'opération !\nID consommable déjà existant")

    else:
        messagebox.showerror("Enregistrement", "Echec de l'opération !\nLes donées de certains champs sont invalides")


def consommables(framescrol):
    """ 
        procédure fondamentale de gestion des consommables:
        elle permet l'enregistrement, la recherche, le sauvegarde
    """
    #Définition des consommables
    

    
    #zone
    conso = ctk.CTkFrame(framescrol, width=1150, height=650, fg_color=set.col_blanc_4,
                         border_color=set.col_border,)
    conso.place(x= 0 , y=0)

    """Formulaire"""
    #Le formulaire
    formulaire = ctk.CTkFrame(conso, width=580, height=550,fg_color=set.col_blanc_4 ,border_color=set.col_noir_1,
                         border_width=1)
    formulaire.place(x=200, y=15)

    liste_conso = ctk.CTkLabel(conso, text= "FORMULAIRE", fg_color =set.col_blanc_4,font = ('Montsérrat', 20),
                             text_color =set.col_noir_1)
    liste_conso.place(x=230, y=8)

    

    #Identifier Verificqtion de l'ID
    id = ctk.CTkLabel(formulaire, text='Identifiant :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    id.place(x=20, y=40)
    id_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=350, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    id_e.place(x=200, y= 40)
    
    #Nom du produit
    nom = ctk.CTkLabel(formulaire, text='Nom :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    nom.place(x=20, y=100)
    nom_e = ctk.CTkEntry(formulaire, placeholder_text="Nom du consommable",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=350, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    nom_e.place(x=200, y= 100)

    #Prix unitaire
    prix_unitaire = ctk.CTkLabel(formulaire, text='Prix unitaire :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    prix_unitaire.place(x=20, y=160)
    prix_unitaire_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=350, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    prix_unitaire_e.place(x=200, y= 160)


    #Quantité en stock du produit
    qtestock = ctk.CTkLabel(formulaire, text='Qte en stock :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    qtestock.place(x=20, y=210)
    qtestock_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=350, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    qtestock_e.place(x=200, y= 210)

    #Quantité seuil du produit a respecter
    qteseuil = ctk.CTkLabel(formulaire, text='Qte seuil :', font= ("Montsérrat",20), text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    qteseuil.place(x=20, y=270)
    qteseuil_e = ctk.CTkEntry(formulaire, placeholder_text="0",text_color=set.col_noir_1,  fg_color= set.col_blanc_4,
                        placeholder_text_color=set.col_placeholder, justify = 'right', width=350, height=30, corner_radius=5,
                        font= ("Montsérrat",15))
    qteseuil_e.place(x=200, y= 270)


    #Categories
    option = gp.get_categories()
    options = ["Choisir une catégorie"]+[str(i[0])+' '+i[1] for i in option]
    categorie = ctk.CTkLabel(formulaire, text='Catégorie :', font= ("Montsérrat",20),text_color=set.col_noir_1,fg_color= set.col_blanc_4)
    categorie.place(x=20, y=330)
    categorie_e= ctk.CTkComboBox(master=formulaire, width=350, height=30, fg_color=set.col_blanc_4, border_width=1, 
                            border_color=set.col_noir_1, values=options,
                            font=('Montsérrat', 12,), text_color= set.col_noir_1, corner_radius=5,
                            )
   
    categorie_e.place(x=200, y=330)

    #Les boutons
    liste_entry = [id_e, nom_e, prix_unitaire_e, qtestock_e, qteseuil_e, categorie_e] #liste des entry
    rechercher_cons = ctk.CTkButton(formulaire, text = "Rechercher".upper(),width=50,height=40, command = lambda :recherche(liste_entry)
                               ,font=('Montsérrat', 15), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    rechercher_cons.place(x=20, y=480)
    
    
    enregistrer_cons = ctk.CTkButton(formulaire, text = "Enregistrer".upper(),width=50,height=40, command = lambda: enregistre(liste_entry)
                               ,font=('Montsérrat', 15), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    enregistrer_cons.place(x=250, y=480)

    modifier_cons = ctk.CTkButton(formulaire, text = "Modifier".upper(),width=50,height=40, command = lambda : modifie(liste_entry)
                               ,font=('Montsérrat', 15), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    modifier_cons.place(x=480, y=480)



    voir_liste = ctk.CTkButton(conso, text = "Aperçu des consommables".upper(),width=50,height=35, command = lambda : lister_les_consommable()
                               ,font=('Montsérrat', 15), fg_color= set.col_noir_5, hover_color= set.col_hover, corner_radius=5)
    voir_liste.place(x=400, y=590)

def consommable(framescrol):
    liste_cons = ctk.CTkScrollableFrame(framescrol, height=630,width=970)
    liste_cons.pack(fill = 'both')
    """
    liste_des_consommables = gp.get_consommables()
    for cons in liste_des_consommables:
        uncons.build_consommable(cons[0] ,liste_cons)
    """
   
    uncons.build_consommable(1,liste_cons)
    uncons.build_consommable(2,liste_cons)