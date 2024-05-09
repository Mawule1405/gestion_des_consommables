import customtkinter as ctk
from PIL import Image



from statistiques.appro_consommable import emp_commande_conso as euc
from statistiques.appro_consommable import emp_ne_commande_pas_conso as enuc
from statistiques.appro_consommable import graphiques as gr
from statistiques.appro_consommable import autres_fonctions as af
import graphi_print as gp
import setting as set

 

def build_statistique(statFrame):
    def switch(aff_frame_x,indicate_l,page):
        """
        Cette procédure permet de ce switcher entre les pages en cliquant dur les boutons
        paramètres: liste de buton,   u_ne zone d'affichage, la page à ouvrir
        
        """
        for widget in aside_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel):
                widget.configure(fg_color = set.col_noir_1)

        indicate_l.configure(fg_color= set.col_blanc_1)

        for iframe in aff_frame_x.winfo_children():
            iframe.destroy()
        
        aff_frame_x.update()
        page()

    #zone de lien
    slide_frame = ctk.CTkScrollableFrame(statFrame, width=400, height= 650, border_color= set.col_border, border_width=1,
                                fg_color=set.col_blanc_4, corner_radius=0)
    slide_frame.place(x=0, y=0)

    #zone d'affichage
    aff_frame = ctk.CTkFrame(statFrame, width=1000, height= 645, border_color= set.col_border, border_width=1,
                                fg_color=set.col_blanc_4, corner_radius=0)
    aff_frame.place(x=200, y=0)

    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(600,600))

    fond = ctk.CTkLabel(aff_frame,text=0,image=image)
    fond.place(x=0, y=0)

    #Les boutons présentants les grandes fonctionnalités de l'application
    aside_frame = ctk.CTkFrame(slide_frame, height=800,fg_color=set.col_noir_1)
    aside_frame.pack(fill = "both")

    #Fonctionnalité 1: statistique sur l'approvisionnement en consommables
    fonction_1 = ctk.CTkButton(aside_frame,text='Approvisionnement\nen consimmables'.upper(),width=190, height=40, fg_color=set.col_noir_1
                               ,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch(aff_frame,fonction_1_label,approvisionnement_en_consommable))
    fonction_1.place(x=2,y=1)
    fonction_1_label = ctk.CTkLabel(aside_frame,text="", width=10, height=40, fg_color=set.col_blanc_1)
    fonction_1_label.place(x=192, y=1)
    
    
    fonction_2 = ctk.CTkButton(aside_frame,text="Utilisations des\n consommables".upper(), width=196, height=40, fg_color=set.col_noir_1,corner_radius=0, 
                               hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : switch(aff_frame,fonction_2_label, utilisation_de_consommable))
    fonction_2.place(x=2,y=42)
    fonction_2_label = ctk.CTkLabel(aside_frame,text="", width=10, height=40,)
    fonction_2_label.place(x=192, y=42)


    fonction_3 = ctk.CTkButton(aside_frame,text="Attribution de consommables".upper(), width=190, height=40, fg_color=set.col_noir_1,
                               corner_radius=0, 
                               hover_color=set.col_hover,font= ('Montsérrat',11),  
                           command= lambda : switch(aff_frame,fonction_3_label,  vue_sur_les_consommables))
    fonction_3.place(x=2,y=84)
    fonction_3_label = ctk.CTkLabel(aside_frame,text="", width=10, height=40)
    fonction_3_label.place(x=192, y=84)



    """fonction_4 = ctk.CTkButton(aside_frame,text="Approvisionnement".upper(), width=190, height=40, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : switch(aff_frame,fonction_4_label, page_vide))
    fonction_4.place(x=2,y=126)
    fonction_4_label = ctk.CTkLabel(aside_frame,text="", width=10, height=40)
    fonction_4_label.place(x=192, y=126)"""




    #Les fonctionnalités
    

    def approvisionnement_en_consommable():
        """
            Procédure de visualisation des statistiques les plus importants sur 
            les dépenses de l'entreprise pour s'approvisionner en consommmable
        """

        zone = ctk.CTkFrame(aff_frame, width=700, height=605, fg_color= set.col_blanc_4,border_width=5, border_color= set.col_noir_1,
                            corner_radius=5)
        zone.place(x=150, y=15)

        #======Ligne 1
        
        btn_1 = ctk.CTkButton(zone,width=300,height=80,text= "Liste des employés ayant effectués\n des commandes",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), command= lambda: euc.liste_emp_commande())
        btn_1.place(x=40, y= 10)

        btn_2 = ctk.CTkButton(zone,width=300,height=80,text= "Liste des employés n'ayant effectués\n aucune commandes",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"), command=lambda: enuc.liste_emp_non_commande())
        btn_2.place(x=365, y= 10)

        #========Ligne 2
        commandes = gp.get_commandes()
        data_1, data_2 =[], []
        for ligne in commandes:
            data_1.append((str(ligne[0]), ligne[3]))
            data_2.append((int(ligne[2]), int(ligne[3])))
        btn_3 = ctk.CTkButton(zone,width=300,height=80,text= "Représentation graphique des commandes",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                              command= lambda: gr.graphique_com_montant(data_1,"Présentation graphique des commandes", "ID commande", "Montant total"))
        btn_3.place(x=40, y= 110)

        btn_4 = ctk.CTkButton(zone,width=300,height=80,text= "Etude du montant total des commandes\n par rapport au nombre de consommables \ncommandés ",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda: gr.graphique_nombre_com_montant(data_2,"Le montant total par rapport au nombre de consommables", "Nombre de concommable", "Montant total"))
        btn_4.place(x=365, y= 110)


        #=======Ligne 3
        btn_5 = ctk.CTkButton(zone,width=300,height=80,text= "Dépense totale par mois",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                              command= lambda: gr.graphique_mois_depense("Dépenses totales de par mois en : ", "Mois", "Montant"))
        btn_5.place(x=40, y= 210)

        btn_6 = ctk.CTkButton(zone,width=300,height=80,text= "Dépense par année",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda: gr.graphique_anne_depense("Dépenses totales de par année", "Années", "Montants"))
        btn_6.place(x=365, y= 210)

        #=====Ligne 4

        btn_8 = ctk.CTkButton(zone,width=300,height=80,text= """La liste des commandes effectués dans \nun mois d'une année""",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda: af.liste_com_eff_moi_annee())
        btn_8.place(x=365, y= 310)

        #=====Ligne 5

        btn_10 = ctk.CTkButton(zone,width=300,height=80,text= "Les n consommables les plus commandées",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda:af.liste_des_n_consommables())
        btn_10.place(x=365, y= 410)

        #====Ligne 6

        btn_11 = ctk.CTkButton(zone,width=300,height=80,text="les comsommables les plus commandés \ndans chaque catégorie",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                              command= lambda:af.liste_des_cons_commande_categorie())
        btn_11.place(x=40, y= 310)

        btn_12 = ctk.CTkButton(zone,width=300,height=80,text= "Les consommables commandés par \nun employé suivants les dates",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda: af.liste_des_cons_commande_employe())
        btn_12.place(x=40, y= 410)

    approvisionnement_en_consommable()

    
    def utilisation_de_consommable():

        zone = ctk.CTkFrame(aff_frame, width=700, height=605, fg_color= set.col_blanc_4,border_width=5, border_color= set.col_noir_1,
                            corner_radius=5)
        zone.place(x=150, y=15)

        #======Ligne 1
        
        btn_1 = ctk.CTkButton(zone,width=300,height=80,text= "Liste des consommables \n les plus utilisés",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), command= lambda: 1)
        btn_1.place(x=40, y= 10)

        btn_2 = ctk.CTkButton(zone,width=300,height=80,text= "Liste des consommables \nles moins utilisés",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"), command=lambda: 2)
        btn_2.place(x=365, y= 10)

        #========Ligne 2
      
        btn_3 = ctk.CTkButton(zone,width=300,height=80,text= "Le coût total des\n consommables utilisés",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                              command= lambda: 3)
        btn_3.place(x=40, y= 110)

        btn_4 = ctk.CTkButton(zone,width=300,height=80,text= "la liste des consommables\n utilisés par un employé",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda: 4)
        btn_4.place(x=365, y= 110)


        #=======Ligne 3
        btn_5 = ctk.CTkButton(zone,width=300,height=80,text= "La liste des consommables\n les plus utilisés dans\n chaque catégorie.",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                              command= lambda: 5)
        btn_5.place(x=40, y= 210)

        btn_6 = ctk.CTkButton(zone,width=300,height=80,text= "La liste des consommables\n qui n'ont jamais\n été utilisé.",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda:5)
        btn_6.place(x=365, y= 210)

        #=====Ligne 4

        btn_8 = ctk.CTkButton(zone,width=300,height=80,text= """La liste des commandes effectués dans \nun mois d'une année""",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda: af.liste_com_eff_moi_annee())
       # btn_8.place(x=365, y= 310)

        #=====Ligne 5

        btn_10 = ctk.CTkButton(zone,width=300,height=80,text= "Les n consommables les plus commandées",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda:af.liste_des_n_consommables())
        #btn_10.place(x=365, y= 410)

        #====Ligne 6

        btn_11 = ctk.CTkButton(zone,width=300,height=80,text="les comsommables les plus commandés \ndans chaque catégorie",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                              command= lambda:af.liste_des_cons_commande_categorie())
        #btn_11.place(x=40, y= 310)

        btn_12 = ctk.CTkButton(zone,width=300,height=80,text= "Les consommables commandés par \nun employé suivants les dates",
                              fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                              command= lambda: af.liste_des_cons_commande_employe())
        #btn_12.place(x=40, y= 410)



    def vue_sur_les_consommables():

            zone = ctk.CTkFrame(aff_frame, width=700, height=605, fg_color= set.col_blanc_4,border_width=5, border_color= set.col_noir_1,
                                corner_radius=5)
            zone.place(x=150, y=15)

            #======Ligne 1
            
            btn_1 = ctk.CTkButton(zone,width=300,height=80,text= "Liste des consommables dont\n la quantité en stock est inférieur \nà la quantité seuil",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), command= lambda: 1)
            btn_1.place(x=40, y= 10)

            btn_2 = ctk.CTkButton(zone,width=300,height=80,text= "Liste des consommables \nles moins utilisés",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"), command=lambda: 2)
            #btn_2.place(x=365, y= 10)

            #========Ligne 2
        
            btn_3 = ctk.CTkButton(zone,width=300,height=80,text= "Le coût total des\n consommables utilisés",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                                command= lambda: 3)
            #btn_3.place(x=40, y= 110)

            btn_4 = ctk.CTkButton(zone,width=300,height=80,text= "la liste des consommables\n utilisés par un employé",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                                command= lambda: 4)
            #btn_4.place(x=365, y= 110)


            #=======Ligne 3
            btn_5 = ctk.CTkButton(zone,width=300,height=80,text= "La liste des consommables\n les plus utilisés dans\n chaque catégorie.",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                                command= lambda: 5)
            #btn_5.place(x=40, y= 210)

            btn_6 = ctk.CTkButton(zone,width=300,height=80,text= "La liste des consommables\n qui n'ont jamais\n été utilisé.",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                                command= lambda:5)
            #btn_6.place(x=365, y= 210)

            #=====Ligne 4

            btn_8 = ctk.CTkButton(zone,width=300,height=80,text= """La liste des commandes effectués dans \nun mois d'une année""",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                                command= lambda: af.liste_com_eff_moi_annee())
        # btn_8.place(x=365, y= 310)

            #=====Ligne 5

            btn_10 = ctk.CTkButton(zone,width=300,height=80,text= "Les n consommables les plus commandées",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                                command= lambda:af.liste_des_n_consommables())
            #btn_10.place(x=365, y= 410)

            #====Ligne 6

            btn_11 = ctk.CTkButton(zone,width=300,height=80,text="les comsommables les plus commandés \ndans chaque catégorie",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13, 'bold'), 
                                command= lambda:af.liste_des_cons_commande_categorie())
            #btn_11.place(x=40, y= 310)

            btn_12 = ctk.CTkButton(zone,width=300,height=80,text= "Les consommables commandés par \nun employé suivants les dates",
                                fg_color=set.col_noir_5,corner_radius=5, font=("Montsérrat", 13,"bold"),
                                command= lambda: af.liste_des_cons_commande_employe())
            #btn_12.place(x=40, y= 410)

    