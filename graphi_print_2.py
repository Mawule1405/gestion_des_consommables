"""
Module pour la gestion de la statistique
"""
import mysql.connector
#=========================================================================
#===============UTILISATIONS DES CONCOMMABLES PAR LES EMPLOYES============
#=========================================================================
def nombre_homme_employe(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération du nombre d'homme dans l'entreprise
    @return entier
    """

    sql = f"SELECT count(*) FROM employe WHERE Sexe='Masculin'"

    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste[0][0]


def nombre_femme_employe(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération du nombre de femme dans l'entreprise
    @return entier
    """

    sql = f"SELECT count(*) FROM employe WHERE Sexe='Féminin'"

    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste[0][0]


def employe_le_mieux_paye(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération des employés ayant le salaire maximal
    """

    sql = """SELECT nom_emp, prenom_emp, salaire_emp, niveau_etu_emp, photo_emp, nom_serv
        FROM employe, service
        WHERE salaire_emp = (SELECT MAX(salaire_emp) FROM employe) AND employe.id_serv = service.id_serv
        """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste

def employe_le_mieux_paye_par_service(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération des employés ayant le salaire maximal
    """

    sql = """SELECT e.nom_emp, e.prenom_emp, e.salaire_emp, e.niveau_etu_emp, e.photo_emp, s.nom_serv
             FROM employe e , service s
             WHERE e.id_serv = s.id_serv
             AND e.salaire_emp = (
                 SELECT MAX(salaire_emp)
                 FROM employe ee
                 WHERE ee.id_serv = s.id_serv
             )""" 
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def employe_le_plus_ancien(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération des les plus anciens de l'entreprise
    """

    sql = """SELECT nom_emp, prenom_emp, salaire_emp, niveau_etu_emp, photo_emp, nom_serv, YEAR(CURRENT_DATE()) - YEAR(date_embau_emp) AS anciennete
                FROM employe , service
                WHERE employe.id_serv = service.id_serv AND date_embau_emp = (
                    SELECT MIN(date_embau_emp)
                    FROM employe
                )""" 
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def employe_le_plus_ancien_par_service(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération des employé les plus anciens dans chaque service  de l'entreprise
    """

    sql = """SELECT e.nom_emp, e.prenom_emp, e.salaire_emp, e.niveau_etu_emp, e.photo_emp, s.nom_serv,
        YEAR(CURRENT_DATE()) - YEAR(e.date_embau_emp) AS anciennete
        FROM employe e
        JOIN service s ON e.id_serv = s.id_serv
        WHERE e.date_embau_emp = (
            SELECT MIN(date_embau_emp)
            FROM employe ee
            WHERE ee.id_serv = s.id_serv
        )""" 
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste




def employe_le_plus_jeune(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération des les plus jeunes de l'entreprise
    """

    sql = """SELECT e.nom_emp, e.prenom_emp, e.salaire_emp, e.niveau_etu_emp, e.photo_emp, s.nom_serv,  YEAR(CURRENT_DATE()) - YEAR(e.date_embau_emp) AS anciennete
            FROM employe e, service s
            WHERE e.id_emp = s.id_emp_resp AND e.date_embau_emp = (
                SELECT MAX(date_embau_emp)
                FROM employe
            )""" 
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def employe_le_plus_jeune_par_service(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération des employé les plus anciens dans chaque service  de l'entreprise
    """

    sql = """SELECT e.nom_emp, e.prenom_emp, e.salaire_emp, e.niveau_etu_emp, e.photo_emp, s.nom_serv,
        YEAR(CURRENT_DATE()) - YEAR(e.date_embau_emp) AS anciennete
        FROM employe e
        JOIN service s ON e.id_emp = s.id_emp_resp
        WHERE e.date_embau_emp = (
            SELECT MAX(date_embau_emp)
            FROM employe ee
            WHERE ee.id_serv = s.id_serv
        )""" 
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def nombre_employe_par_service(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération du nombre d'employés par service de l'entreprise
    """

    sql = """SELECT s.nom_serv, COUNT(ee.id_emp) AS nombre_employes, 
       COALESCE(e.nom_emp, 'Aucun') AS nom_responsable, 
       COALESCE(e.prenom_emp, 'Aucun') AS prenom_responsable
        FROM service s
        LEFT JOIN employe e ON s.id_emp_resp = e.id_emp
        LEFT JOIN employe ee ON s.id_serv = ee.id_serv
        GROUP BY s.nom_serv, e.nom_emp, e.prenom_emp
         """

    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def distribution_de_medaille(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de chaque employé avec son ancienneté
    """

    sql = """SELECT e.nom_emp, e.prenom_emp, e.photo_emp,   YEAR(CURRENT_DATE()) - YEAR(e.date_embau_emp) AS anciennete
            FROM employe e
            ORDER BY anciennete DESC
            """ 
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


#=====================================================================================================================
#========================================STATISTIQUE DES CONSOMMABLES=================================================
def liste_conso_utilise(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de consommable utilisé
    """

    sql = """SELECT d.id_cons, nom_cons, sum(qte_demande) as quantite
            FROM demander d, consommable c
            WHERE d.id_cons = c.id_cons
            GROUP BY d.id_cons
            ORDER BY d.id_cons
       """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste

def liste_conso_non_utilise(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de consommable non utilisé
    """

    sql = """SELECT id_cons, nom_cons, qtestock_cons
            FROM consommable 
            WHERE id_cons NOT IN (SELECT id_cons FROM demander)
            ORDER BY id_cons
       """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def liste_conso_epuise(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de consommable épuisé: la quantité en stock est inférieur à la quantité seuil
    """

    sql = """SELECT id_cons, nom_cons, qtestock_cons, qteseuil_cons
            FROM consommable 
            WHERE qtestock_cons <= qteseuil_cons
            ORDER BY id_cons
       """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def liste_conso_le_plus_utilise_par_categorie(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de consommable les plus utilisés par catégorie
    """

    sql = """SELECT cons.id_cons, nom_cons, nom_cat, count(qte_demande) AS quantite
            FROM categorie cat, consommable cons, demander dem 
            WHERE cat.id_cat = cons.id_cat AND cons.id_cons = dem.id_cons
            GROUP BY cat.id_cat, cons.id_cons
            HAVING quantite = (
                SELECT MAX(quantite_par_categorie)
                FROM (
                    SELECT cat.id_cat, COUNT(dem.qte_demande) AS quantite_par_categorie
                    FROM categorie cat, consommable cons, demander dem
                    WHERE cat.id_cat = cons.id_cat AND cons.id_cons = dem.id_cons
                    GROUP BY cat.id_cat, cons.id_cons
                ) AS quantites_par_categorie
                WHERE quantites_par_categorie.id_cat = cat.id_cat
            )
            ORDER BY cons.id_cons
       """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def liste_conso_le_plus_chere_par_categorie(host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de consommable le plus chère de chaque catégorie
    """

    sql = """SELECT c.id_cons, c.nom_cons, cat.nom_cat, c.prix_unitaire_cons
            FROM consommable c
            JOIN (
                SELECT cons.id_cat, MAX(cons.prix_unitaire_cons) AS max_prix
                FROM consommable cons
                GROUP BY cons.id_cat
            ) AS max_prices ON c.id_cat = max_prices.id_cat AND c.prix_unitaire_cons = max_prices.max_prix
            LEFT JOIN categorie cat ON c.id_cat = cat.id_cat
            ORDER BY c.id_cons
       """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def liste_conso_utilise_par_annee(annee, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de consommable les plus utilisés par année
    """

    sql = f"""SELECT cons.id_cons, cons.nom_cons, cat.nom_cat, sum(dem.qte_demande)
                FROM categorie cat
                JOIN consommable cons ON cat.id_cat = cons.id_cat
                JOIN demander dem ON cons.id_cons = dem.id_cons
                WHERE YEAR(dem.date_demande) = {annee}
                GROUP BY cons.id_cons
                ORDER BY cons.id_cons
       """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def liste_conso_utilise_par_mois(mois, annee, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de consommable les plus utilisés par mois
    """

    sql = f"""SELECT cons.id_cons, cons.nom_cons, cat.nom_cat, sum(dem.qte_demande)
                FROM categorie cat
                JOIN consommable cons ON cat.id_cat = cons.id_cat
                JOIN demander dem ON cons.id_cons = dem.id_cons
                WHERE YEAR(dem.date_demande) = {annee} AND MoNTH(dem.date_demande)= {mois}
                GROUP BY cons.id_cons
                ORDER BY cons.id_cons
       """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def liste_montant_conso_utilise_par_mois(mois, annee, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction de récupération de montant des consommables les plus utilisés par mois
    """

    sql = f"""SELECT sum(dem.qte_demande*cons.prix_unitaire_cons)
                FROM demander dem, consommable cons
                WHERE YEAR(dem.date_demande) = {annee} AND MONTH(dem.date_demande)= {mois} AND dem.id_cons = cons.id_cons
                GROUP BY YEAR(dem.date_demande) AND  MONTH(dem.date_demande)
                ORDER BY cons.id_cons
       """
    
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def liste_conso_commande_par_mois(mois, annee, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction pour récupérer la liste des consommables commandés dans un mois d'une année
    """

    sql = f"""SELECT nom_cons, qte_com*cons.prix_unitaire_cons
                FROM consommable cons
                JOIN appartenir ap ON cons.id_cons = ap.id_cons
                JOIN commande com ON ap.id_com = com.id_com
                WHERE YEAR(com.date_com) = {annee}
                AND MONTH(com.date_com) = {mois}
                ORDER BY cons.id_cons
    """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def liste_conso_plus_commande_par_categorie( host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction pour récupérer la liste des consommables les plus commandés par catégories
    """

    sql = """SELECT cons.id_cons, cons.nom_cons AS consommable, cat.nom_cat AS categorie,  COUNT(ap.id_app) AS nombre_commandes
                FROM categorie cat
                JOIN consommable cons ON cat.id_cat = cons.id_cat
                JOIN appartenir ap ON cons.id_cons = ap.id_cons
                GROUP BY cat.id_cat, cons.id_cons
                HAVING COUNT(ap.id_app) = (
                    SELECT MAX(nb_commandes)
                    FROM (
                        SELECT cat.id_cat, COUNT(ap.id_app) AS nb_commandes
                        FROM categorie cat
                        JOIN consommable cons ON cat.id_cat = cons.id_cat
                        JOIN appartenir ap ON cons.id_cons = ap.id_cons
                        GROUP BY cat.id_cat, cons.id_cons
                    ) AS subquery
                    WHERE subquery.id_cat = cat.id_cat
                )
                ORDER BY cons.id_cons
    """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste



def liste_montant_commande_par_mois(mois, annee, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction pour récupérer la dépense effectuée pour la commandés dans un mois d'une année
    """

    sql = f"""SELECT SUM(cons.prix_unitaire_cons * ap.qte_com) AS total_prix_consommables
                FROM appartenir ap
                JOIN commande com ON ap.id_com = com.id_com
                JOIN consommable cons ON ap.id_cons = cons.id_cons
                WHERE YEAR(com.date_com) = {annee}
                AND MONTH(com.date_com) = {mois}
                GROUP BY YEAR(com.date_com) AND  MONTH(com.date_com)


    """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste




def liste_des_commandes_effectues( host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction pour récupérer la liste des commandes effectués
    """
    sql = """SELECT id_com, nom_emp, prenom_emp, nom_four, com.date_com, com.montant_com
                FROM commande com, employe emp, fournisseur four
                WHERE com.id_emp = emp.id_emp AND com.id_four = four.id_four
                ORDER BY id_com"""
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste




def liste_consommables_utilises_par_employe(id, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction pour récupérer la liste des consommables utilisés un employé
    """
    sql = f"""SELECT id_dem, nom_cons, qte_demande, date_demande
            FROM demander dem, consommable cons
            WHERE dem.id_emp ={id} AND dem.id_cons = cons.id_cons
            ORDER BY dem.id_dem
    
    """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste


def liste_consommables_commande_par_employe(id, host_x='localhost', user_x='root', password_x='', database_name='graphi_print'):
    """
    Fonction pour récupérer la liste des consommables utilisés un employé
    """
    sql = f"""SELECT id_app, nom_cons, qte_com, date_com
            FROM appartenir app, consommable cons, commande com
            WHERE com.id_emp = {id} AND app.id_cons = cons.id_cons AND com.id_com = app.id_com
            ORDER BY app.id_app
    
    """
    bdd = mysql.connector.connect(host=host_x, user=user_x, password=password_x, database=database_name)
    curseur = bdd.cursor()
    curseur.execute(sql)
    liste = curseur.fetchall()
    curseur.close()
    bdd.close()

    return liste