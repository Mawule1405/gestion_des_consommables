import customtkinter as ctk
import math as mt
from datetime import datetime
from PIL import Image

import setting as set

def scroll_text(canvas, text_id, dx):
    # Déplacer le texte horizontalement
    canvas.move(text_id, dx, 0)
    # Récupérer les coordonnées actuelles du texte
    x1, y1, x2, y2 = canvas.bbox(text_id)
    canvas_width = canvas.winfo_width()
    # Si le texte sort complètement de la zone visible, le réinitialiser à la position de départ
    if x1 >= canvas_width:
        canvas.move(text_id, -canvas_width - x1, 0)
    # Appeler la fonction récursivement après un court délai
    canvas.after(15, lambda: scroll_text(canvas, text_id, dx))  # Utilisation de lambda pour encapsuler les arguments

def build_scroll_text(frame,titre):
    # Créer un canevas CustomTkinter
    canvas = ctk.CTkCanvas(frame, width=1300, height=200, bg=set.col_blanc_4, highlightbackground=set.col_blanc_4, highlightthickness=2)
    canvas.pack()

    # Ajouter du texte au canevas
    text_id = canvas.create_text(0, 100, anchor="w", text=titre, font=("Montsérrat", 50, "bold"))

    # Appeler la fonction pour démarrer l'animation de défilement du texte
    scroll_text(canvas, text_id, dx=2)



def draw_watch(canvas):
    # Dessiner le contour du cadran
    canvas.create_oval(50, 50, 250, 250, outline=set.col_noir_1, width=5)
    
    # Dessiner les marqueurs des heures
    for i in range(1, 13):
        angle = mt.radians(i * 30 - 90)  # Convertir en radians
        x = 150 + 90 * mt.cos(angle)
        y = 150 + 90 * mt.sin(angle)
        canvas.create_text(x, y, text=str(i), font=("Helvetica", 12))

    
    # Dessiner les aiguilles des heures, des minutes et des secondes
    hour_hand = canvas.create_line(150, 150, 150, 100, width=4, fill="black")
    minute_hand = canvas.create_line(150, 150, 150, 50, width=2, fill="black")
    second_hand = canvas.create_line(150, 150, 150, 25, width=1, fill="red")
    
    # Mettre à jour l'heure
    update_time(canvas, hour_hand, minute_hand, second_hand)

def update_time(canvas, hour_hand, minute_hand, second_hand):
    # Obtenir l'heure actuelle
    current_time = datetime.now().time()
    hour = current_time.hour % 12
    minute = current_time.minute
    second = current_time.second
    
    # Calculer les angles des aiguilles en radians
    hour_angle = mt.radians((hour + minute / 60) * 30 - 90)
    minute_angle = mt.radians((minute + second / 60) * 6 - 90)
    second_angle = mt.radians(second * 6 - 90)
    
    # Mettre à jour les positions des aiguilles
    canvas.coords(hour_hand, 150, 150, 150 + 60 * mt.cos(hour_angle), 150 + 60 * mt.sin(hour_angle))
    canvas.coords(minute_hand, 150, 150, 150 + 80 * mt.cos(minute_angle), 150 + 80 * mt.sin(minute_angle))
    canvas.coords(second_hand, 150, 150, 150 + 80 * mt.cos(second_angle), 150 + 80 * mt.sin(second_angle))
    
    # Mettre à jour l'heure toutes les 1000 ms (1 seconde)
    canvas.after(1000, update_time, canvas, hour_hand, minute_hand, second_hand)



def build_accueil(frame):
    # Créer un canevas pour dessiner la montre
    titre = ctk.CTkFrame(frame, width = 800, height=10)
    titre.place(x=100,y=0)
    image_path = "images/images_app/papeterie.png"
    image = Image.open(image_path)
    image_final = ctk.CTkImage(image, size=(1000, 600))
    photo = ctk.CTkLabel(frame, image=image_final)
    photo.place(x=50, y=100)

   
    """canvas = ctk.CTkCanvas(frame, width=300, height=300,
                             )
    canvas.place(x=600, y= 10)"""
    build_scroll_text(titre,"GRAPHIPRINT")
    #draw_watch(canvas)
    

    
    


    



