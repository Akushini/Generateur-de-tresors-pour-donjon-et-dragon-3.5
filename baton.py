import random


def determiner_baton_intermediaire(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 15:
        nom_objet_magique = 'baton d\'envoûtement'
        valeur = 16500
    if 16 <= resultat <= 30:
        nom_objet_magique = 'baton de feu'
        valeur = 17750
    if 31 <= resultat <= 40:
        nom_objet_magique = 'baton de grand essaim'
        valeur = 24750
    if 41 <= resultat <= 60:
        nom_objet_magique = 'baton de guérison'
        valeur = 27750
    if 61 <= resultat <= 75:
        nom_objet_magique = 'baton d\'altéréation de taille'
        valeur = 29000
    if 76 <= resultat <= 90:
        nom_objet_magique = 'baton de clarté'
        valeur = 48250
    if 91 <= resultat <= 95:
        nom_objet_magique = 'baton de givre'
        valeur = 56250
    if 96 <= resultat <= 100:
        nom_objet_magique = 'baton de défense'
        valeur = 58250
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_baton_puissant(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_objet_magique = 'baton d\'envoûtement'
        valeur = 16500
    if 4 <= resultat <= 9:
        nom_objet_magique = 'baton de feu'
        valeur = 17750
    if 10 <= resultat <= 11:
        nom_objet_magique = 'baton de grand essaim'
        valeur = 24750
    if 12 <= resultat <= 17:
        nom_objet_magique = 'baton de guérison'
        valeur = 27750
    if 18 <= resultat <= 19:
        nom_objet_magique = 'baton d\'altéréation de taille'
        valeur = 29000
    if 20 <= resultat <= 24:
        nom_objet_magique = 'baton de clarté'
        valeur = 48250
    if 25 <= resultat <= 31:
        nom_objet_magique = 'baton de givre'
        valeur = 56250
    if 32 <= resultat <= 38:
        nom_objet_magique = 'baton de défense'
        valeur = 58250
    if 39 <= resultat <= 43:
        nom_objet_magique = 'baton d\'abjuration'
        valeur = 65000
    if 44 <= resultat <= 48:
        nom_objet_magique = 'baton d\'enchantement'
        valeur = 65000
    if 49 <= resultat <= 53:
        nom_objet_magique = 'baton d\'évocation'
        valeur = 65000
    if 54 <= resultat <= 58:
        nom_objet_magique = 'baton d\'illusion'
        valeur = 65000
    if 59 <= resultat <= 63:
        nom_objet_magique = 'baton d\'invocation'
        valeur = 65000
    if 64 <= resultat <= 68:
        nom_objet_magique = 'baton de nécormancie'
        valeur = 65000
    if 69 <= resultat <= 73:
        nom_objet_magique = 'baton de transmutation'
        valeur = 65000
    if 74 <= resultat <= 77:
        nom_objet_magique = 'baton de divination'
        valeur = 73500
    if 78 <= resultat <= 82:
        nom_objet_magique = 'baton de pierre et de terre'
        valeur = 80500
    if 83 <= resultat <= 87:
        nom_objet_magique = 'baton de forêt profonde'
        valeur = 101250
    if 88 <= resultat <= 92:
        nom_objet_magique = 'baton de vie'
        valeur = 155750
    if 93 <= resultat <= 97:
        nom_objet_magique = 'baton de transport'
        valeur = 170500
    if 98 <= resultat <= 100:
        nom_objet_magique = 'baton de surpuissance'
        valeur = 211000
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur
