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


def grille_jeu_losange_dimension(n):
    with open("losange.txt", "r"):
        print("    ", end="")
        for m in range(0, 19):
            print(chr(97+m), end=" ")
            m += 1
        print()
        print("=================")

    espace1 = n * 2 - 2
    for i in range(0, n-1):
        if i % 2 == 0:
            print(espace1 * " " + i * "# " + "#")
        espace1 -= 1
        i += 1

    espace2 = n * 2 - 10
    x = n
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(espace2 * " " + "#" + (x - 1) * " #")
        espace2 += 1
        x -= 1


def grille_jeu_losange_fichier():
    with open("losange.txt", "r")as f:
        print("    ", end="")
        for m in range(0, 19):
            print(chr(97+m), end=" ")
            m += 1
        print()
        print("=================")
    for i in range(0, 19):
        p = f.readline()
        x = list(p[:len(p) - 1])
        for g in range(0, len(x)):

            if x[g] == chr(48):
                x[g] = " "
            if x[g] == chr(49):
                x[g] = chr(35)
        ligne = ""
        for n in range(len(x)):
            ligne += x[n]
        print(ligne)


def menu_logo():
    print("________________________________________________________________________")
    print("|                                                                      |")
    print("|                              ~Menu~                                  |")
    print("|                                                                      |")
    print("________________________________________________________________________")


def espacement():
    print("________________________________________________________________________")


def afficher_regles():
    print("- ")
