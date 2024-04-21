import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime



import graphi_print as gp
import setting as set

def supprimer_tout_le_tree(tree):
        items = tree.get_children()  # Obtenez tous les éléments du TreeView
        for item in items:
            tree.delete(item)

def liste_com_eff_moi_annee():
    def check_1():
        val = checkbox1.get()
        
        if val:
           
            entry1.configure(state = tk.NORMAL)
        else:
            entry1.configure(state ="disable")

    def check_2():
        val = checkbox2.get()
        if val:
            entry2.configure(state = tk.NORMAL)
        else:
            entry2.configure(state = "disable")

     

    def valider():
        # Vérifier l'état des checkbox et agir en conséquence
        if var_entry1.get() and var_entry2.get():
            mois = entry1.get()
            annee = entry2.get()

            try:
                mois = int(mois)
                annee = int(annee)
               
                assert 0 < mois < 13
                assert 2010 < annee < datetime.now().date().year+1
                
                data = gp.liste_montant_com_mois_annee(annee, mois)
               
                supprimer_tout_le_tree(tree_com)
                for ligne in data:
                    tree_com.insert('', tk.END, values=ligne)
            
            except:
                messagebox.showerror("Validation", "L'un des valeurs est invalides")


            # Insérer ici le code pour exécuter lorsque les deux entry sont activés
        elif var_entry1.get():
            mois = entry1.get()
            try:
                mois = int(mois)
                assert 0 < mois < 13
                data = gp.liste_montant_com_mois_2(mois)
               
                supprimer_tout_le_tree(tree_com)
                for ligne in data:
                    tree_com.insert('', tk.END, values=ligne)

            except:
                messagebox.showerror("Validation", "Valeur invalide!")
            # Insérer ici le code pour exécuter lorsque seul entry 1 est activé
        
        elif var_entry2.get():

            annee = entry2.get()
            try:
                annee = int(annee)
                
                assert 2010 < annee < datetime.now().date().year+1

                data = gp.liste_montant_com_annee_2(annee)
            
                supprimer_tout_le_tree(tree_com)
                for ligne in data:
                    tree_com.insert('', tk.END, values=ligne)
            except:
                messagebox.showerror("Validation" , "Valeur invalide!")
            # Insérer ici le code pour exécuter lorsque seul entry 2 est activé
        else:
            print("Aucun entry n'est activé")


    top = ctk.CTkToplevel()
    top.title("Liste des commandes effectués dans un mois d'une année")
    top.geometry('700x600+0+0')
    top.resizable(width=False, height=False)
    top.configure(fg_color = set.col_blanc_4)
    top.attributes('-topmost', True)

    frame = ctk.CTkFrame(top, fg_color=set.col_blanc_4, border_width=2, border_color=set.col_noir_1, height=550)
    frame.pack(fill='both', pady=20, padx= 15)

    # Variables de contrôle pour les checkboxes
    var_entry1 = ctk.IntVar()
    var_entry2 = ctk.IntVar()

    # Création des checkboxes
    checkbox1 = ctk.CTkCheckBox(frame, text="Mois", variable=var_entry1, onvalue=1, offvalue=0,command= check_1,
                                fg_color=set.col_noir_1
                                )
    checkbox1.place(x=10,y=15)
    checkbox2 = ctk.CTkCheckBox(frame, text="Année", variable=var_entry2, onvalue=1, offvalue=0, command= check_2,
                                fg_color=set.col_noir_1
                                )
    checkbox2.place(x=300, y=15)

    # Création des Entry
    entry1 = ctk.CTkEntry(frame, state="disable",placeholder_text="Mois: DD",fg_color=set.col_blanc_4, corner_radius=5,
                        height=30,width=100)
    entry1.place(x=100,y=15)
    entry2 = ctk.CTkEntry(frame, state="disable",placeholder_text="Année: YYYY",fg_color=set.col_blanc_4, corner_radius=5,
                        height=30,width=100)
    entry2.place(x=400,y=15)

    # Création du bouton
    bouton_valider = ctk.CTkButton(frame,height=30, width=100, text="VALIDER",fg_color=set.col_noir_5, command=valider)
    bouton_valider.place(x=520, y=15)


    tableau = ctk.CTkScrollableFrame(frame,height=400, width=620, fg_color=set.col_blanc_4, border_width=1, corner_radius=5)
    tableau.place(x= 10, y= 80)

    style_com = ttk.Style()
    style_com.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), rowheight=5, foreground=set.col_fg)
    style_com.configure("Treeview", font=('Helvetica', 12, 'bold'), rowheight=30,)
    tree_com = ttk.Treeview(tableau, columns=('id_com', 'date_com',"nombre_com","montant_com"),
                             show='headings', height=50)

    # Définir les en-têtes
    tree_com.column('id_com', width=75) 
    tree_com.heading('id_com', text='ID')
    tree_com.heading('date_com', text='Date')
    tree_com.heading('nombre_com', text='Nombre Conso')
    tree_com.heading('montant_com', text='Montant (FCFA)')
   
    liste_com = []
  
    for ligne in liste_com:

        tree_com.insert('', tk.END, values=ligne)

    tree_com.pack(fill= "both", pady=15, padx=10)



    top.mainloop()


def liste_des_n_consommables():
    """
        Une procédure permettant de connaitre les n consommables les plus utilisés dans la société
    """
    def valider():
        nombre = entry1.get()
        try:
            nombre = int(nombre)
            assert nombre >0
            data = gp.liste_des_n_consommables(nombre)
            supprimer_tout_le_tree(tree_com)
            for ligne in data:
                tree_com.insert('', tk.END, values=ligne)
        except:
            messagebox.showerror("Validation", "La valeur entrer est invalide")
    top = ctk.CTkToplevel()
    top.title("Liste des commandes effectués dans un mois d'une année")
    top.geometry('700x600+0+0')
    top.resizable(width=False, height=False)
    top.configure(fg_color = set.col_blanc_4)
    top.attributes('-topmost', True)

    frame = ctk.CTkFrame(top, fg_color=set.col_blanc_4, border_width=2, border_color=set.col_noir_1, height=550)
    frame.pack(fill='both', pady=20, padx= 15)

    

    # Création des Entry
    entry1 = ctk.CTkEntry(frame,placeholder_text="Entrer le nombre",fg_color=set.col_blanc_4, corner_radius=5,justify="right",
                        height=30,width=200)
    entry1.place(x=10,y=15)
   

    # Création du bouton
    bouton_valider = ctk.CTkButton(frame,height=30, width=100, text="VALIDER",fg_color=set.col_noir_5, command=valider)
    bouton_valider.place(x=520, y=15)


    tableau = ctk.CTkScrollableFrame(frame,height=450, width=620, fg_color=set.col_blanc_4, border_width=1, corner_radius=5)
    tableau.place(x= 10, y= 80)

    style_com = ttk.Style()
    style_com.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), rowheight=5, foreground=set.col_fg)
    style_com.configure("Treeview", font=('Helvetica', 12, 'bold'), rowheight=30,)
    tree_com = ttk.Treeview(tableau, columns=('id_cons', 'nom_cons',"nombre_cons"),
                             show='headings', height=50)

    # Définir les en-têtes
    tree_com.column('id_cons', width=75) 
    tree_com.column('nom_cons', width=300) 
    tree_com.heading('id_cons', text='ID')
    tree_com.heading('nom_cons', text='Nom')
    tree_com.heading('nombre_cons', text='Nombre')
   
   
    liste_com = []
  
    for ligne in liste_com:

        tree_com.insert('', tk.END, values=ligne)

    tree_com.pack(fill= "both", pady=15, padx=10)



    top.mainloop()


