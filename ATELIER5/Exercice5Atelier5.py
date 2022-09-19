import time
import random
from Exercice2Atelier5 import mix_list
from Exercice4Atelier5 import extract_elements_list

import matplotlib.pyplot as plt
import numpy as np

TAILLE_LISTE = [10,500,5000,50000,100000,1000000]
NBR_EXECUTION = 25
NBR_SAMPLE = 20

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

    for nbr in range(len(TAILLE_LISTE) - 1):
        listeTest = [i for i in range(TAILLE_LISTE[nbr])]
        for x in range(nbr_execution):
            start_pc_one = time.perf_counter()
            foncUn(listeTest)
            end_pc_one = time.perf_counter()
            temps_ecoule_one = end_pc_one - start_pc_one
            resultatFonctionUn.append(temps_ecoule_one)
        for y in range(nbr_execution):
            start_pc_two = time.perf_counter()
            foncDeux(listeTest)
            end_pc_two = time.perf_counter()
            temps_ecoule_two = end_pc_two - start_pc_two
            resultatFonctionDeux.append(temps_ecoule_two)


    moyenneFonctionUn = somme(resultatFonctionUn) / NBR_EXECUTION
    moyenneFonctionDeux = somme(resultatFonctionDeux) / NBR_EXECUTION

    retourTuple = (moyenneFonctionUn, moyenneFonctionDeux)

    return retourTuple

def perf_sample(foncUn, foncDeux, tailleListe: list, nbr_execution: int, nbr_sample: int) -> tuple:

    resultatFonctionUn = []
    resultatFonctionDeux = []
    listeTest = [i for i in range(tailleListe)]

    for nbr in range(len(TAILLE_LISTE) - 1):
        listeTest = [i for i in range(TAILLE_LISTE[nbr])]
        for x in range(nbr_execution):
            start_pc_one = time.perf_counter()
            foncUn(listeTest, nbr_sample)
            end_pc_one = time.perf_counter()
            temps_ecoule_one = end_pc_one - start_pc_one
            resultatFonctionUn.append(temps_ecoule_one)
        
        for y in range(nbr_execution):
            start_pc_two = time.perf_counter()
            foncDeux(listeTest, nbr_sample)
            end_pc_two = time.perf_counter()
            temps_ecoule_two = end_pc_two - start_pc_two
            resultatFonctionDeux.append(temps_ecoule_two)

    moyenneFonctionUn = somme(resultatFonctionUn) / NBR_EXECUTION
    moyenneFonctionDeux = somme(resultatFonctionDeux) / NBR_EXECUTION

    retourTuple = (moyenneFonctionUn, moyenneFonctionDeux)

    return retourTuple

#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
x_axis_list = np.arange(0,5.5,0.5)
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de
#choisir éventuellement la couleur et le marqueur
ax.plot(perf_mix(mix_list, random.shuffle, TAILLE_LISTE[2], NBR_EXECUTION),'bo-',label='Fonction de mix')
ax.plot(perf_sample(extract_elements_list, random.sample, TAILLE_LISTE[2], NBR_EXECUTION, NBR_SAMPLE), 'r*-', label='Fonction de samplage')
ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
title='Fonctions identité, cube et carré')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()

print(perf_mix(mix_list, random.shuffle, TAILLE_LISTE[2], NBR_EXECUTION))
print(perf_sample(extract_elements_list, random.sample, TAILLE_LISTE[4], NBR_EXECUTION, NBR_SAMPLE))