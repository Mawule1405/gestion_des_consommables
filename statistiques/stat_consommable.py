"""
But: Module des fonctions des boutons de la zone des consommables
"""
#bibliothèque de python
import customtkinter as ctk
from PIL import Image
from datetime import datetime

#Mes modules
import graphi_print_2 as gp2
import setting as set


def liste_conso_utilise():
    """
    Procéduire de présentation de la liste des consommables utilisés
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable utilisés")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    listes_conso = gp2.liste_conso_utilise()

    ctk.CTkLabel(toplevel, text= "Liste des consommables utilisés dans l'entreprise",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "ID", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Nom", font = ("Montsérrat", 15, "bold")).place(x=70, y=30)
    ctk.CTkLabel(toplevel, text= "Quantité", font = ("Montsérrat", 15, "bold")).place(x=510, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)

    for conso in listes_conso:
        conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
        conso_frame.pack(fill = "both",padx=0, pady=0)

        ctk.CTkLabel(conso_frame, text= conso[0], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
        ctk.CTkLabel(conso_frame, text= conso[1], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=50, y=10)
        ctk.CTkLabel(conso_frame, text= conso[2], font = ("Montsérrat", 15, "bold"), text_color="bleu").place(x=500, y=10)
    

    
    toplevel.mainloop()



def liste_conso_non_utilise():
    """
    Procéduire de présentation de la liste des consommables non utilisés
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable non utilisés")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    listes_conso = gp2.liste_conso_non_utilise()

    ctk.CTkLabel(toplevel, text= "Liste des consommables non utilisés dans l'entreprise",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "ID", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Nom", font = ("Montsérrat", 15, "bold")).place(x=70, y=30)
    ctk.CTkLabel(toplevel, text= "Quantité", font = ("Montsérrat", 15, "bold")).place(x=510, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)

    for conso in listes_conso:
        conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
        conso_frame.pack(fill = "both",padx=0, pady=0)

        ctk.CTkLabel(conso_frame, text= conso[0], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
        ctk.CTkLabel(conso_frame, text= conso[1], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=50, y=10)
        ctk.CTkLabel(conso_frame, text= conso[2], font = ("Montsérrat", 15, "bold"), text_color="bleu").place(x=500, y=10)
    

    
    toplevel.mainloop()



def liste_conso_epuise():
    """
    Procéduire de présentation de la liste des consommables non utilisés
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable épuisés")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    listes_conso = gp2.liste_conso_epuise()

    ctk.CTkLabel(toplevel, text= "Liste des consommables épuisés",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "ID", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Nom", font = ("Montsérrat", 15, "bold")).place(x=70, y=30)
    ctk.CTkLabel(toplevel, text= "Qte stock", font = ("Montsérrat", 15, "bold")).place(x=430, y=30)
    ctk.CTkLabel(toplevel, text= "Qte seuil", font = ("Montsérrat", 15, "bold")).place(x=530, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)

    for conso in listes_conso:
        conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
        conso_frame.pack(fill = "both",padx=0, pady=0)

        ctk.CTkLabel(conso_frame, text= conso[0], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
        ctk.CTkLabel(conso_frame, text= conso[1], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=50, y=10)
        ctk.CTkLabel(conso_frame, text= conso[2], font = ("Montsérrat", 15, "bold"), text_color="red").place(x=410, y=10)
        ctk.CTkLabel(conso_frame, text= conso[3], font = ("Montsérrat", 15, "bold"), text_color="bleu").place(x=510, y=10)

    
    toplevel.mainloop()



def liste_conso_plus_utilise_par_categorie():
    """
    Procéduire de présentation de la liste des consommablesle plus utilisé dans chaque catégorie
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable le plus utilisés dans chaque catégorie")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    listes_conso = gp2.liste_conso_le_plus_utilise_par_categorie()

    ctk.CTkLabel(toplevel, text= "Liste des consommables les plus utilisés dans chaque catégorie",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "ID", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Nom", font = ("Montsérrat", 15, "bold")).place(x=60, y=30)
    ctk.CTkLabel(toplevel, text= "Catégorie", font = ("Montsérrat", 15, "bold")).place(x=300, y=30)
    ctk.CTkLabel(toplevel, text= "Quantité", font = ("Montsérrat", 15, "bold")).place(x=530, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)

    for conso in listes_conso:
        conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
        conso_frame.pack(fill = "both",padx=0, pady=0)

        ctk.CTkLabel(conso_frame, text= conso[0], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
        ctk.CTkLabel(conso_frame, text= conso[1], font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=40, y=10)
        ctk.CTkLabel(conso_frame, text= conso[2], font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=280, y=10)
        ctk.CTkLabel(conso_frame, text= conso[3], font = ("Montsérrat", 15, "bold"), text_color="bleu").place(x=510, y=10)

    
    toplevel.mainloop()



def liste_conso_plus_chere_par_categorie():
    """
    Procéduire de présentation de la liste des consommablesle plus chère dans chaque catégorie
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste de consommables le plus chère de chaque catégorie")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    listes_conso = gp2.liste_conso_le_plus_chere_par_categorie()

    ctk.CTkLabel(toplevel, text= "Liste des consommables les plus chère dans chaque catégorie",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "ID", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Nom", font = ("Montsérrat", 15, "bold")).place(x=60, y=30)
    ctk.CTkLabel(toplevel, text= "Catégorie", font = ("Montsérrat", 15, "bold")).place(x=300, y=30)
    ctk.CTkLabel(toplevel, text= "Prix", font = ("Montsérrat", 15, "bold")).place(x=430, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)

    for conso in listes_conso:
        conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
        conso_frame.pack(fill = "both",padx=0, pady=0)

        ctk.CTkLabel(conso_frame, text= conso[0], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
        ctk.CTkLabel(conso_frame, text= conso[1], font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=40, y=10)
        ctk.CTkLabel(conso_frame, text= conso[2], font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=280, y=10)
        ctk.CTkLabel(conso_frame, text= str(conso[3])+' FCFA', font = ("Montsérrat", 15, "bold"), text_color="bleu").place(x=410, y=10)

    
    toplevel.mainloop()



def liste_conso_utilise_par_annee():
    """
    Procéduire de présentation de la liste des consommablesle plus utilisé dans chaque année
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable le plus utilisés par année")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    

    ctk.CTkLabel(toplevel, text= "Liste des consommables les plus utilisés par année",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "ID", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Nom", font = ("Montsérrat", 15, "bold")).place(x=60, y=30)
    ctk.CTkLabel(toplevel, text= "Année", font = ("Montsérrat", 15, "bold")).place(x=450, y=30)
    ctk.CTkLabel(toplevel, text= "Quantité", font = ("Montsérrat", 15, "bold")).place(x=530, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)
    for annee in range(1970, datetime.now().date().year+1):
        listes_conso = gp2.liste_conso_utilise_par_annee(annee)
        for conso in listes_conso:
            conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
            conso_frame.pack(fill = "both",padx=0, pady=0)

            ctk.CTkLabel(conso_frame, text= conso[0], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
            ctk.CTkLabel(conso_frame, text= conso[1], font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=40, y=10)
            ctk.CTkLabel(conso_frame, text= annee, font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=450, y=10)
            ctk.CTkLabel(conso_frame, text= conso[3], font = ("Montsérrat", 15, "bold"), text_color="bleu").place(x=510, y=10)

    
    toplevel.mainloop()




def liste_conso_utilise_par_mois():
    """
    Procéduire de présentation de la liste des consommablesle plus utilisé dans chaque mois
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable le  utilisés par mois")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    

    ctk.CTkLabel(toplevel, text= "Liste des consommables  utilisés par mois",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "ID", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Nom", font = ("Montsérrat", 15, "bold")).place(x=60, y=30)
    ctk.CTkLabel(toplevel, text= "Mois Année", font = ("Montsérrat", 15, "bold")).place(x=370, y=30)
    ctk.CTkLabel(toplevel, text= "Quantité", font = ("Montsérrat", 15, "bold")).place(x=530, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)
    for indice, mois in enumerate(["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]):
        for annee in range(1970, datetime.now().date().year+1):
            listes_conso = gp2.liste_conso_utilise_par_mois(indice, annee)
            for conso in listes_conso:
                conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
                conso_frame.pack(fill = "both",padx=0, pady=0)

                ctk.CTkLabel(conso_frame, text= conso[0], font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
                ctk.CTkLabel(conso_frame, text= conso[1], font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=40, y=10)
                ctk.CTkLabel(conso_frame, text=mois+' '+str(annee), font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=350, y=10)
                ctk.CTkLabel(conso_frame, text= conso[3], font = ("Montsérrat", 15, "bold"), text_color="bleu").place(x=510, y=10)

    
    toplevel.mainloop()








def liste_montant_conso_utilise_par_mois():
    """
    Procéduire de présentation de la liste des consommablesle plus utilisé dans chaque mois
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable le plus utilisés par mois")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    

    ctk.CTkLabel(toplevel, text= "Liste des consommables les plus utilisés par mois",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "N° Ordre", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Mois Année", font = ("Montsérrat", 15, "bold")).place(x=170, y=30)
    ctk.CTkLabel(toplevel, text= "Total", font = ("Montsérrat", 15, "bold")).place(x=320, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)
    numero_ordre = 0
    for indice, mois in enumerate(["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]):
        for annee in range(1970, datetime.now().date().year+1):
            listes_conso = gp2.liste_montant_conso_utilise_par_mois(indice, annee)
            for conso in listes_conso:
                numero_ordre +=1
                conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
                conso_frame.pack(fill = "both",padx=0, pady=0)

                ctk.CTkLabel(conso_frame, text= numero_ordre, font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
                ctk.CTkLabel(conso_frame, text=mois+' '+str(annee), font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=150, y=10)
                ctk.CTkLabel(conso_frame, text= str(conso[0])+' FCFA', font = ("Montsérrat", 15, "bold"), text_color="red").place(x=300, y=10)


    toplevel.mainloop()




def liste_conso_commande_par_mois():
    """
    Procéduire de présentation de la liste des consommablesle plus commandés chaque mois
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable commandés par mois")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    

    ctk.CTkLabel(toplevel, text= "Liste des consommables commandés par mois",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "N° Ordre", font = ("Montsérrat", 14, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Mois Année", font = ("Montsérrat", 14, "bold")).place(x=100, y=30)
    ctk.CTkLabel(toplevel, text= "Consommable", font = ("Montsérrat", 14, "bold")).place(x=220, y=30)
    ctk.CTkLabel(toplevel, text= "Montant", font = ("Montsérrat", 14, "bold")).place(x=510, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)
    numero_ordre = 0
    for indice, mois in enumerate(["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]):
        for annee in range(1970, datetime.now().date().year+1):
            listes_conso = gp2.liste_conso_commande_par_mois(indice, annee)
            for conso in listes_conso:
                numero_ordre +=1
                conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
                conso_frame.pack(fill = "both",padx=0, pady=0)

                ctk.CTkLabel(conso_frame, text= numero_ordre, font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
                ctk.CTkLabel(conso_frame, text=mois+' '+str(annee), font = ("Montsérrat", 12, "bold"), corner_radius=0).place(x=80, y=10)
                ctk.CTkLabel(conso_frame, text= str(conso[0]), font = ("Montsérrat", 12, "bold"), corner_radius=0).place(x=200, y=10)
                ctk.CTkLabel(conso_frame, text= str(conso[1])+' FCFA', font = ("Montsérrat", 12, "bold"), text_color="red").place(x=490, y=10)


    toplevel.mainloop()





def liste_montant_commande_par_mois():
    """
    Procéduire de présentation de la liste des dépenses effectuées pour des commandes dans un mois
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des dépenses effectuées pour des commandes dans un mois d'une année")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    

    ctk.CTkLabel(toplevel, text= "Liste des dépenses effectuées pour des commandes dans un mois d'une année",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "N° Ordre", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Mois Année", font = ("Montsérrat", 15, "bold")).place(x=170, y=30)
    ctk.CTkLabel(toplevel, text= "Montant", font = ("Montsérrat", 15, "bold")).place(x=320, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=350)
    aff_liste_frame.place(x=10, y=60)
    numero_ordre = 0
    montant_total = 0
    for indice, mois in enumerate(["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]):
        for annee in range(1970, datetime.now().date().year+1):
            listes_conso = gp2.liste_montant_commande_par_mois(indice, annee)
            for conso in listes_conso:
                numero_ordre +=1
                montant_total+=conso[0]
                conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
                conso_frame.pack(fill = "both",padx=0, pady=0)

                ctk.CTkLabel(conso_frame, text= numero_ordre, font = ("Montsérrat", 15, "bold"), corner_radius=0).place(x=10, y=10)
                ctk.CTkLabel(conso_frame, text=mois+' '+str(annee), font = ("Montsérrat", 14, "bold"), corner_radius=0).place(x=150, y=10)
                ctk.CTkLabel(conso_frame, text= str(conso[0])+' FCFA', font = ("Montsérrat", 15, "bold"), text_color="red").place(x=300, y=10)

    ctk.CTkLabel(toplevel, text= "Total:", font = ("Montsérrat", 20, "bold")).place(x=250, y=450)
    ctk.CTkLabel(toplevel, text= str(montant_total)+' FCFA', font = ("Montsérrat", 20, "bold"), text_color= "red").place(x=320, y=450)
    toplevel.mainloop()






def liste_conso_plus_commande_par_categorie():
    """
    Procéduire de présentation de la liste des consommablesle plus utilisé dans chaque catégorie
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des consommable le plus commandés dans chaque catégorie")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    listes_conso = gp2.liste_conso_plus_commande_par_categorie()

    ctk.CTkLabel(toplevel, text= "Liste des consommables les plus commandés dans chaque catégorie",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "ID", font = ("Montsérrat", 15, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Nom", font = ("Montsérrat", 15, "bold")).place(x=60, y=30)
    ctk.CTkLabel(toplevel, text= "Catégorie", font = ("Montsérrat", 15, "bold")).place(x=420, y=30)
    ctk.CTkLabel(toplevel, text= "Quantité", font = ("Montsérrat", 15, "bold")).place(x=530, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)

    for conso in listes_conso:
        conso_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
        conso_frame.pack(fill = "both",padx=0, pady=0)

        ctk.CTkLabel(conso_frame, text= conso[0], font = ("Montsérrat", 15, "bold"),).place(x=10, y=10)
        ctk.CTkLabel(conso_frame, text= conso[1], font = ("Montsérrat", 12, "bold"),).place(x=40, y=10)
        ctk.CTkLabel(conso_frame, text= conso[2], font = ("Montsérrat", 12, "bold"),text_color="bleu").place(x=400, y=10)
        ctk.CTkLabel(conso_frame, text= conso[3], font = ("Montsérrat", 15, "bold"),text_color="red").place(x=510, y=10)

    
    toplevel.mainloop()





def liste_des_commandes_effectifs():
    """
    Procéduire de présentation de la liste des commandes effectifs
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Liste des commandes effectuées")
    toplevel.attributes('-topmost', True)

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    
    ctk.CTkLabel(toplevel, text= "Liste des commandes effectuées",font = ("Montsérrat", 15, "bold")).place(x=30, y=5)

    #entete de la liste
    ctk.CTkLabel(toplevel, text= "N°", font = ("Montsérrat", 13, "bold")).place(x=30, y=30)
    ctk.CTkLabel(toplevel, text= "Date", font = ("Montsérrat", 13, "bold")).place(x=70, y=30)
    ctk.CTkLabel(toplevel, text= "Employé", font = ("Montsérrat", 13, "bold")).place(x=150, y=30)
    ctk.CTkLabel(toplevel, text= "Fournisseur", font = ("Montsérrat", 13, "bold")).place(x=350, y=30)
    ctk.CTkLabel(toplevel, text= "Montant", font = ("Montsérrat", 13, "bold")).place(x=500, y=30)

    aff_liste_frame = ctk.CTkScrollableFrame(toplevel, width=570, height=400)
    aff_liste_frame.place(x=10, y=60)
    
    
    listes_com = gp2.liste_des_commandes_effectues()
    for com in listes_com:
        com_frame = ctk.CTkFrame(aff_liste_frame,height=50, fg_color= set.col_blanc_4)
        com_frame.pack(fill = "both",padx=0, pady=0)

        ctk.CTkLabel(com_frame, text=com[0] , font = ("Montsérrat", 11, "bold"), corner_radius=0).place(x=10, y=10)
        ctk.CTkLabel(com_frame, text= com[4], font = ("Montsérrat", 11, "bold"), corner_radius=0).place(x=50, y=10)
        ctk.CTkLabel(com_frame, text=com[1]+" "+com[2], font = ("Montsérrat", 11, "bold"), corner_radius=0).place(x=130, y=10)
        ctk.CTkLabel(com_frame, text=com[3], font = ("Montsérrat", 11, "bold"), corner_radius=0).place(x=330, y=10)
        ctk.CTkLabel(com_frame, text= str(com[5])+' FCFA', font = ("Montsérrat", 11, "bold"),text_color="red").place(x=480, y=10)


    toplevel.mainloop()


