import random
import os
import time
#Noms variables ################
question = True
nomJoueurUn = None
nomJoueurDeux = None
score = [0,0]
isActive = True
choixJoueurUn = None
choixJoueurDeux = None
tableauChoix = ["papier", "cailloux", "ciseaux", "puits"]
#Fonctions ##############
def pcc():
    if choixJoueurUn == tableauChoix[0] and choixJoueurDeux == tableauChoix[1]:
        score[0] += 1
    if choixJoueurUn == tableauChoix[1] and choixJoueurDeux == tableauChoix[2]:
        score[0] += 1
    if choixJoueurUn == tableauChoix[2] and choixJoueurDeux == tableauChoix[0]:
        score[0] += 1
    if choixJoueurDeux == tableauChoix[0] and choixJoueurUn == tableauChoix[1]:
        score[1] += 1
    if choixJoueurDeux == tableauChoix[1] and choixJoueurUn == tableauChoix[2]:
        score[1] += 1
    if choixJoueurDeux == tableauChoix[2] and choixJoueurUn == tableauChoix[0]:
        score[1] += 1
    if choixJoueurUn == tableauChoix[3] and choixJoueurDeux == tableauChoix[1]:
        score[0] += 1
    if choixJoueurDeux == tableauChoix[3] and choixJoueurUn == tableauChoix[1]:
        score[1]+= 1
    if choixJoueurUn == tableauChoix[3] and choixJoueurDeux == tableauChoix[2]:
        score[0] += 1
    if choixJoueurDeux == tableauChoix[3] and choixJoueurUn == tableauChoix[2]:
        score[1]+= 1
    if choixJoueurUn == tableauChoix[3] and choixJoueurDeux == tableauChoix[0]:
        score[1] += 1
    if choixJoueurDeux == tableauChoix[3] and choixJoueurUn == tableauChoix[0]:
        score[0]+= 1

def tryAgain():
    recommencer = str(input("Voulez-vous recommencer ? O/N" ))
    if recommencer == "O":
        score[0] = 0
        score[1] = 0
        isActive = True
    else:
        isActive = False
#### Programme ####
questionInitiale = str(input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ?" ))

if questionInitiale == "O":
    nomJoueurUn = str(input("Quel est votre nom ?"))
    print("Bienvenue ", nomJoueurUn, " nous allons jouer ensemble ! \n")
    nomJoueurDeux = "Machine"
    while isActive:
        os.system("cls")
        os.system("color e")
        print("Le score est de ", score[0], "(J1) - (J2)", score[1])
        choixJoueurUn = str(input("papier, cailloux, ciseaux ?"))
        i = random.randint(0, 3)
        choixJoueurDeux = tableauChoix[i]
        pcc()
        print("\nLe joueur 2 a choisi", choixJoueurDeux)
        print("Le score est de ", score[0], "-", score[1])
        time.sleep(1)
        if score[0] == 3 or score[1] == 3:
            if score[0] == 3:
                print(nomJoueurUn, "a gagné")
            else:
                print(nomJoueurDeux, "a gagné")
            tryAgain()

elif questionInitiale == "N":
    nomJoueurUn = str(input("Quel est votre nom ?"))
    nomJoueurDeux = str(input("Quel est votre nom ?"))
    if(nomJoueurDeux == "Machine"):
        while nomJoueurDeux == "Machine":
            nomJoueurDeux = str(input("Quel est votre nom ? (différent de machine)"))
    print("Bienvenue", nomJoueurUn, "et", nomJoueurDeux, "feu")
    while isActive:
        os.system("cls")
        os.system("color c")
        print("Le score est de ", score[0], "(J1) - (J2)", score[1])
        choixJoueurUn = str(input("papier, cailloux, ciseaux ?"))
        choixJoueurDeux = str(input("papier, cailloux, ciseaux ?"))
        pcc()
        print("\nLe joueur 2 a choisi", choixJoueurDeux)
        print("Le score est de ", score[0], "-", score[1])
        time.sleep(1)
        if score[0] == 3 or score[1] == 3:
            if score[0] == 3:
                print(nomJoueurUn, "a gagné")
            else:
                print(nomJoueurDeux, "a gagné")
            tryAgain()    
else:
    print("Erreur choix inexistant, veuillez répéter")
