import random


# sorts profanes
def lancer_sort_profane_0():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 4:
        nom_sort = 'aspersion acide'
    if 5 <= resultat <= 6:
        nom_sort = 'berceuse'
    if 7 <= resultat <= 8:
        nom_sort = 'convocation d\'instrument'
    if 9 <= resultat <= 12:
        nom_sort = 'destruction de mort-vivant'
    if 13 <= resultat <= 19:
        nom_sort = 'détection de la magie'
    if 20 <= resultat <= 23:
        nom_sort = 'détection du poison'
    if 24 <= resultat <= 27:
        nom_sort = 'fatigue'
    if 28 <= resultat <= 31:
        nom_sort = 'hébétement'
    if 32 <= resultat <= 36:
        nom_sort = 'illumination'
    if 37 <= resultat <= 42:
        nom_sort = 'lecture de la magie'
    if 43 <= resultat <= 48:
        nom_sort = 'lumière'
    if 49 <= resultat <= 53:
        nom_sort = 'lumières dansantes'
    if 54 <= resultat <= 58:
        nom_sort = 'manipulation à distance'
    if 59 <= resultat <= 63:
        nom_sort = 'message'
    if 64 <= resultat <= 68:
        nom_sort = 'ouverture/fermeture'
    if 69 <= resultat <= 73:
        nom_sort = 'prestidigitation'
    if 74 <= resultat <= 77:
        nom_sort = 'rayon de givre'
    if 78 <= resultat <= 82:
        nom_sort = 'réparation'
    if 83 <= resultat <= 84:
        nom_sort = 'repérage'
    if 85 <= resultat <= 91:
        nom_sort = 'résistance'
    if 92 <= resultat <= 95:
        nom_sort = 'signature magique'
    if 96 <= resultat <= 100:
        nom_sort = 'son imaginaire'
    valeur = 12
    return valeur, nom_sort


def lancer_sort_profane_1():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_sort = 'agrandissement'
        valeur = 25
    if 4 <= resultat <= 6:
        nom_sort = 'alarme'
        valeur = 25
    if resultat == 7:
        nom_sort = 'alignement indétectable'
        valeur = 50
    if 8 <= resultat <= 10:
        nom_sort = 'arme magique'
        valeur = 25
    if 11 <= resultat <= 13:
        nom_sort = 'armure de mage'
        valeur = 25
    if 14 <= resultat <= 15:
        nom_sort = 'aura magique de Nystul'
        valeur = 25
    if 16 <= resultat <= 17:
        nom_sort = 'bouclier'
        valeur = 25
    if 18 <= resultat <= 19:
        nom_sort = 'brume de dissimulation'
        valeur = 25
    if 20 <= resultat <= 22:
        nom_sort = 'charme-personne'
        valeur = 25
    if 23 <= resultat <= 25:
        nom_sort = 'compréhension des langages'
        valeur = 25
    if resultat == 26:
        nom_sort = 'confusion mineure'
        valeur = 50
    if 27 <= resultat <= 28:
        nom_sort = 'contact glacial'
        valeur = 25
    if 29 <= resultat <= 30:
        nom_sort = 'convocation de monstres I'
        valeur = 25
    if 31 <= resultat <= 32:
        nom_sort = 'corde animée'
        valeur = 25
    if 33 <= resultat <= 34:
        nom_sort = 'couleurs dansantes'
        valeur = 25
    if 35 <= resultat <= 36:
        nom_sort = 'coup au but'
        valeur = 25
    if 37 <= resultat <= 38:
        nom_sort = 'décharge électrique'
        valeur = 25
    if 39 <= resultat <= 41:
        nom_sort = 'déguisement'
        valeur = 25
    if 42 <= resultat <= 43:
        nom_sort = 'détection des morts-vivants'
        valeur = 25
    if 44 <= resultat <= 46:
        nom_sort = 'détection des passages secrets'
        valeur = 25
    if 47 <= resultat <= 49:
        nom_sort = 'disque flottant de Tenser'
        valeur = 25
    if 50 <= resultat <= 51:
        nom_sort = 'effacement'
        valeur = 25
    if 52 <= resultat <= 54:
        nom_sort = 'endurance aux énergies destructives'
        valeur = 25
    if resultat == 55:
        nom_sort = 'feuille morte'
        valeur = 25
    if 56 <= resultat <= 57:
        nom_sort = 'frayeur'
        valeur = 25
    if 58 <= resultat <= 59:
        nom_sort = 'graisse'
        valeur = 25
    if 60 <= resultat <= 61:
        nom_sort = 'hypnose'
        valeur = 25
    if 62 <= resultat <= 63:
        nom_sort = 'identification'
        valeur = 125
    if 64 <= resultat <= 65:
        nom_sort = 'image silencieuse'
        valeur = 25
    if 66 <= resultat <= 67:
        nom_sort = 'mains brûlantes'
        valeur = 25
    if 68 <= resultat <= 70:
        nom_sort = 'monture'
        valeur = 25
    if 71 <= resultat <= 72:
        nom_sort = 'projectile magique'
        valeur = 25
    if 73 <= resultat <= 74:
        nom_sort = 'protection contre la Loi'
        valeur = 25
    if 75 <= resultat <= 76:
        nom_sort = 'protection contre le Bien'
        valeur = 25
    if 77 <= resultat <= 78:
        nom_sort = 'protection contre le Chaos'
        valeur = 25
    if 79 <= resultat <= 80:
        nom_sort = 'protection contre le Mal'
        valeur = 25
    if 81 <= resultat <= 82:
        nom_sort = 'rapetissement'
        valeur = 25
    if 83 <= resultat <= 84:
        nom_sort = 'rayon affaiblissant'
        valeur = 25
    if 85 <= resultat <= 86:
        nom_sort = 'regain d\'assurance'
        valeur = 50
    if 87 <= resultat <= 89:
        nom_sort = 'repli expéditif'
        valeur = 25
    if 90 <= resultat <= 91:
        nom_sort = 'saut'
        valeur = 25
    if 92 <= resultat <= 93:
        nom_sort = 'serviteur invisible'
        valeur = 25
    if resultat == 94:
        nom_sort = 'soins légers'
        valeur = 50
    if 95 <= resultat <= 96:
        nom_sort = 'sommeil'
        valeur = 25
    if 97 <= resultat <= 98:
        nom_sort = 'ventriloquie'
        valeur = 25
    if 99 <= resultat <= 100:
        nom_sort = 'verrouillage'
        valeur = 25
    return valeur, nom_sort


def lancer_sort_profane_2():
    resultat = random.randint(1, 100)
    if resultat == 1:
        nom_sort = 'apaisement des émotions'
        valeur = 200
    if resultat == 2:
        nom_sort = 'baiser de la goule'
        valeur = 150
    if resultat == 3:
        nom_sort = 'bouche magique'
        valeur = 160
    if resultat == 4:
        nom_sort = 'bourrasque'
        valeur = 150
    if resultat == 5:
        nom_sort = 'cacophonie'
        valeur = 200
    if 6 <= resultat <= 7:
        nom_sort = 'cécité/surdité'
        valeur = 150
    if 8 <= resultat <= 9:
        nom_sort = 'contrôle mineur des morts-vivants'
        valeur = 150
    if 10 <= resultat <= 11:
        nom_sort = 'convocation de monstres II'
        valeur = 150
    if resultat == 12:
        nom_sort = 'corde enchantée'
        valeur = 150
    if 13 <= resultat <= 15:
        nom_sort = 'déblocage'
        valeur = 150
    if 16 <= resultat <= 18:
        nom_sort = 'détection de l\'invisibilité'
        valeur = 150
    if 19 <= resultat <= 20:
        nom_sort = 'détection de pensées'
        valeur = 150
    if resultat == 21:
        nom_sort = 'détection faussée'
        valeur = 25
    if resultat == 22:
        nom_sort = 'discours captivant'
        valeur = 200
    if resultat == 23:
        nom_sort = 'dissimulation d\'objet'
        valeur = 150
    if resultat == 24:
        nom_sort = 'effroi'
        valeur = 150
    if 25 <= resultat <= 27:
        nom_sort = 'endurance de l\'ours'
        valeur = 150
    if resultat == 28:
        nom_sort = 'flamme éternelle'
        valeur = 200
    if 29 <= resultat <= 30:
        nom_sort = 'flèche acide de Melf'
        valeur = 150
    if 31 <= resultat <= 32:
        nom_sort = 'flou'
        valeur = 150
    if 33 <= resultat <= 35:
        nom_sort = 'force du taureau'
        valeur = 150
    if resultat == 36:
        nom_sort = 'fou rire de Tasha'
        valeur = 150
    if resultat == 37:
        nom_sort = 'fracassement'
        valeur = 150
    if 38 <= resultat <= 40:
        nom_sort = 'grâce féline'
        valeur = 150
    if resultat == 41:
        nom_sort = 'hébétement de monstre'
        valeur = 150
    if resultat == 42:
        nom_sort = 'hypnose des animaux'
        valeur = 200
    if resultat == 43:
        nom_sort = 'idiotie'
        valeur = 150
    if resultat == 44:
        nom_sort = 'image imparfaite'
        valeur = 150
    if 45 <= resultat <= 46:
        nom_sort = 'image miroir'
        valeur = 150
    if 47 <= resultat <= 49:
        nom_sort = 'invisibilité'
        valeur = 150
    if 50 <= resultat <= 51:
        nom_sort = 'lévitation'
        valeur = 150
    if resultat == 52:
        nom_sort = 'localisation d\'objet'
        valeur = 150
    if 53 <= resultat <= 54:
        nom_sort = 'lueurs hypnotiques'
        valeur = 150
    if resultat == 55:
        nom_sort = 'main spectrale'
        valeur = 150
    if resultat == 56:
        nom_sort = 'messager animal'
        valeur = 200
    if 57 <= resultat <= 58:
        nom_sort = 'modification d\'apparence'
        valeur = 150
    if resultat == 59:
        nom_sort = 'nappe de brouillard'
        valeur = 150
    if 60 <= resultat <= 61:
        nom_sort = 'nuée grouillante'
        valeur = 150
    if 62 <= resultat <= 63:
        nom_sort = 'pattes d\'araignée'
        valeur = 150
    if resultat == 64:
        nom_sort = 'piège de Léomund'
        valeur = 200
    if 65 <= resultat <= 66:
        nom_sort = 'poussière scintillante'
        valeur = 150
    if 67 <= resultat <= 69:
        nom_sort = 'protection contre les projectiles'
        valeur = 150
    if 70 <= resultat <= 71:
        nom_sort = 'pyrotechnie'
        valeur = 150
    if resultat == 72:
        nom_sort = 'ralentissement du poison'
        valeur = 200
    if 73 <= resultat <= 74:
        nom_sort = 'rayon ardent'
        valeur = 150
    if 75 <= resultat <= 77:
        nom_sort = 'résistance aux énergies destructives'
        valeur = 150
    if 78 <= resultat <= 80:
        nom_sort = 'ruse du renard'
        valeur = 150
    if 81 <= resultat <= 83:
        nom_sort = 'sagesse du hibou'
        valeur = 200
    if resultat == 84:
        nom_sort = 'silence'
        valeur = 200
    if 85 <= resultat <= 86:
        nom_sort = 'simulacre de vie'
        valeur = 150
    if resultat == 87:
        nom_sort = 'soins modérés'
        valeur = 200
    if 88 <= resultat <= 89:
        nom_sort = 'sphère de feu'
        valeur = 150
    if 90 <= resultat <= 92:
        nom_sort = 'splendeur de l\'aigle'
        valeur = 150
    if resultat == 93:
        nom_sort = 'ténèbres'
        valeur = 150
    if 94 <= resultat <= 95:
        nom_sort = 'toile d\'araignée'
        valeur = 150
    if resultat == 96:
        nom_sort = 'vent de murmures'
        valeur = 150
    if resultat == 97:
        nom_sort = 'verrou du mage'
        valeur = 175
    if 98 <= resultat <= 100:
        nom_sort = 'vision dans le noir'
        valeur = 150
    return valeur, nom_sort


def lancer_sort_profane_3():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_sort = 'abri de Léomund'
        valeur = 375
    if 3 <= resultat <= 5:
        nom_sort = 'affûtage'
        valeur = 375
    if 6 <= resultat <= 7:
        nom_sort = 'antidétection'
        valeur = 425
    if 8 <= resultat <= 10:
        nom_sort = 'arme magique suprême'
        valeur = 375
    if resultat == 11:
        nom_sort = 'bagou'
        valeur = 525
    if 12 <= resultat <= 13:
        nom_sort = 'baiser du vampire'
        valeur = 375
    if 14 <= resultat <= 15:
        nom_sort = 'boule de feu'
        valeur = 375
    if 16 <= resultat <= 17:
        nom_sort = 'cercle de magie contre la Loi'
        valeur = 375
    if 18 <= resultat <= 19:
        nom_sort = 'cercle de magie contre le Bien'
        valeur = 375
    if 20 <= resultat <= 21:
        nom_sort = 'cercle de magie contre le Chaos'
        valeur = 375
    if 22 <= resultat <= 23:
        nom_sort = 'cercle de magie contre le Mal'
        valeur = 375
    if 24 <= resultat <= 25:
        nom_sort = 'clairaudience/clairvoyance'
        valeur = 375
    if 26 <= resultat <= 27:
        nom_sort = 'clignotement'
        valeur = 375
    if resultat == 28:
        nom_sort = 'communication avec les animaux'
        valeur = 525
    if 19 <= resultat <= 30:
        nom_sort = 'convocation de monstres III'
        valeur = 375
    if 31 <= resultat <= 32:
        nom_sort = 'coursier fantôme'
        valeur = 375
    if 33 <= resultat <= 34:
        nom_sort = 'déplacement'
        valeur = 375
    if 35 <= resultat <= 36:
        nom_sort = 'dissipation de la magie'
        valeur = 375
    if 37 <= resultat <= 40:
        nom_sort = 'don des langues'
        valeur = 375
    if 41 <= resultat <= 42:
        nom_sort = 'éclair'
        valeur = 375
    if resultat == 43:
        nom_sort = 'espoir'
        valeur = 525
    if 44 <= resultat <= 45:
        nom_sort = 'état gazeux'
        valeur = 375
    if 46 <= resultat <= 47:
        nom_sort = 'flèches enflammées'
        valeur = 375
    if 48 <= resultat <= 49:
        nom_sort = 'héroïsme'
        valeur = 375
    if 50 <= resultat <= 51:
        nom_sort = 'image accomplie'
        valeur = 375
    if 52 <= resultat <= 53:
        nom_sort = 'immobilisation de morts-vivants'
        valeur = 375
    if 54 <= resultat <= 55:
        nom_sort = 'immobilisation de personne'
        valeur = 375
    if 56 <= resultat <= 57:
        nom_sort = 'lenteur'
        valeur = 375
    if 58 <= resultat <= 60:
        nom_sort = 'lumière du jour'
        valeur = 525
    if resultat == 61:
        nom_sort = 'manipulation des sons'
        valeur = 525
    if 62 <= resultat <= 63:
        nom_sort = 'mur de vent'
        valeur = 375
    if 64 <= resultat <= 65:
        nom_sort = 'localisation d\'nuage nauséabond'
        valeur = 375
    if resultat == 66:
        nom_sort = 'page secrète'
        valeur = 375
    if 67 <= resultat <= 68:
        nom_sort = 'préservation des morts'
        valeur = 375
    if 69 <= resultat <= 71:
        nom_sort = 'protection contre les énergies destructives'
        valeur = 375
    if 72 <= resultat <= 73:
        nom_sort = 'rage'
        valeur = 375
    if 74 <= resultat <= 76:
        nom_sort = 'rapidité'
        valeur = 375
    if 77 <= resultat <= 78:
        nom_sort = 'rayon d\'épuisement'
        valeur = 375
    if resultat == 79:
        nom_sort = 'réduction d\'objet'
        valeur = 375
    if 80 <= resultat <= 82:
        nom_sort = 'respiration aquatique'
        valeur = 375
    if resultat == 83:
        nom_sort = 'runes explosives'
        valeur = 375
    if resultat == 84:
        nom_sort = 'sceau du serpent'
        valeur = 875
    if resultat == 85:
        nom_sort = 'soins importants'
        valeur = 525
    if 86 <= resultat <= 87:
        nom_sort = 'sommeil profond'
        valeur = 375
    if 88 <= resultat <= 90:
        nom_sort = 'sphère d\'invisibilité'
        valeur = 375
    if 91 <= resultat <= 92:
        nom_sort = 'suggestion'
        valeur = 375
    if 93 <= resultat <= 94:
        nom_sort = 'tempête de neuge'
        valeur = 375
    if resultat == 95:
        nom_sort = 'texte illusoire'
        valeur = 425
    if 96 <= resultat <= 97:
        nom_sort = 'vision magique'
        valeur = 375
    if 98 <= resultat <= 100:
        nom_sort = 'vol'
        valeur = 375
    return valeur, nom_sort


def lancer_sort_profane_4():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_sort = 'ancre dimensionnelle'
        valeur = 700
    if 4 <= resultat <= 5:
        nom_sort = 'agrandissement de groupe'
        valeur = 700
    if 6 <= resultat <= 7:
        nom_sort = 'animation des morts'
        valeur = 1050
    if 8 <= resultat <= 9:
        nom_sort = 'assassin imaginaire'
        valeur = 700
    if 10 <= resultat <= 12:
        nom_sort = 'bouclier de feu'
        valeur = 700
    if 13 <= resultat <= 14:
        nom_sort = 'brouillard dense'
        valeur = 700
    if 15 <= resultat <= 17:
        nom_sort = 'charme-monstre'
        valeur = 700
    if resultat == 18:
        nom_sort = 'communication avec les plantes'
        valeur = 100
    if 19 <= resultat <= 21:
        nom_sort = 'confusion'
        valeur = 700
    if 22 <= resultat <= 23:
        nom_sort = 'contageion'
        valeur = 700
    if 24 <= resultat <= 25:
        nom_sort = 'convocation d\'ombres'
        valeur = 700
    if 26 <= resultat <= 27:
        nom_sort = 'convocation de monstres IV'
        valeur = 700
    if 28 <= resultat <= 29:
        nom_sort = 'création mineure'
        valeur = 700
    if 30 <= resultat <= 31:
        nom_sort = 'cri'
        valeur = 700
    if 32 <= resultat <= 34:
        nom_sort = 'délivrance des malédictions'
        valeur = 700
    if 35 <= resultat <= 36:
        nom_sort = 'désespoir foudroyant'
        valeur = 700
    if resultat == 37:
        nom_sort = 'détection de la scrutation'
        valeur = 700
    if 38 <= resultat <= 39:
        nom_sort = 'énergie négative'
        valeur = 700
    if 40 <= resultat <= 41:
        nom_sort = 'façonnage de la pierre'
        valeur = 700
    if 42 <= resultat <= 44:
        nom_sort = 'globe d\'invisibilité partielle'
        valeur = 700
    if 45 <= resultat <= 47:
        nom_sort = 'invisibilité suprême'
        valeur = 700
    if 48 <= resultat <= 50:
        nom_sort = 'liberté de mouvement'
        valeur = 1000
    if resultat == 51:
        nom_sort = 'localisation de créature'
        valeur = 700
    if 52 <= resultat <= 53:
        nom_sort = 'lueur d\'arc-en-ciel'
        valeur = 700
    if 54 <= resultat <= 55:
        nom_sort = 'malédiction'
        valeur = 700
    if resultat == 56:
        nom_sort = 'mémorisation de Rary'
        valeur = 700
    if 57 <= resultat <= 58:
        nom_sort = 'métamorphose'
        valeur = 700
    if resultat == 59:
        nom_sort = 'mission'
        valeur = 700
    if resultat == 60:
        nom_sort = 'modification de mémoire'
        valeur = 1000
    if 61 <= resultat <= 63:
        nom_sort = 'mur de feu'
        valeur = 700
    if 64 <= resultat <= 66:
        nom_sort = 'mur de glace'
        valeur = 700
    if 67 <= resultat <= 68:
        nom_sort = 'mur illusoire'
        valeur = 700
    if resultat == 69:
        nom_sort = 'neutralisation du poison'
        valeur = 1000
    if 70 <= resultat <= 72:
        nom_sort = 'oeil du mage'
        valeur = 700
    if 73 <= resultat <= 75:
        nom_sort = 'peau de pierre'
        valeur = 950
    if 76 <= resultat <= 77:
        nom_sort = 'piège à feu'
        valeur = 725
    if 78 <= resultat <= 81:
        nom_sort = 'porte dimensionnelle'
        valeur = 700
    if 82 <= resultat <= 83:
        nom_sort = 'rapetissement de groupe'
        valeur = 700
    if 84 <= resultat <= 85:
        nom_sort = 'refuge de Léomund'
        valeur = 700
    if resultat == 86:
        nom_sort = 'repulsif'
        valeur = 1000
    if 87 <= resultat <= 88:
        nom_sort = 'scrutation'
        valeur = 700
    if resultat == 89:
        nom_sort = 'soins intensifs'
        valeur = 1000
    if 90 <= resultat <= 91:
        nom_sort = 'sphère d\'isolement d\'Otiluke'
        valeur = 700
    if 92 <= resultat <= 93:
        nom_sort = 'tempête de grêle'
        valeur = 700
    if 94 <= resultat <= 95:
        nom_sort = 'tentacules noirs d\'evard'
        valeur = 700
    if 96 <= resultat <= 97:
        nom_sort = 'terrain hallucinatoire'
        valeur = 700
    if 98 <= resultat <= 99:
        nom_sort = 'terreur'
        valeur = 700
    if resultat == 100:
        nom_sort = 'zone de silence'
        valeur = 1000
    return valeur, nom_sort


def lancer_sort_profane_5():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_sort = 'annulation d\'enchantement'
        valeur = 1125
    if 4 <= resultat <= 5:
        nom_sort = 'brume mentale'
        valeur = 1125
    if 6 <= resultat <= 7:
        nom_sort = 'brume mentale'
        valeur = 1125
    if 8 <= resultat <= 9:
        nom_sort = 'cauchemar'
        valeur = 1125
    if resultat == 10:
        nom_sort = 'chant de discorde'
        valeur = 1625
    if 11 <= resultat <= 12:
        nom_sort = 'chien de garde de Mordenkainen'
        valeur = 1125
    if resultat == 13:
        nom_sort = 'coffre secret de Léomund'
        valeur = 1125
    if 14 <= resultat <= 16:
        nom_sort = 'communication à distance'
        valeur = 1125
    if 17 <= resultat <= 19:
        nom_sort = 'cône de froid'
        valeur = 1125
    if 20 <= resultat <= 21:
        nom_sort = 'contact avec les plans'
        valeur = 1125
    if 22 <= resultat <= 23:
        nom_sort = 'contrat'
        valeur = 1125
    if 24 <= resultat <= 25:
        nom_sort = 'convocation de monstres V'
        valeur = 1125
    if 26 <= resultat <= 27:
        nom_sort = 'création majeure'
        valeur = 1125
    if 28 <= resultat <= 29:
        nom_sort = 'croissance animale'
        valeur = 1125
    if 30 <= resultat <= 31:
        nom_sort = 'débilité'
        valeur = 1125
    if 32 <= resultat <= 34:
        nom_sort = 'dissipation suprême'
        valeur = 1625
    if 35 <= resultat <= 36:
        nom_sort = 'domination'
        valeur = 1125
    if 37 <= resultat <= 38:
        nom_sort = 'fabrication'
        valeur = 1125
    if 39 <= resultat <= 40:
        nom_sort = 'faux-semblant'
        valeur = 1125
    if 41 <= resultat <= 42:
        nom_sort = 'flétrissement végétal'
        valeur = 1125
    if 43 <= resultat <= 44:
        nom_sort = 'image prédéterminée'
        valeur = 1125
    if 45 <= resultat <= 48:
        nom_sort = 'immobilisation de monstre'
        valeur = 1125
    if 49 <= resultat <= 50:
        nom_sort = 'leurre'
        valeur = 1375
    if 51 <= resultat <= 52:
        nom_sort = 'lien télépathique de Rary'
        valeur = 1125
    if 53 <= resultat <= 54:
        nom_sort = 'magie des ombres'
        valeur = 1125
    if 55 <= resultat <= 56:
        nom_sort = 'main interposée de Bigby'
        valeur = 1125
    if 57 <= resultat <= 59:
        nom_sort = 'métamorphose funeste'
        valeur = 1125
    if 60 <= resultat <= 61:
        nom_sort = 'mirage'
        valeur = 1125
    if 62 <= resultat <= 64:
        nom_sort = 'mur de force'
        valeur = 1125
    if 65 <= resultat <= 67:
        nom_sort = 'mur de pierre'
        valeur = 1125
    if 68 <= resultat <= 69:
        nom_sort = 'oeil indiscret'
        valeur = 1125
    if 70 <= resultat <= 72:
        nom_sort = 'passe-muraille'
        valeur = 1125
    if resultat == 73:
        nom_sort = 'permanence'
        valeur = 10125
    if resultat == 74:
        nom_sort = 'possession'
        valeur = 1125
    if 75 <= resultat <= 77:
        nom_sort = 'renvoi'
        valeur = 1125
    if 78 <= resultat <= 79:
        nom_sort = 'sanctuaire de Mordenkainen'
        valeur = 1125
    if resultat == 80:
        nom_sort = 'soins légers de groupe'
        valeur = 1625
    if resultat == 81:
        nom_sort = 'songe'
        valeur = 1125
    if resultat == 82:
        nom_sort = 'symbole de douleur'
        valeur = 2125
    if resultat == 83:
        nom_sort = 'symbole de sommeil'
        valeur = 2125
    if 84 <= resultat <= 85:
        nom_sort = 'télékinésie'
        valeur = 1125
    if 86 <= resultat <= 90:
        nom_sort = 'téléportation'
        valeur = 1125
    if 91 <= resultat <= 92:
        nom_sort = 'transmutation de la boue en pierre'
        valeur = 1125
    if 93 <= resultat <= 94:
        nom_sort = 'transmutation de la pierre en boue'
        valeur = 1125
    if 95 <= resultat <= 96:
        nom_sort = 'vague de fatigue'
        valeur = 1125
    if 97 <= resultat <= 100:
        nom_sort = 'vol supérieur'
        valeur = 1125
    return valeur, nom_sort


def lancer_sort_profane_6():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_sort = 'analyse d\'enchantement'
        valeur = 1650
    if resultat == 4:
        nom_sort = 'animation d\'objet'
        valeur = 2400
    if 5 <= resultat <= 6:
        nom_sort = 'annihilation de mort-vivant'
        valeur = 2150
    if 7 <= resultat <= 8:
        nom_sort = 'brume acide'
        valeur = 1650
    if 9 <= resultat <= 10:
        nom_sort = 'cercle de mort'
        valeur = 2150
    if 11 <= resultat <= 12:
        nom_sort = 'champ de force'
        valeur = 1650
    if 13 <= resultat <= 14:
        nom_sort = 'contrat intermédiaire'
        valeur = 1650
    if 15 <= resultat <= 16:
        nom_sort = 'contrôle de l\'eau'
        valeur = 1650
    if 17 <= resultat <= 18:
        nom_sort = 'convocation de monstres VI'
        valeur = 1650
    if resultat == 19:
        nom_sort = 'création de mort-vivant'
        valeur = 2350
    if resultat == 20:
        nom_sort = 'défense magique'
        valeur = 1650
    if 21 <= resultat <= 23:
        nom_sort = 'désintégration'
        valeur = 1650
    if 24 <= resultat <= 27:
        nom_sort = 'dissipation suprême'
        valeur = 1650
    if 28 <= resultat <= 29:
        nom_sort = 'double illusoire'
        valeur = 1650
    if 30 <= resultat <= 32:
        nom_sort = 'éclair multiple'
        valeur = 1650
    if 33 <= resultat <= 35:
        nom_sort = 'endurance de l\'ours de groupe'
        valeur = 1650
    if resultat == 36:
        nom_sort = 'festin des héros'
        valeur = 2400
    if 37 <= resultat <= 39:
        nom_sort = 'force de taureau de groupe'
        valeur = 1650
    if 40 <= resultat <= 41:
        nom_sort = 'glissement de terrain'
        valeur = 1650
    if 42 <= resultat <= 44:
        nom_sort = 'globe d\'invulnérabilité renforcée'
        valeur = 1650
    if 45 <= resultat <= 47:
        nom_sort = 'grâce féline de groupe'
        valeur = 1650
    if 48 <= resultat <= 49:
        nom_sort = 'héroïsme suprême'
        valeur = 1650
    if 50 <= resultat <= 51:
        nom_sort = 'image permanente'
        valeur = 1650
    if 52 <= resultat <= 53:
        nom_sort = 'image programmée'
        valeur = 1675
    if 54 <= resultat <= 55:
        nom_sort = 'main impérieuse de Bigby'
        valeur = 1650
    if 56 <= resultat <= 57:
        nom_sort = 'mauvais oeil'
        valeur = 1650
    if 58 <= resultat <= 59:
        nom_sort = 'mur de fer'
        valeur = 1700
    if resultat == 60:
        nom_sort = 'mythes et légendes'
        valeur = 1900
    if resultat == 61:
        nom_sort = 'orientation'
        valeur = 2400
    if 62 <= resultat <= 63:
        nom_sort = 'pétrification'
        valeur = 1650
    if resultat == 64:
        nom_sort = 'prévoyance'
        valeur = 1650
    if resultat == 65:
        nom_sort = 'quête'
        valeur = 1650
    if resultat == 66:
        nom_sort = 'remémoration de Mordenkainen'
        valeur = 1650
    if resultat == 67:
        nom_sort = 'résonance'
        valeur = 2400
    if 68 <= resultat <= 70:
        nom_sort = 'ruse du renard de groupe'
        valeur = 1650
    if 71 <= resultat <= 73:
        nom_sort = 'sagesse du hibou de groupe'
        valeur = 1650
    if resultat == 74:
        nom_sort = 'soins modérés de groupe'
        valeur = 2400
    if 75 <= resultat <= 76:
        nom_sort = 'sphère glaciale d\'Otiluke'
        valeur = 1650
    if 77 <= resultat <= 79:
        nom_sort = 'splendeur de l\'aigle de groupe'
        valeur = 1650
    if 80 <= resultat <= 81:
        nom_sort = 'suggestion de groupe'
        valeur = 1650
    if resultat == 82:
        nom_sort = 'symbole de persuasion'
        valeur = 6650
    if resultat == 83:
        nom_sort = 'symbole de terreur'
        valeur = 2650
    if 84 <= resultat <= 85:
        nom_sort = 'transformation de Tenser'
        valeur = 1950
    if 86 <= resultat <= 88:
        nom_sort = 'transmutation de la pierre en chair'
        valeur = 1650
    if 89 <= resultat <= 91:
        nom_sort = 'traversée des ombres'
        valeur = 1650
    if 92 <= resultat <= 94:
        nom_sort = 'vision lucide'
        valeur = 1950
    if 95 <= resultat <= 97:
        nom_sort = 'voile'
        valeur = 1650
    if 98 <= resultat <= 100:
        nom_sort = 'zone d\'antimagie'
        valeur = 1650
    return valeur, nom_sort


def lancer_sort_profane_7():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 3:
        nom_sort = 'aliénation mentale'
        valeur = 2275
    if 4 <= resultat <= 7:
        nom_sort = 'bannissement'
        valeur = 2275
    if 8 <= resultat <= 10:
        nom_sort = 'boule de feu à retardement'
        valeur = 2275
    if 11 <= resultat <= 13:
        nom_sort = 'cage de force'
        valeur = 3775
    if 14 <= resultat <= 16:
        nom_sort = 'changement de plan'
        valeur = 2275
    if 17 <= resultat <= 19:
        nom_sort = 'contrôle des morts-vivants'
        valeur = 2275
    if 20 <= resultat <= 22:
        nom_sort = 'contrôle du climat'
        valeur = 2275
    if 23 <= resultat <= 25:
        nom_sort = 'convocation d\'ombres suprême'
        valeur = 2275
    if 26 <= resultat <= 28:
        nom_sort = 'convocation de monstres VIII'
        valeur = 2275
    if 29 <= resultat <= 31:
        nom_sort = 'dissimulation suprême'
        valeur = 2275
    if 32 <= resultat <= 34:
        nom_sort = 'doigt de mort'
        valeur = 2275
    if 35 <= resultat <= 37:
        nom_sort = 'épée de Mordenkainen'
        valeur = 2275
    if 38 <= resultat <= 41:
        nom_sort = 'forme éthérée'
        valeur = 2275
    if 42 <= resultat <= 45:
        nom_sort = 'immobilisation de personne de groupe'
        valeur = 2275
    if 46 <= resultat <= 48:
        nom_sort = 'inversion de la gravité'
        valeur = 2275
    if 49 <= resultat <= 52:
        nom_sort = 'invisibilité de groupe'
        valeur = 2275
    if 53 <= resultat <= 54:
        nom_sort = 'invocation instantanée de Drawmij'
        valeur = 3775
    if 55 <= resultat <= 56:
        nom_sort = 'manoir somptueux de Mordenkainen'
        valeur = 2275
    if 57 <= resultat <= 59:
        nom_sort = 'mot de pouvoir aveuglant'
        valeur = 2275
    if 60 <= resultat <= 62:
        nom_sort = 'poigne de Bigby'
        valeur = 2275
    if 63 <= resultat <= 65:
        nom_sort = 'porte de phase'
        valeur = 2275
    if 66 <= resultat <= 68:
        nom_sort = 'projection d\'image'
        valeur = 2280
    if 69 <= resultat <= 72:
        nom_sort = 'rayons prismatiques'
        valeur = 2275
    if 73 <= resultat <= 75:
        nom_sort = 'renvoi des sorts'
        valeur = 2275
    if 76 <= resultat <= 78:
        nom_sort = 'scrutation suprême'
        valeur = 2275
    if resultat == 79:
        nom_sort = 'simulacre'
        valeur = 7275
    if resultat == 80:
        nom_sort = 'souhait limité'
        valeur = 3775
    if 81 <= resultat <= 82:
        nom_sort = 'statue'
        valeur = 2275
    if resultat == 83:
        nom_sort = 'symbole d\'étourdissement'
        valeur = 7275
    if resultat == 84:
        nom_sort = 'symbole de faiblesse'
        valeur = 7275
    if 85 <= resultat <= 87:
        nom_sort = 'téléportation d\'objet'
        valeur = 2275
    if 88 <= resultat <= 92:
        nom_sort = 'téléportation suprême'
        valeur = 2275
    if 93 <= resultat <= 95:
        nom_sort = 'vagues d\'épuisement'
        valeur = 2275
    if 96 <= resultat <= 98:
        nom_sort = 'vision magique suprême'
        valeur = 2275
    if 99 <= resultat <= 100:
        nom_sort = 'vision mystique'
        valeur = 3025
    return valeur, nom_sort


def lancer_sort_profane_8():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 4:
        nom_sort = 'animation suspendue'
        valeur = 3500
    if 5 <= resultat <= 6:
        nom_sort = 'attirance'
        valeur = 4500
    if 7 <= resultat <= 8:
        nom_sort = 'aversion'
        valeur = 3000
    if 9 <= resultat <= 12:
        nom_sort = 'charme-monstre de groupe'
        valeur = 3000
    if resultat == 13:
        nom_sort = 'clone'
        valeur = 4000
    if 14 <= resultat <= 16:
        nom_sort = 'contrat suprême'
        valeur = 3000
    if 17 <= resultat <= 19:
        nom_sort = 'convocation de monstres VIII'
        valeur = 3000
    if 20 <= resultat <= 22:
        nom_sort = 'corps de fer'
        valeur = 3000
    if 23 <= resultat <= 25:
        nom_sort = 'création de mort-vivant dominant'
        valeur = 3000
    if 26 <= resultat <= 28:
        nom_sort = 'cri suprême'
        valeur = 3000
    if 29 <= resultat <= 31:
        nom_sort = 'danse irrésistible d\'Otto'
        valeur = 3000
    if 32 <= resultat <= 34:
        nom_sort = 'dédale'
        valeur = 3000
    if 35 <= resultat <= 36:
        nom_sort = 'écran'
        valeur = 3000
    if 37 <= resultat <= 39:
        nom_sort = 'entrave'
        valeur = 8500
    if 40 <= resultat <= 42:
        nom_sort = 'esprit impénétrable'
        valeur = 3000
    if 43 <= resultat <= 45:
        nom_sort = 'exigence'
        valeur = 3600
    if 46 <= resultat <= 48:
        nom_sort = 'explosion de lumière'
        valeur = 3000
    if 49 <= resultat <= 51:
        nom_sort = 'flétrissure'
        valeur = 3000
    if 52 <= resultat <= 55:
        nom_sort = 'localisation suprême'
        valeur = 3000
    if 56 <= resultat <= 58:
        nom_sort = 'magie des ombres suprême'
        valeur = 3000
    if 59 <= resultat <= 61:
        nom_sort = 'métamorphose universelle'
        valeur = 3000
    if 62 <= resultat <= 64:
        nom_sort = 'moment de prescience'
        valeur = 3000
    if 65 <= resultat <= 67:
        nom_sort = 'mot de pouvoir étourdissant'
        valeur = 3000
    if 68 <= resultat <= 70:
        nom_sort = 'motif scintillant'
        valeur = 3000
    if 71 <= resultat <= 73:
        nom_sort = 'mur prismatique'
        valeur = 3000
    if 74 <= resultat <= 76:
        nom_sort = 'nuage incendiaire'
        valeur = 3000
    if 77 <= resultat <= 79:
        nom_sort = 'oeil indiscret suprême'
        valeur = 3000
    if 80 <= resultat <= 82:
        nom_sort = 'poing de Bigby'
        valeur = 3000
    if 83 <= resultat <= 86:
        nom_sort = 'protection contre les sorts'
        valeur = 3000
    if 87 <= resultat <= 89:
        nom_sort = 'rayon polaire'
        valeur = 3000
    if 90 <= resultat <= 91:
        nom_sort = 'séquestration'
        valeur = 13000
    if 92 <= resultat <= 95:
        nom_sort = 'sphère téléguidée d\'Otiluke'
        valeur = 3000
    if resultat == 96:
        nom_sort = 'symbole d\'aliénation mentale'
        valeur = 8000
    if resultat == 97:
        nom_sort = 'symbole de mort'
        valeur = 8000
    if 98 <= resultat <= 100:
        nom_sort = 'verrou dimensionnel'
        valeur = 3000
    return valeur, nom_sort


def lancer_sort_profane_9():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 4:
        nom_sort = 'absorption d\'énergie'
        valeur = 3825
    if 5 <= resultat <= 9:
        nom_sort = 'arrêt du temps'
        valeur = 3825
    if 10 <= resultat <= 12:
        nom_sort = 'capture d\'âme'
        valeur = 3825
    if 13 <= resultat <= 15:
        nom_sort = 'cercle de téléportation'
        valeur = 4825
    if 16 <= resultat <= 21:
        nom_sort = 'changement de forme'
        valeur = 3825
    if 22 <= resultat <= 25:
        nom_sort = 'convocation de monstres IX'
        valeur = 3825
    if 26 <= resultat <= 31:
        nom_sort = 'délivrance'
        valeur = 3825
    if 32 <= resultat <= 35:
        nom_sort = 'disjonction de Mordenkainen'
        valeur = 3825
    if 36 <= resultat <= 40:
        nom_sort = 'domination universelle'
        valeur = 3825
    if 41 <= resultat <= 44:
        nom_sort = 'emprisonnement'
        valeur = 3825
    if 45 <= resultat <= 48:
        nom_sort = 'ennemi subconscient'
        valeur = 3825
    if 49 <= resultat <= 52:
        nom_sort = 'immobilisation de monstre de groupe'
        valeur = 3825
    if 53 <= resultat <= 56:
        nom_sort = 'main broyeuse de Bigby'
        valeur = 3825
    if 57 <= resultat <= 61:
        nom_sort = 'mot de pouvoir mortel'
        valeur = 3825
    if 62 <= resultat <= 66:
        nom_sort = 'nuée de météores'
        valeur = 3825
    if 67 <= resultat <= 71:
        nom_sort = 'passage dans l\'éther'
        valeur = 3825
    if 72 <= resultat <= 75:
        nom_sort = 'plainte d\'outre-tombe'
        valeur = 3825
    if 76 <= resultat <= 80:
        nom_sort = 'portail'
        valeur = 8825
    if 81 <= resultat <= 84:
        nom_sort = 'prémonition'
        valeur = 3825
    if 85 <= resultat <= 87:
        nom_sort = 'projection astrale'
        valeur = 4825
    if 88 <= resultat <= 91:
        nom_sort = 'reflets d\'ombre'
        valeur = 3825
    if 92 <= resultat <= 95:
        nom_sort = 'refuge'
        valeur = 3825
    if resultat == 96:
        nom_sort = 'souhait'
        valeur = 28825
    if 97 <= resultat <= 100:
        nom_sort = 'spère prismatique'
        valeur = 3825
    return valeur, nom_sort


def lancer_sort_divin_0():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 7:
        nom_sort = 'assistance divine'
        valeur = 12
    if 8 <= resultat <= 14:
        nom_sort = 'blessure superficielle'
        valeur = 12
    if 15 <= resultat <= 21:
        nom_sort = 'création d\'eau'
        valeur = 12
    if 22 <= resultat <= 29:
        nom_sort = 'détection de la magie'
        valeur = 12
    if 30 <= resultat <= 36:
        nom_sort = 'détection du poison'
        valeur = 12
    if 37 <= resultat <= 43:
        nom_sort = 'illumination'
        valeur = 12
    if 44 <= resultat <= 50:
        nom_sort = 'lecture de la magie'
        valeur = 12
    if 51 <= resultat <= 58:
        nom_sort = 'lumière'
        valeur = 12
    if 59 <= resultat <= 65:
        nom_sort = 'purification de nourriture et d\'eau'
        valeur = 12
    if 66 <= resultat <= 72:
        nom_sort = 'réparation'
        valeur = 12
    if 73 <= resultat <= 79:
        nom_sort = 'repérage'
        valeur = 12
    if 80 <= resultat <= 86:
        nom_sort = 'résistance'
        valeur = 12
    if 87 <= resultat <= 93:
        nom_sort = 'soins superficiels'
        valeur = 12
    if 94 <= resultat <= 100:
        nom_sort = 'stimulant'
        valeur = 12
    return valeur, nom_sort


def lancer_sort_divin_1():
    resultat = random.randint(1, 100)
    if resultat == 1:
        nom_sort = 'alarme'
        valeur = 100
    if 2 <= resultat <= 3:
        nom_sort = 'anathème'
        valeur = 25
    if 4 <= resultat <= 5:
        nom_sort = 'aparisement des animaux'
        valeur = 25
    if 6 <= resultat <= 7:
        nom_sort = 'arme magique'
        valeur = 25
    if 8 <= resultat <= 9:
        nom_sort = 'baie nourricière'
        valeur = 25
    if 10 <= resultat <= 12:
        nom_sort = 'bénédictione'
        valeur = 25
    if resultat == 13:
        nom_sort = 'bénédiction d\'arme'
        valeur = 100
    if 14 <= resultat <= 16:
        nom_sort = 'bénédiction de l\'eau'
        valeur = 50
    if 17 <= resultat <= 18:
        nom_sort = 'blessure légère'
        valeur = 25
    if 19 <= resultat <= 20:
        nom_sort = 'bouclier de la foi'
        valeur = 25
    if 21 <= resultat <= 22:
        nom_sort = 'bouclier entropique'
        valeur = 25
    if 23 <= resultat <= 26:
        nom_sort = 'brume de dissimulation'
        valeur = 25
    if 27 <= resultat <= 28:
        nom_sort = 'charme-animal'
        valeur = 25
    if 29 <= resultat <= 30:
        nom_sort = 'communication avec les animaux'
        valeur = 25
    if 31 <= resultat <= 32:
        nom_sort = 'compréhension des langages'
        valeur = 25
    if 33 <= resultat <= 34:
        nom_sort = 'convocation d\'alliés naturels I'
        valeur = 25
    if 35 <= resultat <= 36:
        nom_sort = 'convocation de monstres I'
        valeur = 25
    if 37 <= resultat <= 38:
        nom_sort = 'détection de la faune ou de la flore'
        valeur = 25
    if 39 <= resultat <= 42:
        nom_sort = 'détection de la Loi/du Bien/du Chaos/du Mal'
        valeur = 25
    if 43 <= resultat <= 44:
        nom_sort = 'détection des collets et des fosses'
        valeur = 25
    if 45 <= resultat <= 46:
        nom_sort = 'détection des morts-vivants'
        valeur = 25
    if 47 <= resultat <= 48:
        nom_sort = 'enchevêtrement'
        valeur = 25
    if 49 <= resultat <= 52:
        nom_sort = 'endurance aux énerrgies destructives'
        valeur = 25
    if 53 <= resultat <= 54:
        nom_sort = 'faveur divine'
        valeur = 25
    if 55 <= resultat <= 56:
        nom_sort = 'flammes'
        valeur = 25
    if 57 <= resultat <= 58:
        nom_sort = 'frayeur'
        valeur = 25
    if 59 <= resultat <= 60:
        nom_sort = 'gourdin magique'
        valeur = 25
    if 61 <= resultat <= 62:
        nom_sort = 'grand pas'
        valeur = 25
    if 63 <= resultat <= 64:
        nom_sort = 'imprécation'
        valeur = 25
    if 65 <= resultat <= 67:
        nom_sort = 'injonction'
        valeur = 25
    if 68 <= resultat <= 69:
        nom_sort = 'invisibilité pour les animaux'
        valeur = 25
    if 70 <= resultat <= 71:
        nom_sort = 'invisibilité pour les morts-vivants'
        valeur = 25
    if 72 <= resultat <= 73:
        nom_sort = 'lueur féérique'
        valeur = 25
    if 74 <= resultat <= 75:
        nom_sort = 'malédiction de l\'eau'
        valeur = 50
    if 76 <= resultat <= 77:
        nom_sort = 'morsure magique'
        valeur = 25
    if 78 <= resultat <= 79:
        nom_sort = 'passage sans trace'
        valeur = 25
    if 80 <= resultat <= 81:
        nom_sort = 'perception de la mort'
        valeur = 25
    if 82 <= resultat <= 85:
        nom_sort = 'pierre magique'
        valeur = 25
    if 86 <= resultat <= 89:
        nom_sort = 'protection contre la Loi/le Bien/le Chaos/le Mal'
        valeur = 25
    if 90 <= resultat <= 91:
        nom_sort = 'regain d\'assurance'
        valeur = 25
    if 92 <= resultat <= 93:
        nom_sort = 'sanctuaire'
        valeur = 25
    if 94 <= resultat <= 95:
        nom_sort = 'saut'
        valeur = 25
    if 96 <= resultat <= 100:
        nom_sort = 'soins légers'
        valeur = 25
    return valeur, nom_sort


