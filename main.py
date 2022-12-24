from fonction import *
import time

menu_logo()
choice1 = "0"
while choice1 != "3":
    choice1 = menu_1()

    if choice1 == "1":
        choice1_2 = 0
        while choice1_2 != "3":
            espacement()
            choice1_2 = menu_2()

            if choice1_2 == "1":
                choice1_2_3 = 0
                while choice1_2_3 != "2":
                    espacement()
                    choice1_2_3 = menu_3()

                    if choice1_2_3 == "1":
                        espacement()
                        map = grid('cercle.txt')
                        print_grind(map)

                    if choice1_2_3 == "2":
                        espacement()
                        n = int(input("Entrer une dimension : "))
                        while n <= 0:
                            n = int(input("Entrer une dimension : "))
                        contenu = matrice_jeu_cercle(n)


            if choice1_2 == "2":
                choice1_2_3 = 0
                while choice1_2_3 != "2":
                    espacement()
                    choice1_2_3 = menu_3()

                    if choice1_2_3 == "1":
                        espacement()
                        map = grid('losange.txt')
                        print_grind(map)

                    if choice1_2_3 == "2":
                        espacement()
                        nmb = int(input("Saisir un nombre de colonne : "))
                        while nmb < 21 or nmb > 26 or nmb % 2 == 0:
                            nmb = int(input("Saisir un nombre de colonne : "))
                        matrice_jeu_losange(nmb)

            if choice1_2 == "3":
                choice1_2_3 = 0
                while choice1_2_3 != "2":
                    espacement()
                    choice1_2_3 = menu_3()

                    if choice1_2_3 == "1":
                        espacement()
                        map = grid('triangle.txt')
                        print_grind(map)

                    if choice1_2_3 == "2":
                        espacement()
                        nmb = int(input("Saisir un nombre de colonne : "))
                        while nmb < 21 or nmb > 26 or nmb % 2 == 0:
                            nmb = int(input("Saisir un nombre de colonne : "))
                        matrice_jeu_triangle(nmb)

            break
    if choice1 == '2':
        afficher_regles()
        print("\n")

###Quitter le programme
    if choice1 == "3":
        print()
        print("Sortie du programme", end="")
        time.sleep(0.25)
        print(".",end="")
        time.sleep(0.25)
        print(".",end="")
        time.sleep(0.25)
        print(".",end="")
        time.sleep(0.25)