import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import tkinter as tk, tkinter.messagebox as msgbox
import customtkinter as ctk


import graphi_print as gp
import setting as set


def graphique_com_montant(data, titre,xlabel, ylabel):
    """
    Crée un graphique à barres à partir d'une liste de tuples.
    
    Args:
        data (list of tuple): Liste de tuples où chaque tuple contient deux éléments,
                              le premier élément représentant l'ID du consommable et le deuxième
                              élément représentant le montant total de la commande.
    """
    # Séparation des données en deux listes : ID des consommables et montant total
    ids, montants = zip(*data)
    
    plt.close()
    # Création du graphique à barres
    plt.bar(ids, montants, color=set.col_noir_5)

    # Ajout de titres et de labels
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Affichage du graphique
    plt.xticks(rotation=0)  # Rotation des ID des consommables pour éviter les chevauchements
    plt.tight_layout()       # Ajustement automatique de la mise en page pour éviter les coupures
    plt.gcf().canvas.manager.window.attributes('-topmost', True)  # Mettre la fenêtre du graphique au premier plan
    plt.show()

def graphique_nombre_com_montant(data, titre, xlabel, ylabel):

    """
    Crée un nuage de points avec une droite de régression linéaire à partir d'une liste de tuples.

    Args:
        data (list of tuple): Liste de tuples où chaque tuple contient deux éléments,
                              le premier élément représentant l'ID du consommable et le deuxième
                              élément représentant le montant total de la commande.
        titre (str): Titre du graphique.
        xlabel (str): Libellé de l'axe des abscisses.
        ylabel (str): Libellé de l'axe des ordonnées.
    """

    # Séparation des données en deux listes : ID des consommables et montant total
    ids, montants = zip(*data)
    plt.close()
    # Création du nuage de points
    plt.scatter(ids, montants, color='skyblue', label='Données')

    # Calcul de la droite de régression linéaire
    coeffs = np.polyfit(ids, montants, 1)
    droite_reg = np.poly1d(coeffs)

    # Tracé de la droite de régression linéaire
    plt.plot(ids, droite_reg(ids), color='red', label='Régression linéaire')

    # Ajout de titres et de labels
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    # Affichage du graphique
    plt.xticks(rotation=45)  # Rotation des ID des consommables pour éviter les chevauchements
    plt.tight_layout()       # Ajustement automatique de la mise en page pour éviter les coupures
    plt.gcf().canvas.manager.window.attributes('-topmost', True)  # Mettre la fenêtre du graphique au premier plan
    plt.show()

def graphique_mois_depense(titre, xlabel, ylabel):
    """
    Crée un diagramme en bâtons avec une droite de régression linéaire à partir des données de montant des commandes par mois.

    Args:
        titre (str): Titre du graphique.
        xlabel (str): Libellé de l'axe des abscisses.
        ylabel (str): Libellé de l'axe des ordonnées.
    """
    plt.close()
    # Demander à l'utilisateur de saisir une année
    annee_input_dialog = ctk.CTkInputDialog(title="Etude des dépenses d'une année", text="Veillez préciser une année !")
    annee = annee_input_dialog.get_input()
    annee_input_dialog.destroy()
    try:
        
        # Convertir l'entrée de l'utilisateur en entier
        annee = int(annee)
        annee_actuelle = datetime.now().date().year

        annee_minimale = 2010
        annee_maximale = annee_actuelle + 1

        assert annee_minimale < annee < annee_maximale

        # Récupérer les données de montant des commandes par mois pour l'année spécifiée
        data = gp.liste_montant_com_mois(annee)
        
        if data != []:
            # Séparation des données en deux listes : mois et montants
            mois, montants = zip(*data)
            montants = [float(m) for m in montants]
            mois_s = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aoüt", "Septembre",
                      "Octobre", "Novembre", "Décembre"]
            mois = [mois_s[ms-1] for ms in mois]
            # Fermer la fenêtre de graphique précédente s'il en existe une
           

            # Création du diagramme en bâtons
            plt.bar(mois, montants, color='skyblue', label='Données')

            
            # Ajout de titres et de label
            plt.title(titre)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.legend()

            # Affichage du graphique
            plt.xticks(rotation=45)  # Rotation des mois pour éviter les chevauchements
            plt.tight_layout()       # Ajustement automatique de la mise en page pour éviter les coupures
            plt.gcf().canvas.manager.window.attributes('-topmost', True)  # Mettre la fenêtre du graphique au premier plan
            plt.show()

    except ValueError:
        msgbox.showerror("Information", "Veuillez entrer une année valide.")
    except AssertionError:
        msgbox.showerror("Information", "Veuillez entrer une année entre {} et {}.".format(2010, datetime.now().date().year))
    except:
        msgbox.showerror("Information", "Année incorrecte.")


def graphique_anne_depense(titre, xlabel, ylabel):

    """
    Crée un nuage de points avec une droite de régression linéaire à partir d'une liste de tuples.

    Args:
        data (list of tuple): Liste de tuples où chaque tuple contient deux éléments,
                              le premier élément représentant l'ID du consommable et le deuxième
                              élément représentant le montant total de la commande.
        titre (str): Titre du graphique.
        xlabel (str): Libellé de l'axe des abscisses.
        ylabel (str): Libellé de l'axe des ordonnées.
    """
    data = gp.liste_montant_com_annee()
    # Séparation des données en deux listes : ID des consommables et montant total
    annee, montants = zip(*data)
    annee = [float(an) for an in annee]
    montants = [float(m) for m in montants]
    plt.close()
    # Création du nuage de points
    plt.scatter(annee, montants, color='skyblue', label='Données')

    # Calcul de la droite de régression linéaire
    coeffs = np.polyfit(annee, montants, 1)
    droite_reg = np.poly1d(coeffs)

    # Tracé de la droite de régression linéaire
    plt.plot(annee, droite_reg(annee), color='red', label='Régression linéaire')

    # Ajout de titres et de labels
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    # Affichage du graphique
    plt.xticks(rotation=45)  # Rotation des ID des consommables pour éviter les chevauchements
    plt.tight_layout()       # Ajustement automatique de la mise en page pour éviter les coupures
    plt.gcf().canvas.manager.window.attributes('-topmost', True)  # Mettre la fenêtre du graphique au premier plan
    plt.show()

   