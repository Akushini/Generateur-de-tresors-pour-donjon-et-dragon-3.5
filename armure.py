import random


def tirer_armure(valeur_objets_non_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 12:
        nom_objet_non_magique = 'chemise de mailles'
        valeur = 100
    if 13 <= resultat <= 18:
        nom_objet_non_magique = 'armure de cuir cloutée de maître'
        valeur = 175
    if 19 <= resultat <= 26:
        nom_objet_non_magique = 'cuirasse'
        valeur = 200
    if 27 <= resultat <= 34:
        nom_objet_non_magique = 'crevice'
        valeur = 250
    if 35 <= resultat <= 54:
        nom_objet_non_magique = 'armure à plaques'
        valeur = 600
    if 55 <= resultat <= 80:
        nom_objet_non_magique = 'harnois'
        valeur = 1500
    if 81 <= resultat <= 90:
        resultat = random.randint(1,100)
        if 1 <= resultat <= 50:
            nom_objet_non_magique = 'rondache en ébénite'
            valeur = 203
        if 51 <= resultat <= 100:
            nom_objet_non_magique = 'écu en ébénite'
            valeur = 257
    if 91 <= resultat <= 100:
        resultat = random.randint(1,100)
        if 1 <= resultat <= 17:
            nom_objet_non_magique = 'targe de maître'
            valeur = 165
        if 18 <= resultat <= 40:
            nom_objet_non_magique = 'rondache en bois de maître'
            valeur = 153
        if 41 <= resultat <= 60:
            nom_objet_non_magique = 'rondache en acier de maître'
            valeur = 159
        if 61 <= resultat <= 83:
            nom_objet_non_magique = 'écu en bois de maître'
            valeur = 157
        if 84 <= resultat <= 100:
            nom_objet_non_magique = 'écu en acier de maître'
            valeur = 170
    valeur_objets_non_magiques += valeur
    nombre_objet_non_magique = 1
    return valeur_objets_non_magiques, nombre_objet_non_magique, nom_objet_non_magique, valeur


# définir les armures et boucliers faibles intermédiaires et puissantes
def determiner_bouclier(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 65:
        nom_objet_magique = 'écu en acier'
        valeur = 270
    if 66 <= resultat <= 75:
        nom_objet_magique = 'écu en bois'
        valeur = 157
    if 76 <= resultat <= 80:
        nom_objet_magique = 'pavois'
        valeur = 180
    if 81 <= resultat <= 85:
        nom_objet_magique = 'rondache en acier'
        valeur = 159
    if 86 <= resultat <= 90:
        nom_objet_magique = 'rondache en bois'
        valeur = 153
    if 91 <= resultat <= 100:
        nom_objet_magique = 'targe'
        valeur = 165
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_armure(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if resultat == 1:
        nom_objet_magique = 'armure d\'écailles'
        valeur = 200
    if resultat == 2:
        nom_objet_magique = 'armure de cuir'
        valeur = 160
    if 3 <= resultat <= 17:
        nom_objet_magique = 'armure de cuir clouté'
        valeur = 175
    if 18 <= resultat <= 27:
        nom_objet_magique = 'armure de peau'
        valeur = 165
    if resultat == 28:
        nom_objet_magique = 'armure matelassée'
        valeur = 155
    if 29 <= resultat <= 43:
        nom_objet_magique = 'chemise de mailles'
        valeur = 250
    if resultat == 44:
        nom_objet_magique = 'clibanion'
        valeur = 350
    if resultat == 45:
        nom_objet_magique = 'chotte de mailles'
        valeur = 300
    if resultat == 46:
        nom_objet_magique = 'crevice'
        valeur = 400
    if 47 <= resultat <= 59:
        nom_objet_magique = 'cuirasse'
        valeur = 350
    if 60 <= resultat <= 99:
        nom_objet_magique = 'harnois'
        valeur = 1650
    if resultat == 100:
        nom_objet_magique = 'plaques'
        valeur = 750
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


# armes et boucliers faibles
def determiner_armure_bouclier_faible(valeur_objets_magiques):
    valeur_alterations_cumulees = {1: 1000, 2: 4000, 3: 9000, 4: 16000, 5: 25000,
                                   6: 36000, 7: 49000, 8: 64000, 9: 81000, 10: 100000}
    valeur = 0
    enchantements = []
    valeur_cumulee = 0
    alterations_cumulees = 0
    alteration = None
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 60:
        alteration = '+1'
        alterations_cumulees += 1
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 61 <= resultat <= 80:
        alteration = '+1'
        alterations_cumulees += 1
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 81 <= resultat <= 85:
        alteration = '+2'
        alterations_cumulees += 2
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 86 <= resultat <= 87:
        alteration = '+2'
        alterations_cumulees += 2
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 88 <= resultat <= 89:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure_specifique_faible(valeur_objets_magiques)
    if 90 <= resultat <= 91:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier_specifique_faible(valeur_objets_magiques)
    if 92 <= resultat <= 100:
        resultat = random.randint(1, 2)
        if resultat == 1:
            resultat = random.randint(1, 100)
            tirage = False
            while not tirage:
                resultat = random.randint(1, 100)
                if 1 <= resultat <= 79:
                    tirage = False
                if 61 <= resultat <= 80:
                    alteration = '+1'
                    alterations_cumulees += 1
                    tirage = True
                if 81 <= resultat <= 85:
                    tirage = False
                if 86 <= resultat <= 87:
                    alteration = '+2'
                    alterations_cumulees += 2
                    tirage = True
                if 88 <= resultat <= 100:
                    tirage = False
            nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(valeur_objets_magiques)
            armure = True
            enchantements, alterations_cumulees, valeur = determiner_propriete_speciale_bouclier_armure_faible(alterations_cumulees, armure, valeur)
            valeur_cumulee += valeur
            valeur_cumulee += valeur_alterations_cumulees[alterations_cumulees]
            valeur = valeur_cumulee
        if resultat == 2:
            resultat = random.randint(1, 100)
            tirage = False
            while not tirage:
                resultat = random.randint(1, 100)
                if 1 <= resultat <= 60:
                    alteration = '+1'
                    alterations_cumulees += 1
                    tirage = True
                if 61 <= resultat <= 80:
                    tirage = False
                if 81 <= resultat <= 85:
                    alteration = '+2'
                    alterations_cumulees += 2
                    tirage = True
                if 86 <= resultat <= 100:
                    tirage = False
            nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(valeur_objets_magiques)
            armure = False
            enchantements, alterations_cumulees, valeur = determiner_propriete_speciale_bouclier_armure_faible(alterations_cumulees, armure, valeur)
            valeur_cumulee += valeur
            valeur_cumulee += valeur_alterations_cumulees[alterations_cumulees]
            valeur = valeur_cumulee
    valeur_objets_magiques += valeur
    if alteration:
        nom_objet_magique = f'{nom_objet_magique} {alteration} {", ".join(enchantements)}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_armure_specifique_faible(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 50:
        nom_objet_magique = 'chemise de mailles en mithral'
        valeur = 1100
    if 51 <= resultat <= 80:
        nom_objet_magique = 'harnois en peau de dragon'
        valeur = 3300
    if 81 <= resultat <= 100:
        nom_objet_magique = 'cotte de mailles elfique'
        valeur = 4150
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_bouclier_specifique_faible(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 30:
        nom_objet_magique = 'rondache en ébénite'
        valeur = 203
    if 31 <= resultat <= 80:
        nom_objet_magique = 'écu en ébénite'
        valeur = 257
    if 81 <= resultat <= 95:
        nom_objet_magique = 'écu en mithral'
        valeur = 1020
    if 96 <= resultat <= 100:
        nom_objet_magique = 'bouclier des arcanes'
        valeur = 3153
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_propriete_speciale_bouclier_armure_faible(alterations_cumulees, armure, valeur):
    propriete_speciale_inconnue = 1
    propriete_speciale_determinee = 0
    enchantements = []
    while propriete_speciale_determinee < propriete_speciale_inconnue:
        valeur_alteration = 0
        valeur_enchantement = 0
        nom_enchantement = None
        if armure:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 25:
                nom_enchantement = 'mimétisme'
                valeur_enchantement = 2700
            if 26 <= resultat <= 32:
                valeur_alteration += 1
                nom_enchantement = 'défense légère'
            if 33 <= resultat <= 52:
                nom_enchantement = 'déplacement furtif'
                valeur_enchantement = 3750
            if 53 <= resultat <= 72:
                nom_enchantement = 'graisseuse'
                valeur_enchantement = 3750
            if 73 <= resultat <= 93:
                nom_enchantement = 'ombre'
                valeur_enchantement = 3750
            if 94 <= resultat <= 96:
                valeur_alteration += 2
                nom_enchantement = 'résistance à la magie (13)'
            if resultat == 97:
                nom_enchantement = 'déplacement furtif supérieur'
                valeur_enchantement = 15000
            if resultat == 98:
                nom_enchantement = 'graisseuse supérieure'
                valeur_enchantement = 15000
            if resultat == 99:
                nom_enchantement = 'ombre supérieure'
                valeur_enchantement += 15000
            if resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        else:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 20:
                valeur_alteration += 1
                nom_enchantement = 'attaque'
            if 21 <= resultat <= 30:
                valeur_alteration += 1
                nom_enchantement = 'aveuglant'
            if 31 <= resultat <= 55:
                valeur_alteration += 1
                nom_enchantement = 'défense légère'
            if 56 <= resultat <= 75:
                valeur_alteration += 1
                nom_enchantement = 'interception de projectiles'
            if 76 <= resultat <= 80:
                valeur_alteration += 2
                nom_enchantement = 'animé'
            if 81 <= resultat <= 97:
                valeur_alteration += 2
                nom_enchantement = 'antiprojectiles'
            if 98 <= resultat <= 99:
                valeur_alteration += 2
                nom_enchantement = 'résistance à la magie (13)'
            if resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        propriete_speciale_determinee += 1
        valeur_alteration, nom_enchantement, valeur_enchantement, propriete_speciale_determinee = verif_alteration(
            alterations_cumulees, enchantements, propriete_speciale_determinee, nom_enchantement, valeur_alteration,
            valeur_enchantement)
        alterations_cumulees += valeur_alteration
        valeur += valeur_enchantement
        if nom_enchantement is not None:
            enchantements.append(nom_enchantement)
    return enchantements, alterations_cumulees, valeur


# armures et boucliers intermédiaires
def determiner_armure_bouclier_intermediaire(valeur_objets_magiques):
    valeur_alterations_cumulees = {1: 1000, 2: 4000, 3: 9000, 4: 16000, 5: 25000,
                                   6: 36000, 7: 49000, 8: 64000, 9: 81000, 10: 100000}
    valeur = 0
    enchantements = []
    valeur_cumulee = 0
    alterations_cumulees = 0
    alteration = None
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 5:
        alteration = '+1'
        alterations_cumulees += 1
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 6 <= resultat <= 10:
        alteration = '+1'
        alterations_cumulees += 1
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 11 <= resultat <= 20:
        alteration = '+2'
        alterations_cumulees += 2
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 21 <= resultat <= 30:
        alteration = '+2'
        alterations_cumulees += 2
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 31 <= resultat <= 40:
        alteration = '+3'
        alterations_cumulees += 3
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 41 <= resultat <= 50:
        alteration = '+3'
        alterations_cumulees += 3
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 51 <= resultat <= 55:
        alteration = '+4'
        alterations_cumulees += 4
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 56 <= resultat <= 57:
        alteration = '+4'
        alterations_cumulees += 4
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 58 <= resultat <= 60:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure_specifique_intermediaire(
            valeur_objets_magiques)
    if 61 <= resultat <= 63:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier_specifique_intermediaire(
            valeur_objets_magiques)
    if 64 <= resultat <= 100:
        resultat = random.randint(1, 2)
        if resultat == 1:
            resultat = random.randint(1, 100)
            tirage = False
            while not tirage:
                resultat = random.randint(1, 100)
                if 1 <= resultat <= 5:
                    tirage = False
                if 6 <= resultat <= 10:
                    alteration = '+1'
                    alterations_cumulees += 1
                    tirage = True
                if 11 <= resultat <= 20:
                    tirage = False
                if 21 <= resultat <= 30:
                    alteration = '+2'
                    alterations_cumulees += 2
                    tirage = True
                if 31 <= resultat <= 40:
                    tirage = False
                if 41 <= resultat <= 50:
                    alteration = '+3'
                    alterations_cumulees += 3
                    tirage = True
                if 51 <= resultat <= 55:
                    tirage = False
                if 56 <= resultat <= 57:
                    alteration = '+4'
                    alterations_cumulees += 4
                    tirage = True
                if 58 <= resultat <= 100:
                    tirage = False
            nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
                valeur_objets_magiques)
            armure = True
            enchantements, alterations_cumulees, valeur = determiner_propriete_speciale_bouclier_armure_intermediaire(alterations_cumulees, armure, valeur)
            valeur_cumulee += valeur
            valeur_cumulee += valeur_alterations_cumulees[alterations_cumulees]
            valeur = valeur_cumulee
        if resultat == 2:
            tirage = False
            while not tirage:
                resultat = random.randint(1, 100)
                if 1 <= resultat <= 5:
                    alteration = '+1'
                    alterations_cumulees += 1
                    tirage = True
                if 11 <= resultat <= 20:
                    alteration = '+2'
                    alterations_cumulees += 2
                    tirage = True
                if 31 <= resultat <= 40:
                    alteration = '+3'
                    alterations_cumulees += 3
                    tirage = True
                if 51 <= resultat <= 55:
                    alteration = '+4'
                    alterations_cumulees += 4
                    tirage = True
            nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
                valeur_objets_magiques)
            armure = False
            enchantements, alterations_cumulees, valeur = determiner_propriete_speciale_bouclier_armure_intermediaire(
                alterations_cumulees, armure, valeur)
            valeur_cumulee += valeur_alterations_cumulees[alterations_cumulees]
            valeur_cumulee += valeur
            valeur = valeur_cumulee
    valeur_objets_magiques += valeur
    if alteration:
        nom_objet_magique = f'{nom_objet_magique} {alteration} {", ".join(enchantements)}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_armure_specifique_intermediaire(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 25:
        nom_objet_magique = 'chemise de mailles en mithral'
        valeur = 1100
    if 26 <= resultat <= 45:
        nom_objet_magique = 'harnois en peau de dragon'
        valeur = 3300
    if 46 <= resultat <= 57:
        nom_objet_magique = 'cotte de mailles elfique'
        valeur = 4150
    if 58 <= resultat <= 67:
        nom_objet_magique = 'armure en peau de rhinocéros'
        valeur = 5165
    if 68 <= resultat <= 82:
        nom_objet_magique = 'cuirasse en adamantium'
        valeur = 10200
    if 83 <= resultat <= 97:
        nom_objet_magique = 'harnois nain'
        valeur = 16500
    if 98 <= resultat <= 100:
        nom_objet_magique = 'crevice de la seconde chance'
        valeur = 18900
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_bouclier_specifique_intermediaire(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 20:
        nom_objet_magique = 'rondache en ébénite'
        valeur = 203
    if 21 <= resultat <= 45:
        nom_objet_magique = 'écu en ébénite'
        valeur = 257
    if 46 <= resultat <= 70:
        nom_objet_magique = 'écu en mithral'
        valeur = 1020
    if 71 <= resultat <= 85:
        nom_objet_magique = 'bouclier des arcanes'
        valeur = 3153
    if 86 <= resultat <= 90:
        nom_objet_magique = 'bouclier de la manticore'
        valeur = 5580
    if 91 <= resultat <= 95:
        nom_objet_magique = 'bouclier du lion'
        valeur = 9170
    if 96 <= resultat <= 100:
        nom_objet_magique = 'bouclier ailé'
        valeur = 17257
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_propriete_speciale_bouclier_armure_intermediaire(alterations_cumulees, armure, valeur):
    propriete_speciale_inconnue = 1
    propriete_speciale_determinee = 0
    enchantements = []
    while propriete_speciale_determinee < propriete_speciale_inconnue:
        valeur_alteration = 0
        valeur_enchantement = 0
        nom_enchantement = None
        if armure:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 5:
                nom_enchantement = 'mimétisme'
                valeur_enchantement = 2700
            if 6 <= resultat <= 8:
                valeur_alteration += 1
                nom_enchantement = 'défense légère'
            if 9 <= resultat <= 11:
                nom_enchantement = 'déplacement furtif'
                valeur_enchantement = 3750
            if 12 <= resultat <= 14:
                nom_enchantement = 'graisseuse'
                valeur_enchantement = 3750
            if 15 <= resultat <= 17:
                nom_enchantement = 'ombre'
                valeur_enchantement = 3750
            if 18 <= resultat <= 19:
                valeur_alteration += 2
                nom_enchantement = 'résistance à la magie (13)'
            if 20 <= resultat <= 29:
                nom_enchantement = 'déplacement furtif supérieur'
                valeur_enchantement = 15000
            if 30 <= resultat <= 39:
                nom_enchantement = 'graisseuse supérieure'
                valeur_enchantement = 15000
            if 40 <= resultat <= 49:
                nom_enchantement = 'ombre supérieure'
                valeur_enchantement = 15000
            if 50 <= resultat <= 54:
                nom_enchantement = 'résistance à l\'acide'
                valeur_enchantement = 18000
            if 55 <= resultat <= 59:
                nom_enchantement = 'résistance à l\'électricité'
                valeur_enchantement = 18000
            if 60 <= resultat <= 64:
                nom_enchantement = 'résistance au feu'
                valeur_enchantement = 18000
            if 65 <= resultat <= 69:
                nom_enchantement = 'résistance au froid'
                valeur_enchantement = 18000
            if 70 <= resultat <= 74:
                nom_enchantement = 'résistance au son'
                valeur_enchantement = 18000
            if 75 <= resultat <= 79:
                valeur_alteration += 3
                nom_enchantement = 'défense intermédiaire'
            if 80 <= resultat <= 84:
                valeur_alteration += 3
                nom_enchantement = 'forme animale'
            if 85 <= resultat <= 89:
                valeur_alteration += 3
                nom_enchantement = 'invulnérabilité'
            if 90 <= resultat <= 94:
                valeur_alteration += 3
                nom_enchantement = 'résistance à la magie (15)'
            if 95 <= resultat <= 99:
                valeur_alteration += 3
                nom_enchantement = 'spectrale'
            if resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        else:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 10:
                valeur_alteration += 1
                nom_enchantement = 'attaque'
            if 11 <= resultat <= 15:
                valeur_alteration += 1
                nom_enchantement = 'aveuglant'
            if 16 <= resultat <= 30:
                valeur_alteration += 1
                nom_enchantement = 'défense légère'
            if 31 <= resultat <= 40:
                valeur_alteration += 1
                nom_enchantement = 'interception de projectiles'
            if 41 <= resultat <= 47:
                valeur_alteration += 2
                nom_enchantement = 'animé'
            if 48 <= resultat <= 57:
                valeur_alteration += 2
                nom_enchantement = 'antiprojectiles'
            if 58 <= resultat <= 59:
                valeur_alteration += 2
                nom_enchantement = 'résistance à la magie (13)'
            if 60 <= resultat <= 63:
                nom_enchantement = 'résistance à l\'acide'
                valeur_enchantement = 18000
            if 64 <= resultat <= 67:
                nom_enchantement = 'résistance à l\'électricité'
                valeur_enchantement = 18000
            if 68 <= resultat <= 71:
                nom_enchantement = 'résistance au feu'
                valeur_enchantement = 18000
            if 72 <= resultat <= 75:
                nom_enchantement = 'résistance au froid'
                valeur_enchantement = 18000
            if 76 <= resultat <= 79:
                nom_enchantement = 'résistance au son'
                valeur_enchantement = 18000
            if 80 <= resultat <= 89:
                valeur_alteration += 3
                nom_enchantement = 'défense intermédiaire'
            if resultat == 90:
                valeur_alteration += 3
                nom_enchantement = 'forme animale'
            if 91 <= resultat <= 93:
                valeur_alteration += 3
                nom_enchantement = 'résistance à la magie (15)'
            if 94 <= resultat <= 99:
                valeur_alteration += 3
                nom_enchantement = 'spectrale'
            if resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        propriete_speciale_determinee += 1
        valeur_alteration, nom_enchantement, valeur_enchantement, propriete_speciale_determinee = verif_alteration(
            alterations_cumulees, enchantements, propriete_speciale_determinee, nom_enchantement, valeur_alteration,
            valeur_enchantement)
        alterations_cumulees += valeur_alteration
        valeur += valeur_enchantement
        if nom_enchantement is not None:
            enchantements.append(nom_enchantement)
    return enchantements, alterations_cumulees, valeur


# armures et boucliers puissants
def determiner_armure_bouclier_puissante(valeur_objets_magiques):
    valeur_alterations_cumulees = {1: 1000, 2: 4000, 3: 9000, 4: 16000, 5: 25000,
                                   6: 36000, 7: 49000, 8: 64000, 9: 81000, 10: 100000}
    valeur = 0
    enchantements = []
    valeur_cumulee = 0
    alterations_cumulees = 0
    alteration = None
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 8:
        alteration = '+3'
        alterations_cumulees += 3
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 9 <= resultat <= 16:
        alteration = '+3'
        alterations_cumulees += 3
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 17 <= resultat <= 27:
        alteration = '+4'
        alterations_cumulees += 4
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 28 <= resultat <= 38:
        alteration = '+4'
        alterations_cumulees += 4
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 39 <= resultat <= 49:
        alteration = '+5'
        alterations_cumulees += 5
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 50 <= resultat <= 57:
        alteration = '+5'
        alterations_cumulees += 5
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
            valeur_objets_magiques)
        valeur += valeur_alterations_cumulees[alterations_cumulees]
    if 58 <= resultat <= 60:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure_specifique_puissante(
            valeur_objets_magiques)
    if 61 <= resultat <= 63:
        nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier_specifique_puissant(
            valeur_objets_magiques)
    if 64 <= resultat <= 100:
        resultat = random.randint(1, 2)
        if resultat == 1:
            resultat = random.randint(1, 100)
            tirage = False
            while not tirage:
                resultat = random.randint(1, 100)
                if 1 <= resultat <= 8:
                    tirage = False
                if 9 <= resultat <= 16:
                    alteration = '+3'
                    alterations_cumulees += 3
                    tirage = True
                if 17 <= resultat <= 27:
                    tirage = False
                if 28 <= resultat <= 38:
                    alteration = '+4'
                    alterations_cumulees += 4
                    tirage = True
                if 39 <= resultat <= 49:
                    tirage = False
                if 50 <= resultat <= 57:
                    alteration = '+5'
                    alterations_cumulees += 5
                    tirage = True
                if 58 <= resultat <= 100:
                    tirage = False
            nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_armure(
                valeur_objets_magiques)
            armure = True
            enchantements, alterations_cumulees, valeur = determiner_propriete_speciale_bouclier_armure_puissant(
                alterations_cumulees, armure, valeur)
            valeur_cumulee += valeur
            valeur_cumulee += valeur_alterations_cumulees[alterations_cumulees]
            valeur = valeur_cumulee
        if resultat == 2:
            tirage = False
            while not tirage:
                resultat = random.randint(1, 100)
                if 1 <= resultat <= 8:
                    alteration = '+3'
                    alterations_cumulees += 3
                    tirage = True
                if 17 <= resultat <= 27:
                    alteration = '+4'
                    alterations_cumulees += 4
                    tirage = True
                if 50 <= resultat <= 57:
                    alteration = '+5'
                    alterations_cumulees += 5
                    tirage = True
            nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur = determiner_bouclier(
                valeur_objets_magiques)
            armure = False
            enchantements, alterations_cumulees, valeur = determiner_propriete_speciale_bouclier_armure_puissant(
                alterations_cumulees, armure, valeur)
            valeur_cumulee += valeur
            valeur_cumulee += valeur_alterations_cumulees[alterations_cumulees]
            valeur = valeur_cumulee
    valeur_objets_magiques += valeur
    if alteration:
        nom_objet_magique = f'{nom_objet_magique} {alteration} {", ".join(enchantements)}'
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_armure_specifique_puissante(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 10:
        nom_objet_magique = 'cuirasse en adamantium'
        valeur = 10200
    if 11 <= resultat <= 20:
        nom_objet_magique = 'harnois nain'
        valeur = 16500
    if 21 <= resultat <= 32:
        nom_objet_magique = 'crevice de la seconde chance'
        valeur = 18900
    if 33 <= resultat <= 50:
        nom_objet_magique = 'armure céleste'
        valeur = 22400
    if 51 <= resultat <= 60:
        nom_objet_magique = 'harnois des profondeurs'
        valeur = 24650
    if 61 <= resultat <= 75:
        nom_objet_magique = 'cuirasse de commandement'
        valeur = 35400
    if 76 <= resultat <= 90:
        nom_objet_magique = 'harnois en mithral de vitesse'
        valeur = 26500
    if 91 <= resultat <= 100:
        nom_objet_magique = 'armure démoniaque'
        valeur = 52260
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_bouclier_specifique_puissant(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 20:
        nom_objet_magique = 'bouclier des arcanes'
        valeur = 3153
    if 21 <= resultat <= 40:
        nom_objet_magique = 'bouclier de la manticore'
        valeur = 5580
    if 41 <= resultat <= 60:
        nom_objet_magique = 'bouclier du lion'
        valeur = 9170
    if 61 <= resultat <= 80:
        nom_objet_magique = 'bouclier ailé'
        valeur = 17257
    if 81 <= resultat <= 100:
        nom_objet_magique = 'bouclier phagocyte'
        valeur = 50170
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_propriete_speciale_bouclier_armure_puissant(alterations_cumulees, armure, valeur):
    propriete_speciale_inconnue = 1
    propriete_speciale_determinee = 0
    enchantements = []
    while propriete_speciale_determinee < propriete_speciale_inconnue:
        valeur_enchantement = 0
        valeur_alteration = 0
        nom_enchantement = None
        if armure:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 3:
                nom_enchantement = 'mimétisme'
                valeur_enchantement = 2700
            if resultat == 4:
                valeur_alteration += 1
                nom_enchantement = 'défense légère'
            if 5 <= resultat <= 7:
                nom_enchantement = 'déplacement furtif supérieur'
                valeur_enchantement = 15000
            if 8 <= resultat <= 10:
                nom_enchantement = 'graisseuse supérieure'
                valeur_enchantement = 15000
            if 11 <= resultat <= 13:
                nom_enchantement = 'ombre supérieure'
                valeur_enchantement = 15000
            if 14 <= resultat <= 16:
                nom_enchantement = 'résistance à l\'acide'
                valeur_enchantement = 18000
            if 17 <= resultat <= 19:
                nom_enchantement = 'résistance à l\'électricité'
                valeur_enchantement = 18000
            if 20 <= resultat <= 22:
                nom_enchantement = 'résistance au feu'
                valeur_enchantement = 18000
            if 23 <= resultat <= 25:
                nom_enchantement = 'résistance au froid'
                valeur_enchantement = 18000
            if 26 <= resultat <= 28:
                nom_enchantement = 'résistance au son'
                valeur_enchantement = 18000
            if 29 <= resultat <= 33:
                valeur_alteration += 3
                nom_enchantement = 'défense intermédiaire'
            if resultat == 34:
                valeur_alteration += 3
                nom_enchantement = 'forme animale'
            if 35 <= resultat <= 36:
                valeur_alteration += 3
                nom_enchantement = 'invulnérabilité'
            if 37 <= resultat <= 38:
                valeur_alteration += 3
                nom_enchantement = 'résistance à la magie (15)'
            if 39 <= resultat <= 43:
                valeur_alteration += 3
                nom_enchantement = 'spectrale'
            if 44 <= resultat <= 48:
                nom_enchantement = 'déplacement furtif suprême'
                valeur_enchantement = 33750
            if 49 <= resultat <= 53:
                nom_enchantement = 'graisseuse suprême'
                valeur_enchantement = 33750
            if 54 <= resultat <= 58:
                nom_enchantement = 'ombre suprême'
                valeur_enchantement = 33750
            if 59 <= resultat <= 63:
                nom_enchantement = 'résistance à l\'acide supérieure'
                valeur_enchantement = 42000
            if 64 <= resultat <= 68:
                nom_enchantement = 'résistance à l\'électricité supérieure'
                valeur_enchantement = 42000
            if 69 <= resultat <= 73:
                nom_enchantement = 'résistance au feu supérieure'
                valeur_enchantement = 42000
            if 74 <= resultat <= 78:
                nom_enchantement = 'résistance au froid supérieure'
                valeur_enchantement = 42000
            if 79 <= resultat <= 83:
                nom_enchantement = 'résistance son supérieure'
                valeur_enchantement = 42000
            if 84 <= resultat <= 88:
                valeur_alteration += 4
                nom_enchantement = 'résistance à la magie (17)'
            if resultat == 89:
                nom_enchantement = 'controle des morts-vivants'
                valeur_enchantement = 49000
            if resultat == 90:
                nom_enchantement = 'éthérée'
                valeur_enchantement = 49000
            if 91 <= resultat <= 92:
                valeur_alteration += 5
                nom_enchantement = 'défense lourde'
            if 93 <= resultat <= 94:
                valeur_alteration += 5
                nom_enchantement = 'résistance à la magie (19)'
            if resultat == 95:
                nom_enchantement = 'résistance à l\'acide suprême'
                valeur_enchantement = 66000
            if resultat == 96:
                nom_enchantement = 'résistance à l\'électricité suprême'
                valeur_enchantement = 66000
            if resultat == 97:
                nom_enchantement = 'résistance au feu suprême'
                valeur_enchantement = 66000
            if resultat == 98:
                nom_enchantement = 'résistance au froid suprême'
                valeur_enchantement = 66000
            if resultat == 99:
                nom_enchantement = 'résistance son suprême'
                valeur_enchantement = 66000
            if resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        else:
            resultat = random.randint(1, 100)
            if 1 <= resultat <= 3:
                valeur_alteration += 1
                nom_enchantement = 'attaque'
            if 4 <= resultat <= 5:
                valeur_alteration += 1
                nom_enchantement = 'aveuglant'
            if 6 <= resultat <= 10:
                valeur_alteration += 1
                nom_enchantement = 'défense légère'
            if 11 <= resultat <= 15:
                valeur_alteration += 1
                nom_enchantement = 'interception de projectiles'
            if 16 <= resultat <= 20:
                valeur_alteration += 2
                nom_enchantement = 'animé'
            if 21 <= resultat <= 25:
                valeur_alteration += 2
                nom_enchantement = 'antiprojectiles'
            if 26 <= resultat <= 28:
                nom_enchantement = 'résistance à l\'acide'
                valeur_enchantement = 18000
            if 29 <= resultat <= 31:
                nom_enchantement = 'résistance à l\'électricité'
                valeur_enchantement = 18000
            if 32 <= resultat <= 34:
                nom_enchantement = 'résistance au feu'
                valeur_enchantement = 18000
            if 35 <= resultat <= 37:
                nom_enchantement = 'résistance au froid'
                valeur_enchantement = 18000
            if 38 <= resultat <= 40:
                nom_enchantement = 'résistance au son'
                valeur_enchantement = 18000
            if 41 <= resultat <= 50:
                valeur_alteration += 3
                nom_enchantement = 'défense intermédiaire'
            if resultat == 51:
                valeur_alteration += 3
                nom_enchantement = 'forme animale'
            if 52 <= resultat <= 53:
                valeur_alteration += 3
                nom_enchantement = 'résistance à la magie (15)'
            if 54 <= resultat <= 59:
                valeur_alteration += 3
                nom_enchantement = 'spectrale'
            if 60 <= resultat <= 64:
                nom_enchantement = 'résistance à l\'acide supérieure'
                valeur_enchantement = 42000
            if 65 <= resultat <= 69:
                nom_enchantement = 'résistance à l\'électricité supérieure'
                valeur_enchantement = 42000
            if 70 <= resultat <= 74:
                nom_enchantement = 'résistance au feu supérieure'
                valeur_enchantement = 42000
            if 75 <= resultat <= 79:
                nom_enchantement = 'résistance au froid supérieure'
                valeur_enchantement = 42000
            if 80 <= resultat <= 84:
                nom_enchantement = 'résistance son supérieure'
                valeur_enchantement = 42000
            if 85 <= resultat <= 86:
                valeur_alteration += 4
                nom_enchantement = 'résistance à la magie (17)'
            if resultat == 87:
                nom_enchantement = 'controle des morts-vivants'
                valeur_enchantement = 49000
            if 88 <= resultat <= 91:
                nom_enchantement = 'défense lourde'
                valeur_enchantement = 49000
            if 92 <= resultat <= 93:
                valeur_alteration += 5
                nom_enchantement = 'réfléchissant'
            if resultat == 94:
                valeur_alteration += 5
                nom_enchantement = 'résistance à la magie (19)'
            if resultat == 95:
                nom_enchantement = 'résistance à l\'acide suprême'
                valeur_enchantement = 66000
            if resultat == 96:
                nom_enchantement = 'résistance à l\'électricité suprême'
                valeur_enchantement = 66000
            if resultat == 97:
                nom_enchantement = 'résistance au feu suprême'
                valeur_enchantement = 66000
            if resultat == 98:
                nom_enchantement = 'résistance au froid suprême'
                valeur_enchantement = 66000
            if resultat == 99:
                nom_enchantement = 'résistance son suprême'
                valeur_enchantement = 66000
            if resultat == 100:
                propriete_speciale_inconnue += 1
                propriete_speciale_determinee -= 1
        propriete_speciale_determinee += 1
        valeur_alteration, nom_enchantement, valeur_enchantement, propriete_speciale_determinee = verif_alteration(
            alterations_cumulees, enchantements, propriete_speciale_determinee, nom_enchantement, valeur_alteration,
            valeur_enchantement)
        alterations_cumulees += valeur_alteration
        valeur += valeur_enchantement
        if nom_enchantement is not None:
            enchantements.append(nom_enchantement)
    return enchantements, alterations_cumulees, valeur


def verif_alteration(alterations_cumulees, enchantements, propriete_speciale_determinee, nom_enchantement, valeur_alteration, valeur_enchantement):
    if alterations_cumulees + valeur_alteration > 10 or nom_enchantement in enchantements:
        valeur_alteration = 0
        nom_enchantement = None
        valeur_enchantement = 0
        propriete_speciale_determinee = propriete_speciale_determinee - 1
    return valeur_alteration, nom_enchantement, valeur_enchantement, propriete_speciale_determinee
        
        
