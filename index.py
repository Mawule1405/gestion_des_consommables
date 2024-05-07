"""Ce ci me servira à implémenter l'interface de connexion de l'application"""
import customtkinter as ctk
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk
import graphi_print as gp
import setting as set

#Definition de la logique
def apercu_check():
    val = apercu.get()
    if val == 1 :
        mot_de_passe.configure(show='')
    else :
        mot_de_passe.configure(show='*')

def valider():
    val_id = identifiant.get()
    val_mp = mot_de_passe.get()
    is_id_vide, is_mp_vide = False, False

    if val_id == "":
        is_id_vide = True
        identifiant.configure(border_color="red")
    else:
        is_id_vide = False
        identifiant.configure(border_color="green")

    if val_mp == "":
        is_mp_vide = True
        mot_de_passe.configure(border_color="red")
    else:
        is_mp_vide = False
        mot_de_passe.configure(border_color="green")
    
    if not is_id_vide and not is_mp_vide:
        curseur = gp.connexion_database()

        if curseur == None:
            messagebox.showwarning('Connexion échoué', "La tentative de connexion à la base de données a échoué.\n Veuillez vérifier le serveur de la base de données ou réessayer plutard!")
        else :
            print(val_id , val_mp)

    
        
    


#Definition de la fenêtre
fen = ctk.CTk()
fen.title('GraphiPrint : Connexion')
largeur = 500
hauteur = 400
fen.geometry("500x350")
fen.resizable(width = False, height = False)

#Definition de la zone de connexion
zone_de_con = ctk.CTkFrame(fen, width = 300, height =400, border_color="#fff",)


label_image = ctk.CTkLabel(fen, text= "",width=200,height=500,fg_color=set.col_noir_1
                            )
label_image.place(x=0, y=0)

#Définition de l'entete
titre_connexion = ctk.CTkLabel(zone_de_con, text="Page de connexion", font=('Montserrat', 25,"bold"))
titre_connexion.place(x=25,y=10)

#Définition de l'identifiant
identifiant= ctk.CTkEntry(zone_de_con, placeholder_text="Entrer l'identifiant", width=250, height=40,
                          font=('Montserrat', 18),border_width= 2, border_color= "#fff")
identifiant.place(x= 25 , y= 70)

#Définition du mot de passe
mot_de_passe = ctk.CTkEntry(zone_de_con, placeholder_text="Entrer le mot de passe", width=250,height=40, show="*",
                            font=('Montserrat', 18),border_width= 2, border_color= "#fff")
mot_de_passe.place(x= 25 , y= 150)

#Definition du checkbox pour apercevoir le mot de passe
apercu = ctk.CTkCheckBox(zone_de_con, text="Aperçu du mot de passe", hover_color= set.col_hover,checkmark_color=set.col_white,
                         fg_color=set.col_noir_1,font=('Montserrat', 18), command= apercu_check)
apercu.place(x= 25 , y=220)

#Définition du bouton de validation
validation = ctk.CTkButton(zone_de_con, text="Connecter", width=250, height=35, font=('Montserrat', 20, "bold"),
                           hover_color=set.col_hover, fg_color=set.col_noir_1,command= lambda : valider())
validation.place(x= 25, y=280)

zone_de_con.place(x = 200,y = 0)




fen.mainloop()


