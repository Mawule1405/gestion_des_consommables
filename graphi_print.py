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

def get_employes(sql="SELECT * FROM Employe",host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    return curseur.fetchall()

def get_one_employe(id_emp = 0,host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """La fonction de recherche d'un employe a partir de son identifiant"""
    attr = "id_emp,nom_emp, prenom_emp, date_nais_emp, date_embau_emp, nationalite_emp, niveau_etu_emp, salaire_emp, lieu_res_emp, email_emp, contact_emp, photo_emp, e.id_serv,sexe, nom_serv"
    sql=f"SELECT {attr} FROM Employe e, Service s WHERE id_emp = {id_emp} AND e.id_serv = s.id_serv"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()
    return liste

def get_one_categories(id_cat = 0,host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """La fonction de recherche d'un employe a partir de son identifiant"""
    attr = "nom_cat"
    sql=f"SELECT {attr} FROM Categorie WHERE id_cat= {id_cat}"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()
    return liste

def get_services(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql=f"SELECT * FROM Service"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    
    return liste




def get_categories(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """Fonction de récupération des catégories"""
    sql=f"SELECT * FROM Categorie ORDER BY id_cat"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()
    return liste

def inserer_categorie(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """INSERT INTO Categorie
                 (id_cat,
                 nom_cat
             )
             
             VALUES (%s, %s)"""
    bdd = None
    curseur = None
    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        curseur = bdd.cursor()
        curseur.execute(sql, information)
        bdd.commit()
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False
    finally:
        if curseur:
            curseur.close()
        if bdd:
            bdd.close()



def modifier_categories(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """Fonction pour modifier le nom d'une catégories"""
    
    sql = """UPDATE Categories
             SET nom_cat = %s,
             WHERE id_cat = %s"""
    bdd = None
    curseur = None
    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        curseur = bdd.cursor()
        curseur.execute(sql, information)
        bdd.commit()
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False
    finally:
        if curseur:
            curseur.close()
        if bdd:
            bdd.close()




def modifier_employe(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """UPDATE Employe
             SET nom_emp = %s,
                 prenom_emp = %s,
                 date_nais_emp = %s,
                 date_embau_emp = %s,
                 nationalite_emp = %s,
                 niveau_etu_emp = %s,
                 salaire_emp = %s,
                 lieu_res_emp = %s,
                 email_emp = %s,
                 contact_emp = %s,
                 photo_emp = %s,
                 id_serv = %s,
                 sexe = %s
             WHERE id_emp = %s"""
    bdd = None
    curseur = None
    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        curseur = bdd.cursor()
        curseur.execute(sql, information)
        bdd.commit()
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False
    finally:
        if curseur:
            curseur.close()
        if bdd:
            bdd.close()


def inserer_employe(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """INSERT INTO Employe
                 (nom_emp,
                 prenom_emp,
                 date_nais_emp ,
                 date_embau_emp ,
                 nationalite_emp ,
                 niveau_etu_emp ,
                 salaire_emp ,
                 lieu_res_emp ,
                 email_emp ,
                 contact_emp ,
                 photo_emp,
                 id_serv ,
                 sexe
             )
             
             VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s)"""
    bdd = None
    curseur = None
    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        curseur = bdd.cursor()
        curseur.execute(sql, information)
        bdd.commit()
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False
    finally:
        if curseur:
            curseur.close()
        if bdd:
            bdd.close()

def delete_employe(id, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = f"""DELETE FROM Employe WHERE id_emp = {id}"""
    bdd = None
    curseur = None
    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        curseur = bdd.cursor()
        curseur.execute(sql)
        bdd.commit()
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False
    finally:
        if curseur:
            curseur.close()
        if bdd:
            bdd.close()
