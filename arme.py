import random


def tirer_arme(valeur_objets_non_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 50:
        # arme de cac usuelle de maître p222 guide maitre
        cac = True
        resultat = random.randint(1, 100)
        if 1 <= resultat <= 3:
            nom_objet_non_magique = 'bâton de maître'
            valeur = 600
        if 4 <= resultat <= 8:
            nom_objet_non_magique = 'cimeterre de maître'
            valeur = 315
        if 9 <= resultat <= 12:
            nom_objet_non_magique = 'dague de maître'
            valeur = 302
        if 13 <= resultat <= 22:
            nom_objet_non_magique = 'épée à deux mains de maître'
            valeur = 350
        if 23 <= resultat <= 32:
            nom_objet_non_magique = 'épée bâtarde de maître'
            valeur = 335
        if 33 <= resultat <= 37:
            nom_objet_non_magique = 'épée courte de maître'
            valeur = 310
        if 38 <= resultat <= 50:
            nom_objet_non_magique = 'épée longue de maître'
            valeur = 315
        if 51 <= resultat <= 3:
            nom_objet_non_magique = 'grande hache de maître'
            valeur = 320
        if 61 <= resultat <= 3:
            nom_objet_non_magique = 'hache de guerre naine de maître'
            valeur = 330
        if 72 <= resultat <= 75:
            nom_objet_non_magique = 'kama de maître'
            valeur = 302
        if 76 <= resultat <= 79:
            nom_objet_non_magique = 'lance de maître'
            valeur = 302
        if 80 <= resultat <= 83:
            nom_objet_non_magique = 'masse d\arme légère de maître'
            valeur = 305
        if 84 <= resultat <= 88:
            nom_objet_non_magique = 'masse d\arme lourde de maître'
            valeur = 312
        if 89 <= resultat <= 92:
            nom_objet_non_magique = 'nunchaku de maître'
            valeur = 302
        if 93 <= resultat <= 96:
            nom_objet_non_magique = 'rapière de maître'
            valeur = 320
        if 97 <= resultat <= 100:
            nom_objet_non_magique = 'siangham de maître'
            valeur = 303
    if 51 <= resultat <= 70:
        # arme inhabituelle de maître p222 guide maitre
        cac = True
        resultat = random.randint(1, 100)
        if 1 <= resultat <= 2:
            cac = False
            nom_objet_non_magique = 'arbalète légère à répétition de maître'
            valeur = 550
        if 3 <= resultat <= 4:
            cac = False
            nom_objet_non_magique = 'arbalète lourde à répétition de maître'
            valeur = 700
        if 5 <= resultat <= 7:
            cac = False
            nom_objet_non_magique = 'arbalète de poing de maître'
            valeur = 400
        if 8 <= resultat <= 9:
            cac = False
            nom_objet_non_magique = 'bolas de maître'
            valeur = 305
        if 10 <= resultat <= 12:
            nom_objet_non_magique = 'chaîne cloutée de maître'
            valeur = 325
        if 13 <= resultat <= 14:
            nom_objet_non_magique = 'cimeterre à deux mains de maître'
            valeur = 375
        if 15 <= resultat <= 16:
            nom_objet_non_magique = 'corsèque de maître'
            valeur = 310
        if 17 <= resultat <= 18:
            nom_objet_non_magique = 'coutille de maître'
            valeur = 308
        if 19 <= resultat <= 20:
            nom_objet_non_magique = 'dague coup-de-poing de maître'
            valeur = 302
        if 21 <= resultat <= 23:
            nom_objet_non_magique = 'double-lame de maître'
            valeur = 700
        if 24 <= resultat <= 26:
            nom_objet_non_magique = 'épieu de maître'
            valeur = 301
        if 27 <= resultat <= 28:
            nom_objet_non_magique = 'faux de maître'
            valeur = 318
        if 29 <= resultat <= 30:
            nom_objet_non_magique = 'filet de maître'
            valeur = 320
        if 31 <= resultat <= 33:
            nom_objet_non_magique = 'fléau d\'armes léger de maître'
            valeur = 308
        if 34 <= resultat <= 36:
            nom_objet_non_magique = 'fléau d\'armes lourd de maître'
            valeur = 315
        if 37 <= resultat <= 39:
            nom_objet_non_magique = 'fléau double de maître'
            valeur = 690
        if 40 <= resultat <= 41:
            nom_objet_non_magique = 'fouet de maître'
            valeur = 301
        if 42 <= resultat <= 43:
            nom_objet_non_magique = 'gantelet de maître'
            valeur = 302
        if 44 <= resultat <= 45:
            nom_objet_non_magique = 'gantelet clouté de maître'
            valeur = 305
        if 46 <= resultat <= 47:
            nom_objet_non_magique = 'gourdin de maître'
            valeur = 300
        if 48 <= resultat <= 49:
            nom_objet_non_magique = 'guisarme de maître'
            valeur = 309
        if 50 <= resultat <= 53:
            nom_objet_non_magique = 'hache d\'armes de maître'
            valeur = 310
        if 54 <= resultat <= 56:
            nom_objet_non_magique = 'hache double orque de maître'
            valeur = 660
        if 57 <= resultat <= 58:
            nom_objet_non_magique = 'hachette de maître'
            valeur = 306
        if 59 <= resultat <= 61:
            nom_objet_non_magique = 'hallebarde de maître'
            valeur =  310
        if 62 <= resultat <= 64:
            nom_objet_non_magique = 'kukri de maître'
            valeur = 308
        if 65 <= resultat <= 67:
            nom_objet_non_magique = 'lance d\'arçon de maître'
            valeur = 310
        if 68 <= resultat <= 70:
            nom_objet_non_magique = 'marteau de guerrede maître'
            valeur = 312
        if 71 <= resultat <= 72:
            nom_objet_non_magique = 'marteau léger de maître'
            valeur = 301
        if 73 <= resultat <= 75:
            nom_objet_non_magique = 'marteau-piolet gnome de maître'
            valeur = 620
        if 76 <= resultat <= 77:
            nom_objet_non_magique = 'massue de maître'
            valeur = 305
        if 78 <= resultat <= 79:
            nom_objet_non_magique = 'matraque de maître'
            valeur = 301
        if 80 <= resultat <= 82:
            nom_objet_non_magique = 'morgenstern de maître'
            valeur = 308
        if 83 <= resultat <= 84:
            nom_objet_non_magique = 'pic de guerre léger de maître'
            valeur = 304
        if 85 <= resultat <= 86:
            nom_objet_non_magique = 'pic de guerre lourd de maître'
            valeur = 308
        if 87 <= resultat <= 89:
            nom_objet_non_magique = 'pique de maître'
            valeur = 305
        if 90 <= resultat <= 91:
            nom_objet_non_magique = 'sai de maître'
            valeur = 301
        if 92 <= resultat <= 93:
            nom_objet_non_magique = 'serpe de maître'
            valeur = 306
        if 94 <= resultat <= 95:
            cac = False
            nom_objet_non_magique = 'shuriken (50) de maître'
            valeur = 301
        if 96 <= resultat <= 97:
            nom_objet_non_magique = 'trident de maître'
            valeur = 315
        if 98 <= resultat <= 100:
            nom_objet_non_magique = 'urgrosh nain de maître'
            valeur = 650
    if 71 <= resultat <= 100:
        cac = False
        # arme à distance usuelle de maître p222 guide maitre
        resultat = random.randint(1, 100)
        if 1 <= resultat <= 10:
            nom_objet_non_magique = 'arbalère légère de maître'
            valeur = 335
        if 11 <= resultat <= 20:
            nom_objet_non_magique = 'arbalète lourde de maître'
            valeur = 350
        if 21 <= resultat <= 25:
            nom_objet_non_magique = 'arc court de maître'
            valeur = 330
        if 26 <= resultat <= 30:
            nom_objet_non_magique = 'arc court composite de maître(limite de For de +0)'
            valeur = 375
        if 31 <= resultat <= 35:
            nom_objet_non_magique = 'arc court composite de maître(limite de For de +1)'
            valeur = 450
        if 36 <= resultat <= 40:
            nom_objet_non_magique = 'arc court composite de maître(limite de For de +2)'
            valeur = 525
        if 41 <= resultat <= 50:
            nom_objet_non_magique = 'arc long de maître'
            valeur = 375
        if 51 <= resultat <= 55:
            nom_objet_non_magique = 'arc long composite de maître (limite de bonus de For de +0)'
            valeur = 400
        if 56 <= resultat <= 60:
            nom_objet_non_magique = 'arc long composite de maître (limite de bonus de For de +1)'
            valeur = 500
        if 61 <= resultat <= 65:
            nom_objet_non_magique = 'arc long composite de maître (limite de bonus de For de +2)'
            valeur = 600
        if 66 <= resultat <= 70:
            nom_objet_non_magique = 'arc long composite de maître (limite de bonus de For de +3)'
            valeur = 700
        if 71 <= resultat <= 75:
            nom_objet_non_magique = 'arc long composite de maître (limite de bonus de For de +4)'
            valeur = 800
        if 76 <= resultat <= 79:
            nom_objet_non_magique = 'dard de maître'
            valeur = 300
        if 80 <= resultat <= 83:
            nom_objet_non_magique = 'fronde de maître'
            valeur = 300
        if 84 <= resultat <= 88:
            nom_objet_non_magique = 'hache de lancer de maître'
            valeur = 308
        if 89 <= resultat <= 90:
            nom_objet_non_magique = 'javeline de maître'
            valeur = 301
        if 91 <= resultat <= 100:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 20:
                nom_objet_non_magique = 'billes de maître(50)'
                valeur = 350
            if 21 <= resultat <= 50:
                nom_objet_non_magique = 'carreaux de maître (50)'
                valeur = 350
            if 51 <= resultat <= 100:
                nom_objet_non_magique = 'flèches de maître (50)'
                valeur = 350
    nombre_objet_non_magique = 1
    return valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur, cac


def verif_arme_magique(alterations_cumulees, valeur_alteration, nom_enchantement, enchantements, propriete_speciale_determinee):
    if alterations_cumulees + valeur_alteration > 10 or nom_enchantement in enchantements:
        valeur_alteration = 0
        nom_enchantement = None
        propriete_speciale_determinee = propriete_speciale_determinee - 1
    return valeur_alteration, nom_enchantement, propriete_speciale_determinee


# définir les armes faibles intermédiaires et puissantes
# armes faibles
def determiner_arme_faible(valeur_objets_magiques):
    valeur_alterations_cumulees = {1: 2000, 2: 8000, 3: 18000, 4: 32000, 5: 50000,
                                   6: 72000, 7: 98000, 8: 128000, 9: 162000, 10: 200000}
    valeur = 0
    alterations_cumulees = 0
    resultat = random.randint(1, 100)
    enchantements = []
    alteration = None
    if 1 <= resultat <= 70:
        alteration = '+1'
        alterations_cumulees += 1
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 71 <= resultat <= 85:
        alteration = '+2'
        alterations_cumulees += 2
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 86 <= resultat <= 90:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_specifique_faible(valeur_objets_magiques)
    if 91 <= resultat <= 100:
        resultat = random.randint(1, 100)
        tirage = False
        while not tirage:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 70:
                alteration = '+1'
                alterations_cumulees += 1
                tirage = True
            if 71 <= resultat <= 85:
                alteration = '+2'
                alterations_cumulees += 2
                tirage = True
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        enchantements, alterations_cumulees = determiner_propriete_speciale_faible(cac, alterations_cumulees)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    valeur_objets_magiques += valeur
    if alteration:
        nom_objet_magique = f'{nom_objet_magique} {alteration} {", ".join(enchantements)}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_arme_specifique_faible(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 15:
        nom_objet_magique = 'flèche endormante'
        valeur = 132
    if 16 <= resultat <= 25:
        nom_objet_magique = 'carreau hurleur'
        valeur = 267
    if 26 <= resultat <= 45:
        nom_objet_magique = 'dague de maître en argent'
        valeur = 322
    if 46 <= resultat <= 65:
        nom_objet_magique = 'épée longue de maître en fer froid'
        valeur = 330
    if 66 <= resultat <= 75:
        nom_objet_magique = 'javeline de foudre'
        valeur = 1500
    if 76 <= resultat <= 80:
        nom_objet_magique = 'flèche mortelle'
        # definir aléatoirement flèche mortelle
        valeur = 2282
    if 81 <= resultat <= 90:
        nom_objet_magique = 'dague en adamantium'
        valeur = 3002
    if 91 <= resultat <= 100:
        nom_objet_magique = 'hache d\'armes en adamantium'
        valeur = 3010
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_propriete_speciale_faible(cac, alterations_cumulees):
    propriete_speciale_inconnue = 1
    propriete_speciale_determinee = 0
    enchantements = []
    while propriete_speciale_determinee < propriete_speciale_inconnue:
        valeur_alteration = 0
        nom_enchantement = None
        if cac:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 11:
                valeur_alteration += 1
                nom_enchantement = 'acérée'
            if 12 <= resultat <= 18:
                valeur_alteration += 1
                nom_enchantement = 'enchaînement'
            if 19 <= resultat <= 28:
                valeur_alteration += 1
                nom_enchantement = 'feu'
            if 29 <= resultat <= 32:
                valeur_alteration += 1
                nom_enchantement = 'focalisation ki'
            if 33 <= resultat <= 42:
                valeur_alteration += 1
                nom_enchantement = 'foudre'
            if 43 <= resultat <= 52:
                valeur_alteration += 1
                nom_enchantement = 'froid'
            if 53 <= resultat <= 59:
                valeur_alteration += 1
                nom_enchantement = 'gardienne'
            if 60 <= resultat <= 63:
                valeur_alteration += 1
                nom_enchantement = 'lancer'
            if 64 <= resultat <= 67:
                valeur_alteration += 1
                nom_enchantement = 'miséricordieuse'
            if 68 <= resultat <= 76:
                valeur_alteration += 1
                nom_enchantement = 'spectrale'
            if 77 <= resultat <= 81:
                valeur_alteration += 1
                nom_enchantement = 'stockage de sort'
            if 82 <= resultat <= 85:
                valeur_alteration += 1
                nom_enchantement = 'tonnerre'
            if 86 <= resultat <= 95:
                valeur_alteration += 1
                # déterminer aléatoirement tueuse
                nom_enchantement = 'tueuse'
            if 96 <= resultat <= 99:
                valeur_alteration += 1
                nom_enchantement = 'vicieuse'
            if resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        else:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 8:
                valeur_alteration += 1
                nom_enchantement = 'boomerang'
            if 9 <= resultat <= 23:
                valeur_alteration += 1
                nom_enchantement = 'feu'
            if 24 <= resultat <= 38:
                valeur_alteration += 1
                nom_enchantement = 'foudre'
            if 39 <= resultat <= 53:
                valeur_alteration += 1
                nom_enchantement = 'froid'
            if 54 <= resultat <= 66:
                valeur_alteration += 1
                nom_enchantement = 'longue portée'
            if 67 <= resultat <= 71:
                valeur_alteration += 1
                nom_enchantement = 'miséricordieuse'
            if 72 <= resultat <= 77:
                valeur_alteration += 1
                nom_enchantement = 'tonnerre'
            if 78 <= resultat <= 87:
                valeur_alteration += 1
                nom_enchantement = 'traqueuse'
            if 88 <= resultat <= 99:
                valeur_alteration += 1
                # determiner tueuse
                nom_enchantement = 'tueuse'
            if resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        propriete_speciale_determinee += 1
        valeur_alteration, nom_enchantement, propriete_speciale_determinee = verif_arme_magique(alterations_cumulees,
                                                                                                valeur_alteration,
                                                                                                nom_enchantement,
                                                                                                enchantements,
                                                                                                propriete_speciale_determinee)
        if nom_enchantement is not None:
            enchantements.append(nom_enchantement)
        alterations_cumulees += valeur_alteration
    return enchantements, alterations_cumulees


# armes intermédiaires
def determiner_arme_intermediaire(valeur_objets_magiques):
    valeur_alterations_cumulees = {1: 2000, 2: 8000, 3: 18000, 4: 32000, 5: 50000,
                                   6: 72000, 7: 98000, 8: 128000, 9: 162000, 10: 200000}
    enchantements = []
    valeur = 0
    alterations_cumulees = 0
    alteration = None
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 10:
        alteration = '+1'
        alterations_cumulees += 1
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 11 <= resultat <= 29:
        alteration = '+2'
        alterations_cumulees += 2
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 30 <= resultat <= 58:
        alteration = '+3'
        alterations_cumulees += 3
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 59 <= resultat <= 62:
        alteration = '+4'
        alterations_cumulees += 4
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 63 <= resultat <= 68:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_specifique_intermediaire(valeur_objets_magiques)
    if 69 <= resultat <= 100:
        resultat = random.randint(1, 100)
        tirage = False
        while not tirage:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 10:
                alteration = '+1'
                alterations_cumulees += 1
                tirage = True
            if 11 <= resultat <= 29:
                alteration = '+2'
                alterations_cumulees += 2
                tirage = True
            if 30 <= resultat <= 58:
                alteration = '+3'
                alterations_cumulees += 3
                tirage = True
            if 59 <= resultat <= 62:
                alteration = '+4'
                alterations_cumulees += 4
                tirage = True
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        enchantements,alterations_cumulees = determiner_propriete_speciale_intermediaire(cac, alterations_cumulees)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    valeur_objets_magiques += valeur
    if alteration:
        nom_objet_magique = f'{nom_objet_magique} {alteration} {", ".join(enchantements)}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_arme_specifique_intermediaire(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 9:
        nom_objet_magique = 'javeline de foudre'
        valeur = 1500
    if 10 <= resultat <= 15:
        nom_objet_magique = 'flèche mortelle'
        # definir aléatoirement flèche mortelle
        valeur = 2282
    if 16 <= resultat <= 24:
        nom_objet_magique = 'dague en adamantium'
        valeur = 3002
    if 25 <= resultat <= 33:
        nom_objet_magique = 'hache d\'armes en adamantium'
        valeur = 3010
    if 34 <= resultat <= 37:
        nom_objet_magique = 'grande flèche mortelle'
        # definir comme pour flèche mortelle
        valeur = 4057
    if 38 <= resultat <= 40:
        nom_objet_magique = 'brise-arme'
        valeur = 4315
    if 41 <= resultat <= 46:
        nom_objet_magique = 'Dague venimeuse'
        valeur = 8302
    if 47 <= resultat <= 51:
        nom_objet_magique = 'trident d\'alerte'
        valeur = 10115
    if 52 <= resultat <= 56:
        nom_objet_magique = 'regret du changeant'
        valeur = 12780
    if 57 <= resultat <= 62:
        nom_objet_magique = 'dague de l\'assassin'
        valeur = 18650
    if 63 <= resultat <= 66:
        nom_objet_magique = 'trident de domination aquatique'
        valeur = 18650
    if 67 <= resultat <= 74:
        nom_objet_magique = 'épée ardente'
        valeur = 20715
    if 75 <= resultat <= 79:
        nom_objet_magique = 'épée de bonne fortune (0 souhait)'
        valeur = 22060
    if 80 <= resultat <= 86:
        nom_objet_magique = 'épée de précision'
        valeur = 22310
    if 87 <= resultat <= 91:
        nom_objet_magique = 'épée des plans'
        valeur = 22315
    if 92 <= resultat <= 95:
        nom_objet_magique = 'épée des neuf vies'
        valeur = 23057
    if 96 <= resultat <= 97:
        nom_objet_magique = 'arc du long serment'
        valeur = 25600
    if 98 <= resultat <= 100:
        nom_objet_magique = 'épée voleuse de vie'
        valeur = 25715
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_propriete_speciale_intermediaire(cac, alterations_cumulees):
    propriete_speciale_inconnue = 1
    propriete_speciale_determinee = 0
    enchantements = []
    while propriete_speciale_determinee < propriete_speciale_inconnue:
        valeur_alteration = 0
        nom_enchantement = None
        if cac:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 6:
                valeur_alteration += 1
                nom_enchantement = 'acérée'
            if 7 <= resultat <= 10:
                valeur_alteration += 1
                nom_enchantement = 'enchaînement'
            if 11 <= resultat <= 17:
                valeur_alteration += 1
                nom_enchantement = 'feu'
            if 18 <= resultat <= 21:
                valeur_alteration += 1
                nom_enchantement = 'focalisation ki'
            if 22 <= resultat <= 28:
                valeur_alteration += 1
                nom_enchantement = 'foudre'
            if 29 <= resultat <= 35:
                valeur_alteration += 1
                nom_enchantement = 'froid'
            if 36 <= resultat <= 41:
                valeur_alteration += 1
                nom_enchantement = 'gardienne'
            if 42 <= resultat <= 45:
                valeur_alteration += 1
                nom_enchantement = 'lancer'
            if 46 <= resultat <= 47:
                valeur_alteration += 1
                nom_enchantement = 'miséricordieuse'
            if 48 <= resultat <= 52:
                valeur_alteration += 1
                nom_enchantement = 'spectrale'
            if 53 <= resultat <= 57:
                valeur_alteration += 1
                nom_enchantement = 'stockage de sort'
            if 58 <= resultat <= 59:
                valeur_alteration += 1
                nom_enchantement = 'tonnerre'
            if 60 <= resultat <= 65:
                valeur_alteration += 1
                # déterminer aléatoirement tueuse
                nom_enchantement = 'tueuse'
            if 66 <= resultat <= 69:
                valeur_alteration += 1
                nom_enchantement = 'vicieuse'
            if 70 <= resultat <= 72:
                valeur_alteration += 2
                nom_enchantement = 'anarchique'
            if 73 <= resultat <= 75:
                valeur_alteration += 2
                nom_enchantement = 'axiomatique'
            if 76 <= resultat <= 78:
                valeur_alteration += 2
                nom_enchantement = 'destruction'
            if 79 <= resultat <= 81:
                valeur_alteration += 2
                nom_enchantement = 'feu intense'
            if 82 <= resultat <= 84:
                valeur_alteration += 2
                nom_enchantement = 'foudre intense'
            if 85 <= resultat <= 97:
                valeur_alteration += 2
                nom_enchantement = 'froid intense'
            if 88 <= resultat <= 90:
                valeur_alteration += 2
                nom_enchantement = 'impie'
            if 91 <= resultat <= 93:
                valeur_alteration += 2
                nom_enchantement = 'sainte'
            if 94 <= resultat <= 95:
                valeur_alteration += 2
                nom_enchantement = 'sanglante'
            if 96 <= resultat <= 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        else:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 5:
                valeur_alteration += 1
                nom_enchantement = 'boomerang'
            if 6 <= resultat <= 17:
                valeur_alteration += 1
                nom_enchantement = 'feu'
            if 18 <= resultat <= 29:
                valeur_alteration += 1
                nom_enchantement = 'foudre'
            if 30 <= resultat <= 41:
                valeur_alteration += 1
                nom_enchantement = 'froid'
            if 42 <= resultat <= 49:
                valeur_alteration += 1
                nom_enchantement = 'longue portée'
            if 50 <= resultat <= 51:
                valeur_alteration += 1
                nom_enchantement = 'miséricordieuse'
            if 52 <= resultat <= 55:
                valeur_alteration += 1
                nom_enchantement = 'tonnerre'
            if 56 <= resultat <= 60:
                valeur_alteration += 1
                nom_enchantement = 'traqueuse'
            if 61 <= resultat <= 68:
                valeur_alteration += 1
                # determiner tueuse
                nom_enchantement = 'tueuse'
                valeur_alteration += 1
            if 69 <= resultat <= 71:
                nom_enchantement = 'anarchique'
                valeur_alteration += 2
            if 72 <= resultat <= 74:
                nom_enchantement = 'axiomatique'
                valeur_alteration += 2
            if 75 <= resultat <= 79:
                nom_enchantement = 'feu intense'
                valeur_alteration += 2
            if 80 <= resultat <= 84:
                nom_enchantement = 'foudre intense'
                valeur_alteration += 2
            if 85 <= resultat <= 89:
                nom_enchantement = 'froid intense'
                valeur_alteration += 2
            if 90 <= resultat <= 92:
                nom_enchantement = 'impie'
                valeur_alteration += 2
            if 93 <= resultat <= 95:
                nom_enchantement = 'sainte'
                valeur_alteration += 2
            if 96 <= resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        propriete_speciale_determinee += 1
        valeur_alteration, nom_enchantement, propriete_speciale_determinee = verif_arme_magique(alterations_cumulees,
                                                                                                valeur_alteration,
                                                                                                nom_enchantement,
                                                                                                enchantements,
                                                                                                propriete_speciale_determinee)
        if nom_enchantement is not None:
            enchantements.append(nom_enchantement)
        alterations_cumulees += valeur_alteration
    return enchantements, alterations_cumulees


# armes puissante
def determiner_arme_puissante(valeur_objets_magiques):
    valeur_alterations_cumulees = {1: 2000, 2: 8000, 3: 18000, 4: 32000, 5: 50000,
                                   6: 72000, 7: 98000, 8: 128000, 9: 162000, 10: 200000}
    enchantements = []
    alteration = None
    valeur = 0
    alterations_cumulees = 0
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 20:
        alteration = '+3'
        alterations_cumulees += 3
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 21 <= resultat <= 38:
        alteration = '+4'
        alterations_cumulees += 4
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 39 <= resultat <= 49:
        alteration = '+5'
        alterations_cumulees += 5
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 50 <= resultat <= 63:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_arme_specifique_puissante(valeur_objets_magiques)
    if 64 <= resultat <= 100:
        resultat = random.randint(1, 100)
        tirage = False
        while not tirage:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 20:
                alteration = '+3'
                alterations_cumulees += 3
                tirage = True
            if 21 <= resultat <= 38:
                alteration = '+4'
                alterations_cumulees += 4
                tirage = True
            if 39 <= resultat <= 49:
                alteration = '+5'
                alterations_cumulees += 5
                tirage = True
        valeur_objets_magiques, nombre_objet_magique, nom_objet_magique, valeur, cac = tirer_arme(
            valeur_objets_magiques)
        enchantements, alterations_cumulees = determiner_propriete_speciale_puissante(cac, alterations_cumulees)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    valeur_objets_magiques += valeur
    if alteration:
        nom_objet_magique = f'{nom_objet_magique} {alteration} {", ".join(enchantements)}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_arme_specifique_puissante(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_objet_magique = 'regret du changeant'
        valeur = 12780
    if 4 <= resultat <= 7:
        nom_objet_magique = 'dague de l\'assassin'
        valeur = 18650
    if 8 <= resultat <= 9:
        nom_objet_magique = 'trident de domination aquatique'
        valeur = 18650
    if 10 <= resultat <= 13:
        nom_objet_magique = 'épée ardente'
        valeur = 20715
    if 14 <= resultat <= 17:
        nom_objet_magique = 'épée de bonne fortune (0 souhait)'
        valeur = 22060
    if 18 <= resultat <= 24:
        nom_objet_magique = 'épée de précision'
        valeur = 22310
    if 25 <= resultat <= 31:
        nom_objet_magique = 'épée des plans'
        valeur = 22315
    if 32 <= resultat <= 37:
        nom_objet_magique = 'épée des neuf vies'
        valeur = 23057
    if 38 <= resultat <= 41:
        nom_objet_magique = 'arc du long serment'
        valeur = 25600
    if 42 <= resultat <= 46:
        nom_objet_magique = 'épée voleuse de vie'
        valeur = 25715
    if 47 <= resultat <= 51:
        nom_objet_magique = 'masse d\'épouvante'
        valeur = 38552
    if 52<= resultat <= 57:
        nom_objet_magique = 'hache dévitalisante'
        valeur = 40320
    if 58 <= resultat <= 62:
        nom_objet_magique = 'cimeterre des bois'
        valeur = 47315
    if 63 <= resultat <= 67:
        nom_objet_magique = 'rapière d\'anémie'
        valeur = 50320
    if 68 <= resultat <= 73:
        nom_objet_magique = 'épée radieuse'
        valeur = 50335
    if 74 <= resultat <= 79:
        nom_objet_magique = 'épée de givre'
        valeur = 54475
    if 80 <= resultat <= 84:
        nom_objet_magique = 'marteau de lancer nain'
        valeur = 60312
    if 85 <= resultat <= 91:
        nom_objet_magique = 'épée de bonne fortune (1 souhait)'
        valeur = 62360
    if 92 <= resultat <= 95:
        nom_objet_magique = 'masse de démolition'
        valeur = 75312
    if 96 <= resultat <= 97:
        nom_objet_magique = 'épée de bonne fortune (2 souhaits)'
        valeur = 102660
    if 98 <= resultat <= 99:
        nom_objet_magique = 'épée de justice'
        valeur = 120630
    if resultat == 100:
        nom_objet_magique = 'épée de bonne fortune (3 souhaits)'
        valeur = 142960
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_propriete_speciale_puissante(cac, alterations_cumulees):
    propriete_speciale_inconnue = 1
    propriete_speciale_determinee = 0
    enchantements = []
    while propriete_speciale_determinee < propriete_speciale_inconnue:
        valeur_alteration = 0
        nom_enchantement = None
        if cac:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 2:
                valeur_alteration += 1
                nom_enchantement = 'enchaînement'
            if 3 <= resultat <= 5:
                valeur_alteration += 1
                nom_enchantement = 'feu'
            if 6 <= resultat <= 9:
                valeur_alteration += 1
                nom_enchantement = 'focalisation ki'
            if 10 <= resultat <= 12:
                valeur_alteration += 1
                nom_enchantement = 'foudre'
            if 13 <= resultat <= 15:
                valeur_alteration += 1
                nom_enchantement = 'froid'
            if 16 <= resultat <= 19:
                valeur_alteration += 1
                nom_enchantement = 'lancer'
            if 20 <= resultat <= 22:
                valeur_alteration += 1
                nom_enchantement = 'spectrale'
            if 23 <= resultat <= 25:
                valeur_alteration += 1
                nom_enchantement = 'stockage de sort'
            if 26 <= resultat <= 29:
                valeur_alteration += 1
                nom_enchantement = 'tonnerre'
            if 30 <= resultat <= 32:
                valeur_alteration += 1
                # déterminer aléatoirement tueuse
                nom_enchantement = 'tueuse'
            if 33 <= resultat <= 36:
                valeur_alteration += 1
                nom_enchantement = 'vicieuse'
            if 37 <= resultat <= 41:
                valeur_alteration += 2
                nom_enchantement = 'anarchique'
            if 42 <= resultat <= 46:
                valeur_alteration += 2
                nom_enchantement = 'axiomatique'
            if 47 <= resultat <= 49:
                valeur_alteration += 2
                nom_enchantement = 'destruction'
            if 50 <= resultat <= 54:
                valeur_alteration += 2
                nom_enchantement = 'feu intense'
            if 55 <= resultat <= 59:
                valeur_alteration += 2
                nom_enchantement = 'foudre intense'
            if 60 <= resultat <= 64:
                valeur_alteration += 2
                nom_enchantement = 'froid intense'
            if 65 <= resultat <= 69:
                valeur_alteration += 2
                nom_enchantement = 'impie'
            if 70 <= resultat <= 74:
                valeur_alteration += 2
                nom_enchantement = 'sainte'
            if 75 <= resultat <= 78:
                valeur_alteration += 2
                nom_enchantement = 'sanglante'
            if 79 <= resultat <= 83:
                valeur_alteration += 3
                nom_enchantement = 'rapidité'
            if 84 <= resultat <= 85:
                valeur_alteration += 4
                nom_enchantement = 'dansante'
            if 86 <= resultat <= 88:
                valeur_alteration += 4
                nom_enchantement = 'lumière'
            if 89 <= resultat <= 90:
                valeur_alteration += 5
                nom_enchantement = 'vorpale'
            if 91 <= resultat <= 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        else:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 5:
                valeur_alteration += 1
                nom_enchantement = 'boomerang'
            if 6 <= resultat <= 9:
                valeur_alteration += 1
                nom_enchantement = 'feu'
            if 10 <= resultat <= 13:
                valeur_alteration += 1
                nom_enchantement = 'foudre'
            if 14 <= resultat <= 17:
                valeur_alteration += 1
                nom_enchantement = 'froid'
            if 18 <= resultat <= 21:
                valeur_alteration += 1
                nom_enchantement = 'longue portée'
            if 22 <= resultat <= 23:
                valeur_alteration += 1
                nom_enchantement = 'tonnerre'
            if 24 <= resultat <= 25:
                valeur_alteration += 1
                nom_enchantement = 'traqueuse'
            if 26 <= resultat <= 29:
                valeur_alteration += 1
                # determiner tueuse
                nom_enchantement = 'tueuse'
            if 30 <= resultat <= 34:
                valeur_alteration += 2
                nom_enchantement = 'anarchique'
                valeur_alteration += 2
            if 35 <= resultat <= 39:
                nom_enchantement = 'axiomatique'
                valeur_alteration += 2
            if 40 <= resultat <= 49:
                nom_enchantement = 'feu intense'
                valeur_alteration += 2
            if 50 <= resultat <= 59:
                nom_enchantement = 'foudre intense'
                valeur_alteration += 2
            if 60 <= resultat <= 69:
                nom_enchantement = 'froid intense'
                valeur_alteration += 2
            if 70 <= resultat <= 74:
                nom_enchantement = 'impie'
                valeur_alteration += 2
            if 75 <= resultat <= 79:
                nom_enchantement = 'sainte'
                valeur_alteration += 2
            if 80 <= resultat <= 84:
                nom_enchantement = 'rapidité'
                valeur_alteration += 3
            if 85 <= resultat <= 90:
                nom_enchantement = 'lumière'
                valeur_alteration += 4
            if 91 <= resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        propriete_speciale_determinee += 1
        valeur_alteration, nom_enchantement, propriete_speciale_determinee = verif_arme_magique(alterations_cumulees,
                                                                                                valeur_alteration,
                                                                                                nom_enchantement,
                                                                                                enchantements,
                                                                                                propriete_speciale_determinee)
        if nom_enchantement is not None:
            enchantements.append(nom_enchantement)
        alterations_cumulees += valeur_alteration
    return enchantements, alterations_cumulees
