import time
import random
from Exercice2Atelier5 import mix_list

TAILLE_LISTE = [10,500,5000,50000,100000]
NBR_EXECUTION = 2

def somme(L: list) -> int:
    """Une troisième fonction qui permet de faire la somme d'une liste

    Args:
        L (list): Une liste de nombres

    Returns:
        int: retourne la somme des nombres
    """
    i = 0
    somme = 0
    while i <= len(L) - 1:
        somme += L[i]
        i += 1
    
    return somme

def perf_mix(foncUn, foncDeux, tailleListe: list, nbr_execution: int) -> tuple:

    resultatFonctionUn = []
    resultatFonctionDeux = []
    listeTestUn = [i for i in range(tailleListe)]
    listeTestDeux = [j for j in range(tailleListe)]

    for x in range(nbr_execution):
        start_pc_one = time.perf_counter()
        foncUn(listeTestUn)
        end_pc_one = time.perf_counter()
        temps_ecoule_one = end_pc_one - start_pc_one
        resultatFonctionUn.append(temps_ecoule_one)
    
    for y in range(nbr_execution):
        start_pc_two = time.perf_counter()
        foncDeux(listeTestDeux)
        end_pc_two = time.perf_counter()
        temps_ecoule_two = end_pc_two - start_pc_two
        resultatFonctionDeux.append(temps_ecoule_two)

    moyenneFonctionUn = somme(resultatFonctionUn) / NBR_EXECUTION
    moyenneFonctionDeux = somme(resultatFonctionDeux) / NBR_EXECUTION

    retourTuple = (moyenneFonctionUn, moyenneFonctionDeux)

    return retourTuple

print(perf_mix(mix_list, random.shuffle, TAILLE_LISTE[4], NBR_EXECUTION))