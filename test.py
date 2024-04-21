import customtkinter as ctk
from datetime import datetime
import math as mt

def draw_watch(canvas):
    # Dessiner le contour du cadran
    canvas.create_oval(50, 50, 250, 250, outline="black", width=2)
    
    # Dessiner les marqueurs des heures
    for i in range(1, 13):
        angle = i * 30 - 90  # 30 degrés pour chaque marqueur d'heure
        x = 150 + 90 * mt.cos(mt.radians(angle))
        y = 150 + 90 * mt.sin(mt.radians(angle))
        canvas.create_text(x, y, text=str(i), font=("Helvetica", 12))
    
    # Dessiner les aiguilles des heures, des minutes et des secondes
    hour_hand = canvas.create_line(150, 150, 150, 100, width=4, fill="black")
    minute_hand = canvas.create_line(150, 150, 150, 50, width=2, fill="black")
    second_hand = canvas.create_line(150, 150, 150, 25, width=1, fill="red")

    # Ajouter un texte pour afficher la date et l'heure
    date_time_text = canvas.create_text(150, 270, text="", font=("Helvetica", 12))
    
    # Mettre à jour l'heure
    update_time(canvas, hour_hand, minute_hand, second_hand, date_time_text)

def update_time(canvas, hour_hand, minute_hand, second_hand, date_time_text):
    # Obtenir la date et l'heure actuelles
    current_time = datetime.now()
    day_of_week = current_time.strftime("%A")  # Jour de la semaine (ex: lundi)
    day = current_time.day  # Jour du mois
    month = current_time.strftime("%B")  # Mois (ex: janvier)
    year = current_time.year  # Année
    hour = current_time.hour % 12
    minute = current_time.minute
    second = current_time.second
    
    # Formater la date et l'heure pour affichage
    formatted_date_time = f"{day_of_week} {day} {month} {year}     {hour:02d}:{minute:02d}:{second:02d}"
    
    # Mettre à jour le texte affichant la date et l'heure
    canvas.itemconfigure(date_time_text, text=formatted_date_time)
    
    # Calculer les angles des aiguilles
    hour_angle = (hour + minute / 60) * 30 - 90
    minute_angle = (minute + second / 60) * 6 - 90
    second_angle = second * 6 - 90
    
    # Mettre à jour les positions des aiguilles
    canvas.coords(hour_hand, 150, 150, 150 + 60 * mt.cos(mt.radians(hour_angle)), 150 + 60 * mt.sin(mt.radians(hour_angle)))
    canvas.coords(minute_hand, 150, 150, 150 + 80 * mt.cos(mt.radians(minute_angle)), 150 + 80 * mt.sin(mt.radians(minute_angle)))
    canvas.coords(second_hand, 150, 150, 150 + 80 * mt.cos(mt.radians(second_angle)), 150 + 80 * mt.sin(mt.radians(second_angle)))
    
    # Mettre à jour l'heure toutes les 1000 ms (1 seconde)
    canvas.after(1000, update_time, canvas, hour_hand, minute_hand, second_hand, date_time_text)

def build_watch(frame):
    # Créer un canevas pour dessiner la montre
    canvas = ctk.CTkCanvas(frame, width=300, height=300, bg="white")
    canvas.pack()

    # Dessiner la montre
    draw_watch(canvas)

t = ctk.CTk()
build_watch(t)
t.mainloop()