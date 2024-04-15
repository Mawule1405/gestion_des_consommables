-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 05 avr. 2024 à 12:03
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `graphi_print`
--

-- --------------------------------------------------------

--
-- Structure de la table `appartenir`
--
DROP TABLE IF EXISTS `appartenir`;
CREATE TABLE IF NOT EXISTS `appartenir` (
  `id_app` int NOT NULL AUTO_INCREMENT,
  `id_com` int NOT NULL,
  `id_cons` int NOT NULL,
  `qte_com` int DEFAULT NULL,
  PRIMARY KEY (`id_app`),
  KEY `appartient_consommable_fk` (`id_cons`)
) ;

--
-- Déchargement des données de la table `appartenir`
--

INSERT INTO `appartenir` (`id_com`, `id_cons`, `qte_com`) VALUES
(1, 1, 20),
(1, 2, 12),
(1, 14, 18),
(1, 20, 11),
(1, 17, 5);

--
-- Déclencheurs `appartenir`
--
DROP TRIGGER IF EXISTS `ajout_appartenir`;
DELIMITER $$
CREATE TRIGGER `ajout_appartenir` BEFORE INSERT ON `appartenir` FOR EACH ROW BEGIN
    IF NEW.id_com IS NOT NULL AND NEW.id_cons IS NOT NULL THEN
        -- Mettre à jour le nombre_com
        UPDATE Commande 
        SET nombre_com = nombre_com + 1
        WHERE id_com = NEW.id_com;

        -- Mettre à jour le montant_com
        UPDATE Commande 
        SET montant_com = montant_com + (SELECT prix_unitaire_cons FROM Consommable WHERE id_cons = NEW.id_cons) * NEW.qte_com
        WHERE id_com = NEW.id_com;
        
        -- Mettre à jour le qtestock_cons
        UPDATE Consommable
        SET qtestock_cons = qtestock_cons + NEW.qte_com
        WHERE id_cons = NEW.id_cons;
    END IF;
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `supprimer_appartenir`;
DELIMITER $$
CREATE TRIGGER `supprimer_appartenir` BEFORE DELETE ON `appartenir` FOR EACH ROW BEGIN
    -- Décrément le nombre_com de 1
    IF OLD.id_com IS NOT NULL AND OLD.id_cons IS NOT NULL THEN
        UPDATE Commande 
        SET nombre_com = nombre_com - 1 
        WHERE id_com = OLD.id_com;

        -- Réduire le montant_com en déduisant le prix de la consommable à supprimer
        UPDATE Commande 
        SET montant_com = montant_com - (SELECT prix_unitaire_cons FROM Consommable WHERE id_cons = OLD.id_cons)*OLD.qte_com 
        WHERE id_com = OLD.id_com;

        -- Augmenter la quantité du consommable
        UPDATE Consommable 
        SET qtestock_cons = qtestock_cons - OLD.qte_com 
        WHERE id_cons = OLD.id_cons;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Structure de la table `categorie`
--

DROP TABLE IF EXISTS `categorie`;
CREATE TABLE IF NOT EXISTS `categorie` (
  `id_cat` int NOT NULL AUTO_INCREMENT,
  `nom_cat` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_cat`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `categorie`
--

INSERT INTO `categorie` (`id_cat`, `nom_cat`) VALUES
(1, 'Papeteries'),
(2, 'Produit chimique'),
(3, 'Encre'),
(4, 'Toners'),
(5, 'Ruban'),
(6, 'EPI'),
(7, 'Produit de maintenance'),
(8, 'Stylos'),
(9, 'crayons');

-- --------------------------------------------------------

--
-- Structure de la table `commande`
--

DROP TABLE IF EXISTS `commande`;
CREATE TABLE IF NOT EXISTS `commande` (
  `id_com` int NOT NULL AUTO_INCREMENT,
  `date_com` date NOT NULL,
  `nombre_com` int NOT NULL DEFAULT '0',
  `montant_com` decimal(10,0) NOT NULL DEFAULT '0',
  `id_emp` int NOT NULL,
  PRIMARY KEY (`id_com`),
  KEY `commande_employe_fk` (`id_emp`)
) ;

--
-- Déchargement des données de la table `commande`
--

INSERT INTO `commande` (`id_com`, `date_com`, `nombre_com`, `montant_com`, `id_emp`) VALUES
(1, '2024-02-11', 5, '66000', 3);

-- --------------------------------------------------------

--
-- Structure de la table `consommable`
--

DROP TABLE IF EXISTS `consommable`;
CREATE TABLE IF NOT EXISTS `consommable` (
  `id_cons` int NOT NULL AUTO_INCREMENT,
  `nom_cons` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `qtestock_cons` int NOT NULL,
  `qteseuil_cons` int NOT NULL,
  `id_cat` int NOT NULL,
  `prix_unitaire_cons` int DEFAULT '1000',
  PRIMARY KEY (`id_cons`),
  KEY `consommable_categorie_fk` (`id_cat`)
) ;

--
-- Déchargement des données de la table `consommable`
--

INSERT INTO `consommable` (`id_cons`, `nom_cons`, `qtestock_cons`, `qteseuil_cons`, `id_cat`, `prix_unitaire_cons`) VALUES
(1, 'Papier A4', 55, 10, 1, 1000),
(2, 'Papier A3', 62, 10, 1, 1000),
(3, 'Papier photo satiné', 20, 5, 1, 1000),
(4, 'Papier photo brillant', 20, 5, 1, 1000),
(5, 'Papier photo mat', 20, 5, 1, 1000),
(6, 'Papier photo lustré', 20, 5, 1, 1000),
(7, 'Encres acryliques à haut extrait sec (HSA)', 10, 2, 2, 1000),
(8, 'Encres prêtes à l\'emploi (RFU)', 15, 3, 2, 1000),
(9, 'INKTRONIC AG/AGCL 65:35', 20, 4, 2, 1000),
(10, 'INKTRONIC AG/AGCL 80:20', 25, 5, 2, 1000),
(11, 'Encres pour des applications spéciales UV', 30, 6, 2, 1000),
(12, 'Encres flexographiques UV', 35, 5, 2, 1000),
(13, 'Encres métalliques offset UV', 40, 4, 2, 1000),
(14, 'Encres blanches impression offset UV', 63, 3, 2, 1000),
(15, 'Encres à base d\'algues', 50, 4, 2, 1000),
(16, 'Encres pour le jet d’encre continu dévié (CIJ)', 55, 6, 2, 1000),
(17, 'Encres pour la goutte à la demande (DOD)', 65, 5, 2, 1000),
(18, 'Brother TN3480', 20, 5, 4, 1000),
(19, 'HP 44A CF244A Toner authentique noir', 20, 5, 4, 1000),
(20, 'Cartouche d\'encre générique équivalent à CANON 541XL', 31, 5, 4, 1000),
(21, 'Cartouche d\'encre FranceToner équivalent à CANON PG540XL', 20, 5, 4, 1000),
(22, 'Cartouches toner remanufacturée compatible avec BROTHER TN-2421', 20, 5, 4, 1000),
(23, 'Cartouches toner remanufacturée compatible avec HP CF259X', 20, 5, 4, 1000),
(24, 'Brother TN-243 CMYK', 20, 5, 4, 1000),
(25, 'Samsung CLT-P404C pack de 4 toners authentique', 20, 5, 4, 1000),
(26, 'Toner pour HP N°98A 92298 A', 20, 5, 4, 1000),
(27, 'LxTek TN1050', 20, 5, 4, 1000),
(28, 'HP 83A (CF283A) - Noir', 20, 5, 4, 1000),
(29, 'HP 30X (CF230X) - Noir haute capacité', 20, 5, 4, 1000),
(30, 'Cartouche de toner cyan Canon 067', 20, 5, 4, 1000),
(31, 'HP 220X (W2201X) - Cyan Haute Capacité', 20, 5, 4, 1000),
(32, 'Canon 718 - Magenta', 20, 5, 4, 1000),
(33, 'Brother TN-247 - Magenta', 20, 5, 4, 1000),
(34, 'Cartouche de toner jaune Canon 067H', 20, 5, 4, 1000),
(35, 'HP 117A (W2073A) - Jaune', 20, 5, 4, 1000);

-- --------------------------------------------------------

--
-- Structure de la table `demander`
--
DROP TABLE IF EXISTS `demander`;
CREATE TABLE IF NOT EXISTS `demander` (
  `id_dem` int NOT NULL AUTO_INCREMENT,
  `id_emp` int NOT NULL,
  `id_cons` int NOT NULL,
  `qte_demande` int DEFAULT NULL,
  `date_demande` date DEFAULT NULL,
  PRIMARY KEY (`id_dem`),
  KEY `demande_consommable_fk` (`id_cons`)
) ;
--
-- Déchargement des données de la table `demander`
--

INSERT INTO `demander` (`id_emp`, `id_cons`, `qte_demande`, `date_demande`) VALUES
(1, 1, 15, '2024-04-04');

--
-- Déclencheurs `demander`
--
DROP TRIGGER IF EXISTS `ajout_demande`;
DELIMITER $$
CREATE TRIGGER `ajout_demande` BEFORE INSERT ON `demander` FOR EACH ROW BEGIN
    UPDATE Consommable
    SET qtestock_cons = qtestock_cons - NEW.qte_demande
    WHERE id_cons = NEW.id_cons;
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `supprime_demande`;
DELIMITER $$
CREATE TRIGGER `supprime_demande` BEFORE DELETE ON `demander` FOR EACH ROW BEGIN
    -- Augmenter la quantité du consommable en stock
    UPDATE Consommable
    SET qtestock_cons = qtestock_cons + OLD.qte_demande
    WHERE id_cons = OLD.id_cons;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Structure de la table `employe`
--

DROP TABLE IF EXISTS `employe`;
CREATE TABLE IF NOT EXISTS `employe` (
  `id_emp` int NOT NULL AUTO_INCREMENT,
  `nom_emp` varchar(75) COLLATE utf8mb4_general_ci NOT NULL,
  `prenom_emp` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `date_nais_emp` date NOT NULL,
  `date_embau_emp` date NOT NULL,
  `nationalite_emp` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `niveau_etu_emp` varchar(580) COLLATE utf8mb4_general_ci NOT NULL,
  `salaire_emp` decimal(10,2) NOT NULL,
  `lieu_res_emp` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `email_emp` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `contact_emp` varchar(12) COLLATE utf8mb4_general_ci NOT NULL,
  `photo_emp` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id_serv` int DEFAULT NULL,
  `Sexe` varchar(10) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id_emp`),
  KEY `employe_service_fk` (`id_serv`)
) ;

--
-- Déchargement des données de la table `employe`
--

INSERT INTO `employe` (`id_emp`, `nom_emp`, `prenom_emp`, `date_nais_emp`, `date_embau_emp`, `nationalite_emp`, `niveau_etu_emp`, `salaire_emp`, `lieu_res_emp`, `email_emp`, `contact_emp`, `photo_emp`, `id_serv`, `Sexe`) VALUES
(1, 'HELOU', 'Komlan Mawulé', '1996-05-14', '2022-02-01', 'Togolaise', 'Licence en Mathématiques', '400000.00', 'Libreville', 'heloumawule@gmail.com', '+24174630473', 'D:\\TP_GESTION_DES_CONSOMMABLES\\projet_python\\images\\photo_employe\\mathias.jpg', 3, 'Masculin'),
(2, 'HELOU', 'Kodjo Jules', '1991-04-08', '2019-11-05', 'Togolaise', 'CAP Electicité', '200000.00', 'Lomé', 'heloukodjododji@gmail.com', '+22893669653', 'D:\\TP_GESTION_DES_CONSOMMABLES\\projet_python\\images\\photo_employe\\IMG-20240330-WA0001.jpg', 2, 'Masculin'),
(3, 'DONYO', 'Afivi Mawupémo', '2000-06-28', '2023-10-07', 'Togolaise', 'BAC A4', '100000.00', 'Lomé', 'donyoreine@gmail.com', '+22893643213', 'D:\\TP_GESTION_DES_CONSOMMABLES\\projet_python\\images\\photo_employe\\reine.jpg', 1, 'Féminin'),
(4, 'DZIDJINYO', 'Komlan Maurice Yann', '1998-10-19', '2023-10-22', 'Togolaise', 'BAC D + 2', '300000.00', 'Lomé', 'mauriceyann05@gmail.com', '+22897821183', 'D:\\TP_GESTION_DES_CONSOMMABLES\\projet_python\\images\\photo_employe\\maurice.jpg', 4, 'Masculin');

-- --------------------------------------------------------

--
-- Structure de la table `service`
--

DROP TABLE IF EXISTS `service`;
CREATE TABLE IF NOT EXISTS `service` (
  `id_serv` int NOT NULL AUTO_INCREMENT,
  `nom_serv` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `description_serv` text COLLATE utf8mb4_general_ci,
  `date_serv` date NOT NULL,
  `id_emp_resp` int DEFAULT NULL,
  PRIMARY KEY (`id_serv`),
  KEY `service_employe_2_fk` (`id_emp_resp`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `service`
--

INSERT INTO `service` (`id_serv`, `nom_serv`, `description_serv`, `date_serv`, `id_emp_resp`) VALUES
(1, 'Secrétariat', NULL, '2022-01-01', 3),
(2, 'Maintenance', NULL, '2022-01-01', 2),
(3, 'Direction', NULL, '2022-01-01', 1),
(4, 'Production', NULL, '2022-01-01', 4);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
