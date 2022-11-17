def menu_1():
    print()

    choice1 = 0
    while choice1 != "3":
        print("Entrez 1: Jouer dans un cercle (19x19)")
        print("Entrez 2: Jouer dans un losange (19x19)")
        print("Entrer 3: Jouer dans un triangle (19x9)")
        print()
        choice1 = str(input("Entrez votre réponse: "))
        print()
        while choice1 < "1" or choice1 > "3":
            choice1 = str(input("Réponse incorrect. Ressaisissez votre réponse svp : "))
        if choice1 != "3":
            return choice1
    return choice1



def grille_jeu_losange():
    with open("losange.txt", "r") as f:
        print("  ",end="")
        for m in range (0, 19):
            print(chr(97+m), end=" ")
            m += 1
        print()
        print("=================")


        for i in range(0, 19):
            I = f.readline()
            L = list(I[:len(I) - 1])
            for i in range(0, len(L)):

                if (L[i] == chr(48)):
                    L[i] = " "
                if (L[i] == chr(49)):
                    L[i] = chr(35)
            ligne = ""
            for i in range(len(L)):
                ligne += L[i]
            print(ligne)

def menu_logo():
    print("________________________________________________________________________")
    print("|                                                                      |")
    print("|                              ~Menu~                                  |")
    print("|                                                                      |")
    print("________________________________________________________________________")




