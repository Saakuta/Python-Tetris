from fonction import *
from BlocsCercle import *
from BlocsLosange import *
from BlocsTriangle import *
from BlocsCommuns import *
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
            ### Cercle
            if choice1_2 == "1":
                choice1_2_3 = 0
                while choice1_2_3 != "2":
                    espacement()
                    choice1_2_3 = menu_3()

                    if choice1_2_3 == "1":
                        espacement()
                        map = grid('cercle.txt')
                        print_grid(map)



                        choice1_2_3_4 = 0
                        while choice1_2_3_4 != "2":
                            espacement()
                            choice1_2_3_4 = choix_print_block()

                            if choice1_2_3_4 =="1":
                                print_blocs(C)

                            if choice1_2_3_4 =="2":
                                print_blocs(C)



                    if choice1_2_3 == "2":
                        espacement()
                        nmb = int(input("Saisir un nombre de colonne : "))
                        while nmb < 21 or nmb > 26:
                            nmb = int(input("Saisir un nombre de colonne : "))
                        matrice_jeu_cercle(nmb)
                        choice1_2_3_4 = 0
                        while choice1_2_3_4 != "2":
                            espacement()
                            choice1_2_3_4 = choix_print_block()

                            if choice1_2_3_4 == "1":
                                print_blocs(C)

                            if choice1_2_3_4 == "2":
                                print_blocs(C)

            ### Losange
            if choice1_2 == "2":
                choice1_2_3 = 0
                while choice1_2_3 != "2":
                    espacement()
                    choice1_2_3 = menu_3()


                    if choice1_2_3 == "1":
                        espacement()
                        map = grid('losange.txt')
                        print_grid(map)
                        choice1_2_3_4 = 0
                        while choice1_2_3_4 != "2":
                            espacement()
                            choice1_2_3_4 = choix_print_block()

                            if choice1_2_3_4 == "1":
                                print_blocs(L)

                            if choice1_2_3_4 == "2":
                                print_blocs(L)

                    if choice1_2_3 == "2":
                        espacement()
                        nmb = int(input("Saisir un nombre de colonne : "))
                        while nmb < 21 or nmb > 26 or nmb % 2 == 0:
                            nmb = int(input("Saisir un nombre de colonne : "))
                        matrice_jeu_losange(nmb)

                        choice1_2_3_4 = 0
                        while choice1_2_3_4 != "2":
                            espacement()
                            choice1_2_3_4 = choix_print_block()

                            if choice1_2_3_4 == "1":
                                print_blocs(L)

                            if choice1_2_3_4 == "2":
                                print_blocs(L)

            ### Triangle
            if choice1_2 == "3":
                choice1_2_3 = 0
                while choice1_2_3 != "2":
                    espacement()
                    choice1_2_3 = menu_3()

                    if choice1_2_3 == "1":
                        espacement()
                        map = grid('triangle.txt')
                        print_grid(map)
                        choice1_2_3_4 = 0
                        while choice1_2_3_4 != "2":
                            espacement()
                            choice1_2_3_4 = choix_print_block()

                            if choice1_2_3_4 == "1":
                                print_blocs(T)

                            if choice1_2_3_4 == "2":
                                print_blocs(T)

                    if choice1_2_3 == "2":
                        espacement()
                        nmb = int(input("Saisir un nombre de colonne : "))
                        while nmb < 21 or nmb > 26 or nmb % 2 == 0:
                            nmb = int(input("Saisir un nombre de colonne : "))
                        matrice_jeu_triangle(nmb)
                        choice1_2_3_4 = 0
                        while choice1_2_3_4 != "2":
                            espacement()
                            choice1_2_3_4 = choix_print_block()

                            if choice1_2_3_4 == "1":
                                print_blocs(T)

                            if choice1_2_3_4 == "2":
                                print_blocs(T)

            break

    ### Afficher les règles
    if choice1 == '2':
        afficher_regles()
        print("\n")

### Quitter le programme
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