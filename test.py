from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('images/images_app/bg_page_connexion.png', 10, 8, 33)
        # Police Arial gras 15
        self.set_font('Arial', 'B', 15)
        # Décalage à droite
        self.cell(80)
        # Titre
        self.cell(30, 10, 'GRAPHIPRINT', 0, 0, 'C')
        # Retour à la ligne
        self.ln(10)
        # Police de caractère régulière 12
        self.set_font('Arial', '', 12)
        # Adresse
        self.cell(0, 10, 'TOGO-Lomé', 0, 1, 'C')
        self.cell(0, 10, 'Tel: +22893497606  BP: 4545-05', 0, 1, 'C')
        # Ligne de séparation
        self.line(10, 35, 200, 35)
        self.ln(10)

    def employee_info(self, employee_data):
        # Rectangle pour les informations de l'employé
        self.set_fill_color(255, 255, 255)
        self.rect(10, 45, 100, 80, 'FD')

        # Ajouter la photo de l'employé
        self.image('images/photo_employe/mathias.jpg', 12, 47, 30)

        # Définir la police et la taille du texte
        self.set_font('Arial', '', 10)

        # Informations de l'employé
        y_position = 47
        for key, value in employee_data.items():
            if key in ['Nom', 'Prénom']:
                self.set_xy(45, y_position)
                self.cell(0, 10, f'{key}: {value}', ln=True)
                y_position += 5
            else:
                self.set_xy(45, y_position)
                self.cell(0, 10, f'{key}: {value}', ln=True)
                y_position += 10

# Exemple d'utilisation
pdf = PDF()
pdf.add_page()

# Informations sur l'employé
employee_data = {
    'Nom': 'Doe',
    'Prénom': 'John',
    'Sexe': 'Homme',
    'Date de naissance': '01/01/1990',
    'Date d\'embauche': '01/01/2020',
    'Nationalité': 'Française',
    'Lieu de résidence': 'Paris',
    'Salaire': '$5000',
    'Service': 'Informatique'
}
pdf.employee_info(employee_data)

# Enregistrer le PDF
pdf.output('employee_report.pdf')
