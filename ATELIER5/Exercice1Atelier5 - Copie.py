import random

def gen_list_random_int(int_nbr: int, int_binf: int, int_bsup: int) -> list:
    """fonction qui génère une liste de valeurs aléatoires

    Args:
        int_nbr (int): taille de la liste
        int_binf (int): valeur inférieure
        int_bsup (int): valeur supérieure

    Returns:
        list: liste créée par la fonction
    """
    retourListe = []
    for i in range(int_nbr):
        nbrAleatoire = random.randint(int_binf, int_bsup)
        retourListe.append(nbrAleatoire)
    
    return retourListe

print(gen_list_random_int(3, 5, 24))