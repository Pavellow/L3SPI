from email import message


def message_imc(imc):
    if imc < 16.5:
        print("Dénutrition ou famine\n") 
    if imc >= 16.5 and imc < 18.5:
        print("Maigreur\n") 
    if imc >= 18.5 and imc < 25:
        print("Corpulence normale\n") 
    if imc >= 25 and imc < 30:
        print("Surpoids\n") 
    if imc >= 30 and imc < 35:
        print("Obésité modérée\n") 
    if imc >= 35 and imc < 40:
        print("Obésité sévère\n") 
    if imc >= 40:
        print("Obésité morbide\n") 

input()
