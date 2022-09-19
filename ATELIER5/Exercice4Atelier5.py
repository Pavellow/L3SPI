from Exercice3Atelier5 import choose_element_list
import random

def extract_elements_list(list_in_which_to_choose: list, int_number_of_element_to_extract: int) -> list:
    """fonction permettant de choisir un sample d'une liste

    Args:
        list_in_which_to_choose (list): liste contenant les éléments
        int_number_of_element_to_extract (int): nombre d'éléments à extraire

    Returns:
        list: éléments choisis entrés dans une liste
    """
    i = 0
    retourListe = [] #liste temporaire
    while i < int_number_of_element_to_extract:
        element = choose_element_list(list_in_which_to_choose) #on stocke l'élément choisi dans une var
        if element not in retourListe: #si l'élément est ajouté pour la première fois dans la liste
            retourListe.append(element)
            i += 1
    return retourListe

liste = [i for i in range(20)]

print("fonction random.sample :", random.sample(liste, 5))
print("fonction créée par nous :", extract_elements_list(liste, 5))