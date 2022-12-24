def menu_1():
    print()

    choice1 = 0
    while choice1 != "3":
        print("Entrez 1 pour commencer à jouer.")
        print("Entrez 2 afficher les règles.")
        print("Entrez 3 pour quitter le jeu.")
        print()
        choice1 = str(input("Entrez votre réponse: "))
        print()
        while choice1 < "1" or choice1 > "3":
            choice1 = str(input("Réponse incorrect. Ressaisissez votre réponse svp : "))
        if choice1 != "3":
            return choice1
    return choice1


def menu_2():
    print()

    choice1_2 = 0
    while choice1_2 != "3":
        print("Entrez 1: Jouer dans un cercle")
        print("Entrez 2: Jouer dans un losange")
        print("Entrer 3: Jouer dans un triangle")
        print()
        choice1_2 = str(input("Entrez votre réponse: "))
        print()
        while choice1_2 < "1" or choice1_2 > "3":
            choice1_2 = str(input("Réponse incorrect. Ressaisissez votre réponse svp : "))
        if choice1_2 != "3":
            return choice1_2
    return choice1_2


def menu_3():
    print()

    choice1_2_3 = 0
    while choice1_2_3 != "2":
        print("Entrez 1: Jouer avec la grille d'un fichier")
        print("Entrez 2: Jouer en choisissant les dimensions")
        print()
        choice1_2_3 = str(input("Entrez votre réponse: "))
        print()
        while choice1_2_3 < "1" or choice1_2_3 > "2":
            choice1_2_3 = str(input("Réponse incorrect. Ressaisissez votre réponse svp : "))
        if choice1_2_3 != "2":
            return choice1_2_3
    return choice1_2_3


def menu_logo():
    print("________________________________________________________________________")
    print("|                                                                      |")
    print("|                              ~Menu~                                  |")
    print("|                                                                      |")
    print("________________________________________________________________________")


def espacement():
    print("________________________________________________________________________")


def afficher_regles():
    espacement()
    with open("regles.txt", "r") as f:
        contenu = f.readlines()
    for ligne in contenu:
        print(ligne)
    espacement()

def matrice_jeu_dimension(nmb):
    n = int(input("Entrer une dimension : "))
    while n <= 0:
        n = int(input("Entrer une dimension : "))

    nmb += 2
    M = []
    m = 0
    L = []
    L.append(" ")
    L.append(" ")
    for j in range(nmb - 2):
        if m < 26:
            L.append(chr(97 + m))
        m += 1
    L.append(" ")
    M.append(L)
    L = []
    L.append(" ")
    L.append("╔")
    for k in range(nmb - 2):
        L.append("═")
    L.append("╗")
    M.append(L)
    n = 0
    for l in range(2, nmb):
        L = []
        if n < 26:
            L.append(chr(65 + n))
        else:
            L.append(n)
        n += 1
        L.append("║")
        for m in range(nmb - 2):
            L.append("0")
        L.append("║")
        M.append(L)
    L = []
    L.append(" ")
    L.append("╚")
    for h in range(1, nmb - 1):
        L.append("═")
    L.append("╝")
    M.append(L)


    for a in range(nmb + 1):
        for b in range(nmb + 1):
            print(M[a][b], end=" ")
        print()


def grid(fichier):
    with open (fichier, "r") as f:
        contenu = f.readlines()
        contenu = [ligne.strip().split(" ") for ligne in contenu]
        contenu = [[int(x) for x in ligne] for ligne in contenu]

        return contenu

def print_grind(fichier):
    print("    ", end=" ")
    for m in range(19):
        print(chr(97 + m), end=" ")
    print()
    print("   ╔", end=" ")
    for i in range(19):
        print("═", end=" ")
    print("╗", end="\n")

    n = 0
    for ligne in fichier:
        print(chr(65 + n)," ║", end=" ")
        n += 1
        for elem in ligne:
            if elem == 0:
                print(" ", end=" ")
            elif elem == 1:
                print("•", end=" ")
            elif elem == 2:
                print("■", end=" ")
        print("║", end=" ")
        print()

    print("   ╚", end=" ")
    for i in range(19):
        print("═", end=" ")
    print("╝", end="\n")