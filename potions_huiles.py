import random


def determiner_potion_huile_faibles(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_objet_magique = 'arme magique'
        type = 'huile'
        valeur = 50
    if 4 <= resultat <= 6:
        nom_objet_magique = 'armure du mage'
        type = 'potion'
        valeur = 50
    if 7 <= resultat <= 9:
        nom_objet_magique = 'bouclier de la foi (+2)'
        type = 'potion'
        valeur = 50
    if 10 <= resultat <= 12:
        nom_objet_magique = 'endurance aux énergies destructives'
        type = 'potion'
        valeur = 50
    if resultat == 13:
        nom_objet_magique = 'gourdin magique'
        type = 'huile'
        valeur = 50
    if 14 <= resultat <= 15:
        nom_objet_magique = 'invisibilité pour les animaux'
        type = 'potion'
        valeur = 50
    if 16 <= resultat <= 17:
        nom_objet_magique = 'invisibilité pour les morts-vivants'
        type = 'potion'
        valeur = 50
    if 18 <= resultat <= 20:
        nom_objet_magique = 'morsure magique'
        type = 'potion'
        valeur = 50
    if resultat == 21:
        nom_objet_magique = 'passage sans trace'
        type = 'potion'
        valeur = 50
    if resultat == 22:
        nom_objet_magique = 'pierre magique'
        type = 'huile'
        valeur = 50
    if 23 <= resultat <= 24:
        nom_objet_magique = 'protection contre (un alignement)'
        type = 'potion'
        valeur = 50
    if 25 <= resultat <= 26:
        nom_objet_magique = 'regain d\'assurance'
        type = 'potion'
        valeur = 50
    if resultat == 27:
        nom_objet_magique = 'sanctuaire'
        type = 'potion'
        valeur = 50
    if 28 <= resultat <= 29:
        nom_objet_magique = 'saut'
        type = 'potion'
        valeur = 50
    if 30 <= resultat <= 39:
        nom_objet_magique = 'soins légers'
        type = 'potion'
        valeur = 50
    if 40 <= resultat <= 41:
        nom_objet_magique = 'bénédiction d\'arme'
        type = 'huile'
        valeur = 100
    if 42 <= resultat <= 45:
        nom_objet_magique = 'agrandissement'
        type = 'potion'
        valeur = 200
    if resultat == 45:
        nom_objet_magique = 'rapetissement'
        type = 'potion'
        valeur = 200
    if 46 <= resultat <= 47:
        nom_objet_magique = 'aide'
        type = 'potion'
        valeur = 300
    if resultat == 48:
        nom_objet_magique = 'alignement indétectable'
        type = 'potion'
        valeur = 300
    if resultat == 49:
        nom_objet_magique = 'bouclier de la foi (+3)'
        type = 'potion'
        valeur = 300
    if 50 <= resultat <= 51:
        nom_objet_magique = 'délivrance de la paralysie'
        type = 'potion'
        valeur = 300
    if resultat == 52:
        nom_objet_magique = 'détection faussée'
        type = 'potion'
        valeur = 300
    if 53 <= resultat <= 55:
        nom_objet_magique = 'endurance de l\'ours'
        type = 'potion'
        valeur = 300
    if 56 <= resultat <= 58:
        nom_objet_magique = 'flou'
        type = 'potion'
        valeur = 300
    if 59 <= resultat <= 61:
        nom_objet_magique = 'force de taureau'
        type = 'potion'
        valeur = 300
    if 62 <= resultat <= 64:
        nom_objet_magique = 'grâce féline'
        type = 'potion'
        valeur = 300
    if 65 <= resultat <= 67:
        nom_objet_magique = 'invisibilité'
        resultat = random.randint(1, 2)
        if resultat == 1:
            type = 'potion'
        else:
            type = 'huile'
        valeur = 300
    if 68 <= resultat <= 69:
        nom_objet_magique = 'lévitation'
        resultat = random.randint(1, 2)
        if resultat== 1:
            type = 'potion'
        else:
            type = 'huile'
        valeur = 300
    if 70 <= resultat <= 71:
        nom_objet_magique = 'patte d\'araignée'
        type = 'potion'
        valeur = 300
    if 72 <= resultat <= 74:
        nom_objet_magique = 'peau d\'écorce (+2)'
        type = 'potion'
        valeur = 300
    if 75 <= resultat <= 76:
        nom_objet_magique = 'protection contre les projectiles (10/magie)'
        type = 'potion'
        valeur = 300
    if 77 <= resultat <= 79:
        nom_objet_magique = 'ralentissement du poison'
        type = 'potion'
        valeur = 300
    if 80 <= resultat <= 82:
        nom_objet_magique = 'résistance aux énergies destructives (une énergie, 10)'
        type = 'potion'
        valeur = 300
    if 83 <= resultat <= 85:
        nom_objet_magique = 'restauration partielle'
        type = 'potion'
        valeur = 300
    if 86 <= resultat <= 87:
        nom_objet_magique = 'ruse du renard'
        type = 'potion'
        valeur = 300
    if 88 <= resultat <= 89:
        nom_objet_magique = 'sagesse du hibou'
        type = 'potion'
        valeur = 300
    if 90 <= resultat <= 94:
        nom_objet_magique = 'soins modérés'
        type = 'potion'
        valeur = 300
    if 95 <= resultat <= 96:
        nom_objet_magique = 'splendeur de l\'aigle'
        type = 'potion'
        valeur = 300
    if resultat == 97:
        nom_objet_magique = 'ténèbres'
        type = 'huile'
        valeur = 300
    if 98 <= resultat <= 100:
        nom_objet_magique = 'vision dans le noir'
        type = 'potion'
        valeur = 300
    nom_objet_magique = f'{type} de {nom_objet_magique}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur