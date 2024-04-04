from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import red, blue, black

from datetime import datetime
import customtkinter as ctk
def export_employe_information(liste):
    """Procédure d'exportation des informations sur l'employé"""
    types_de_fichiers=[("Fichiers Pdf","*.pdf")]
    lien_export = ctk.filedialog.asksaveasfilename(title="Exportation des informations d'un l'employé",
                                                   filetypes= types_de_fichiers)
    
    # Créer un fichier PDF
    c = canvas.Canvas(lien_export, pagesize=A4)
    c.setTitle("Informations de l' employé")
    
    #Définition des marges et de la bordures
    marge_gauche_1 = 20
    marge_haut_1 = 800
    marge_droite_1 = 550
    marge_bas_1 = 20

    
    #Dessiner la deuxième bordure
    epaisseur_bordure_2 = 10
    c.setLineWidth(epaisseur_bordure_2)
    c.rect(marge_gauche_1, marge_bas_1, marge_droite_1 , marge_haut_1 )
    
    
    # Ajouter le logo
    logo = "images/photo_employe/reine.jpg"  # Remplacez par le chemin vers votre fichier logo
    c.drawImage(logo, 1*cm, 26.5*cm, 2*cm, 2*cm)  

    c.setFont("Helvetica-Bold", 30)
    # Ajouter les informations au centre
    # IMPRIMERIE en noir
    c.setFillColor(black)
    c.drawCentredString(7*cm, 27.5*cm, "IMPRIMERIE")

    # GRAPHI en rouge
    c.setFillColor(red)
    c.drawCentredString(12.5*cm, 27.5*cm, "GRAPHI")

    # PRINT en bleu
    c.setFillColor(blue)
    c.drawCentredString(16.25*cm, 27.5*cm, "PRINT")
    c.setFillColor(black)
    c.setFont("Helvetica", 20)
    c.drawCentredString(10.5*cm, 26.75*cm, "Email: graphiprint@gmail.com")
    c.drawCentredString(10.5*cm, 25.75*cm, "Tel: +241 74 63 04 73 // +241 62 40 45 30")
    c.drawCentredString(6*cm, 25*cm, "Lomé-Togo")

    # Ajouter la date du jour à droite
    c.setFont("Helvetica", 20)
    date_du_jour = datetime.now().strftime("%d/%m/%Y   %H:%M:%S")
    c.drawRightString(15.5*cm, 25*cm, date_du_jour)

    #Tracer une droite horizontale en bas de l'entete
    epaisseur_bordure_2 = 5
    c.setLineWidth(epaisseur_bordure_2)
    x_debut = 100  # Position de départ sur l'axe X
    y_position = 690  # Position sur l'axe Y où la ligne sera tracée
    x_fin = 500  # Position de fin sur l'axe X
    c.line(x_debut, y_position, x_fin, y_position)
    c.save()