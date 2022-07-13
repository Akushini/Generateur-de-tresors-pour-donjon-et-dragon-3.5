import random


# determiner les différents anneaux
def determiner_anneau_faible(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 18:
        nom_objet_magique = 'anneau de protection +1'
        valeur = 2000
    if 19 <= resultat <= 28:
        nom_objet_magique = 'anneau de feuille morte'
        valeur = 2200
    if 29 <= resultat <= 36:
        nom_objet_magique = 'anneau d\'escalade'
        valeur = 2500
    if 37 <= resultat <= 44:
        nom_objet_magique = 'anneau de nage'
        valeur = 2500
    if 45 <= resultat <= 52:
        nom_objet_magique = 'anneau de saut'
        valeur = 2500
    if 53 <= resultat <= 60:
        nom_objet_magique = 'anneau de subsistance'
        valeur = 2500
    if 61 <= resultat <= 70:
        nom_objet_magique = 'anneau de contresort'
        valeur = 4000
    if 71 <= resultat <= 75:
        nom_objet_magique = 'anneau de barrière mentale'
        valeur = 8000
    if 76 <= resultat <= 80:
        nom_objet_magique = 'anneau de protection +2'
        valeur = 8000
    if 81 <= resultat <= 85:
        nom_objet_magique = 'anneau de bouclier de force'
        valeur = 8500
    if 86 <= resultat <= 90:
        nom_objet_magique = 'anneau de bélier'
        valeur = 8600
    if 91 <= resultat <= 93:
        nom_objet_magique = 'anneau d\'amitié avec les animaux'
        valeur = 10800
    if 94 <= resultat <= 96:
        nom_objet_magique = 'anneau de résitance aux énergies destructives, mineur'
        valeur = 12000
    if 97 <= resultat <= 98:
        nom_objet_magique = 'anneau de caméléon'
        valeur = 12700
    if 99 <= resultat <= 100:
        nom_objet_magique = 'anneau de marche sur l\'onde'
        valeur = 15000
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_anneau_intermediaire(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 5:
        nom_objet_magique = 'anneau de contresort'
        valeur = 4000
    if 6 <= resultat <= 8:
        nom_objet_magique = 'anneau de barrière mentale'
        valeur = 8000
    if 9 <= resultat <= 18:
        nom_objet_magique = 'anneau de protection +2'
        valeur = 8000
    if 19 <= resultat <= 23:
        nom_objet_magique = 'anneau de bouclier de force'
        valeur = 8500
    if 24 <= resultat <= 28:
        nom_objet_magique = 'anneau de bélier'
        valeur = 8600
    if 29 <= resultat <= 34:
        nom_objet_magique = 'anneau d\'escalade supérieure'
        valeur = 10000
    if 35 <= resultat <= 40:
        nom_objet_magique = 'anneau de nage supérieure'
        valeur = 10000
    if 41 <= resultat <= 46:
        nom_objet_magique = 'anneau de saut supérieur'
        valeur = 10000
    if 47 <= resultat <= 51:
        nom_objet_magique = 'anneau d\'amitié avec les animaux'
        valeur = 10800
    if 52 <= resultat <= 56:
        nom_objet_magique = 'anneau de résistance aux énergies destructives, mineur'
        valeur = 12000
    if 57 <= resultat <= 61:
        nom_objet_magique = 'anneau de caméléon'
        valeur = 12700
    if 62 <= resultat <= 66:
        nom_objet_magique = 'anneau de marche sur l\'onde'
        valeur = 15000
    if 67 <= resultat <= 71:
        nom_objet_magique = 'anneau de protection +3'
        valeur = 18000
    if 72 <= resultat <= 76:
        nom_objet_magique = 'anneau de stokage de sorts mineurs'
        valeur = 18000
    if 77 <= resultat <= 80:
        nom_objet_magique = 'anneau d\'arcanes (premiers)'
        valeur = 20000
    if 81 <= resultat <= 85:
        nom_objet_magique = 'anneau d\'invisibilité'
        valeur = 20000
    if 86 <= resultat <= 90:
        nom_objet_magique = 'anneau d\'esquive totale'
        valeur = 25000
    if 91 <= resultat <= 93:
        nom_objet_magique = 'anneau de rayon X'
        valeur = 25000
    if 94 <= resultat <= 97:
        nom_objet_magique = 'anneau de clignotement'
        valeur = 27000
    if 98 <= resultat <= 100:
        nom_objet_magique = 'anneau de résistance aux énergies destructives, majeur'
        valeur = 28000
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_anneau_puissant(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_objet_magique = 'anneau de résistance aux énergies destructives, mineur'
        valeur = 12000
    if 3 <= resultat <= 7:
        nom_objet_magique = 'anneau de protection +3'
        valeur = 18000
    if 8 <= resultat <= 10:
        nom_objet_magique = 'anneau de stockage de sorts mineurs'
        valeur = 18000
    if 11 <= resultat <= 14:
        nom_objet_magique = 'anneau d\'arcanes (premiers)'
        valeur = 20000
    if 15 <= resultat <= 19:
        nom_objet_magique = 'anneau d\'invisibilité'
        valeur = 20000
    if 20 <= resultat <= 25:
        nom_objet_magique = 'anneau d\'esquive totale'
        valeur = 25000
    if 26 <= resultat <= 28:
        nom_objet_magique = 'anneau de rayon X'
        valeur = 25000
    if 29 <= resultat <= 32:
        nom_objet_magique = 'anneau de clignotement'
        valeur = 27000
    if 33 <= resultat <= 39:
        nom_objet_magique = 'anneau de résistance aux énergies destructives, majeur'
        valeur = 28000
    if 40 <= resultat <= 49:
        nom_objet_magique = 'anneau de protection +4'
        valeur = 32000
    if 50 <= resultat <= 55:
        nom_objet_magique = 'anneau d\'arcanes (deuxième)'
        valeur = 40000
    if 56 <= resultat <= 60:
        nom_objet_magique = 'anneau de liberté de mouvement'
        valeur = 40000
    if 61 <= resultat <= 63:
        nom_objet_magique = 'anneau de résistance aux énergies destructives suprême'
        valeur = 44000
    if 64 <= resultat <= 67:
        nom_objet_magique = 'anneau de feu d\'étoiles'
        valeur = 50000
    if 68 <= resultat <= 72:
        nom_objet_magique = 'anneau de protection +5'
        valeur = 50000
    if 73 <= resultat <= 74:
        nom_objet_magique = 'anneau de protection mutuelle (une paire)'
        valeur = 50000
    if 75 <= resultat <= 79:
        nom_objet_magique = 'anneau de stockage de sorts'
        valeur = 50000
    if 80 <= resultat <= 83:
        nom_objet_magique = 'anneau d\'arcanes (troisièmes)'
        valeur = 70000
    if 84 <= resultat <= 86:
        nom_objet_magique = 'anneau de télékinésie'
        valeur = 75000
    if 87 <= resultat <= 88:
        nom_objet_magique = 'anneau de régénération'
        valeur = 90000
    if resultat == 89:
        nom_objet_magique = 'anneau de triple souhait'
        valeur = 97950
    if 90 <= resultat <= 92:
        nom_objet_magique = 'anneau de renvoi des sorts'
        valeur = 98280
    if 93 <= resultat <= 94:
        nom_objet_magique = 'anneau d\'arcanes (quatrièmes)'
        valeur = 100000
    if resultat == 95:
        nom_objet_magique = 'anneau de bon génie'
        valeur = 125000
    if resultat == 96:
        nom_objet_magique = 'anneau de stockage de sorts majeurs'
        valeur = 200000
    if resultat == 97:
        nom_objet_magique = 'anneau de contrôle des éléments (air)'
        valeur = 200000
    if resultat == 98:
        nom_objet_magique = 'anneau de contrôle des éléments (eau)'
        valeur = 200000
    if resultat == 99:
        nom_objet_magique = 'anneau de contrôle des éléments (feu)'
        valeur = 200000
    if resultat == 100:
        nom_objet_magique = 'anneau de contrôle des éléments (terre)'
        valeur = 200000
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur
