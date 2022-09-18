import matplotlib as plt

def histo(F: list) -> list:
    """Fonction permettant de définir l'histogramme d'une liste (je ne sais plus ce qu'est un histogramme (à enlever après recherche))

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """
    maximum = max(F) + 1
    H = [0] * maximum
    
    for i in F:
        H[i] += 1
    
    return H

def est_injective(F: list) -> bool:
    H = histo(F)

    estInjective = True

    for element in H:
        if element > 1:
            estInjective = False

    return estInjective

def est_surjective(F: list) -> bool:
    H = histo(F)

    estSurjective = True

    for element in H:
        if element < 1:
            estSurjective = False

    return estSurjective

def est_bijective(F: list) -> bool:
    H = histo(F)

    estBijective = True

    estInjective = est_injective(F)
    estSurjective = est_surjective(F)

    if not estInjective and not estSurjective:
            estBijective = False

    return estBijective



L1 = [6,5,6,7,4,2,1,5]
L2 = [3,0,6,7,4,2,1,5]

#print(est_injective(L1))
#print(est_injective(L2))
print(est_bijective(L1))
print(est_bijective(L2))