import random

from anneau import determiner_anneau_faible
from arme import determiner_arme_faible, tirer_arme
from armure import determiner_armure_bouclier_faible, tirer_armure
from baguette import determiner_baguette_faible
from objet_merveilleux import determiner_objet_merveilleux_faible
from parchemin import lancer_sort_profane_0, lancer_sort_profane_1, lancer_sort_profane_2, lancer_sort_profane_3, \
    lancer_sort_divin_3, lancer_sort_divin_2, lancer_sort_divin_1, lancer_sort_divin_0, lancer_sort_profane_5, \
    lancer_sort_divin_5, lancer_sort_profane_4, lancer_sort_divin_4, lancer_sort_divin_6, lancer_sort_profane_6, \
    lancer_sort_divin_7, lancer_sort_profane_7, lancer_sort_profane_8, lancer_sort_divin_8, lancer_sort_divin_9, \
    lancer_sort_profane_9
from potions_huiles import determiner_potion_huile_faibles


def lancer_des(nombre_des, valeur_des):
    somme = 0
    for _ in range(nombre_des + 1):
        somme = somme + random.randint(1, valeur_des)
    return somme


def lancer_gemme(valeur_des_gemmes):
    type1 = ['agate mousse', 'agate xiloïde', 'azurite', 'hématite', 'lapis-lazuli', 'malachite','obsidienne',
             'oeil-de-chat', 'oeil-de-tigre', 'perle irrégulière', 'quartz bleu', 'rhodochrosite', 'turaquoise']
    type2 = ['calcédoine', 'chrysoprase', 'citrine', 'cordiérite', 'cormaline', 'cristal de roche', 'quartz limpide',
             'héliotrope', 'jaspe', 'onyx', 'onyx marbre', 'péridot', 'pierre de lune', 'quartz rose', 'quartz laiteux',
             'quartz rutilé', 'sardoine', 'zircon']
    type3 = ['ambre', 'améthyste', 'chrysobéryl', 'corail', 'grenat rouge', 'granat brun vert', 'jade', 'jais',
             'perle blanche', 'perle dorée', 'perle rose', 'perle argentée', 'spinelle rouge', 'spinelle brun rouge',
             'spinelle vert sombre', 'tourmaline']
    type4 = ['aigue-marine', 'alexandrite', 'grenat almandin', 'perle noire', 'spinelle bleu nuit','topaze jaune d\'or']
    type5 = ['corindon jaune ambré', 'corindon pourpre', 'émeraude', 'opale blanche', 'opale noire',
             'opale de feu', 'rubis', 'saphir bleu', 'saphir noir']
    type6 = ['diamant limpide', 'diamant jaune', 'diamant rose', 'diamant brun', 'diamant bleu', 'émeuraude pure',
             'hyacinthe']
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 25:
        valeur = random.randint(4, 16)
        nom_gemme = random.choice(type1)
    if 26 <= resultat <= 50:
        valeur = random.randrange(20, 80, 10)
        nom_gemme = random.choice(type2)
    if 51 <= resultat <= 70:
        valeur = random.randrange(40, 160, 10)
        nom_gemme = random.choice(type3)
    if 71 <= resultat <= 90:
        valeur = random.randrange(200, 800, 100)
        nom_gemme = random.choice(type4)
    if 91 <= resultat <= 99:
        valeur = random.randrange(400, 1600, 100)
        nom_gemme = random.choice(type5)
    if resultat == 100:
        valeur = random.randrange(2000, 8000, 1000)
        nom_gemme = random.choice(type6)
    valeur_des_gemmes += valeur
    return valeur_des_gemmes, valeur, nom_gemme


