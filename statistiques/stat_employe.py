"""
But: Module des fonctions des boutons de la zone employés
"""
#bibliothèque de python
import customtkinter as ctk
from PIL import Image

#Mes modules
import graphi_print_2 as gp2
import setting as set


def nombre_employe():
    """
    Procéduire de présentation de l'effectifs de l'entreprise en terme d'homme et de femme
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("550x500")
    toplevel.title("Effectif des employés de l'entreprise")
    toplevel.attributes('-topmost', True)

    nbre_femme = gp2.nombre_femme_employe()
    nbre_homme = gp2.nombre_homme_employe()

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,500))
    homme = ctk.CTkImage(Image.open("images/images_app/homme.png"), size=(150,250))
    femme = ctk.CTkImage(Image.open("images/images_app/femme.png"), size=(150,250))

    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)
    ctk.CTkLabel(toplevel, text="", image=homme).place(x=50,y=50)
    ctk.CTkLabel(toplevel, text="", image=femme).place(x=350,y=50)  

    ctk.CTkLabel(toplevel, text = f"Homme", font=('Montsérrat', 40, 'bold'), bg_color="transparent").place(x=50  , y=300)
    ctk.CTkLabel(toplevel, text = f"Femme", font=('Montsérrat', 40, 'bold'), bg_color="transparent").place(x=350  , y=300)

    ctk.CTkLabel(toplevel, text = f"{nbre_homme}", font=('Montsérrat', 100, 'bold'), bg_color="transparent").place(x=75  , y=350)
    ctk.CTkLabel(toplevel, text = f"{nbre_femme}", font=('Montsérrat', 100, 'bold'), bg_color="transparent").place(x=375  , y=350)

    toplevel.mainloop()


def employe_mieux_paye():
    """
    Procédure de présentation de l'employé le mieux payé
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Employé le mieux payé de l'entreprise")
    toplevel.attributes('-topmost', True)

    les_employes = gp2.employe_le_mieux_paye()
   

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,595))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    ctk.CTkLabel(toplevel, text = f"Employé le mieux payé de l'entreprise", font=('Montsérrat', 20, 'bold'),
                  bg_color="transparent").place(x=50  , y=5)
    
    liste_frame = ctk.CTkScrollableFrame(toplevel, width=580, height=400,fg_color=set.col_blanc_1)
    liste_frame.place(x=0, y=30)

    employe = les_employes[0]

    for employe in les_employes:
        #Traitement d'un employé le mieux payé de l'entreprise
        employe_frame = ctk.CTkFrame(liste_frame,height=250, fg_color= set.col_blanc_4)
        employe_frame.pack(fill = "both", pady=3)
        fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,250))
        ctk.CTkLabel(employe_frame, text="", image=fond_image).place(x=0,y=0)

        photo = ctk.CTkImage(Image.open(employe[4].replace("\\","/")), size=(150,200))
        photo_emp = ctk.CTkLabel(employe_frame, text="", image=photo)
        photo_emp.place(x=50,y=10)
        ctk.CTkLabel(employe_frame, text ="Nom: "+ employe[0], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=10)
        ctk.CTkLabel(employe_frame, text = "Prénoms: "+employe[1], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=60)
        ctk.CTkLabel(employe_frame, text = "Salaire: "+str(int(employe[2]))+' FCFA', font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=110)
        ctk.CTkLabel(employe_frame, text = "Niveau d'étude: "+ employe[3], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=160)
        ctk.CTkLabel(employe_frame, text = "Service: "+ employe[5], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=210)


    toplevel.mainloop()


