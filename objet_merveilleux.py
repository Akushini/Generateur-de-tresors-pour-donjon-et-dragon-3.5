import random


def determiner_objet_merveilleux_faible(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 50:
        nom_objet_magique = 'objet merveilleux'
        valeur = 0
    if 51 <= resultat <= 100:
        nom_objet_magique = 'objet merveilleux'
        valeur = 0
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur
