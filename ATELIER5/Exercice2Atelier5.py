import random

def mix_list(list_to_mix: list) -> list:
    """Fonction mélangeant la liste entrée

    Args:
        list_to_mix (list): liste triée

    Returns:
        list: liste mélangée
    """
    retourListe = list_to_mix.copy() #copie de la liste triée
    for i in range(len(list_to_mix) - 1, 0, -1): #boucle for avec un démarrage d'un entier de la taille de la liste, un arrêt à 0, avec un pas de -1
        aleatoire = random.randint(0, i+1) #on génère un nombre aléatoire avec une marge de plus en plus grande au fur et à mesure qu'on avance dans l'algorithme
        retourListe[i], retourListe[aleatoire] = retourListe[aleatoire], retourListe[i] #on échange les valeurs

    return retourListe

listeAMixer = [1,2,3,4,5,6,7,8,9]

print(listeAMixer, mix_list(listeAMixer))