def lancer_sort_divin_2():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_sort = 'aide'
        valeur = 150
    if 3 <= resultat <= 4:
        nom_sort = 'ailignement indétectable'
        valeur = 150
    if 5 <= resultat <= 6:
        nom_sort = 'apaisement des émotions'
        valeur = 150
    if 7 <= resultat <= 8:
        nom_sort = 'arme alignée'
        valeur = 150
    if 9 <= resultat <= 10:
        nom_sort = 'arme spirituelle'
        valeur = 150
    if 11 <= resultat <= 12:
        nom_sort = 'augure'
        valeur = 175
    if 13 <= resultat <= 14:
        nom_sort = 'blessure modérée'
        valeur = 150
    if resultat == 15:
        nom_sort = 'bourrasque'
        valeur = 150
    if 16 <= resultat <= 17:
        nom_sort = 'cacophonie'
        valeur = 150
    if resultat == 18:
        nom_sort = 'consécration'
        valeur = 200
    if 19 <= resultat <= 20:
        nom_sort = 'convocation d\'alliés naturels II'
        valeur = 150
    if 21 <= resultat <= 22:
        nom_sort = 'convocation de monstres II'
        valeur = 150
    if 23 <= resultat <= 24:
        nom_sort = 'délivrance de la paralysie'
        valeur = 150
    if 25 <= resultat <= 26:
        nom_sort = 'détection des pièges'
        valeur = 150
    if 27 <= resultat <= 28:
        nom_sort = 'discours captivant'
        valeur = 150
    if 29 <= resultat <= 30:
        nom_sort = 'distorsion du bois'
        valeur = 150
    if 31 <= resultat <= 33:
        nom_sort = 'endurance de l\'ours'
        valeur = 150
    if resultat == 34:
        nom_sort = 'façonnage du bois'
        valeur = 150
    if 35 <= resultat <= 37:
        nom_sort = 'force de taureau'
        valeur = 150
    if resultat == 38:
        nom_sort = 'forme d\'arbre'
        valeur = 150
    if 39 <= resultat <= 40:
        nom_sort = 'fracassement'
        valeur = 150
    if 41 <= resultat <= 43:
        nom_sort = 'grâce féline'
        valeur = 150
    if resultat == 44:
        nom_sort = 'hypnose des animaux'
        valeur = 150
    if 45 <= resultat <= 46:
        nom_sort = 'immobilisation d\'animal'
        valeur = 150
    if 47 <= resultat <= 49:
        nom_sort = 'immobilisation de personne'
        valeur = 150
    if 50 <= resultat <= 51:
        nom_sort = 'lame de feu'
        valeur = 150
    if resultat == 52:
        nom_sort = 'messager animal'
        valeur = 150
    if resultat == 53:
        nom_sort = 'métal brûlant'
        valeur = 150
    if resultat == 54:
        nom_sort = 'métal gelé'
        valeur = 150
    if resultat == 55:
        nom_sort = 'mise à mort'
        valeur = 150
    if 56 <= resultat <= 57:
        nom_sort = 'nappe de brouillard'
        valeur = 150
    if 58 <= resultat <= 59:
        nom_sort = 'nuée grouillante'
        valeur = 150
    if 60 <= resultat <= 61:
        nom_sort = 'pattes d\'araignée'
        valeur = 150
    if 62 <= resultat <= 63:
        nom_sort = 'peau d\'écorce'
        valeur = 150
    if resultat == 64:
        nom_sort = 'piège à feu'
        valeur = 175
    if resultat == 65:
        nom_sort = 'préservation des morts'
        valeur = 150
    if resultat == 66:
        nom_sort = 'profanation'
        valeur = 200
    if 67 <= resultat <= 68:
        nom_sort = 'protection d\'autrui'
        valeur = 150
    if 69 <= resultat <= 71:
        nom_sort = 'ralentissement du poison'
        valeur = 150
    if resultat == 72:
        nom_sort = 'ramolissement de la terre et de la pierre'
        valeur = 150
    if resultat == 73:
        nom_sort = 'rapetissement d\'animal'
        valeur = 150
    if resultat == 74:
        nom_sort = 'rapport'
        valeur = 150
    if 75 <= resultat <= 76:
        nom_sort = 'réparation intégrale'
        valeur = 150
    if 77 <= resultat <= 79:
        nom_sort = 'résistance aux énergies destructives'
        valeur = 150
    if 80 <= resultat <= 82:
        nom_sort = 'restauration partielle'
        valeur = 150
    if 83 <= resultat <= 85:
        nom_sort = 'sagesse du hibou'
        valeur = 150
    if 86 <= resultat <= 87:
        nom_sort = 'silence'
        valeur = 150
    if 88 <= resultat <= 91:
        nom_sort = 'soins modérés'
        valeur = 150
    if 92 <= resultat <= 93:
        nom_sort = 'sphère de feu'
        valeur = 150
    if 94 <= resultat <= 96:
        nom_sort = 'splendeur de l\'aigle'
        valeur = 150
    if 97 <= resultat <= 98:
        nom_sort = 'ténèbres'
        valeur = 150
    if 99 <= resultat <= 100:
        nom_sort = 'zone de vérité'
        valeur = 150
    return valeur, nom_sort


def lancer_sort_divin_3():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_sort = 'animation des morts'
        valeur = 625
    if 3 <= resultat <= 4:
        nom_sort = 'appel de la foudre'
        valeur = 375
    if 5 <= resultat <= 6:
        nom_sort = 'blessure grave'
        valeur = 375
    if 7 <= resultat <= 8:
        nom_sort = 'cécité/surdité'
        valeur = 375
    if 9 <= resultat <= 16:
        nom_sort = 'cercle magique contre la Loi/le Bien/le Chaos/le Mal'
        valeur = 375
    if 17 <= resultat <= 18:
        nom_sort = 'collet'
        valeur = 375
    if 19 <= resultat <= 20:
        nom_sort = 'communication avec les morts'
        valeur = 375
    if 21 <= resultat <= 22:
        nom_sort = 'communication avec les plantes'
        valeur = 375
    if 23 <= resultat <= 24:
        nom_sort = 'contagion'
        valeur = 375
    if 25 <= resultat <= 26:
        nom_sort = 'convocation d\'alliés naturels III'
        valeur = 375
    if 27 <= resultat <= 28:
        nom_sort = 'convocation de monstres III'
        valeur = 375
    if 29 <= resultat <= 30:
        nom_sort = 'création de nourriture et d\'eau'
        valeur = 375
    if 31 <= resultat <= 32:
        nom_sort = 'croissance d\'épines'
        valeur = 375
    if 33 <= resultat <= 34:
        nom_sort = 'croissance végétale'
        valeur = 375
    if 35 <= resultat <= 36:
        nom_sort = 'délivrance des malédictions'
        valeur = 375
    if 37 <= resultat <= 38:
        nom_sort = 'dissimulation d\'objet'
        valeur = 375
    if 39 <= resultat <= 40:
        nom_sort = 'dissipation de la magie'
        valeur = 375
    if 41 <= resultat <= 42:
        nom_sort = 'domination d\'aniaml'
        valeur = 375
    if 43 <= resultat <= 44:
        nom_sort = 'extinction des feux'
        valeur = 375
    if 45 <= resultat <= 46:
        nom_sort = 'façonnage de la pierre'
        valeur = 375
    if resultat == 47:
        nom_sort = 'flamme éternelle'
        valeur = 425
    if 48 <= resultat <= 49:
        nom_sort = 'fusion dans la pierre'
        valeur = 375
    if 50 <= resultat <= 51:
        nom_sort = 'glyphe de garde'
        valeur = 575
    if resultat == 52:
        nom_sort = 'guérison de destrier'
        valeur = 375
    if 53 <= resultat <= 55:
        nom_sort = 'guérison de la cécité/surdité'
        valeur = 375
    if 56 <= resultat <= 57:
        nom_sort = 'guérison des maladies'
        valeur = 375
    if 58 <= resultat <= 59:
        nom_sort = 'localisation d\'objet'
        valeur = 375
    if 60 <= resultat <= 62:
        nom_sort = 'lumière brûlante'
        valeur = 375
    if 63 <= resultat <= 64:
        nom_sort = 'lumière du jour'
        valeur = 375
    if 65 <= resultat <= 66:
        nom_sort = 'main du berger'
        valeur = 375
    if 67 <= resultat <= 68:
        nom_sort = 'malédiction'
        valeur = 375
    if 69 <= resultat <= 70:
        nom_sort = 'marche sur l\'onde'
        valeur = 375
    if 71 <= resultat <= 72:
        nom_sort = 'morsure margique aggravée'
        valeur = 375
    if 73 <= resultat <= 74:
        nom_sort = 'mur de vent'
        valeur = 375
    if 75 <= resultat <= 76:
        nom_sort = 'négation de l\'invisibilité'
        valeur = 375
    if 77 <= resultat <= 79:
        nom_sort = 'neutralisation du poison'
        valeur = 375
    if 80 <= resultat <= 81:
        nom_sort = 'panoplie magique'
        valeur = 375
    if 82 <= resultat <= 84:
        nom_sort = 'prière'
        valeur = 375
    if 85 <= resultat <= 86:
        nom_sort = 'protection contre les énergies destructives'
        valeur = 375
    if 87 <= resultat <= 88:
        nom_sort = 'rabougrissement des plantes'
        valeur = 375
    if 89 <= resultat <= 91:
        nom_sort = 'respiration aquatique'
        valeur = 375
    if 92 <= resultat <= 95:
        nom_sort = 'soins importants'
        valeur = 375
    if 96 <= resultat <= 97:
        nom_sort = 'tempête de neige'
        valeur = 375
    if 98 <= resultat <= 99:
        nom_sort = 'ténèbres profondes'
        valeur = 375
    if resultat == 100:
        nom_sort = 'vision dans le noir'
        valeur = 375
    return valeur, nom_sort


