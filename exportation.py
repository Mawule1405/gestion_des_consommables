from datetime import datetime
import customtkinter as ctk
from fpdf import FPDF
from tkinter import messagebox



class PDF(FPDF):
    def header(self):
        # Logo
        self.image('images/images_app/bg_page_connexion.png', 20, 8, 20)
        # Police Arial gras 15
        self.set_font('Arial', 'B', 25)
        # Décalage à droite
        self.cell(80)
        self.set_text_color(0,0,255)
        self.cell(30, 10, 'GRAPHIPRINT', 0, 0, 'C')
        # Retour à la ligne
        self.ln(5)
        self.set_font('Arial', 'B', 10)
        self.set_text_color(255,0,0)
        self.cell(0,10,"Votre partenaire d'impression",0,0,"C")
        self.ln(5)
        # Police de caractère régulière 12
        self.set_font('Arial', 'B', 8)
        self.set_text_color(0,0,0)
        self.cell(0, 10, 'Adresse: TOGO-Lomé   Tel: +22893497606   BP: 4545-05', 0, 0, 'C')
        self.ln(5)
        self.cell(0, 10, 'Email: graphiprint@gmail.com', 0, 0, 'C')

        # Ligne de séparation
        self.set_line_width(2)
        self.line(10, 35, 200, 35)
        self.ln(10)

    def employee_info(self, employee_data):
        # Rectangle pour les informations de l'employé
        self.set_fill_color(255, 255, 255)
        #self.rect(10, 40, 190, 50, 'FD')

        # Ajouter la photo de l'employé
        self.image(employee_data["photo"], 11, 41, 30)
        self.cell(40)
        self.set_font('Arial', 'B', 8)
        self.cell(50,20,"Nom: "+employee_data['Nom'],0,0,"L")
        self.cell(50,20,"Prénom(s): "+employee_data['Prénom'],0,0,"L")

        self.ln(7)
        self.cell(40)
        self.cell(50,20,"Sexe: "+employee_data['Sexe'],0,0,"L")
        self.cell(0,20,"Nationalité: "+employee_data['Nationalité'],0,0,"L")

        self.ln(7)
        self.cell(40)
        self.cell(50,20,"Date de naissance: "+employee_data['Date de naissance'],0,0,"L")
        self.cell(0,20,"Date d'embauche: "+employee_data['Date d\'embauche'],0,0,"L")


        self.ln(7)
        self.cell(40)
        self.cell(50,20,"Lieu de résidence: "+employee_data['Lieu de résidence'],0,0,"L")
        self.cell(0,20,"Service: "+employee_data['Service'],0,0,"L")

        self.ln(7)
        self.cell(40)
        self.cell(50,20,"Salaire: "+employee_data['Salaire']+"FCFA",0,0,"L")
        self.cell(0,20,"Email: "+employee_data['Email'],0,0,"L")
        # Définir la police et la taille du texte
        self.ln(15)
        self.set_text_color(255,0,0)
        self.set_font('Arial', 'B', 16)
        self.cell(0,20,f"Rapport d'activité du {datetime.strftime(datetime.now(), "%d-%m-%Y // %H:%M:%S")}".upper(),0,0,"C")

    
    def add_consumables_table(self,titre_table, consumables_data):
    # Titre du tableau
        self.ln(20)
        self.set_text_color(0,0,255)
        self.set_font('Arial', 'BU', 16)
        self.cell(0, 10, titre_table, 0, 1, 'C')
        self.ln(5)

        self.set_text_color(0,0,0)
        # Définir les en-têtes de colonnes
        self.set_font('Arial', 'B', 10)
        self.cell(30, 10, 'Numéro', 1, 0, 'C')
        self.cell(60, 10, 'Nom du Consommable', 1, 0, 'C')
        self.cell(40, 10, 'Quantité', 1, 0, 'C')
        self.cell(60, 10, 'Date', 1, 1, 'C')

        # Remplir le tableau avec les données
        self.set_font('Arial', '', 10)
        for consumable in consumables_data:
            self.cell(30, 10, consumable['numero'], 1, 0, 'C')
            self.cell(60, 10, consumable['nom'], 1, 0, 'C')
            self.cell(40, 10, consumable['quantite'], 1, 0, 'C')
            self.cell(60, 10, consumable['date'], 1, 1, 'C')


    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')



def export_employe_information(employe):
    """Fonction d'exportation des informations sur l'employé au format PDF"""
  
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    
    employee_data = {
        "photo": employe[11],
        'Nom': employe[1],
        'Prénom': employe[2],
        'Sexe':  employe[13],
        'Date de naissance': datetime.strftime(employe[3], "%d-%m-%Y"),
        'Date d\'embauche': datetime.strftime(employe[4], "%d-%m-%Y"),
        'Nationalité': employe[5],
        'Lieu de résidence':  employe[8],
        'Salaire': str(int( employe[7])),
        'Service': str( employe[12]),
        "Email": employe[9],
        "téléphone":  employe[10],
        "Niveau":  employe[6]
    }
    consumables_data = [
        {"numero": "1", "nom": "Papier A4", "quantite": "100", "date": "2024-05-01"},
        {"numero": "2", "nom": "Encre Noire", "quantite": "5", "date": "2024-05-02"},
        {"numero": "3", "nom": "Stylo Bleu", "quantite": "10", "date": "2024-05-03"},
        {"numero": "4", "nom": "Cartouche d'encre", "quantite": "2", "date": "2024-05-04"},
        {"numero": "5", "nom": "Cahier", "quantite": "20", "date": "2024-05-05"}
    ]

    titre1 = "Liste des consommables utilisés"
    titre2 = "Liste des consommables commandés"
    pdf.employee_info(employee_data)
    pdf.add_consumables_table(titre1,consumables_data)
    pdf.add_consumables_table(titre2,consumables_data)
        
    
    types_de_fichiers=[("Fichiers Pdf","*.pdf")]

    try:
        lien_export = ctk.filedialog.asksaveasfilename(title="Exportation des informations d'un l'employé",
                                                    filetypes= types_de_fichiers)
        
        pdf.output(lien_export, 'F')
    except:

        messagebox.showinfo("Exportation des information de l'employé", "Vous avez annuler l'exportation.")
