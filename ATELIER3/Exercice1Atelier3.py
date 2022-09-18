def full_name(str_arg: str) -> str:
    temp = str_arg.split()
    nom = temp[0]
    prenom = temp[1]
    nom = nom.upper()
    prenom = prenom.capitalize()
    fullName = nom + " " + prenom
    return fullName

def positionArobase(temp: list) -> int:
    i = 0
    arobase = "@"
    while i <= len(temp) - 1:
        if temp[i] == arobase:
            indice = temp.index(arobase)
            return indice
    

        if temp[i] != arobase:
            i += 1

def is_mail(str_arg: str) -> tuple:

    temp = []
    tempCorps = []

    erreur = (0,0)

    arobase = positionArobase(str_arg)

    corps = str_arg[:arobase]
    nom_domaine = "univ-corse"
    pays = ".fr"
    arobase = str_arg[-14]

    for element in corps:
        tempCorps.append(element)

    
    
    temp.append(tempCorps)
    temp.append(arobase)
    temp.append(nom_domaine)
    temp.append(pays)

    print(temp)

    if "@" not in temp:
        print("Arobase manquant dans l'adresse mail")
        erreur = (0,2)
    if temp[2] != nom_domaine:
        print("Le nom de domaine n'est pas valide")
        erreur = (0,3)
    if temp[3] != pays:
        print("Il manque le .")
        erreur = (0,4)

    for i in range(len(tempCorps)):
        if tempCorps[0] == "." or tempCorps[-1] == ".":
            print("Point au début ou à la fin du corps")
            erreur = (0,1)
        if tempCorps[i] == "." and tempCorps[i+1] == ".":
            print("Deux points se suivent dans le corps")
            erreur = (0,1)
        else:
            erreur = (1,656)

    return erreur

    

nom_prenom = "bisgambiglia@univ-corse.fr"

print(is_mail(nom_prenom))