def lancer_sort_divin_4():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_sort = 'allié d\'outreplan'
        valeur = 1200
    if 3 <= resultat <= 7:
        nom_sort = 'ancre dimensionnelle'
        valeur = 700
    if 8 <= resultat <= 10:
        nom_sort = 'antidétection'
        valeur = 750
    if 11 <= resultat <= 13:
        nom_sort = 'arme magique suprême'
        valeur = 700
    if 14 <= resultat <= 16:
        nom_sort = 'blessure critique'
        valeur = 700
    if 17 <= resultat <= 19:
        nom_sort = 'communication à distance'
        valeur = 700
    if 20 <= resultat <= 21:
        nom_sort = 'contrôle de l\'eau'
        valeur = 700
    if 22 <= resultat <= 24:
        nom_sort = 'convocation d\'alliés naturels IV'
        valeur = 700
    if 25 <= resultat <= 27:
        nom_sort = 'convocation de monstres IV'
        valeur = 700
    if 28 <= resultat <= 29:
        nom_sort = 'coquille antiplantes'
        valeur = 700
    if 30 <= resultat <= 32:
        nom_sort = 'détection du mensonge'
        valeur = 700
    if 33 <= resultat <= 34:
        nom_sort = 'divination'
        valeur = 725
    if 35 <= resultat <= 39:
        nom_sort = 'don des langues'
        valeur = 700
    if 40 <= resultat <= 41:
        nom_sort = 'empire végétal'
        valeur = 700
    if 42 <= resultat <= 44:
        nom_sort = 'empoisonnement'
        valeur = 700
    if 45 <= resultat <= 46:
        nom_sort = 'épée sainte'
        valeur = 700
    if 47 <= resultat <= 48:
        nom_sort = 'flétrissement végétal'
        valeur = 700
    if 49 <= resultat <= 52:
        nom_sort = 'immunité contre les sorts'
        valeur = 700
    if 53 <= resultat <= 57:
        nom_sort = 'liberté de mouvement'
        valeur = 700
    if 58 <= resultat <= 62:
        nom_sort = 'marche dans les aires'
        valeur = 700
    if 63 <= resultat <= 64:
        nom_sort = 'pierres acérées'
        valeur = 700
    if 65 <= resultat <= 69:
        nom_sort = 'protection contre la mort'
        valeur = 700
    if 70 <= resultat <= 72:
        nom_sort = 'puissance divine'
        valeur = 700
    if 73 <= resultat <= 74:
        nom_sort = 'réincarnation'
        valeur = 700
    if 75 <= resultat <= 77:
        nom_sort = 'renvoi'
        valeur = 700
    if 78 <= resultat <= 79:
        nom_sort = 'répulsif'
        valeur = 700
    if 80 <= resultat <= 84:
        nom_sort = 'restauration'
        valeur = 800
    if 85 <= resultat <= 86:
        nom_sort = 'rouille'
        valeur = 700
    if 87 <= resultat <= 92:
        nom_sort = 'soins intensifs'
        valeur = 700
    if 93 <= resultat <= 95:
        nom_sort = 'tempête de grêle'
        valeur = 700
    if 96 <= resultat <= 98:
        nom_sort = 'transfert de sorts'
        valeur = 700
    if 99 <= resultat <= 100:
        nom_sort = 'vermine géante'
        valeur = 700
    return valeur, nom_sort


def lancer_sort_divin_5():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 4:
        nom_sort = 'annulation d\'enchantement'
        valeur = 1125
    if 5 <= resultat <= 7:
        nom_sort = 'appel de la tempête'
        valeur = 1125
    if 8 <= resultat <= 11:
        nom_sort = 'arme destructrice'
        valeur = 1125
    if 12 <= resultat <= 14:
        nom_sort = 'blessure légère de groupe'
        valeur = 1125
    if 15 <= resultat <= 17:
        nom_sort = 'changement de plan'
        valeur = 1125
    if 18 <= resultat <= 20:
        nom_sort = 'colonne de feu'
        valeur = 1125
    if resultat == 21:
        nom_sort = 'communion'
        valeur = 1625
    if resultat <= 22:
        nom_sort = 'communion avec la nature'
        valeur = 1125
    if 23 <= resultat <= 24:
        nom_sort = 'contrôle des vents'
        valeur = 1125
    if 25 <= resultat <= 27:
        nom_sort = 'convocation d\'alliés naturels V'
        valeur = 1125
    if 28 <= resultat <= 30:
        nom_sort = 'convocation de monstres V'
        valeur = 1125
    if 31 <= resultat <= 33:
        nom_sort = 'croissance animale'
        valeur = 1125
    if resultat == 34:
        nom_sort = 'éveil'
        valeur = 2375
    if 35 <= resultat <= 37:
        nom_sort = 'exécution'
        valeur = 1125
    if 38 <= resultat <= 40:
        nom_sort = 'fléau d\'insectes'
        valeur = 1125
    if 41 <= resultat <= 43:
        nom_sort = 'force du colosse'
        valeur = 1125
    if 44 <= resultat <= 47:
        nom_sort = 'injonction suprême'
        valeur = 1125
    if resultat == 48:
        nom_sort = 'marque de la justice'
        valeur = 1125
    if 49 <= resultat <= 51:
        nom_sort = 'métamorphose funeste'
        valeur = 1125
    if 52 <= resultat <= 54:
        nom_sort = 'mur d\'épines'
        valeur = 1125
    if 55 <= resultat <= 57:
        nom_sort = 'mur de feu'
        valeur = 1125
    if 58 <= resultat <= 60:
        nom_sort = 'mur de pierre'
        valeur = 1125
    if 61 <= resultat <= 62:
        nom_sort = 'peau de pierre'
        valeur = 1375
    if 63 <= resultat <= 64:
        nom_sort = 'pénitence'
        valeur = 3625
    if 65 <= resultat <= 67:
        nom_sort = 'rappel à la vie'
        valeur = 6125
    if 68 <= resultat <= 71:
        nom_sort = 'rejet de la Loi/du Bien/du Chaos/du Mal'
        valeur = 1125
    if 72 <= resultat <= 74:
        nom_sort = 'résitance à la magie'
        valeur = 1125
    if 75 <= resultat <= 76:
        nom_sort = 'sanctification'
        valeur = 6125
    if 77 <= resultat <= 78:
        nom_sort = 'sanctification maléfique'
        valeur = 6125
    if 79 <= resultat <= 80:
        nom_sort = 'scrutation'
        valeur = 1125
    if 81 <= resultat <= 86:
        nom_sort = 'soins légers de groupe'
        valeur = 1125
    if resultat == 87:
        nom_sort = 'symbole de douleur'
        valeur = 2125
    if resultat == 88:
        nom_sort = 'symbole de sommeil'
        valeur = 2125
    if 89 <= resultat <= 91:
        nom_sort = 'transmutation de la boue en pierre'
        valeur = 1125
    if 92 <= resultat <= 94:
        nom_sort = 'transmutation de la pierre en boue'
        valeur = 1125
    if 95 <= resultat <= 98:
        nom_sort = 'vision lucide'
        valeur = 1375
    if 99 <= resultat <= 100:
        nom_sort = 'voyage par les arbres'
        valeur = 1125
    return valeur, nom_sort