def employe_mieux_paye_par_service():
    """
    Procédure de présentation de l'employé le mieux payé par service
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Employé le mieux payé dans chaque service de l'entreprise")
    toplevel.attributes('-topmost', True)

    les_employes = gp2.employe_le_mieux_paye_par_service()
   

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,595))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    ctk.CTkLabel(toplevel, text = f"Employé le mieux payé dans chaque service de l'entreprise", font=('Montsérrat', 15, 'bold'),
                  bg_color="transparent").place(x=50  , y=5)
    
    liste_frame = ctk.CTkScrollableFrame(toplevel, width=580, height=400,fg_color=set.col_blanc_1)
    liste_frame.place(x=0, y=30)


    for employe in les_employes:
        #Traitement d'un employé le mieux payé de l'entreprise
        employe_frame = ctk.CTkFrame(liste_frame,height=250, fg_color= set.col_blanc_4)
        employe_frame.pack(fill = "both", pady=3)
        fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,250))
        ctk.CTkLabel(employe_frame, text="", image=fond_image).place(x=0,y=0)

        photo = ctk.CTkImage(Image.open(employe[4].replace("\\","/")), size=(150,200))
        ctk.CTkLabel(employe_frame, text="", image=photo).place(x=50,y=10)
        ctk.CTkLabel(employe_frame, text ="Nom: "+ employe[0], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=10)
        ctk.CTkLabel(employe_frame, text = "Prénoms: "+employe[1], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=60)
        ctk.CTkLabel(employe_frame, text = "Salaire: "+str(int(employe[2]))+' FCFA', font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=110)
        ctk.CTkLabel(employe_frame, text = "Niveau d'étude: "+ employe[3], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=160)
        ctk.CTkLabel(employe_frame, text = "Service: "+ employe[5], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=210)
        

    toplevel.mainloop()


def employe_le_plus_ancien():
    """
    Procédure de présentation de l'employé le plus ancien
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Employé le plus ancien de l'entreprise")
    toplevel.attributes('-topmost', True)

    les_employes = gp2.employe_le_plus_ancien()
   

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,595))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    ctk.CTkLabel(toplevel, text = f"Employé le plus ancien de l'entreprise", font=('Montsérrat', 15, 'bold'),
                  bg_color="transparent").place(x=50  , y=5)
    
    liste_frame = ctk.CTkScrollableFrame(toplevel, width=580, height=400,fg_color=set.col_blanc_1)
    liste_frame.place(x=0, y=30)


    for employe in les_employes:
        #Traitement d'un employé le mieux payé de l'entreprise
        employe_frame = ctk.CTkFrame(liste_frame,height=300, fg_color= set.col_blanc_4)
        employe_frame.pack(fill = "both", pady=3)
        fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,300))
        ctk.CTkLabel(employe_frame, text="", image=fond_image).place(x=0,y=0)

        photo = ctk.CTkImage(Image.open(employe[4].replace("\\","/")), size=(150,200))
        ctk.CTkLabel(employe_frame, text="", image=photo).place(x=50,y=10)
        ctk.CTkLabel(employe_frame, text ="Nom: "+ employe[0], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=10)
        ctk.CTkLabel(employe_frame, text = "Prénoms: "+employe[1], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=60)
        ctk.CTkLabel(employe_frame, text = "Salaire: "+str(int(employe[2]))+' FCFA', font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=110)
        ctk.CTkLabel(employe_frame, text = "Niveau d'étude: "+ employe[3], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=160)
        ctk.CTkLabel(employe_frame, text = "Service: "+ employe[5], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=210)
        ctk.CTkLabel(employe_frame, text = "Ancienneté: "+ str(employe[6])+" ans", font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=260)
        


    toplevel.mainloop()