def lancer_objet_art(valeur_des_objets_arts):
    type1 = ['aiguière en argent', 'statuette en os', 'statuette en ivoire', 'bracelet d\'or fin']
    type2 = ['vêtement tissés de fil d\'or fin', 'masque de velours noir agrémenté de nombreuses citrines',
             'calice en argent serti de lapis-lazuli']
    type3 = ['grande tapisserie en laine', 'chope en laiton crustée de motifs en jade']
    type4 = ['peigne en argent serti de pierres de lune',
             'épée longue à la lame plaquée d\'argent et au pommeau taillé dans le jais']
    type5 = ['harpe en bois exotique sculptée et ornée d\'ivoire et de zircons', 'statuette en or massif (5 kilos)']
    type6 = ['peigne en or en forme de dragon avec un oeil de grenat',
             'dague d\'apparat en électrum avvec un rubis enchâssé dans son pommeau']
    type7 = ['bandeau sur lequel un faux oeil a été tissé à l\'aide de saphirs et de pierres de lune',
             'opale de feu fixée à une chaîne d\'or fin', 'peinture de maître']
    type8 = ['manteau de soie et de velours orné de nommbreuses pierres de lune',
             'pendentif en saphir fixé à une chaîne en or']
    type9 = ['gant brodé et garni de nombreuses pierres fines', 'bracelet de cheville serti de pierres fines',
             'boîte à musique en or']
    type10 = ['serre-tête en or serti de quatre aigues-marines', 'collier de petites perles roses']
    type11 = ['couronne en or sertie de joyaux', 'anneau en électrum serti d\'une pierre précieuse']
    type12 = ['anneau d\'or serti d\'un rubis', 'coupe en or sertie d\'émeraudes']
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 10:
        valeur = random.randrange(10, 100, 10)
        nom_objet_art = random.choice(type1)
    if 11 <= resultat <= 25:
        valeur = random.randrange(30, 180, 10)
        nom_objet_art = random.choice(type2)
    if 26 <= resultat <= 40:
        valeur = random.randrange(100, 600, 100)
        nom_objet_art = random.choice(type3)
    if 41 <= resultat <= 50:
        valeur = random.randrange(100, 1000, 100)
        nom_objet_art = random.choice(type4)
    if 51 <= resultat <= 60:
        valeur = random.randrange(200, 1200, 100)
        nom_objet_art = random.choice(type5)
    if 61 <= resultat <= 70:
        valeur = random.randrange(300, 1800, 100)
        nom_objet_art = random.choice(type6)
    if 71 <= resultat <= 80:
        valeur = random.randrange(400, 2400, 100)
        nom_objet_art = random.choice(type7)
    if 81 <= resultat <= 85:
        valeur = random.randrange(500, 3000, 100)
        nom_objet_art = random.choice(type8)
    if 86 <= resultat <= 90:
        valeur = random.randrange(1000, 4000, 1000)
        nom_objet_art = random.choice(type9)
    if 91 <= resultat <= 95:
        valeur = random.randrange(1000, 6000, 1000)
        nom_objet_art = random.choice(type10)
    if 96 <= resultat <= 99:
        valeur = random.randrange(2000, 8000, 1000)
        nom_objet_art = random.choice(type11)
    if resultat == 100:
        valeur = random.randrange(2000, 12000, 1000)
        nom_objet_art = random.choice(type12)
    valeur_des_objets_arts += valeur
    return valeur_des_objets_arts, valeur, nom_objet_art