def lancer_sort_divin_6():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 2:
        nom_sort = 'allié majeur d\'outreplan'
        valeur = 2400
    if 3 <= resultat <= 5:
        nom_sort = 'animation d\'objet'
        valeur = 1625
    if 6 <= resultat <= 8:
        nom_sort = 'annihilation de mort-vivant'
        valeur = 2125
    if 9 <= resultat <= 11:
        nom_sort = 'bannissement'
        valeur = 1625
    if 12 <= resultat <= 14:
        nom_sort = 'barrière de lame'
        valeur = 1625
    if 15 <= resultat <= 17:
        nom_sort = 'bâton à sort'
        valeur = 1625
    if 18 <= resultat <= 20:
        nom_sort = 'blessure modérée de groupe'
        valeur = 1625
    if 21 <= resultat <= 23:
        nom_sort = 'bois de fer'
        valeur = 1625
    if resultat == 24:
        nom_sort = 'chêne animé'
        valeur = 1625
    if 25 <= resultat <= 27:
        nom_sort = 'convocation d\'alliés naturels VI'
        valeur = 1625
    if 28 <= resultat <= 30:
        nom_sort = 'convocation de monstres VI'
        valeur = 1625
    if 31 <= resultat <= 33:
        nom_sort = 'coquille antivie'
        valeur = 1625
    if resultat == 34:
        nom_sort = 'création de mort-vivant'
        valeur = 1625
    if 35 <= resultat <= 38:
        nom_sort = 'dissipation suprême'
        valeur = 1625
    if 39 <= resultat <= 41:
        nom_sort = 'éloignement du bois'
        valeur = 1625
    if 42 <= resultat <= 45:
        nom_sort = 'endurance de l\'ours de groupe'
        valeur = 1625
    if 46 <= resultat <= 48:
        nom_sort = 'festin des héros'
        valeur = 1625
    if 49 <= resultat <= 52:
        nom_sort = 'force de taureau de groupe'
        valeur = 1625
    if 53 <= resultat <= 55:
        nom_sort = 'germes de feu'
        valeur = 1625
    if 56 <= resultat <= 58:
        nom_sort = 'glissement de terrain'
        valeur = 1625
    if resultat == 59:
        nom_sort = 'glyphe de garde suprême'
        valeur = 1625
    if 60 <= resultat <= 63:
        nom_sort = 'grâce féline de groupe'
        valeur = 1625
    if 64 <= resultat <= 66:
        nom_sort = 'guérison suprême'
        valeur = 1625
    if resultat == 67:
        nom_sort = 'interdiction'
        valeur = 4625
    if 68 <= resultat <= 70:
        nom_sort = 'mise à mal'
        valeur = 1625
    if 71 <= resultat <= 73:
        nom_sort = 'mot de rappel'
        valeur = 1625
    if 74 <= resultat <= 76:
        nom_sort = 'orientation'
        valeur = 1625
    if 77 <= resultat <= 79:
        nom_sort = 'pierres commères'
        valeur = 1625
    if resultat == 80:
        nom_sort = 'quête'
        valeur = 1625
    if 81 <= resultat <= 84:
        nom_sort = 'sagesse du hibou de groupe'
        valeur = 1625
    if 85 <= resultat <= 88:
        nom_sort = 'soins modérés de groupe'
        valeur = 1625
    if 89 <= resultat <= 92:
        nom_sort = 'splendeur de l\'aigle de groupe'
        valeur = 1625
    if resultat == 93:
        nom_sort = 'symbole de persuasion'
        valeur = 6625
    if resultat == 94:
        nom_sort = 'symbole de terreur'
        valeur = 2625
    if 95 <= resultat <= 97:
        nom_sort = 'vent divin'
        valeur = 1625
    if 98 <= resultat <= 100:
        nom_sort = 'voie végétale'
        valeur = 1625
    return valeur, nom_sort


def lancer_sort_divin_7():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 5:
        nom_sort = 'animation des plantes'
        valeur = 2275
    if 6 <= resultat <= 10:
        nom_sort = 'bâton sylvanien'
        valeur = 2275
    if 11 <= resultat <= 14:
        nom_sort = 'blasphème'
        valeur = 2275
    if 15 <= resultat <= 19:
        nom_sort = 'blessure importante de groupe'
        valeur = 2275
    if 20 <= resultat <= 24:
        nom_sort = 'champ de force'
        valeur = 2275
    if 25 <= resultat <= 26:
        nom_sort = 'contrôle du climat'
        valeur = 2275
    if 27 <= resultat <= 30:
        nom_sort = 'convocation d\'alliés naturels VII'
        valeur = 2275
    if 31 <= resultat <= 35:
        nom_sort = 'convocation de monstres VII'
        valeur = 2275
    if 36 <= resultat <= 39:
        nom_sort = 'décret'
        valeur = 2275
    if 40 <= resultat <= 44:
        nom_sort = 'destruction'
        valeur = 2275
    if 45 <= resultat <= 49:
        nom_sort = 'forme éthérée'
        valeur = 2275
    if 50 <= resultat <= 54:
        nom_sort = 'mort rampante'
        valeur = 2275
    if 55 <= resultat <= 57:
        nom_sort = 'parole du Chaos'
        valeur = 2275
    if 58 <= resultat <= 61:
        nom_sort = 'parole sacrée'
        valeur = 2275
    if 62 <= resultat <= 66:
        nom_sort = 'rayon de soleil'
        valeur = 2275
    if 67 <= resultat <= 71:
        nom_sort = 'refuge'
        valeur = 3275
    if 72 <= resultat <= 76:
        nom_sort = 'régénération'
        valeur = 2275
    if 77 <= resultat <= 80:
        nom_sort = 'restauration suprême'
        valeur = 4775
    if 81 <= resultat <= 82:
        nom_sort = 'résurrection'
        valeur = 12275
    if 83 <= resultat <= 87:
        nom_sort = 'scrutation suprême'
        valeur = 2275
    if 88 <= resultat <= 93:
        nom_sort = 'soins importants de groupe'
        valeur = 2275
    if resultat == 94:
        nom_sort = 'symbole d\'étourdissement'
        valeur = 7275
    if resultat == 95:
        nom_sort = 'symbole de faiblesse'
        valeur = 7275
    if 96 <= resultat <= 100:
        nom_sort = 'transmutation du métal en bois'
        valeur = 2275
    return valeur, nom_sort


def lancer_sort_divin_8():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 4:
        nom_sort = 'allié suprême d\'outreplan'
        valeur = 5500
    if 5 <= resultat <= 7:
        nom_sort = 'aura maudite'
        valeur = 3000
    if 8 <= resultat <= 10:
        nom_sort = 'aura sacrée'
        valeur = 3000
    if 11 <= resultat <= 14:
        nom_sort = 'blessure critique de groupe'
        valeur = 3000
    if 15 <= resultat <= 17:
        nom_sort = 'bouclier de la Loi'
        valeur = 3000
    if 18 <= resultat <= 21:
        nom_sort = 'contrôle des plantes'
        valeur = 3000
    if 22 <= resultat <= 25:
        nom_sort = 'convocation d\'alliés naturels VIII'
        valeur = 3000
    if 26 <= resultat <= 29:
        nom_sort = 'convocation de monstres VIII'
        valeur = 3000
    if 30 <= resultat <= 32:
        nom_sort = 'création de mort-vivant dominant'
        valeur = 3600
    if 33 <= resultat <= 36:
        nom_sort = 'cyclone'
        valeur = 3000
    if 37 <= resultat <= 40:
        nom_sort = 'doigt de mort'
        valeur = 3000
    if 41 <= resultat <= 45:
        nom_sort = 'éloignement du métal et de la pierre'
        valeur = 3000
    if 46 <= resultat <= 50:
        nom_sort = 'explosion de lumière'
        valeur = 3000
    if 51 <= resultat <= 54:
        nom_sort = 'immunité contre les sorts suprême'
        valeur = 3000
    if 55 <= resultat <= 58:
        nom_sort = 'inversion de la gravité'
        valeur = 3000
    if 59 <= resultat <= 62:
        nom_sort = 'localisation suprême'
        valeur = 3000
    if 63 <= resultat <= 65:
        nom_sort = 'manteau du Chaos'
        valeur = 3000
    if 66 <= resultat <= 69:
        nom_sort = 'métamorphose animale'
        valeur = 3000
    if 70 <= resultat <= 76:
        nom_sort = 'soins intensifs de groupe'
        valeur = 3000
    if 77 <= resultat <= 78:
        nom_sort = 'symbole d\'aliénation mentale'
        valeur = 8000
    if 79 <= resultat <= 80:
        nom_sort = 'symbole de mort'
        valeur = 8000
    if 81 <= resultat <= 84:
        nom_sort = 'tempête de feu'
        valeur = 3000
    if 85 <= resultat <= 89:
        nom_sort = 'tremblement de terre'
        valeur = 3000
    if 90 <= resultat <= 94:
        nom_sort = 'verrou dimensionnel'
        valeur = 3000
    if 95 <= resultat <= 100:
        nom_sort = 'zone d\'antimagie'
        valeur = 3000
    return valeur, nom_sort


def lancer_sort_divin_9():
    resultat = random.randint(1, 100)
    if 1 <= resultat <= 6:
        nom_sort = 'absorption d\'énergie'
        valeur = 3825
    if 7 <= resultat <= 10:
        nom_sort = 'attirance'
        valeur = 5325
    if 11 <= resultat <= 14:
        nom_sort = 'aversion'
        valeur = 3825
    if 15 <= resultat <= 19:
        nom_sort = 'capture d\'âme'
        valeur = 3825
    if 20 <= resultat <= 25:
        nom_sort = 'changement de forme'
        valeur = 3825
    if 26 <= resultat <= 31:
        nom_sort = 'convocation d\'alliés naturels IX'
        valeur = 3825
    if 32 <= resultat <= 37:
        nom_sort = 'convocation de monstres IX'
        valeur = 3825
    if 38 <= resultat <= 42:
        nom_sort = 'grand tertre'
        valeur = 3825
    if 43 <= resultat <= 51:
        nom_sort = 'guérison suprême de groupe'
        valeur = 3825
    if 52 <= resultat <= 58:
        nom_sort = 'implosion'
        valeur = 3825
    if 59 <= resultat <= 60:
        nom_sort = 'miracle'
        valeur = 28825
    if 61 <= resultat <= 66:
        nom_sort = 'nuée d\'élémentaires'
        valeur = 3825
    if 67 <= resultat <= 72:
        nom_sort = 'passage dans l\'éther'
        valeur = 3825
    if 73 <= resultat <= 78:
        nom_sort = 'portail'
        valeur = 8825
    if 79 <= resultat <= 84:
        nom_sort = 'prémonition'
        valeur = 3825
    if 85 <= resultat <= 87:
        nom_sort = 'projection astrale'
        valeur = 4870
    if 88 <= resultat <= 93:
        nom_sort = 'régénération'
        valeur = 3825
    if resultat == 94:
        nom_sort = 'résurrection suprême'
        valeur = 28825
    if 95 <= resultat <= 100:
        nom_sort = 'tempête vengeresse'
        valeur = 3825
    return valeur, nom_sort
