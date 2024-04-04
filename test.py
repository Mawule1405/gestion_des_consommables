import tkinter as tk
from tkinter import ttk

# Données de la liste
donnees = [
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    ("2", "Encres prêtes à l'emploi (RFU)", "15", "3", "2"),
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    ("1", "Encres acryliques à haut extrait sec (HSA)", "10", "2", "1"),
    # Ajoutez d'autres tuples de données ici
]

# Créer la fenêtre principale
root = tk.Tk()
root.title("Affichage des données")
style = ttk.Style()

style.configure("Treeview.Heading", font=('Helvetica', 20, 'bold'), rowheight=25)

# Créer le Treeview
tree = ttk.Treeview(root, columns=('ID', 'Description', 'Prix', 'Quantité', 'Commandes'), show='headings')
style.configure("Treeview", font=('Helvetica', 12, 'bold'), rowheight=25)
# Définir les en-têtes
tree.heading('ID', text='ID')
tree.heading('Description', text='Description')
tree.heading('Prix', text='Prix')
tree.heading('Quantité', text='Quantité')
tree.heading('Commandes', text='Commandes')

# Ajouter les données dans le Treeview
for donnee in donnees:
    tree.insert('', tk.END, values=donnee)

# Pack le Treeview dans la fenêtre principale
tree.pack(expand=True, fill='both')

# Exécuter la boucle principale
root.mainloop()
