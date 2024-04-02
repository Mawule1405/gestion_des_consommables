import mysql.connector

# Connexion à la base de données
def connexion_database(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Établit une connexion à une base de données MySQL.

    Parameters:
    - host_x : str : L'adresse IP ou le nom d'hôte de la base de données.
    - user_x : str : Le nom d'utilisateur pour se connecter à la base de données.
    - password_x : str : Le mot de passe associé à l'utilisateur.
    - database_name : str : Le nom de la base de données à laquelle se connecter.

    Returns:
    - cursor : Cursor : Le curseur pour exécuter les requêtes SQL.
    """

    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        return bdd.cursor()
    except mysql.connector.Error:
        return None
    except mysql.connector.errors.ProgrammingError:
        return None

def get_employe(sql="SELECT * FROM Employe",host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    return curseur.fetchall()

def get_one_employe(id_emp = 0,host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql=f"SELECT * FROM Employe WHERE id_emp = {id_emp}"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    return curseur.fetchall()


