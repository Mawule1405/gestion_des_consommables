import customtkinter as ctk
from PIL import Image



import statistiques.stat_employe as sse
import statistiques.stat_consommable as ssc
import setting as set

 
def build_statistique(statFrame):
   
    #zone d'affichage
    aff_frame = ctk.CTkScrollableFrame(statFrame, width=1180, height= 650, border_color= set.col_border, border_width=0,
                                fg_color=set.col_blanc_4, corner_radius=0)
    aff_frame.place(x=0, y=0)

    #==============STATISTIQUE SUR L'EFFECTIFS ET QUANTITES
    employe_frame = ctk.CTkFrame(aff_frame, width=1175, height= 350, border_color= set.col_border, border_width=1,
                                fg_color=set.col_blanc_4, corner_radius=0)
    employe_frame.pack(fill="both", padx=10, pady=5)

    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(1175,350))

    fond = ctk.CTkLabel(employe_frame,text=0,image=image)
    fond.place(x=0, y=0)

    ctk.CTkLabel(employe_frame,text="Statistique sur les employés".upper(), font = ("Montsérrat", 15, 'bold')).place(x=5, y=15)

    nbre_emp = ctk.CTkButton(employe_frame,text="Nombre d'employé".upper(),width=250, height=50, fg_color=set.col_noir_1
                               ,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : sse.nombre_employe())
    nbre_emp.place(x=10,y=50)
  
    
    emp_mieu_paye = ctk.CTkButton(employe_frame,text="Employé le mieux payé".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0, 
                               hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : sse.employe_mieux_paye())
    emp_mieu_paye.place(x=310,y=50)
  


    emp_plus_ancien = ctk.CTkButton(employe_frame,text="Employé le plus ancien".upper(), width=250, height=50, fg_color=set.col_noir_1,
                               corner_radius=0, hover_color=set.col_hover,font= ('Montsérrat',11),  command= lambda : sse.employe_le_plus_ancien())
    emp_plus_ancien.place(x=610,y=50)



    distribution_de_badget = ctk.CTkButton(employe_frame,text="Distributtion des médailles".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda: sse.distribution_de_medaille() )
    distribution_de_badget.place(x=910,y=50)


    employe_par_service = ctk.CTkButton(employe_frame,text="Nombre d'employés par service".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command=lambda: sse.nombre_employe_par_service() )
    employe_par_service.place(x=10,y=150)

    employe_mieux_paye_par_service = ctk.CTkButton(employe_frame,text="Employé le mieux payé \ndans chaque service".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda: sse.employe_mieux_paye_par_service() )
    employe_mieux_paye_par_service.place(x=310,y=150)


    employe_plus_ancien_par_service = ctk.CTkButton(employe_frame,text="Employé le plus ancien \ndans chaque service".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda: sse.employe_le_plus_ancien_par_service() )
    employe_plus_ancien_par_service.place(x=610,y=150)

    employe_le_plus_jeune = ctk.CTkButton(employe_frame,text="Employé le plus jeune \nde l'entreprise".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda:sse.employe_le_plus_jeune() )
    employe_le_plus_jeune.place(x=910,y=150)


    employe_le_plus_recent_par_service = ctk.CTkButton(employe_frame,text="Employé le plus jeune \ndans chaque service".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command=lambda: sse.employe_le_plus_jeune_par_service() )
    employe_le_plus_recent_par_service.place(x=10,y=250)

    """etude_statistique = ctk.CTkButton(employe_frame,text="Etude \nstatistique".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command=2 )
    etude_statistique.place(x=310,y=250)"""




    #==============STATISTIQUE SUR UTILISATIONS ET LA COMMANDES DES CONSOMMABLES
    consommable_frame = ctk.CTkFrame(aff_frame, width=1180, height= 420, border_color= set.col_border, border_width=1,
                                fg_color=set.col_blanc_4, corner_radius=0)
    consommable_frame.pack(fill="both", padx=10, pady=5)

    fond_image_path = "images/image_consommable/pngwing.com (1).png"
    fond_image = Image.open(fond_image_path)
    image = ctk.CTkImage(fond_image, size=(1175,420))

    fond = ctk.CTkLabel(consommable_frame,text=0,image=image)
    fond.place(x=0, y=0)

    ctk.CTkLabel(consommable_frame,text="Statistique sur les consommables".upper(), font = ("Montsérrat", 15, 'bold')).place(x=5, y=15)

    conso_utilise = ctk.CTkButton(consommable_frame,text="Liste des consommables \nutilisés".upper(),width=250, height=50, fg_color=set.col_noir_1
                               ,corner_radius=0, hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : ssc.liste_conso_utilise())
    conso_utilise.place(x=10,y=50)
  
    
    conso_non_utilise = ctk.CTkButton(consommable_frame,text="Liste des consommables \nnon utilisés".upper(), width=250, height=50, fg_color=set.col_noir_1,corner_radius=0, 
                               hover_color=set.col_hover,
                           font= ('Montsérrat',11), command= lambda : ssc.liste_conso_non_utilise())
    conso_non_utilise.place(x=310,y=50)
  


    conso_en_dessous_du_seuil = ctk.CTkButton(consommable_frame,text="Liste des consommables \népuisés".upper(), width=250, height=50, fg_color=set.col_noir_1,
                               corner_radius=0, hover_color=set.col_hover,font= ('Montsérrat',11),  command= lambda : ssc.liste_conso_epuise())
    conso_en_dessous_du_seuil.place(x=610,y=50)



    conso_plus_utilse_categorie = ctk.CTkButton(consommable_frame,text="Liste des consommables les plus \nutilisés par catégorie".upper(),
                                                 width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda: ssc.liste_conso_plus_utilise_par_categorie() )
    conso_plus_utilse_categorie.place(x=910,y=50)


    conco_plus_cher_par_cat = ctk.CTkButton(consommable_frame,text="Liste des consommables les plus \ncouteux dans chaque catégorie".upper(),
                                             width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda: ssc.liste_conso_plus_chere_par_categorie() )
    conco_plus_cher_par_cat.place(x=10,y=150)

    
    conco_utilise_dans_un_annee = ctk.CTkButton(consommable_frame,text="Liste des consommables \nutilisés dans une année".upper(),
                                             width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command=lambda: ssc.liste_conso_utilise_par_annee() )
    conco_utilise_dans_un_annee.place(x=310,y=150)



    conco_utilise_dans_un_mois = ctk.CTkButton(consommable_frame,text="Liste des consommables utilisés \ndans un mois d'une année".upper(),
                                             width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda: ssc.liste_conso_utilise_par_mois() )
    conco_utilise_dans_un_mois.place(x=610,y=150)


    conso_montant_utilise_mois = ctk.CTkButton(consommable_frame,text="Le montant des consommables \nutilisés par mois".upper(),
                                             width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command=lambda : ssc.liste_montant_conso_utilise_par_mois() )
    conso_montant_utilise_mois.place(x=910,y=150)


    conco_plus_commande_categorie = ctk.CTkButton(consommable_frame,text="Liste des consommables les plus\n commandés par catégories".upper(),
                                             width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda: ssc.liste_conso_plus_commande_par_categorie())
    
    conco_plus_commande_categorie.place(x=10,y=250)


    conso_plus_commande_dans_mois = ctk.CTkButton(consommable_frame,text="Liste des consommables \ncommandés dans un mois d'une année".upper(),
                                             width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : ssc.liste_conso_commande_par_mois() )
    conso_plus_commande_dans_mois.place(x=310,y=250)


    montant_depense_mensuelle = ctk.CTkButton(consommable_frame,text="La dépense mensuelle pour l'approvi-\nsionnement en consommables".upper(),
                                             width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command=lambda : ssc.liste_montant_commande_par_mois() )
    montant_depense_mensuelle.place(x=610,y=250)


    vue_des_commande = ctk.CTkButton(consommable_frame,text="Liste des commandes effectués".upper(),
                                             width=250, height=50, fg_color=set.col_noir_1,corner_radius=0,
                                hover_color=set.col_hover,
                           font= ('Montsérrat',11),  command= lambda : ssc.liste_des_commandes_effectifs())
    vue_des_commande.place(x=910,y=250)



    