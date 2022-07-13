import random

from anneau import determiner_anneau_puissant, determiner_anneau_intermediaire, determiner_anneau_faible
from arme import determiner_arme_faible, determiner_arme_intermediaire, determiner_arme_puissante
from armure import determiner_armure_bouclier_faible, determiner_armure_bouclier_intermediaire, \
    determiner_armure_bouclier_puissante
from baguette import determiner_baguette_faible, determiner_baguette_intermediaire, determiner_baguette_puissante
from baton import determiner_baton_puissant, determiner_baton_intermediaire
from utils import lancer_des, lancer_gemme, lancer_objet_art, tirer_objet_non_magique, \
    determiner_objet_magique_faible, poser_question_puissance, determiner_parchemin_faible, \
    determiner_parchemin_puissant, determiner_parchemin_intermediaire


def menu(tresor, choix_menu):
    valeur_objets_magiques = 0
    objets_magiques_faibles_definis = 0
    objets_magiques_intermediaires_definis = 0
    objets_magiques_puissants_definis = 0
    list_objets_magiques_faibles = []
    list_objets_magiques_intermediaires = []
    list_objets_magiques_puissants = []
    reponse_menu = input("Que voulez-vous faire ?            \n"
                         "1  - Tirer des gemmes            \n"
                         "2  - Tirer des objets d\'arts     \n"
                         "3  - Tirer des baguettes          \n"
                         "4  - Tirer des armes magiques     \n"
                         "5  - Tirer des armures magiques   \n"
                         "6  - Tirer des anneaux            \n"
                         "7  - Tirer des parchemins  \n"
                         "8  - Tirer des batons        \n"
                         "9  - Tirer des scpetres       \n")
    if reponse_menu.isdigit() and 1 <= int(reponse_menu) <= 8:
        if reponse_menu.isdigit() and int(reponse_menu) == 1:
            bonne_reponse = False
            while not bonne_reponse:
                gemmes = int(input("combien de gemmes ?"))
                if gemmes > 0:
                    list_gemmes = []
                    valeur_des_gemmes = 0
                    gemmes_estimees = 0
                    bonne_reponse = True
                else:
                    print("Veuillez entrer un nombre entier supérieur à 0")
                while gemmes_estimees < gemmes:
                    valeur_des_gemmes, valeur, nom_gemme = lancer_gemme(valeur_des_gemmes)
                    list_gemmes.append((nom_gemme, valeur))
                    gemmes_estimees += 1
                print(f'Gemmes trouvées : {gemmes}')
                for aTuple in list_gemmes:
                    print('%s d\'une valeur de %s pièces d\'or' % aTuple)
                    print()
                    print(f'Valeur totale des gemmes récupérées : {valeur_des_gemmes} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 2:
            bonne_reponse = False
            while not bonne_reponse:
                objets_arts = int(input("combien d\'objet d\'arts ?"))
                if objets_arts > 0:
                    list_objets_arts = []
                    valeur_des_objets_arts = 0
                    objets_arts_estimees = 0
                    bonne_reponse = True
                else:
                    print("Veuillez entrer un nombre entier supérieur à 0")
                while objets_arts_estimees < objets_arts:
                    valeur_des_objets_arts, valeur, nom_objet_art = lancer_objet_art(valeur_des_objets_arts)
                    list_objets_arts.append((nom_objet_art, valeur))
                    objets_arts_estimees += 1
                    print(f'Objets d\'arts trouvés : {objets_arts}')
                    for aTuple in list_objets_arts:
                        print('%s d\'une valeur de %s pièces d\'or' % aTuple)
                    print()
                    print(f'Valeurs totale des objets d\'arts récupérés : {valeur_des_objets_arts} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 3:
            bonne_reponse = False
            while not bonne_reponse:
                puissance, combien = poser_question_puissance()
                if puissance == 1:
                    objet_magique_faible = combien
                    while objets_magiques_faibles_definis < objet_magique_faible:
                        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_baguette_faible(valeur_objets_magiques)
                        list_objets_magiques_faibles.append((nombre_objet_magique, nom_objet_magique, valeur))
                        objets_magiques_faibles_definis += 1
                        bonne_reponse = True
                if puissance == 2:
                    objet_magique_intermediare = combien
                    while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_baguette_intermediaire(valeur_objets_magiques)
                        list_objets_magiques_intermediaires.append((nombre_objet_magique, nom_objet_magique, valeur))
                        objets_magiques_intermediaires_definis += 1
                        bonne_reponse = True
                if puissance == 3:
                    objet_magique_puissant = combien
                    while objets_magiques_puissants_definis < objet_magique_puissant:
                        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_baguette_puissante(valeur_objets_magiques)
                        list_objets_magiques_puissants.append((nombre_objet_magique, nom_objet_magique, valeur))
                        objets_magiques_puissants_definis += 1
                        bonne_reponse = True
                for aTuple in list_objets_magiques_faibles:
                    print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
                print()
                for aTuple in list_objets_magiques_intermediaires:
                    print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
                print()
                for aTuple in list_objets_magiques_puissants:
                    print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
                print()
                print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 4:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_faible(
                        valeur_objets_magiques)
                    list_objets_magiques_faibles.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_intermediaire(
                        valeur_objets_magiques)
                    list_objets_magiques_intermediaires.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_puissante(
                        valeur_objets_magiques)
                    list_objets_magiques_puissants.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_puissants_definis += 1
            for aTuple in list_objets_magiques_faibles:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_intermediaires:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_puissants:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 5:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure_bouclier_faible(
                        valeur_objets_magiques)
                    list_objets_magiques_faibles.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure_bouclier_intermediaire(
                        valeur_objets_magiques)
                    list_objets_magiques_intermediaires.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure_bouclier_puissante(
                        valeur_objets_magiques)
                    list_objets_magiques_puissants.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_puissants_definis += 1
            for aTuple in list_objets_magiques_faibles:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_intermediaires:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_puissants:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 6:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_anneau_faible(
                        valeur_objets_magiques)
                    list_objets_magiques_faibles.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_anneau_intermediaire(
                        valeur_objets_magiques)
                    list_objets_magiques_intermediaires.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_anneau_puissant(
                        valeur_objets_magiques)
                    list_objets_magiques_puissants.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_puissants_definis += 1
            for aTuple in list_objets_magiques_faibles:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_intermediaires:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_puissants:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 7:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                objet_magique_faible = combien
                while objets_magiques_faibles_definis < objet_magique_faible:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_parchemin_faible(
                        valeur_objets_magiques)
                    list_objets_magiques_faibles.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_faibles_definis += 1
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_parchemin_intermediaire(
                        valeur_objets_magiques)
                    list_objets_magiques_intermediaires.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_parchemin_puissant(
                        valeur_objets_magiques)
                    list_objets_magiques_puissants.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_puissants_definis += 1
            for aTuple in list_objets_magiques_faibles:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_intermediaires:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_puissants:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 8:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                print("les batons de faible puissance n'existent pas")
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_baton_intermediaire(
                        valeur_objets_magiques)
                    list_objets_magiques_intermediaires.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_baton_puissant(
                        valeur_objets_magiques)
                    list_objets_magiques_puissants.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_puissants_definis += 1
            for aTuple in list_objets_magiques_faibles:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_intermediaires:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_puissants:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            if valeur_objets_magiques > 0:
                print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
        if reponse_menu.isdigit() and int(reponse_menu) == 9:
            puissance, combien = poser_question_puissance()
            if puissance == 1:
                print("les sceptres de faible puissance n'existent pas")
            if puissance == 2:
                objet_magique_intermediare = combien
                while objets_magiques_intermediaires_definis < objet_magique_intermediare:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_baton_intermediaire(
                        valeur_objets_magiques)
                    list_objets_magiques_intermediaires.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_intermediaires_definis += 1
            if puissance == 3:
                objet_magique_puissant = combien
                while objets_magiques_puissants_definis < objet_magique_puissant:
                    nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_baton_puissant(
                        valeur_objets_magiques)
                    list_objets_magiques_puissants.append((nombre_objet_magique, nom_objet_magique, valeur))
                    objets_magiques_puissants_definis += 1
            for aTuple in list_objets_magiques_faibles:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_intermediaires:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            for aTuple in list_objets_magiques_puissants:
                print('%s %s d\'une valeur de %s pièces d\'or' % aTuple)
            print()
            if valeur_objets_magiques > 0:
                print(f'Valeurs totale des objets magiques récupérés : {valeur_objets_magiques} pièces d\'or')
    else:
        print("Veuillez entrer un nombre entier entre 1 et 9")
    reponse_finale = False
    while not reponse_finale:
        recommencer = input("Voulez-vous tirer un autre butin ? :")
        if recommencer == "oui":
            reponse_finale = True
            return tresor, choix_menu
        if recommencer == "non":
            tresor = True
            choix_menu = True
            reponse_finale = True
            print("Au revoir")
            return tresor, choix_menu
        else:
            print("Répondez par oui ou non")