def liste_des_cons_commande_categorie():
    """
    Procédure pour connaître les consommables plus commandés dans chaque catégories
    """
    top = ctk.CTkToplevel()
    top.title("Liste des consommables les plus commandés dans chaque catégorie")
    top.geometry('700x600+0+0')
    top.resizable(width=False, height=False)
    top.configure(fg_color = set.col_blanc_4)
    top.attributes('-topmost', True)

    frame = ctk.CTkFrame(top, fg_color=set.col_blanc_4, border_width=2, border_color=set.col_noir_1, height=550)
    frame.pack(fill='both', pady=20, padx= 15)
   

    tableau = ctk.CTkScrollableFrame(frame,height=500, width=620, fg_color=set.col_blanc_4, border_width=1, corner_radius=5)
    tableau.place(x= 10, y= 10)

    style_com = ttk.Style()
    style_com.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), rowheight=5, foreground=set.col_fg)
    style_com.configure("Treeview", font=('Helvetica', 12, 'bold'), rowheight=30,)
    tree_com = ttk.Treeview(tableau, columns=('id_cons', 'nom_cons',"nombre_cons"),
                             show='headings', height=50)

    # Définir les en-têtes
    tree_com.column('id_cons', width=75) 
    tree_com.column('nom_cons', width=300) 
    tree_com.heading('id_cons', text='ID')
    tree_com.heading('nom_cons', text='Nom')
    tree_com.heading('nombre_cons', text='Nombre')
   
   
    liste_com = gp.liste_des_conso_commande_cat()
  
    for ligne in liste_com:

        tree_com.insert('', tk.END, values=ligne)

    tree_com.pack(fill= "both", pady=15, padx=10)



    top.mainloop()



def liste_des_cons_commande_employe():
    """
    Procédure pour connaître les consommables plus commandés dans chaque catégories
    """

    def valider():
        id_emp = choix_emp.get().split()[0]
        id_emp=int(id_emp)

        supprimer_tout_le_tree(tree_com)
        employes = gp.liste_conso_commande_employe(id_emp)
        for emp in employes:
            tree_com.insert('', tk.END, values=emp)


    top = ctk.CTkToplevel()
    top.title("Liste des consommables les plus commandés dans chaque catégorie")
    top.geometry('700x600+0+0')
    top.resizable(width=False, height=False)
    top.configure(fg_color = set.col_blanc_4)
    top.attributes('-topmost', True)

    frame = ctk.CTkFrame(top, fg_color=set.col_blanc_4, border_width=2, border_color=set.col_noir_1, height=550)
    frame.pack(fill='both', pady=20, padx= 15)

    employes = gp.get_employes()
    options  = [str(emp[0])+" "+emp[1]+" "+emp[2]  for emp in employes]

    #Choix d'un employé
    choix_emp = ctk.CTkComboBox(frame, fg_color=set.col_blanc_4, width=300, height=30,values= options,
                                corner_radius=5, border_width=1)
    choix_emp.place(x= 100, y=15)

    #Button de validation pour lancer la recherhe
    validation_btn = ctk.CTkButton(frame, fg_color= set.col_noir_5, width=100, text= "VALIDER", height=30, command= valider
                                   )
    validation_btn.place(x=450, y=15)

    tableau = ctk.CTkScrollableFrame(frame,height=400, width=620, fg_color=set.col_blanc_4, border_width=1, corner_radius=5)
    tableau.place(x= 10, y= 80)

    style_com = ttk.Style()
    style_com.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), rowheight=5, foreground=set.col_fg)
    style_com.configure("Treeview", font=('Helvetica', 12, 'bold'), rowheight=30,)
    tree_com = ttk.Treeview(tableau, columns=('nom_cons', 'date_com',"prix_cons","nombre_cons"),
                             show='headings', height=50)

    # Définir les en-têtes
    tree_com.heading('nom_cons', text='Consommables')
    tree_com.heading('date_com', text='Date')
    tree_com.heading('prix_cons', text='Prix (FCFA)')
    tree_com.heading('nombre_cons', text='Nombre')
   
   
    liste_com = gp.liste_conso_commande_employe(1)
  
    for ligne in liste_com:

        tree_com.insert('', tk.END, values=ligne)

    tree_com.pack(fill= "both", pady=15, padx=10)



    top.mainloop()