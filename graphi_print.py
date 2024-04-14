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
    sql="SELECT s.id_serv, nom_serv, description_serv, date_serv, nom_emp, prenom_emp FROM Service s, Employe e WHERE s.id_emp_resp = e.id_emp"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    
    return liste

def get_one_service(id,host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql=f"SELECT s.id_serv, nom_serv, description_serv, date_serv, nom_emp, prenom_emp FROM Service s, Employe e WHERE s.id_emp_resp = e.id_emp AND s.id_serv = {id}"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    
    return liste

def inserer_service(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """INSERT INTO Service
                 (id_serv,
                 nom_serv,
                 description_serv,
                 date_serv,
                 id_emp_resp
             )
             
             VALUES (%s, %s,%s,%s,%s)"""
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



def update_service(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """UPDATE Service
             SET 
                 nom_serv =  %s,
                 description_serv = %s,
                 date_serv = %s,
                 id_emp_resp = %s
            WHERE id_serv = %s
             """
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



def supprimer_service(id, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """Fonction pour supprimer un service"""
    
    
    sql = f"""DELETE FROM Service
             WHERE id_serv = {id} """
    
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
#=====================CATEGORIES======================================================
#=====================================================================================

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
    
    sql = """UPDATE Categorie
             SET nom_cat = %s
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


def supprimer_categories(id, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """Fonction pour supprimer un nom de catégories"""
    
    sql1 = f"""
             SELECT id_cat FROM Consommable"""
    
    sql2 = f"""DELETE FROM Categorie
             WHERE id_cat = {id} """
    
    bdd = None
    curseur = None
    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        curseur = bdd.cursor()
        curseur.execute(sql1)

        reponse = curseur.fetchall()

        if id in [ i[0] for i in reponse]:
            return False
        else:
            curseur.execute(sql2)
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

"""
-----TOUS POUR LES CONSOMMABLES
"""
def get_consommables(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """Fonction de récupération des catégories"""
    sql="SELECT id_cons, nom_cons, qtestock_cons, qteseuil_cons, prix_unitaire_cons, nom_cat FROM Consommable co, Categorie ca WHERE co.id_cat = ca.id_cat  ORDER BY id_cons"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()
    return liste

def get_consommables_by_cat(id_cat,host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """Fonction de récupération des catégories"""
    sql=f"SELECT id_cons, nom_cons, qtestock_cons, qteseuil_cons, prix_unitaire_cons FROM Consommable co WHERE co.id_cat = {id_cat}  ORDER BY id_cons"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()
    return liste

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
    sql = f"""DELETE FROM Employe WHERE id_emp = {id} """
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