def employe_le_plus_ancien_par_service():
    """
    Procédure de présentation de l'employé le plus ancien dans chaque service
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Employé le plus ancien das chaque service de l'entreprise")
    toplevel.attributes('-topmost', True)

    les_employes = gp2.employe_le_plus_ancien_par_service()
   

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,595))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    ctk.CTkLabel(toplevel, text = f"Employé le mieux payé dans chaque service de l'entreprise", font=('Montsérrat', 15, 'bold'),
                  bg_color="transparent").place(x=50  , y=5)
    
    liste_frame = ctk.CTkScrollableFrame(toplevel, width=580, height=400,fg_color=set.col_blanc_1)
    liste_frame.place(x=0, y=30)


    for employe in les_employes:
        #Traitement d'un employé le mieux payé de l'entreprise
        employe_frame = ctk.CTkFrame(liste_frame,height=300, fg_color= set.col_blanc_4)
        employe_frame.pack(fill = "both", pady=3)
        fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,300))
        ctk.CTkLabel(employe_frame, text="", image=fond_image).place(x=0,y=0)

        photo = ctk.CTkImage(Image.open(employe[4].replace("\\","/")), size=(150,200))
        ctk.CTkLabel(employe_frame, text="", image=photo).place(x=50,y=10)
        ctk.CTkLabel(employe_frame, text ="Nom: "+ employe[0], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=10)
        ctk.CTkLabel(employe_frame, text = "Prénoms: "+employe[1], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=60)
        ctk.CTkLabel(employe_frame, text = "Salaire: "+str(int(employe[2]))+' FCFA', font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=110)
        ctk.CTkLabel(employe_frame, text = "Niveau d'étude: "+ employe[3], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=160)
        ctk.CTkLabel(employe_frame, text = "Service: "+ employe[5], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=210)
        ctk.CTkLabel(employe_frame, text = "Ancienneté: "+ str(employe[6])+" ans", font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=260)
        


    toplevel.mainloop()





def employe_le_plus_jeune():
    """
    Procédure de présentation de l'employé le plus jeune
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Employé le plus jeune de l'entreprise")
    toplevel.attributes('-topmost', True)

    les_employes = gp2.employe_le_plus_jeune()
   

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,595))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    ctk.CTkLabel(toplevel, text = f"Employé le plus jeune de l'entreprise", font=('Montsérrat', 15, 'bold'),
                  bg_color="transparent").place(x=50  , y=5)
    
    liste_frame = ctk.CTkScrollableFrame(toplevel, width=580, height=400,fg_color=set.col_blanc_1)
    liste_frame.place(x=0, y=30)


    for employe in les_employes:
        #Traitement d'un employé le mieux payé de l'entreprise
        employe_frame = ctk.CTkFrame(liste_frame,height=300, fg_color= set.col_blanc_4)
        employe_frame.pack(fill = "both", pady=3)
        fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,300))
        ctk.CTkLabel(employe_frame, text="", image=fond_image).place(x=0,y=0)

        photo = ctk.CTkImage(Image.open(employe[4].replace("\\","/")), size=(150,200))
        ctk.CTkLabel(employe_frame, text="", image=photo).place(x=50,y=10)
        ctk.CTkLabel(employe_frame, text ="Nom: "+ employe[0], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=10)
        ctk.CTkLabel(employe_frame, text = "Prénoms: "+employe[1], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=60)
        ctk.CTkLabel(employe_frame, text = "Salaire: "+str(int(employe[2]))+' FCFA', font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=110)
        ctk.CTkLabel(employe_frame, text = "Niveau d'étude: "+ employe[3], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=160)
        ctk.CTkLabel(employe_frame, text = "Service: "+ employe[5], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=210)
        ctk.CTkLabel(employe_frame, text = "Ancienneté: "+ str(employe[6])+" ans", font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=260)
        


    toplevel.mainloop()




def employe_le_plus_jeune_par_service():
    """
    Procédure de présentation de l'employé le plus jeune dans chaque service
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Employé le plus jeune dans chaque service de l'entreprise")
    toplevel.attributes('-topmost', True)

    les_employes = gp2.employe_le_plus_jeune_par_service()
   

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,595))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    ctk.CTkLabel(toplevel, text = f"Employé le plus jeune dans chaque service de l'entreprise", font=('Montsérrat', 15, 'bold'),
                  bg_color="transparent").place(x=50  , y=5)
    
    liste_frame = ctk.CTkScrollableFrame(toplevel, width=580, height=400,fg_color=set.col_blanc_1)
    liste_frame.place(x=0, y=30)


    for employe in les_employes:
        #Traitement d'un employé le mieux payé de l'entreprise
        employe_frame = ctk.CTkFrame(liste_frame,height=300, fg_color= set.col_blanc_4)
        employe_frame.pack(fill = "both", pady=3)
        fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,300))
        ctk.CTkLabel(employe_frame, text="", image=fond_image).place(x=0,y=0)

        photo = ctk.CTkImage(Image.open(employe[4].replace("\\","/")), size=(150,200))
        ctk.CTkLabel(employe_frame, text="", image=photo).place(x=50,y=10)
        ctk.CTkLabel(employe_frame, text ="Nom: "+ employe[0], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=10)
        ctk.CTkLabel(employe_frame, text = "Prénoms: "+employe[1], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=60)
        ctk.CTkLabel(employe_frame, text = "Salaire: "+str(int(employe[2]))+' FCFA', font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=110)
        ctk.CTkLabel(employe_frame, text = "Niveau d'étude: "+ employe[3], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=160)
        ctk.CTkLabel(employe_frame, text = "Service: "+ employe[5], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=210)
        ctk.CTkLabel(employe_frame, text = "Ancienneté: "+ str(employe[6])+" ans", font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=250  , y=260)
        


    toplevel.mainloop()



def nombre_employe_par_service():
    """
    Procédure de présentation de l'employé le plus jeune dans chaque service
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Employé le plus jeune dans chaque service de l'entreprise")
    toplevel.attributes('-topmost', True)

    services = gp2.nombre_employe_par_service()
   

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,595))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    ctk.CTkLabel(toplevel, text = f"Nombre d'employé dans chaque service", font=('Montsérrat', 15, 'bold'),
                  bg_color="transparent").place(x=50  , y=5)
    
    liste_frame = ctk.CTkScrollableFrame(toplevel, width=580, height=400,fg_color=set.col_blanc_1)
    liste_frame.place(x=0, y=30)

    service_frame = ctk.CTkFrame(liste_frame,height=50, fg_color= set.col_blanc_4)
    service_frame.pack(fill = "both")
    

    ctk.CTkLabel(service_frame, text ="Nom service", font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=50  , y=10)
    ctk.CTkLabel(service_frame, text ="Effectifs", font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=210  , y=10)
    ctk.CTkLabel(service_frame, text ="Responsable", font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=275  , y=10)
    
    for service in services:
        #Traitement d'un employé le mieux payé de l'entreprise
        service_frame = ctk.CTkFrame(liste_frame,height=50, fg_color= set.col_blanc_4)
        service_frame.pack(fill = "both", pady=1)
        ctk.CTkLabel(service_frame, text =service[0], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=50  , y=10)
        ctk.CTkLabel(service_frame, text =service[1], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=210  , y=10)
        ctk.CTkLabel(service_frame, text =service[2]+' '+service[3], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=275  , y=10)
        


    toplevel.mainloop()


