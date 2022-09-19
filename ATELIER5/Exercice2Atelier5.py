import random

def mix_list(list_to_mix: list) -> list:
    """Fonction mélangeant la liste entrée

    Args:
        list_to_mix (list): liste triée

    Returns:
        list: liste mélangée
    """
    retourListe = list_to_mix.copy() #copie de la liste triée
    print(retourListe)
    for i in range(len(retourListe) - 1, 0, -1): #boucle for avec un démarrage d'un entier de la taille de la liste, un arrêt à 0, avec un pas de -1
        aleatoire = random.randint(0, i+1) #on génère un nombre aléatoire avec une marge de plus en plus grande au fur et à mesure qu'on avance dans l'algorithme
        retourListe[i], retourListe[aleatoire] = retourListe[aleatoire], retourListe[i] #on échange les valeurs
        #changement valeur logique XOR (NEFONCTIONNEPAS)
        """
        retourListe[i] = retourListe[i] ^ retourListe[aleatoire]
        retourListe[aleatoire] = retourListe[i] ^ retourListe[aleatoire]
        retourListe[i] = retourListe[i] ^ retourListe[aleatoire]
        """

    return retourListe

def mixlistdeux(list_to_mix: list) -> list:
    """fonction mélangeant une liste

    Args:
        list_to_mix (list): liste de nombre triée

    Returns:
        list: liste mélangée
    """

listeAMixer = [20,21,22,23,24,25,26,27,28,29,30]

print(mix_list(listeAMixer))
