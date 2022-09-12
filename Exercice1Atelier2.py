L = [420,2,4,6,8,7,10,12,16]

def sommeUn(L: list) -> int:
    """Une fonction qui permet de faire la somme d'une liste

    Args:
        L (list): Une liste de nombres

    Returns:
        int: retourne la somme des nombres
    """
    somme = 0
    for i in range(len(L)):
        somme += L[i]
    
    return somme

def sommeDeux(L: list) -> int:
    """Une autre fonction qui permet de faire la somme d'une liste

    Args:
        L (list): Une liste de nombres

    Returns:
        int: retourne la somme des nombres
    """
    somme = 0
    for i in L:
        somme += i
    
    return(somme)

def sommeTrois(L: list) -> int:
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

def test_exercice1():
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide :", sommeTrois([]))
    #test somme 11111
    S = [1, 10, 100, 1000, 10000]
    print("Test somme 1111 :", sommeTrois(S))

def moyenne(L: list) -> float:
    """Fonction permettant de calculer la moyenne des nombres d'une liste

    Args:
        L (list): liste de nombre

    Returns:
        float: moyenne
    """

    moyenne = sommeTrois(L) / len(L)

    return moyenne

def nb_sup1(L: list, e: float) -> int:
    """Fonction permettant de retourner le nombre de valeurs supérieures à la valeur entrée par l'utilisateur version boucle while

    Args:
        L (list): liste de nombre
        e (float): entier entré par l'utilisateur

    Returns:
        int: retourne le nombre de valeurs supérieures à e
    """
    i = 0
    nbSuperieur = 0
    while i <= len(L) - 1:
        if L[i] > e:
            nbSuperieur += 1
        i += 1

    return nbSuperieur

def nb_sup2(L: list, e: float) -> int:
    """Fonction permettant de retourner le nombre de valeurs supérieures à la valeur entrée par l'utilisateur version boucle for

    Args:
        L (list): liste de nombre
        e (float): entier entré par l'utilisateur

    Returns:
        int: retourne le nombre de valeurs supérieures à e
    """
    nbSuperieur = 0
    for i in range(len(L)):
        if L[i] > e:
            nbSuperieur += 1
    
    print(nbSuperieur)
    return nbSuperieur

def nb_sup3(L: list, e: float) -> int:
    """Fonction permettant de retourner le nombre de valeurs supérieures à la valeur entrée par l'utilisateur version boucle for 2

    Args:
        L (list): liste de nombre
        e (float): entier entré par l'utilisateur

    Returns:
        int: retourne le nombre de valeurs supérieures à e
    """
    nbSuperieur = 0
    for element in L:
        if element > e:
            nbSuperieur += 1
    
    return nbSuperieur

def get_nb_sup(L: list, e: int) -> list:
    """Fonction permettant de retourner les valeurs supérieures à la valeur entrée par l'utilisateur version boucle for

    Args:
        L (list): liste de nombre
        e (float): entier entré par l'utilisateur

    Returns:
        list: retourne une liste comprennant les valeurs supérieures à e dans L
    """
    listeNbSup = []
    for i in range(len(L)):
        if L[i] > e:
            listeNbSup.append(L[i])
    
    return listeNbSup

def moy_sup(L: list, e: int) -> float:
    """Fonction permettant de retourner la moyenne des valeurs supérieures à la valeur entrée par l'utilisateur version boucle for

    Args:
        L (list): liste de nombre
        e (float): entier entré par l'utilisateur

    Returns:
        float: retourne la moyenne des valeurs supérieures à e dans L
    """
    moyenneSup = 0
    nbSup = get_nb_sup(L,e)
    sommeSup = sommeTrois(nbSup)

    moyenneSup = sommeSup / nb_sup3(L, e)
    
    return moyenneSup

def val_max(L: list) -> float:
    """Fonction permettant de retourner la valeur maximale de la liste

    Args:
        L (list): liste de nombre

    Returns:
        float: retourne le nombre le plus haut de la liste
    """
    valMax = L[0]
    for element in L:
        if element >= valMax:
            valMax = element
    
    return valMax

def ind_max(L: list) -> int:
    """Fonction permettant de retourner l'indice de la valeur maximale de la liste

    Args:
        L (list): liste de nombre

    Returns:
        int: retourne l'indice de la valeur max
    """
    return L.index(val_max(L))


        


#print("Première fonction par indice :", sommeUn(L))
#print("Deuxième fonction par éléments:",sommeDeux(L))
#print("Deuxième fonction par while:",sommeTrois(L))

#test_exercice1()
#moyenne(L)
#nb_sup1(L, 7)
#nb_sup2(L, 8)
print("Nombre d'éléments au dessus de e: ",nb_sup3(L, 3))
print("Valeurs des indices au dessus de e:", get_nb_sup(L, 3))
print("Moyenne des éléments supérieurs à e:", moy_sup(L, 3))
print("Valeur maximale de L:", val_max(L))
print("Indice de la valeur maximale:", ind_max(L))