def tirer_objet_non_magique(valeur_objets_non_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 17:
        valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur = tirer_objet_special(valeur_objets_non_magiques)
    if 18 <= resultat <= 50:
        valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur = tirer_armure(valeur_objets_non_magiques)
    if 51 <= resultat <= 83:
        valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur, cac = tirer_arme(valeur_objets_non_magiques)
    if 84 <= resultat <= 100:
        valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur = tirer_materiel_et_equipement(valeur_objets_non_magiques)
    return valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur


def tirer_objet_special(valeur_objets_non_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 12:
        nom_objet_non_magique = 'feu grégeois'
        nombre_objet_non_magique = random.randint(1, 4)
        valeur = nombre_objet_non_magique * 20
    if 13 <= resultat <= 24:
        nom_objet_non_magique = 'acide'
        nombre_objet_non_magique = random.randint(2, 8)
        valeur = nombre_objet_non_magique * 10
    if 25 <= resultat <= 36:
        nom_objet_non_magique = 'bâtonnets fumigènes'
        nombre_objet_non_magique = random.randint(1, 4)
        valeur = nombre_objet_non_magique * 20
    if 37 <= resultat <= 48:
        nom_objet_non_magique = 'eau bénite'
        nombre_objet_non_magique = random.randint(1, 4)
        valeur = nombre_objet_non_magique * 25
    if 49 <= resultat <= 62:
        nom_objet_non_magique = 'antidote'
        nombre_objet_non_magique = random.randint(1, 4)
        valeur = nombre_objet_non_magique * 50
    if 63 <= resultat <= 74:
        nom_objet_non_magique = 'torche éternelle'
        nombre_objet_non_magique = 1
        valeur = nombre_objet_non_magique * 110
    if 75 <= resultat <= 88:
        nom_objet_non_magique = 'sacoches immobilisantes'
        nombre_objet_non_magique = random.randint(1, 4)
        valeur = nombre_objet_non_magique * 50
    if 89 <= resultat <= 100:
        nom_objet_non_magique = 'pierres à tonnerre'
        nombre_objet_non_magique = random.randint(1, 4)
        valeur = nombre_objet_non_magique * 30
    valeur_objets_non_magiques += valeur
    return valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur


def tirer_materiel_et_equipement(valeur_objets_non_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_objet_non_magique = 'sac à dos vide'
        valeur = 2
    if 4 <= resultat <= 6:
        nom_objet_non_magique = 'pied-de-biche'
        valeur = 2
    if 7 <= resultat <= 11:
        nom_objet_non_magique = 'lanterne sourde'
        valeur = 12
    if 12 <= resultat <= 16:
        nom_objet_non_magique = 'cadenas simple'
        valeur = 20
    if 17 <= resultat <= 21:
        nom_objet_non_magique = 'cadenas moyen'
        valeur = 40
    if 22 <= resultat <= 28:
        nom_objet_non_magique = 'bon cadenas'
        valeur = 80
    if 29 <= resultat <= 35:
        nom_objet_non_magique = 'excellent cadenas'
        valeur = 150
    if 36 <= resultat <= 40:
        nom_objet_non_magique = 'menotte de qualité supérieure'
        valeur = 50
    if 41 <= resultat <= 43:
        nom_objet_non_magique = 'petit miroir en acier'
        valeur = 10
    if 44 <= resultat <= 46:
        nom_objet_non_magique = 'corde en soie, 15m'
        valeur = 10
    if 47 <= resultat <= 53:
        nom_objet_non_magique = 'longue-vue'
        valeur = 1000
    if 54 <= resultat <= 58:
        nom_objet_non_magique = 'outils de maître artisan'
        valeur = 55
    if 59 <= resultat <= 63:
        nom_objet_non_magique = 'matériel d\'escalade'
        valeur = 80
    if 64 <= resultat <= 68:
        nom_objet_non_magique = 'trousse de déguisement'
        valeur = 50
    if 69 <= resultat <= 73:
        nom_objet_non_magique = 'trouse de premiers secours'
        valeur = 50
    if 74 <= resultat <= 77:
        nom_objet_non_magique = 'symbole sacré en argent'
        valeur = 25
    if 78 <= resultat <= 81:
        nom_objet_non_magique = 'sablier'
        valeur = 25
    if 82 <= resultat <= 88:
        nom_objet_non_magique = 'loupe'
        valeur = 100
    if 89 <= resultat <= 95:
        nom_objet_non_magique = 'intrument de musique de maître'
        valeur = 100
    if 96 <= resultat <= 100:
        nom_objet_non_magique = 'outils de cambrioleur de qualité supérieure'
        valeur = 50
    nombre_objet_non_magique = 1
    valeur_objets_non_magiques += valeur
    return valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur


def determiner_objet_magique_faible(valeur_objets_magiques):
    resultat = random.randint(1,100)
    if 1 <= resultat <= 2:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_anneau_faible(valeur_objets_magiques)
    if 3 <= resultat <= 7:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_faible(valeur_objets_magiques)
    if 8 <= resultat <= 11:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure_bouclier_faible(valeur_objets_magiques)
    if 12 <= resultat <= 21:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_baguette_faible(valeur_objets_magiques)
    if 22 <= resultat <= 30:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_objet_merveilleux_faible(valeur_objets_magiques)
    if 31 <= resultat <= 65:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_parchemin_faible(valeur_objets_magiques)
    if 66 <= resultat <= 100:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_potion_huile_faibles(valeur_objets_magiques)
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


# les parchemins
def determiner_parchemin_faible(valeur_objets_magiques):
    list_sorts_parchemin = []
    valeur_parchemin = 0
    niveau_sorts_determines = 0
    sorts_determines = 0
    niveau_sort_0 = 0
    niveau_sort_1 = 0
    niveau_sort_2 = 0
    niveau_sort_3 = 0
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 70:
        profane = True
    else:
        profane = False
    nombre_sorts = random.randint(1, 3)
    while niveau_sorts_determines < nombre_sorts:
        resultat = random.randint(1, 100)
        if 1 <= resultat <= 5:
            niveau_sort_0 += 1
        if 6 <= resultat <= 50:
            niveau_sort_1 += 1
        if 51 <= resultat <= 95:
            niveau_sort_2 += 1
        if 96 <= resultat <= 100:
            niveau_sort_3 += 1
        niveau_sorts_determines += 1
    while sorts_determines < niveau_sorts_determines:
        while niveau_sort_3 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_3()
            else:
                valeur, nom_sort = lancer_sort_divin_3()
            niveau_sort_3 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_2 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_2()
            else:
                valeur, nom_sort = lancer_sort_divin_2()
            niveau_sort_2 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_1 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_1()
            else:
                valeur, nom_sort = lancer_sort_divin_1()
            niveau_sort_1 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_0 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_0()
            else:
                valeur, nom_sort = lancer_sort_divin_0()
            niveau_sort_0 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
    valeur_objets_magiques += valeur_parchemin
    valeur = valeur_parchemin
    nombre_objet_magique = 1
    type_magie = 'profane' if profane else 'divin'
    nom_objet_magique = f'parchemin {type_magie} de {", ".join(list_sorts_parchemin)}'
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_parchemin_intermediaire(valeur_objets_magiques):
    list_sorts_parchemin = []
    valeur_parchemin = 0
    niveau_sorts_determines = 0
    sorts_determines = 0
    niveau_sort_2 = 0
    niveau_sort_3 = 0
    niveau_sort_4 = 0
    niveau_sort_5 = 0
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 70:
        profane = True
    else:
        profane = False
    nombre_sorts = random.randint(1, 4)
    while niveau_sorts_determines < nombre_sorts:
        resultat = random.randint(1, 100)
        if 1 <= resultat <= 5:
            niveau_sort_2 += 1
        if 6 <= resultat <= 65:
            niveau_sort_3 += 1
        if 66 <= resultat <= 95:
            niveau_sort_4 += 1
        if 96 <= resultat <= 100:
            niveau_sort_5 += 1
        niveau_sorts_determines += 1
    while sorts_determines < niveau_sorts_determines:
        while niveau_sort_5 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_5()
            else:
                valeur, nom_sort = lancer_sort_divin_5()
            niveau_sort_5 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_4 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_4()
            else:
                valeur, nom_sort = lancer_sort_divin_4()
            niveau_sort_4 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_3 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_3()
            else:
                valeur, nom_sort = lancer_sort_divin_3()
            niveau_sort_3 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_2 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_2()
            else:
                valeur, nom_sort = lancer_sort_divin_2()
            niveau_sort_2 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
    valeur_objets_magiques += valeur_parchemin
    valeur = valeur_parchemin
    nombre_objet_magique = 1
    type_magie = 'profane' if profane else 'divin'
    nom_objet_magique = f'parchemin {type_magie} de {", ".join(list_sorts_parchemin)}'
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_parchemin_puissant(valeur_objets_magiques):
    list_sorts_parchemin = []
    valeur_parchemin = 0
    niveau_sorts_determines = 0
    sorts_determines = 0
    niveau_sort_4 = 0
    niveau_sort_5 = 0
    niveau_sort_6 = 0
    niveau_sort_7 = 0
    niveau_sort_8 = 0
    niveau_sort_9 = 0
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 70:
        profane = True
    else:
        profane = False
    nombre_sorts = random.randint(1, 6)
    while niveau_sorts_determines < nombre_sorts:
        resultat = random.randint(1, 100)
        if 1 <= resultat <= 5:
            niveau_sort_4 += 1
        if 6 <= resultat <= 50:
            niveau_sort_5 += 1
        if 51 <= resultat <= 70:
            niveau_sort_6 += 1
        if 71 <= resultat <= 85:
            niveau_sort_7 += 1
        if 86 <= resultat <= 95:
            niveau_sort_8 += 1
        if 96 <= resultat <= 100:
            niveau_sort_9 += 1
        niveau_sorts_determines += 1
    while sorts_determines < niveau_sorts_determines:
        while niveau_sort_9 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_9()
            else:
                valeur, nom_sort = lancer_sort_divin_9()
            niveau_sort_9 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_8 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_8()
            else:
                valeur, nom_sort = lancer_sort_divin_8()
            niveau_sort_8 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_7 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_7()
            else:
                valeur, nom_sort = lancer_sort_divin_7()
            niveau_sort_7 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_6 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_6()
            else:
                valeur, nom_sort = lancer_sort_divin_6()
            niveau_sort_6 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_5 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_5()
            else:
                valeur, nom_sort = lancer_sort_divin_5()
            niveau_sort_5 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
        while niveau_sort_4 > 0:
            if profane:
                valeur, nom_sort = lancer_sort_profane_4()
            else:
                valeur, nom_sort = lancer_sort_divin_4()
            niveau_sort_4 -= 1
            sorts_determines += 1
            valeur_parchemin += valeur
            list_sorts_parchemin.append(nom_sort)
    valeur_objets_magiques += valeur_parchemin
    valeur = valeur_parchemin
    nombre_objet_magique = 1
    type_magie = 'profane' if profane else 'divin'
    nom_objet_magique = f'parchemin {type_magie} de {", ".join(list_sorts_parchemin)}'
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def poser_question_puissance():
    bonne_reponse = False
    while not bonne_reponse:
        puissance = input("1 - Faible \n"
                          "2 - Intermédiaire \n"
                          "3 - Fort \n")
        if puissance.isdigit() and 1 <= int(puissance) <= 3:
            puissance = int(puissance)
            bonne_reponse = True
            bonne_reponse_2 = False
            while not bonne_reponse_2:
                combien = input('Combien ?')
                if combien.isdigit() and int(combien) > 0:
                    combien = int(combien)
                    return puissance, combien
                else:
                    print("Veuillez entrer un nombre entier supérieur à 0")
        else:
            print("Veuillez entrer un nombre entier entre 1 et 3")
