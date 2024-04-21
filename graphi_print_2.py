import mysql.connector
#=========================================================================
#===============UTILISATIONS DES CONCOMMABLES PAR LES EMPLOYES============
#=========================================================================

def liste_conso_commande_employe(id_emp,host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Cette fonction permet de récupérer la dépense totale de l'entreprise pour une année spécifiée.

    Args:
        annee (int): L'année pour laquelle récupérer les données.
        host_x (str): L'adresse IP ou le nom d'hôte du serveur MySQL. Par défaut, 'localhost'.
        user_x (str): Le nom d'utilisateur du compte MySQL. Par défaut, 'root'.
        password_x (str): Le mot de passe du compte MySQL. Par défaut, ''.
        database_name (str): Le nom de la base de données MySQL. Par défaut, 'graphi_print'.

    Returns:
        list: Une liste de tuples contenant les consommables commandés par un employe
              Chaque tuple contient deux éléments : nom consommable, date commande, prix unitaire ,quantite commande.
    """

    sql = f"""SELECT c.nom_cons,co.date_com, c.prix_unitaire_cons, c.qtestock_cons
                FROM commande co
                INNER JOIN appartenir a ON co.id_com = a.id_com
                INNER JOIN consommable c ON a.id_cons = c.id_cons
                WHERE co.id_emp ={id_emp}

           """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste