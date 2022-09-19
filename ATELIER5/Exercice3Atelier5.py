from multiprocessing.sharedctypes import Value
import random
from re import A

def choose_element_list(list_in_which_to_choose: list) -> object:
    """Fonction choisissant un élément au hasard

    Args:
        list_in_which_to_choose (list): liste contenant les éléments

    Returns:
        object: élément choisi
    """
    return list_in_which_to_choose[random.randint(0, len(list_in_which_to_choose) - 1)]

print(choose_element_list([i for i in range(10)]))