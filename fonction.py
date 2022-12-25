from BlocsCercle import *
from BlocsLosange import *
from BlocsTriangle import *
from BlocsCommuns import *
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

def matrice_jeu_cercle(nmb):
    grille = []
    n = 65
    y = 97
    L = ['   ']
    for i in range(nmb):
        L.append(chr(y))
        y += 1
    grille.append(L)
    L = [' ']
    L.append("╔")
    for i in range(nmb):
        L.append("═")
    L.append("╗")
    grille.append(L)
    for i in range(3):
        L = []
        L.append(chr(n))
        n += 1
        L.append("║")
        for j in range(nmb):
            if (j < 3 - i) or (nmb - 4 + i < j < nmb):
                L.append(0)
            else:
                L.append(1)
        L.append("║")
        grille.append(L)
    for i in range(nmb - 6):
        L = []
        L.append(chr(n))
        n += 1
        L.append("║")
        for j in range(nmb):
            L.append(1)
        L.append("║")
        grille.append(L)
    for i in range(3):
        L = []
        L.append(chr(n))
        n += 1
        L.append("║")
        for j in range(nmb):
            if (j == 0 or j - i < 1) or (nmb - 2 - i < j <= nmb):
                L.append(0)
            else:
                L.append(1)
        L.append("║")
        grille.append(L)
    L = [' ']
    L.append("╚")
    for i in range(nmb):
        L.append("═")
    L.append("╝")
    grille.append(L)

    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == 0:
                grille[i][j] = ' '
            if grille[i][j] == 1:
                grille[i][j] = '*'
            print(grille[i][j], end=' ')
        print()

def matrice_jeu_losange(nmb):
    grille = []
    nbLig = nmb // 2
    n = 65
    y = 97
    L = ['   ']
    for i in range(nmb):
        L.append(chr(y))
        y += 1
    grille.append(L)
    L = [' ']

    L.append("╔")
    for i in range(nmb):
        L.append("═")
    L.append("╗")
    grille.append(L)
    for i in range(nbLig + 1):
        L = []
        L.append(chr(n))
        n += 1
        L.append("║")
        for j in range(nmb):
            if j == nmb // 2 or (nmb // 2 + i >= j >= nmb // 2 - i):
                L.append(1)
            else:
                L.append(0)
        L.append("║")
        grille.append(L)
    for i in range(nbLig):
        L = []
        L.append(chr(n))
        n += 1
        L.append("║")
        for j in range(nmb):
            if (j == 0 or j - i < 1) or (nmb - 2 - i < j <= nmb):
                L.append(0)
            else:
                L.append(1)
        L.append("║")
        grille.append(L)
    L = [' ']
    L.append("╚")
    for i in range(nmb):
        L.append("═")
    L.append("╝")
    grille.append(L)
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == 0:
                grille[i][j] = ' '
            if grille[i][j] == 1:
                grille[i][j] = "•"
            print(grille[i][j], end=' ')
        print()

def matrice_jeu_triangle(nmb):
    grille = []
    nbLig = nmb // 2
    n = 65
    y = 97
    L = ['   ']
    for i in range(nmb):
        L.append(chr(y))
        y += 1
    grille.append(L)
    L = [' ']
    L.append("╔")
    for i in range(nmb):
        L.append("═")
    L.append("╗")
    grille.append(L)
    for i in range(nbLig):
        L = []
        L.append(chr(n))
        n += 1
        L.append("║")
        for j in range(nmb):
            if j == ((nmb) // 2) or (j <= (nmb) // 2 + i) and (j >= (nmb) // 2 - i) and j:
                L.append('*')
            else:
                L.append(' ')
        L.append("║")
        grille.append(L)
    L = [' ']
    L.append("╚")
    for i in range(nmb):
        L.append("═")
    L.append("╝")
    grille.append(L)
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            print(grille[i][j], end=' ')
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

def choix_print_block():
    print()

    choice1_2_3_4 = 0
    while choice1_2_3_4 != "2":
        print("Entrez 1: Afficher tous les blocs")
        print("Entrez 2: Afficher les blocs 3 par 3")
        print()
        choice1_2_3_4 = str(input("Entrez votre réponse: "))
        print()
        while choice1_2_3_4 < "1" or choice1_2_3_4 > "2":
            choice1_2_3_4 = str(input("Réponse incorrect. Ressaisissez votre réponse svp : "))
        if choice1_2_3_4 != "2":
            return choice1_2_3_4
    return choice1_2_3_4
def print_blocs(fichier):
    with open(fichier, "r") as f:
        contenu = f.readlines()

        print(contenu)
