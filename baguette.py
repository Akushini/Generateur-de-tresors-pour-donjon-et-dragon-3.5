import random


# determiner les différentes baguette
def determiner_baguette_faible(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_objet_magique = 'baguette de détection de la magie'
        valeur = 375
    if 3 <= resultat <= 4:
        nom_objet_magique = 'baguette de  lumière'
        valeur = 375
    if 5 <= resultat <= 7:
        nom_objet_magique = 'baguette d\'agrandissement'
        valeur = 750
    if 8 <= resultat <= 10:
        nom_objet_magique = 'baguette de charme animal'
        valeur = 750
    if 11 <= resultat <= 13:
        nom_objet_magique = 'baguette de baguette de charme personne'
        valeur = 750
    if 14 <= resultat <= 16:
        nom_objet_magique = 'baguette de convocation de monstres I'
        valeur = 750
    if 17 <= resultat <= 19:
        nom_objet_magique = 'baguette de couleurs dansantes'
        valeur = 750
    if 20 <= resultat <= 22:
        nom_objet_magique = 'baguette de décharge électrique'
        valeur = 750
    if 23 <= resultat <= 25:
        nom_objet_magique = 'baguette de détection des passages secrets'
        valeur = 750
    if 26 <= resultat <= 28:
        nom_objet_magique = 'baguette de mains brûlantes'
        valeur = 750
    if 29 <= resultat <= 31:
        nom_objet_magique = 'baguette de projectile magique'
        valeur = 750
    if 32 <= resultat <= 34:
        nom_objet_magique = 'baguette de soins légers'
        valeur = 750
    if 35 <= resultat <= 36:
        nom_objet_magique = 'baguette de projectile magique (niveau 3)'
        valeur = 2250
    if resultat == 37:
        nom_objet_magique = 'baguette de projectile magique (niveau 5)'
        valeur = 3750
    if 38 <= resultat <= 39:
        nom_objet_magique = 'baguette de baiser de la goule'
        valeur = 4500
    if 40 <= resultat <= 42:
        nom_objet_magique = 'baguette de convocation de monstres II'
        valeur = 4500
    if 43 <= resultat <= 45:
        nom_objet_magique = 'baguette de déblocage'
        valeur = 4500
    if 46 <= resultat <= 48:
        nom_objet_magique = 'baguette d\'endurance de l\'ours'
        valeur = 4500
    if 49 <= resultat <= 51:
        nom_objet_magique = 'baguette de flècge acide de Melf'
        valeur = 4500
    if 52 <= resultat <= 54:
        nom_objet_magique = 'baguette de force du taureau'
        valeur = 4500
    if 55 <= resultat <= 56:
        nom_objet_magique = 'baguette de fracassement'
        valeur = 4500
    if 57 <= resultat <= 59:
        nom_objet_magique = 'baguette de grâce féline'
        valeur = 4500
    if 60 <= resultat <= 62:
        nom_objet_magique = 'baguette d\'image miroir'
        valeur = 4500
    if 63 <= resultat <= 65:
        nom_objet_magique = 'baguette d\'immobilisation de personne'
        valeur = 4500
    if 66 <= resultat <= 68:
        nom_objet_magique = 'baguette d\'invisibilité'
        valeur = 4500
    if 69 <= resultat <= 71:
        nom_objet_magique = 'baguette de lévitation'
        valeur = 4500
    if 72 <= resultat <= 74:
        nom_objet_magique = 'baguette de lumière du jour'
        valeur = 4500
    if 75 <= resultat <= 77:
        nom_objet_magique = 'baguette de ralentissement du poison'
        valeur = 4500
    if 78 <= resultat <= 80:
        nom_objet_magique = 'baguette de ruse du renard'
        valeur = 4500
    if 81 <= resultat <= 83:
        nom_objet_magique = 'baguette de sagesse du hibou'
        valeur = 4500
    if 84 <= resultat <= 86:
        nom_objet_magique = 'baguette de silence'
        valeur = 4500
    if 87 <= resultat <= 89:
        nom_objet_magique = 'baguette de simulacre de vie'
        valeur = 4500
    if 90 <= resultat <= 92:
        nom_objet_magique = 'baguette de soins modérés'
        valeur = 4500
    if 93 <= resultat <= 95:
        nom_objet_magique = 'baguette de splendeur de l\'aigle'
        valeur = 4500
    if 96 <= resultat <= 97:
        nom_objet_magique = 'baguette de ténèbres'
        valeur = 4500
    if 98 <= resultat <= 100:
        nom_objet_magique = 'baguette de toile d\'araignée'
        valeur = 4500
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_baguette_intermediaire(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_objet_magique = 'baguette de projectile magique (niveau 5)'
        valeur = 3750
    if resultat == 4:
        nom_objet_magique = 'baguette de baiser de la goule'
        valeur = 4500
    if resultat == 5:
        nom_objet_magique = 'baguette de convocation de monstres II'
        valeur = 4500
    if 6 <= resultat <= 7:
        nom_objet_magique = 'baguette de déblocage'
        valeur = 4500
    if 8 <= resultat <= 11:
        nom_objet_magique = 'baguette d\'endurance de l\'ours'
        valeur = 4500
    if 12 <= resultat <= 13:
        nom_objet_magique = 'baguette de flècge acide de Melf'
        valeur = 4500
    if 14 <= resultat <= 17:
        nom_objet_magique = 'baguette de force du taureau'
        valeur = 4500
    if resultat == 18:
        nom_objet_magique = 'baguette de fracassement'
        valeur = 4500
    if 19 <= resultat <= 22:
        nom_objet_magique = 'baguette de grâce féline'
        valeur = 4500
    if 23 <= resultat <= 24:
        nom_objet_magique = 'baguette d\'image miroir'
        valeur = 4500
    if resultat == 25:
        nom_objet_magique = 'baguette d\'immobilisation de personne'
        valeur = 4500
    if 26 <= resultat <= 28:
        nom_objet_magique = 'baguette d\'invisibilité'
        valeur = 4500
    if resultat == 29:
        nom_objet_magique = 'baguette de lévitation'
        valeur = 4500
    if 30 <= resultat <= 31:
        nom_objet_magique = 'baguette de lumière du jour'
        valeur = 4500
    if 32 <= resultat <= 34:
        nom_objet_magique = 'baguette de ralentissement du poison'
        valeur = 4500
    if 35 <= resultat <= 38:
        nom_objet_magique = 'baguette de ruse du renard'
        valeur = 4500
    if 39 <= resultat <= 42:
        nom_objet_magique = 'baguette de sagesse du hibou'
        valeur = 4500
    if 43 <= resultat <= 44:
        nom_objet_magique = 'baguette de silence'
        valeur = 4500
    if 45 <= resultat <= 46:
        nom_objet_magique = 'baguette de simulacre de vie'
        valeur = 4500
    if 47 <= resultat <= 51:
        nom_objet_magique = 'baguette de soins modérés'
        valeur = 4500
    if 52 <= resultat <= 55:
        nom_objet_magique = 'baguette de splendeur de l\'aigle'
        valeur = 4500
    if 56 <= resultat <= 57:
        nom_objet_magique = 'baguette de ténèbres'
        valeur = 4500
    if 58 <= resultat <= 59:
        nom_objet_magique = 'baguette de toile d\'araignée'
        valeur = 4500
    if 60 <= resultat <= 62:
        nom_objet_magique = 'baguette de projectile magique (niveau 7)'
        valeur = 5250
    if 63 <= resultat <= 64:
        nom_objet_magique = 'baguette de projectile magique (niveau 9)'
        valeur = 6750
    if 65 <= resultat <= 66:
        nom_objet_magique = 'baguette d\'affûtage'
        valeur = 11250
    if 67 <= resultat <= 69:
        nom_objet_magique = 'baguette d\'appel de la foudre'
        valeur = 11250
    if 70 <= resultat <= 73:
        nom_objet_magique = 'baguette de boule de feu'
        valeur = 11250
    if resultat == 74:
        nom_objet_magique = 'baguette de charme personne à intensité augmentée au 3e niveau'
        valeur = 11250
    if 75 <= resultat <= 76:
        nom_objet_magique = 'baguette de contagion'
        valeur = 11250
    if 77 <= resultat <= 79:
        nom_objet_magique = 'baguette de convocation de monstres III'
        valeur = 11250
    if 80 <= resultat <= 82:
        nom_objet_magique = 'baguette de dissipation de la magie'
        valeur = 11250
    if 83 <= resultat <= 86:
        nom_objet_magique = 'baguette d\'éclair'
        valeur = 11250
    if 87 <= resultat <= 88:
        nom_objet_magique = 'baguette d\'image accomplie'
        valeur = 11250
    if 89 <= resultat <= 90:
        nom_objet_magique = 'baguette de lenteur'
        valeur = 11250
    if 91 <= resultat <= 96:
        nom_objet_magique = 'baguette de soins importants'
        valeur = 11250
    if resultat == 97:
        nom_objet_magique = 'baguette de suggestion'
        valeur = 11250
    if resultat == 98:
        nom_objet_magique = 'baguette de boule de feu (niveau 6)'
        valeur = 13500
    if resultat == 99:
        nom_objet_magique = 'baguette d\'éclair (niveau 6)'
        valeur = 13500
    if resultat == 100:
        nom_objet_magique = 'baguette de lumière brûlante (niveau 6)'
        valeur = 13500

    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur


def determiner_baguette_puissante(valeur_objets_magiques):
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_objet_magique = 'baguette de projectile magique (niveau 7)'
        valeur = 5250
    if 3 <= resultat <= 5:
        nom_objet_magique = 'baguette de projectile magique (niveau 9)'
        valeur = 6750
    if 6 <= resultat <= 7:
        nom_objet_magique = 'baguette d\'affûtage'
        valeur = 11250
    if 8 <= resultat <= 9:
        nom_objet_magique = 'baguette d\'appel de la foudre'
        valeur = 11250
    if 10 <= resultat <= 11:
        nom_objet_magique = 'baguette de boule de feu'
        valeur = 11250
    if resultat == 12:
        nom_objet_magique = 'baguette de charme personne à intensité augmentée au 3e niveau'
        valeur = 11250
    if 13 <= resultat <= 14:
        nom_objet_magique = 'baguette de contagion'
        valeur = 11250
    if 15 <= resultat <= 16:
        nom_objet_magique = 'baguette de convocation de monstres III'
        valeur = 11250
    if 17 <= resultat <= 18:
        nom_objet_magique = 'baguette de dissipation de la magie'
        valeur = 11250
    if 19 <= resultat <= 20:
        nom_objet_magique = 'baguette d\'éclair'
        valeur = 11250
    if 21 <= resultat <= 22:
        nom_objet_magique = 'baguette d\'image accomplie'
        valeur = 11250
    if 23 <= resultat <= 24:
        nom_objet_magique = 'baguette de lenteur'
        valeur = 11250
    if 25 <= resultat <= 27:
        nom_objet_magique = 'baguette de soins importants'
        valeur = 11250
    if 28 <= resultat <= 29:
        nom_objet_magique = 'baguette de suggestion'
        valeur = 11250
    if 30 <= resultat <= 31:
        nom_objet_magique = 'baguette de boule de feu (niveau 6)'
        valeur = 13500
    if 32 <= resultat <= 33:
        nom_objet_magique = 'baguette d\'éclair (niveau 6)'
        valeur = 13500
    if 34 <= resultat <= 35:
        nom_objet_magique = 'baguette de lumière brûlante (niveau 6)'
        valeur = 13500
    if 36 <= resultat <= 37:
        nom_objet_magique = 'baguette d\'appel de la foudre (niveau 8)'
        valeur = 18000
    if 38 <= resultat <= 39:
        nom_objet_magique = 'baguette de boule de feu (niveau 8)'
        valeur = 18000
    if 40 <= resultat <= 41:
        nom_objet_magique = 'baguette d\'éclair (niveau 8)'
        valeur = 18000
    if 42 <= resultat <= 43:
        nom_objet_magique = 'baguette d\'ancre dimensionnelle'
        valeur = 21000
    if 44 <= resultat <= 46:
        nom_objet_magique = 'baguette de blessure critique'
        valeur = 21000
    if 47 <= resultat <= 50:
        nom_objet_magique = 'baguette de charme-monstre'
        valeur = 21000
    if 51 <= resultat <= 53:
        nom_objet_magique = 'baguette de convocation de monstre IV'
        valeur = 21000
    if 54 <= resultat <= 55:
        nom_objet_magique = 'baguette d\'empoisonnement'
        valeur = 21000
    if resultat == 56:
        nom_objet_magique = 'baguette d\'immobilisation de personne à intensité augmentée au 4e niveau'
        valeur = 21000
    if 57 <= resultat <= 60:
        nom_objet_magique = 'baguette d\'invisibilité suprême'
        valeur = 21000
    if 61 <= resultat <= 63:
        nom_objet_magique = 'baguette de métamorphose'
        valeur = 21000
    if 64 <= resultat <= 67:
        nom_objet_magique = 'baguette de mur de feu'
        valeur = 21000
    if 68 <= resultat <= 71:
        nom_objet_magique = 'baguette de mur de glace'
        valeur = 21000
    if 72 <= resultat <= 75:
        nom_objet_magique = 'baguette de neutralisation du poison'
        valeur = 21000
    if resultat == 76:
        nom_objet_magique = 'baguette de rayon affaiblissant à intensité augmentée au 4e niveau'
        valeur = 21000
    if 77 <= resultat <= 81:
        nom_objet_magique = 'baguette de soins intensifs'
        valeur = 21000
    if resultat == 82:
        nom_objet_magique = 'baguette de suggestion à intensité augmentée au 4e niveau'
        valeur = 21000
    if 83 <= resultat <= 87:
        nom_objet_magique = 'baguette de tempête de grêle'
        valeur = 21000
    if 88 <= resultat <= 90:
        nom_objet_magique = 'baguette de terreur'
        valeur = 21000
    if resultat == 91:
        nom_objet_magique = 'baguette de boule de feu (niveau 10)'
        valeur = 22500
    if resultat == 92:
        nom_objet_magique = 'baguette de dissipation de la magie (niveau 10)'
        valeur = 22500
    if resultat == 93:
        nom_objet_magique = 'baguette d\'éclair (niveau 10)'
        valeur = 22500
    if resultat == 94:
        nom_objet_magique = 'baguette de châtiment sacré (niveau 8)'
        valeur = 24000
    if resultat == 95:
        nom_objet_magique = 'baguette de courroux de l\'ordre(niveau 8)'
        valeur = 24000
    if resultat == 96:
        nom_objet_magique = 'baguette de marteau du chaos (niveau 8)'
        valeur = 24000
    if resultat == 97:
        nom_objet_magique = 'baguette de ténèbres maudites (niveau 8)'
        valeur = 24000
    if 98 <= resultat <= 99:
        nom_objet_magique = 'baguette de restauration'
        valeur = 26000
    if resultat == 100:
        nom_objet_magique = 'baguette de peau de pierre'
        valeur = 37700
    valeur_objets_magiques += valeur
    nombre_objet_magique = 1
    return nom_objet_magique, nombre_objet_magique, valeur_objets_magiques, valeur