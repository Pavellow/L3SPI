def positionFor(L: list, e: int) -> int:
    """Une fonction qui permet de renvoyer la position de l'entier donné dans la liste en utilisant la boucle for

    Args:
        L (list): liste où sont présents les entiers
        e (int): entier rentré par l'utilisateur

    Returns:
        int: position de la liste de l'entier e
    """
    for i in range(len(L)):
        if L[i] == e:
            indice = L.index(e)
            return indice

    for i in range(len(L)):
        if L[i] != e:
            return -1

def positionWhile(L: list, e: int) -> int:
    """Une fonction qui permet de renvoyer la position de l'entier donné dans la liste en utilisant la boucle while

    Args:
        L (list): liste où sont présents les entiers
        e (int): entier rentré par l'utilisateur

    Returns:
        int: position de la liste de l'entier e
    """
    i = 0
    while i <= len(L):
        if L[i] == e:
            indice = L.index(e)
            return indice

        if L[i] != e:
            i += 1

        if e not in L:
            return -1

def nb_occurences(L: list, e: int) -> int:
    """Une fonction qui donne combien de fois apparait dans la liste donnée l'entier donnée par l'utilisateur

    Args:
        L (list): liste où sont présents les nombres
        e (int): entier entré par l'utilisateur

    Returns:
        int: nombre de fois où l'entier apparait
    """
    nbOccurence = 0
    for element in L:
        if e == element:
            nbOccurence += 1

    return nbOccurence

def est_triee_for(L: list) -> bool:
    """Fonction permettant de vérifier si la liste est triée en utilisant la boucle for

    Args:
        L (list): Liste où sont présents les nombres

    Returns:
        bool: Renvoie True si la liste est triée sinon False
    """
    for i in range(len(L)):
        if L[i] < L[i+1]:
            i+=1
            if i == (len(L)-1) and L[i] >= L[i-1]:
                return True
        else:
            return False
    
def est_triee_while(L: list) -> bool:
    """Fonction permettant de vérifier si la liste est triée en utilisant la boucle while

    Args:
        L (list): Liste où sont présents les nombres

    Returns:
        bool: Renvoie True si la liste est triée sinon False
    """
    i = 0
    while i <= len(L):
        if L[i] < L[i+1]:
            i+=1
            if i == (len(L)-1) and L[i] >= L[i-1]:
                return True
        else:
            return False

def position_tri(L: list, e: int) -> int:
    """Fonction permettant de donner la position d'un élément entré par l'utilisateur dans la liste de manière dichotomique

    Args:
        L (list): Liste de nombre
        e (int): entier entré par l'utilisateur

    Returns:
        int: renvoie la position de l'élément demandé par l'utilisateur
    """
    milieuListe = 0
    debut = 0
    fin = len(L)
    trouve = False

    while trouve != True and debut <= fin:
        milieuListe = (debut + fin) // 2
        if L[milieuListe] == e:
            trouve = True
        else:
            if e > L[milieuListe]:
                debut = milieuListe + 1
            else:
                if e > L[milieuListe]:
                    début = milieuListe + 1
                else:
                    fin = milieuListe - 1
    
    if trouve == True:
        print("La valeur", e, "est au rang", milieuListe)
    else:
        print("La valeur", e, "n'est pas dans le tableau")

def a_repetition(L: list) -> bool:
    """Fonction permettant de détecter les répétitions dans L

    Args:
        L (list): Liste de nombre

    Returns:
        bool: renvoie la position de l'élément demandé par l'utilisateur
    """
    T = []
    i = 0
    x = 0
    repetitionDansListe = False
    while i <= len(L):
        if x in T:
            T.append(x)
        else:
            repetitionDansListe = True
            print("il y a répétition")
            return repetitionDansListe

#print(e, "est situé à la position", positionFor(L, e), " pour les développeurs et est situé à la position", positionWhile(L, e) + 1, "pour tout être humain normal")
#print(e, "apparaît", nb_occurences(L, e), "fois dans la liste")

L1 = [10,11,12,13,14,15,16] #triée
L2 = [10,11,12,13,13,14,15,16] #triée et répétition
L3 = [10,12,11,13,14,16,15] #non triée
L4 = [11,10,12,13,14,15,16] #premières valeurs non triées
L5 = [10,11,12,13,14,16,15] #dernières valeurs non triées

e = 1

a_repetition(L1)
a_repetition(L2)