import random


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
