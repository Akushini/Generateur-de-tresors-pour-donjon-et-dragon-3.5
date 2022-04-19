import random

from utils import lancer_des

bonne_reponse = False
while not bonne_reponse:
    niveau_rencontre = input("Entrez le niveau de la rencontre (entre 1 et 5) :")
    if niveau_rencontre.isdigit() and 1 <= int(niveau_rencontre) <= 5:
        bonne_reponse = True
    else:
        print("Veuillez entrer un nombre entier entre 1 et 5")

facteur_tresor = input("Entrez le facteur de tresor :")

# tirage aleatoire du tresor en pieces
piece_cuivre = piece_argent = piece_or = piece_platine = 0

# tirage niveau 1
if niveau_rencontre == "1":
    tresors_tires = 0
    while tresors_tires < int(facteur_tresor):
        resultat = random.randint(1, 100)
        if 15 <= resultat <= 29:
            piece_cuivre += lancer_des(1, 6) * 1000
        if 30 <= resultat <= 52:
            piece_argent += lancer_des(1, 8) * 100
        if 53 <= resultat <= 95:
            piece_or += lancer_des(2, 8) * 10
        if 96 <= resultat <= 100:
            piece_platine += lancer_des(1, 3) * 10
        tresors_tires += 1

# tirage niveau 2
if niveau_rencontre == "2":
    tresors_tires = 0
    while tresors_tires < int(facteur_tresor):
        resultat = random.randint(1, 100)
        if 14 <= resultat <= 23:
            piece_cuivre += lancer_des(1, 10) * 1000
        if 24 <= resultat <= 43:
            piece_argent += lancer_des(2, 10) * 100
        if 44 <= resultat <= 95:
            piece_or += lancer_des(4, 10) * 10
        if 96 <= resultat <= 100:
            piece_platine += lancer_des(1, 4) * 10
        tresors_tires += 1

# tirage niveau 3
if niveau_rencontre == "3":
    tresors_tires = 0
    while tresors_tires < int(facteur_tresor):
        resultat = random.randint(1, 100)
        if 12 <= resultat <= 21:
            piece_cuivre += lancer_des(2, 10) * 1000
        if 22 <= resultat <= 41:
            piece_argent += lancer_des(4, 8) * 100
        if 42 <= resultat <= 95:
            piece_or += lancer_des(1, 4) * 100
        if 96 <= resultat <= 100:
            piece_platine += lancer_des(1, 6) * 10
        tresors_tires += 1

# tirage niveau 4
if niveau_rencontre == "4":
    tresors_tires = 0
    while tresors_tires < int(facteur_tresor):
        resultat = random.randint(1, 100)
        if 12 <= resultat <= 21:
            piece_cuivre += lancer_des(3, 10) * 1000
        if 22 <= resultat <= 41:
            piece_argent += lancer_des(4, 12) * 100
        if 42 <= resultat <= 95:
            piece_or += lancer_des(1, 6) * 100
        if 96 <= resultat <= 100:
            piece_platine += lancer_des(1, 8) * 10
        tresors_tires += 1

# tirage niveau 5
if niveau_rencontre == "5":
    tresors_tires = 0
    while tresors_tires < int(facteur_tresor):
        resultat = random.randint(1, 100)
        if 11 <= resultat <= 19:
            piece_cuivre += lancer_des(1, 4) * 10000
        if 20 <= resultat <= 38:
            piece_argent += lancer_des(1, 6) * 1000
        if 39 <= resultat <= 95:
            piece_or += lancer_des(1, 8) * 100
        if 96 <= resultat <= 100:
            piece_platine += lancer_des(1, 10) * 10
        tresors_tires += 1
print(f'Piece de Cuivre : {piece_cuivre}')
print(f'Piece d\'argent : {piece_argent}')
print(f'Piece d\'or : {piece_or}')
print(f'Piece de platine : {piece_platine}')

