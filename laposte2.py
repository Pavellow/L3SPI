listeTypeCourrier = ["lettre verte", "lettre priotitaire", "ecopli", "colissimo eco outre mer", "cecogramme"]

choixTypeCourrier = int(input("Entre le nombre correspondant : lettre verte [0], lettre prioritaire [1], ecopli [2], colissimo eco outre-mer [3], cécogramme [4]"))

def foncEnvoieOutreMer():
    envoieOutreMer = input("Envoie en outre mer ?")
    if envoieOutreMer == "True":
        return True
    if envoieOutreMer == "False":
        return False

def tarifLettreVerte(poids: int, envoieOutreMer: bool) -> float:
    tarif = None
    categoriePoids = [20, 100, 250, 500, 1000, 3000]
    tarifNet = [1.16, 2.32, 4, 6, 7.5, 10.5]
    #Pour un envoie hors outre mer
    for i in range(len(categoriePoids)):
        if foncEnvoieOutreMer() == False:
            #En dessous de 20g
            if poids <= categoriePoids[1]:
                tarif = tarifNet[1]
            #Entre 20g et 3 kilos
            if poids > categoriePoids[i] and poids <= categoriePoids[i+1]:
                tarif = tarifNet[i]
            #Au delà de 3 kilos
            if poids > categoriePoids[5]: print("Erreur, le colis est trop lourd")
    return tarif

########################################################################################################################################################

if choixTypeCourrier == 0:
    poids = int(input("Entrez le poids du colis"))
    tarifLettreVerte(poids, foncEnvoieOutreMer())
    print(tarifLettreVerte)
    input()

if choixTypeCourrier == 1:
    print("lettre priotitaire")

if choixTypeCourrier == 2:
    print("ecopli")

if choixTypeCourrier == 3:
    print("colissimo eco outre mer")

if choixTypeCourrier == 4:
    print("cecogramme")

#rip