import random

def mix_list(list_to_mix: list) -> list:
    """Fonction mélangeant la liste entrée

    Args:
        list_to_mix (list): liste triée

    Returns:
        list: liste mélangée
    """
    #Copie de la liste triée
    retourListe = list_to_mix.copy()
    #Boucle for avec un démarrage d'un entier de la taille de la liste, un arrêt à 0, avec un pas de -1
    for i in range(len(retourListe) - 1): 
        #On génère un nombre aléatoire avec une marge de plus en plus grande au fur et à mesure qu'on avance dans l'algorithme
        aleatoire = random.randint(0, i) 
        #On échange les valeurs
        retourListe[i], retourListe[aleatoire] = retourListe[aleatoire], retourListe[i] 
    
    return retourListe

listeAMixer = [20,21,22,23,24,25,26,27,28,29,30]

print("Liste initiale :",listeAMixer,"\n","Liste mélangée :", mix_list(listeAMixer))
