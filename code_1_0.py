import time



print("machine de Glace")
temp =int(input("entrez la température"))
ReservChoco = 1
H = ReservChoco

# Fanction BuildGlace
def buidGlace():

    vent = 0

    if temp >=-18:
        print("mauvaise température ")
        if ReservChoco == 1:
            vent = 1
            print("Niveau choco haut ")

        elif ReservChoco == 0:
            vent = 0
            print("Niveau choco Bas")

    elif temp <=-18:
        vent = 0
        print("température ideal")

    print("vent = ", vent)



    
    return

buidGlace()


# Facntion checkGlace
def checkglace():

    if H == 1 and temp <= -18:
        print("niveau De Glace OK")
        return 1
    else:
        print("Glace non disponible ou mauvaise température")
        return 0


statut = checkglace()
print("statut = ", statut)

# distribution De Glace


# 1=choco
# 2=blanc
# 3=melange
c = input("veuillez Choisir le Gout")
if c == '1' and statut == 1:
    M = 1
    V1 = 1
    V2 = 0
    print("choco")
    print("M=", M, "V1=", V1, "V2=", V2)
    time.sleep(10)
    M = 0
    V1 = 0
    print("le Glace est pret")
    print("M=", M, "V1=", V1, "V2=", V2)

elif c == '2' and statut == 1:
    M = 1
    V1 = 0
    V2 = 1
    print("blanc")
    print("M=", M, "V1=", V1, "V2=", V2)
    time.sleep(10)
    M = 0
    V2 = 0
    print("le Glace est pret")
    print("M=", M, "V1=", V1, "V2=", V2)

elif c == '3' and statut == 1:
    M = 1
    V1 = 1
    V2 = 1
    print("melange")
    print("M=", M, "V1=", V1, "V2=", V2)

    time.sleep(10)
    M = 0
    V1 = 0
    V2 = 0
    print("le Glace est pret")
    print("M=", M, "V1=", V1, "V2=", V2)



else:
    print("choix incorrect ou le Glace n'est pas pret ")
