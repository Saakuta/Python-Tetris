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
                        map = plateau('cercle.txt')
                        afficher(map)

                    if choice1_2_3 == "2":
                        espacement()


            if choice1_2 == "2":
                choice1_2_3 = 0
                while choice1_2_3 != "2":
                    espacement()
                    choice1_2_3 = menu_3()

                    if choice1_2_3 == "1":
                        espacement()
                        map = plateau('losange.txt')
                        afficher(map)

                    if choice1_2_3 == "2":
                        espacement()
                        n = int(input("Entrer une dimension : "))
                        while n <= 0:
                            n = int(input("Entrer une dimension : "))


            if choice1_2 == "3":
                choice1_2_3 = 0
                while choice1_2_3 != "2":
                    espacement()
                    choice1_2_3 = menu_3()

                    if choice1_2_3 == "1":
                        espacement()
                        map = plateau('triangle.txt')
                        afficher(map)

                    if choice1_2_3 == "2":
                        espacement()
                        n = int(input("Entrer une dimension : "))
                        while n <= 0:
                            n = int(input("Entrer une dimension : "))

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