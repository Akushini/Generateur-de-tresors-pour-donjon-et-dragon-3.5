import random


def lancer_des(nombre_des, valeur_des):
    somme = 0
    for _ in range(nombre_des + 1):
        somme = somme + random.randint(1, valeur_des)
    return somme

