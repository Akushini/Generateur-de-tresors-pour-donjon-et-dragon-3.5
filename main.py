import random

from menu import menu
from utils import lancer_des, lancer_gemme, lancer_objet_art, tirer_objet_non_magique, determiner_objet_magique_faible

choix_menu = False
butin = False
tresor = False
fin = False
while not tresor:
    while not choix_menu:
        tirer_tresor = input("Voulez-vous tirer un tresor complet ? :")
        if tirer_tresor == "oui":
            choix_menu = True
            while not butin:
                bonne_reponse = False
                while not bonne_reponse:
                    niveau_rencontre = input("Entrez le niveau de la rencontre (entre 1 et 5) :")
                    if niveau_rencontre.isdigit() and 1 <= int(niveau_rencontre) <= 5:
                        bonne_reponse = True
                    else:
                        print("Veuillez entrer un nombre entier entre 1 et 5")

                facteur_tresor = input("Entrez le facteur de tresor :")

                # tirage aleatoire du tresor en pieces
                piece_cuivre = piece_argent = piece_or = piece_platine = gemmes = objets_arts = objets_non_magiques = 0
                objet_magique_faible = objets_magique_intermediare = objets_magique_puissant = 0

                # tirage niveau 1
                if niveau_rencontre == "1":
                    pieces_tirees = 0
                    while pieces_tirees < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 15 <= resultat <= 29:
                            piece_cuivre += lancer_des(1, 6) * 1000
                        if 30 <= resultat <= 52:
                            piece_argent += lancer_des(1, 8) * 100
                        if 53 <= resultat <= 95:
                            piece_or += lancer_des(2, 8) * 10
                        if 96 <= resultat <= 100:
                            piece_platine += lancer_des(1, 3) * 10
                        pieces_tirees += 1
                    # tirage des gemmes et objets d'arts
                    biens_precieux_tires = 0
                    while biens_precieux_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 91 <= resultat <= 95:
                            gemmes += 1
                        if 96 <= resultat <= 100:
                            objets_arts += 1
                        biens_precieux_tires += 1
                    # tirage des objets communs ou magiques
                    objets_tires = 0
                    while objets_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 75 <= resultat <= 95:
                            objets_non_magiques += 1
                        if 96 <= resultat <= 100:
                            objet_magique_faible += 1
                        objets_tires += 1

                # tirage niveau 2
                if niveau_rencontre == "2":
                    pieces_tirees = 0
                    while pieces_tirees < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 14 <= resultat <= 23:
                            piece_cuivre += lancer_des(1, 10) * 1000
                        if 24 <= resultat <= 43:
                            piece_argent += lancer_des(2, 10) * 100
                        if 44 <= resultat <= 95:
                            piece_or += lancer_des(4, 10) * 10
                        if 96 <= resultat <= 100:
                            piece_platine += lancer_des(1, 4) * 10
                        pieces_tirees += 1
                    # tirage des gemmes et objets d'arts
                    biens_precieux_tires = 0
                    while biens_precieux_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 82 <= resultat <= 95:
                            gemmes += lancer_des(1, 3)
                        if 96 <= resultat <= 100:
                            objets_arts += lancer_des(1, 3)
                        biens_precieux_tires += 1
                    # tirage des objets communs ou magiques
                    objets_tires = 0
                    while objets_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 50 <= resultat <= 85:
                            objets_non_magiques += 1
                        if 86 <= resultat <= 100:
                            objet_magique_faible += 1
                        objets_tires += 1

                # tirage niveau 3
                if niveau_rencontre == "3":
                    pieces_tirees = 0
                    while pieces_tirees < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 12 <= resultat <= 21:
                            piece_cuivre += lancer_des(2, 10) * 1000
                        if 22 <= resultat <= 41:
                            piece_argent += lancer_des(4, 8) * 100
                        if 42 <= resultat <= 95:
                            piece_or += lancer_des(1, 4) * 100
                        if 96 <= resultat <= 100:
                            piece_platine += lancer_des(1, 6) * 10
                        pieces_tirees += 1
                    # tirage des gemmes et objets d'arts
                    biens_precieux_tires = 0
                    while biens_precieux_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 78 <= resultat <= 95:
                            gemmes += lancer_des(1, 3)
                        if 96 <= resultat <= 100:
                            objets_arts += lancer_des(1, 3)
                        biens_precieux_tires += 1
                    # tirage des objets communs ou magiques
                    objets_tires = 0
                    while objets_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 50 <= resultat <= 79:
                            objets_non_magiques += lancer_des(1, 3)
                        if 80 <= resultat <= 100:
                            objet_magique_faible += 1
                        objets_tires += 1

                # tirage niveau 4
                if niveau_rencontre == "4":
                    pieces_tirees = 0
                    while pieces_tirees < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 12 <= resultat <= 21:
                            piece_cuivre += lancer_des(3, 10) * 1000
                        if 22 <= resultat <= 41:
                            piece_argent += lancer_des(4, 12) * 100
                        if 42 <= resultat <= 95:
                            piece_or += lancer_des(1, 6) * 100
                        if 96 <= resultat <= 100:
                            piece_platine += lancer_des(1, 8) * 10
                        pieces_tirees += 1
                    # tirage des gemmes et objets d'arts
                    biens_precieux_tires = 0
                    while biens_precieux_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 71 <= resultat <= 95:
                            gemmes += lancer_des(1, 4)
                        if 96 <= resultat <= 100:
                            objets_arts += lancer_des(1, 3)
                        biens_precieux_tires += 1
                    # tirage des objets communs ou magiques
                    objets_tires = 0
                    while objets_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 43 <= resultat <= 62:
                            objets_non_magiques += lancer_des(1, 4)
                        if 63 <= resultat <= 100:
                            objet_magique_faible += 1
                        objets_tires += 1

                # tirage niveau 5
                if niveau_rencontre == "5":
                    pieces_tirees = 0
                    while pieces_tirees < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 11 <= resultat <= 19:
                            piece_cuivre += lancer_des(1, 4) * 10000
                        if 20 <= resultat <= 38:
                            piece_argent += lancer_des(1, 6) * 1000
                        if 39 <= resultat <= 95:
                            piece_or += lancer_des(1, 8) * 100
                        if 96 <= resultat <= 100:
                            piece_platine += lancer_des(1, 10) * 10
                        pieces_tirees += 1
                    # tirage des gemmes et objets d'arts
                    biens_precieux_tires = 0
                    while biens_precieux_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 61 <= resultat <= 95:
                            gemmes += lancer_des(1, 4)
                        if 96 <= resultat <= 100:
                            objets_arts += lancer_des(1, 4)
                        biens_precieux_tires += 1
                    # tirage des objets communs ou magiques
                    objets_tires = 0
                    while objets_tires < int(facteur_tresor):
                        resultat = random.randint(1, 100)
                        if 58 <= resultat <= 67:
                            objets_non_magiques += lancer_des(1, 4)
                        if 68 <= resultat <= 100:
                            objet_magique_faible += lancer_des(1, 3)
                        objets_tires += 1

                # Tirage du nom de la valeur des gemmes
                list_gemmes = []
                valeur_des_gemmes = 0
                gemmes_estimees = 0
                while gemmes_estimees < gemmes:
                    valeur_des_gemmes, valeur, nom_gemme = lancer_gemme(valeur_des_gemmes)
                    list_gemmes.append((nom_gemme, valeur))
                    gemmes_estimees += 1

                # Tirage du nom et de la valeur des objets d'art
                list_objets_arts = []
                valeur_des_objets_arts = 0
                objets_arts_estimees = 0
                while objets_arts_estimees < objets_arts:
                    valeur_des_objets_arts, valeur, nom_objet_art = lancer_objet_art(valeur_des_objets_arts)
                    list_objets_arts.append((nom_objet_art, valeur))
                    objets_arts_estimees += 1

                # Tirage des objets non magiques
                list_objets_non_magiques = []
                valeur_objets_non_magiques = 0
                objets_non_magiques_definis = 0
                while objets_non_magiques_definis < objets_non_magiques:
                    valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur = tirer_objet_non_magique(
                        valeur_objets_non_magiques)
                    list_objets_non_magiques.append((nombre_objet_non_magique, nom_objet_non_magique, valeur))
                    objets_non_magiques_definis += 1

                # Tirage des objets magiques faibles
                list_objets_magiques_faibles = []
                valeur_objets_magiques = 0
                objets_magiques_faibles_definis = 0
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_objet_magique_faible(
                        valeur_objets_magiques)
                    list_objets_magiques_faibles.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_faibles_definis += 1
                print()
                print(f'Piece de Cuivre : {piece_cuivre}')
                print(f'Piece d\'argent : {piece_argent}')
                print(f'Piece d\'or : {piece_or}')
                print(f'Piece de platine : {piece_platine}')
                print()
                print(f'Gemmes trouvées : {gemmes}')
                for aTuple in list_gemmes:
                    print('%s d\'une valeur de %s pièces d\'or' % aTuple)
                print()
                print(f'Valeur totale des gemmes récupérées : {valeur_des_gemmes} pièces d\'or')
                print()
                print(f'Objets d\'arts trouvés : {objets_arts}')
                for aTuple in list_objets_arts:
                    print('%s d\'une valeur de %s pièces d\'or' % aTuple)
                print()
                print(f'Valeurs totale des objets d\'arts récupérés : {valeur_des_objets_arts} pièces d\'or')
                print()
                print(f'Objets non magiques trouvés : {objets_non_magiques}')
                for aTuple in list_objets_non_magiques:
                    print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
                print()
                print(f'Valeurs totale des objets non magiques récupérés : {valeur_objets_non_magiques} pièces d\'or')
                print()
                print(f'Objets magiques faibles : {objet_magique_faible}')
                print(f'Objets magiques intermédiaires : {objets_magique_intermediare}')
                print(f'Objets magiques puissants : {objets_magique_puissant}')
                for aTuple in list_objets_magiques_faibles:
                    print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
                print()
                print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
                print()
                reponse_finale = False
                while not reponse_finale:
                    recommencer = input("Voulez-vous tirer un autre butin ? :")
                    if recommencer == "oui":
                        butin = False
                        reponse_finale = True
                        tresor = False
                    if recommencer == "non":
                        butin = True
                        reponse_finale = True
                        tresor = True
                        print("Au revoir")
                    else:
                        print("Répondez par oui ou non")
        if tirer_tresor == "non":
            tresor, choix_menu = menu(tresor, choix_menu)
        else:
            print("Répondez par oui ou non")

