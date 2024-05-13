from fpdf import FPDF
from datetime import datetime

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
  
        self.set_font('Arial', 'BU', 16)
        self.cell(0, 10, titre_table, 0, 1, 'C')
        self.ln(5)

        self.set_text_color(0,0,0)
        # Définir les en-têtes de colonnes
        self.cell(10)
        self.set_font('Arial', 'B', 10)
        self.cell(20, 10, 'Numéro', 1, 0, 'C')
        self.cell(110, 10, 'Nom du Consommable', 1, 0, 'C')
        self.cell(20, 10, 'Quantité', 1, 0, 'C')
        self.cell(20, 10, 'Date', 1, 1, 'C')

        # Remplir le tableau avec les données
        self.set_font('Arial', '', 10)
        for consumable in consumables_data:
            self.cell(10)
            self.cell(20, 10, consumable['numero'], 1, 0, 'C')
            self.cell(110, 10, consumable['nom'], 1, 0, 'C')
            self.cell(20, 10, consumable['quantite'], 1, 0, 'C')
            self.cell(20, 10, consumable['date'], 1, 1, 'C')

        



        



# Exemple d'utilisation
pdf = PDF()
pdf.add_page()

# Informations sur l'employé
employee_data = {
        "photo":'images/photo_employe/mathias.jpg',
    'Nom': 'Doe',
    'Prénom': 'John',
    'Sexe': 'Homme',
    'Date de naissance': '01/01/1990',
    'Date d\'embauche': '01/01/2020',
    'Nationalité': 'Française',
    'Lieu de résidence': 'Paris',
    'Salaire': '5000',
    'Service': 'Informatique',
    "Email":"doejohn@gmail.com"
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
# Enregistrer le PDF
pdf.output('employee_report.pdf')