def distribution_de_medaille():
    """
    Procédure de présentation de l'employé le plus jeune dans chaque service
    """
    toplevel = ctk.CTkToplevel()
    toplevel.geometry("600x500")
    toplevel.title("Employé le plus jeune dans chaque service de l'entreprise")
    toplevel.attributes('-topmost', True)

    les_employes = gp2.distribution_de_medaille()
   

    fond_image = ctk.CTkImage(Image.open("images/image_consommable/pngwing.com (1).png"), size=(600,595))
    ctk.CTkLabel(toplevel, text="", image=fond_image).place(x=0,y=0)

    ctk.CTkLabel(toplevel, text = f"Attribution de médaille aux employés", font=('Montsérrat', 15, 'bold'),
                  bg_color="transparent").place(x=50  , y=5)
    
    liste_frame = ctk.CTkScrollableFrame(toplevel, width=580, height=400,fg_color=set.col_blanc_1)
    liste_frame.place(x=0, y=30)


    for employe in les_employes:
        #Traitement d'un employé le mieux payé de l'entreprise
        employe_frame = ctk.CTkFrame(liste_frame,height=300, fg_color= set.col_blanc_4)
        employe_frame.pack(fill = "both", pady=3)
        
        photo = ctk.CTkImage(Image.open(employe[2].replace("\\","/")), size=(150,200))
        ctk.CTkLabel(employe_frame, text="", image=photo).place(x=10,y=10)

        if employe[3]>30:
            photox = ctk.CTkImage(Image.open("images/images_app/or.png"), size=(100,100))
            
        elif employe[3]>20:
            photox = ctk.CTkImage(Image.open("images/images_app/argent.png"), size=(100,100))
            
        elif employe[3]>15:
            photox = ctk.CTkImage(Image.open("images/images_app/bronze.png"), size=(100,100))
            
        else:
            photox = ctk.CTkImage(Image.open("images/images_app/defaut.png"), size=(100,100))
        
        ctk.CTkLabel(employe_frame, text="", image=photox).place(x=470,y=10) #médaille


        ctk.CTkLabel(employe_frame, text =employe[0]+" "+employe[1], font=('Montsérrat', 15, 'bold'), bg_color="transparent").place(x=180  , y=10)
        ctk.CTkLabel(employe_frame, text =  str(employe[3])+" ans", font=('Montsérrat', 20, 'bold'), bg_color="transparent").place(x=180  , y=60)
    
        if employe[3]>30:
            photox = ctk.CTkImage(Image.open("images/images_app/or.png"), size=(100,100))
            
        elif employe[3]>20:
            photox = ctk.CTkImage(Image.open("images/images_app/argent.png"), size=(100,100))
            
        elif employe[3]>15:
            photox = ctk.CTkImage(Image.open("images/images_app/bronze.png"), size=(100,100))
            
        else:
            photox = ctk.CTkImage(Image.open("images/images_app/defaut.png"), size=(100,100))
        
        ctk.CTkLabel(employe_frame, text="", image=photox).place(x=470,y=10)
    
    toplevel.mainloop()

