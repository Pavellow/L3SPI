from Exercice3Atelier5 import choose_element_list

def extract_elements_list(list_in_which_to_choose: list, int_number_of_element_to_extract: int) -> list:
    """fonction permettant de choisir un sample d'une liste

    Args:
        list_in_which_to_choose (list): liste contenant les éléments
        int_number_of_element_to_extract (int): nombre d'éléments à extraire

    Returns:
        list: éléments choisis entrés dans une liste
    """
    retourListe = [] #liste temporaire
    for i in range(int_number_of_element_to_extract):
        element = choose_element_list(list_in_which_to_choose) #on stocke l'élément choisi dans une var
        if element not in retourListe: #si l'élément est ajouté pour la première fois dans la liste
            retourListe.append(element) #bah on l'ajoute
        else: #sinon
            element = choose_element_list(list_in_which_to_choose) #on choisit un autre élément
            retourListe.append(element) #et on le stocke

    return retourListe

liste = [5, "ALBERT", (3, 4), "A", False, 64.32, ["l","i","s","t","e"]]

print(liste, extract_elements_list(liste, 3))