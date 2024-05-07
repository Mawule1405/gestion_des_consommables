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

#=========================================================================================================
#==================================GESTIONS DES CONSOMMABLES==============================================

def get_consommables(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """Fonction de récupération des consommables"""
    sql="SELECT id_cons, nom_cons, qtestock_cons, qteseuil_cons, prix_unitaire_cons, nom_cat, image FROM Consommable co, Categorie ca WHERE co.id_cat = ca.id_cat  ORDER BY id_cons"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()
    return liste

def get_consommables_by_cat(id_cat,host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """Fonction de récupération des catégories"""
    sql=f"SELECT id_cons, nom_cons, qtestock_cons, qteseuil_cons, prix_unitaire_cons, image  FROM Consommable co WHERE co.id_cat = {id_cat}  ORDER BY id_cons"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()
    return liste


def get_consommables_by_id_cons(id_cons,host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Une fonction de récupération d'un consommable à partir de son id
    """
   
    sql=f"""SELECT id_cons, nom_cons, qtestock_cons, qteseuil_cons, prix_unitaire_cons, ca.id_cat, ca.nom_cat, image
            FROM Consommable co, Categorie ca 
            WHERE co.id_cons = {id_cons} AND co.id_cat = ca.id_cat
            """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()
    return liste



def update_consommable(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """UPDATE Consommable
            SET  nom_cons = %s,
                 prix_unitaire_cons = %s
            WHERE id_cons = %s
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


def inserer_consommable(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """INSERT INTO Consommable
                 (id_cons,
                 nom_cons,
                 qtestock_cons,
                 qteseuil_cons,
                 id_cat, 
                 prix_unitaire_cons
             )
             
             VALUES (%s, %s, %s, %s, %s, %s)"""
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


#==================================================================================================================
#==========================================GESTION DES EMPLOYES====================================================

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

#==================================================================================
#================= GESTION DE LA TABLES DEMANDER ==================================

def inserer_demande(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """INSERT INTO Demander
                 (id_emp,
                 id_cons,
                 qte_demande,
                 date_demande
             )
             
             VALUES (%s, %s, %s, %s)"""
    bdd = None
    curseur = None
    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        curseur = bdd.cursor()
        curseur.executemany(sql, information)
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

def inserer_one_demande(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
        fonction d'insertion de gestion de l'attribution d'un consopmmable attribuer à un employé
        @param information tuple(id_emp, id_cons, qte_demande, date_demande)
        @return: Boolean
    """
    sql = """INSERT INTO Demander
                 (id_emp,
                 id_cons,
                 qte_demande,
                 date_demande
             )
             
             VALUES (%s, %s, %s, %s)"""
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



#=========================================================================================================
#=========================GESTION DES PPROVISIONNEMENT: TABLE APPARTENIR==================================

    

def inserer_appartenir(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    sql = """INSERT INTO Appartenir
                 (id_com,
                 id_cons,
                 qte_com
             )
             
             VALUES (%s, %s, %s)"""
    bdd = None
    curseur = None
    try:
        bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
        curseur = bdd.cursor()
        curseur.executemany(sql, information)
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

#=========================================================================================================
#=========================GESTION DES COMMANDES: TABLES COMMANDES=========================================
def get_last_commande_id( host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
        Cette fonction permet récuper id de la dernière commande enrégistrer
    """
    sql=f"SELECT  id_com FROM Commande ORDER BY id_com  DESC LIMIT 1"
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()

    if liste:
        return liste[0][0]
    else:
        return 0



def inserer_commande(information, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
        Une fonction pour insérer une nouvelle entité commande dans la table
        Commande
    """
    sql = """INSERT INTO Commande
                 (id_com,
                 date_com,
                 id_emp
             )
             VALUES (%s, %s, %s)"""
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


def get_commande_of_emp(id_emp_x, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
        Cette fonction permet récuper la liste des commandes d'un employés
    """
    sql=f"""SELECT  id_com, date_com,nombre_com, montant_com
            FROM Commande
            WHERE id_emp = {id_emp_x}
            
            """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def get_commandes( host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
        Cette fonction permet récuper la liste des commandes 
    """
    sql=f"""SELECT  id_com, date_com,nombre_com, montant_com
            FROM Commande
            """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste
#==============================================================================================================
#==============================================================================================================
#======================================LES REQUETES POUR LES FONCTIONNALITES===================================

def get_emp_commande_conso( host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
        Cette fonction permet récuper la liste des employés ayant effectuée de commandes
    """
    sql=f"""SELECT  e.id_emp , nom_emp,prenom_emp, date_nais_emp, date_embau_emp, lieu_res_emp, email_emp, contact_emp, photo_emp
            FROM Employe e, Commande c
            WHERE e.id_emp = c.id_emp 
            """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def get_emp_non_commande_conso( host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
        Cette fonction permet récuper la liste des employés n'ayant effectuée aucune commandes
    """
    sql=f"""SELECT  e.id_emp , nom_emp,prenom_emp, date_nais_emp, date_embau_emp, lieu_res_emp, email_emp, contact_emp, photo_emp
            FROM Employe e
            WHERE e.id_emp  NOT IN (SELECT id_emp
                                    FROM commande) 
            """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste
    
   


def liste_montant_com_mois(annee, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    
    """Cette fonction permet de recuperer lister les dépenses effectuées dans tous les mois de l'année
    parametre: annee
    return: liste: mois, montant"""
    
    sql=f"""SELECT MONTH(date_com) AS mois, SUM(montant_com) AS montant_total
            FROM Commande
            WHERE YEAR(date_com) = {annee}
            GROUP BY MONTH(date_com)
            ORDER BY mois;
            """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur= bdd.cursor()
    curseur.execute(sql)
    liste= curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def liste_montant_com_annee(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Cette fonction permet de récupérer la dépense annuelle totale de l'entreprise pour chaque année.

    Returns:
        list: Une liste de tuples contenant chaque année avec le montant total des dépenses pour cette année.
              Chaque tuple contient deux éléments : l'année et le montant total des dépenses.
    """


    sql = f"""SELECT YEAR(date_com) AS annee, SUM(montant_com) AS montant_total
              FROM Commande
              GROUP BY YEAR(date_com)
              ORDER BY annee
           """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def liste_montant_com_mois_annee(annee, mois, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Cette fonction permet de récupérer la dépense totale de l'entreprise pour un mois spécifié d'une année donnée.

    Args:
        annee (int): L'année pour laquelle récupérer les données.
        mois (int): Le mois pour lequel récupérer les données (de 1 à 12).
        host_x (str): L'adresse IP ou le nom d'hôte du serveur MySQL. Par défaut, 'localhost'.
        user_x (str): Le nom d'utilisateur du compte MySQL. Par défaut, 'root'.
        password_x (str): Le mot de passe du compte MySQL. Par défaut, ''.
        database_name (str): Le nom de la base de données MySQL. Par défaut, 'graphi_print'.

    Returns:
        list: Une liste de tuples contenant chaque mois avec le montant total des dépenses pour ce mois.
              Chaque tuple contient deux éléments : le mois et le montant total des dépenses.
    """

    sql = f"""SELECT id_com, date_com , nombre_com, montant_com
              FROM Commande
              WHERE YEAR(date_com) = {annee} AND MONTH(date_com) = {mois}
              ORDER BY date_com DESC
             
           """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def liste_montant_com_mois_2(mois, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Cette fonction permet de récupérer la dépense totale de l'entreprise pour un mois spécifié, toutes les années confondues.

    Args:
        mois (int): Le mois pour lequel récupérer les données (de 1 à 12).
        host_x (str): L'adresse IP ou le nom d'hôte du serveur MySQL. Par défaut, 'localhost'.
        user_x (str): Le nom d'utilisateur du compte MySQL. Par défaut, 'root'.
        password_x (str): Le mot de passe du compte MySQL. Par défaut, ''.
        database_name (str): Le nom de la base de données MySQL. Par défaut, 'graphi_print'.

    Returns:
        list: Une liste de tuples contenant chaque année avec le montant total des dépenses pour ce mois.
              Chaque tuple contient deux éléments : l'année et le montant total des dépenses.
    """

    sql = f"""SELECT id_com, date_com, nombre_com, montant_com
              FROM Commande
              WHERE MONTH(date_com) = {mois}
              ORDER BY date_com DES
           """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste




def liste_des_n_consommables(n, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Cette fonction permet de récupérer la dépense totale de l'entreprise pour une année spécifiée.

    Args:
        annee (int): L'année pour laquelle récupérer les données.
        host_x (str): L'adresse IP ou le nom d'hôte du serveur MySQL. Par défaut, 'localhost'.
        user_x (str): Le nom d'utilisateur du compte MySQL. Par défaut, 'root'.
        password_x (str): Le mot de passe du compte MySQL. Par défaut, ''.
        database_name (str): Le nom de la base de données MySQL. Par défaut, 'graphi_print'.

    Returns:
        list: Une liste de tuples contenant chaque mois avec le montant total des dépenses pour ce mois.
              Chaque tuple contient deux éléments : le mois et le montant total des dépenses.
    """

    sql = f"""SELECT c.id_cons, c.nom_cons, COUNT(*) AS nombre_commandes
                FROM commande co
                INNER JOIN appartenir a ON co.id_com = a.id_com
                INNER JOIN consommable c ON a.id_cons = c.id_cons
                GROUP BY c.nom_cons
                ORDER BY COUNT(*) DESC
                LIMIT {n}
           """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste




def liste_des_conso_commande_cat(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Cette fonction permet de récupérer la dépense totale de l'entreprise pour une année spécifiée.

    Args:
        annee (int): L'année pour laquelle récupérer les données.
        host_x (str): L'adresse IP ou le nom d'hôte du serveur MySQL. Par défaut, 'localhost'.
        user_x (str): Le nom d'utilisateur du compte MySQL. Par défaut, 'root'.
        password_x (str): Le mot de passe du compte MySQL. Par défaut, ''.
        database_name (str): Le nom de la base de données MySQL. Par défaut, 'graphi_print'.

    Returns:
        list: Une liste de tuples contenant chaque mois avec le montant total des dépenses pour ce mois.
              Chaque tuple contient deux éléments : le mois et le montant total des dépenses.
    """

    sql = f"""SELECT nom_cat, nom_cons, nombre_commandes
                FROM (
                    SELECT cat.nom_cat, c.nom_cons, COUNT(*) AS nombre_commandes,
                        ROW_NUMBER() OVER(PARTITION BY c.id_cat ORDER BY COUNT(*) DESC) AS rn
                    FROM commande co
                    INNER JOIN appartenir a ON co.id_com = a.id_com
                    INNER JOIN consommable c ON a.id_cons = c.id_cons
                    INNER JOIN categorie cat ON c.id_cat = cat.id_cat
                    GROUP BY cat.id_cat, c.nom_cons
                ) AS sub
                WHERE rn = 1
           """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


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