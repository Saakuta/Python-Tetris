def menu_1():
    print()

    choice1 = 0
    while choice1 != "3":
        print("Entrez 1: Jouer dans un cercle")
        print("Entrez 2: Jouer dans un losange")
        print("Entrer 3: Jouer dans un triangle")
        choice1 = str(input("Entrez votre réponse: "))
        while choice1 < "1" or choice1 > "3":
            choice1 = str(input("Réponse incorrect. Ressaisissez votre réponse svp : "))
        if choice1 != "3":
            return choice1
    return choice1



def grille_jeu_losange():
    with open("Losange.txt", "r") as f:
        for l in f:
            for j in l:
                if j == '0':
                    print(" ", end="")
                else:
                    print(".", end="")
            print("\n")

def menu_logo():
    print("________________________________________________________________________")
    print("|                                                                      |")
    print("|                               Menu                                   |")
    print("|                                                                      |")
    print("________________________________________________________________________")

