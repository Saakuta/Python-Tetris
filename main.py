from fonction import *
import time

menu_logo()
choice1="0"
while choice1!="3":
    choice1 = menu_1()

    if choice1 =="1":
        choice1_1 = 0
        while choice1_1 != "3":
            print("________________________________________________________________________")
            choice1_1 = menu_2()

            #if choice1_1 == "1":

            if choice1_1 == "2":
                print("________________________________________________________________________")
                grille_jeu_losange()


    if choice1 == '2':
        afficher_regles()


#Quitter le prgramme
    if choice1=="3":
        print()
        print("Sortie du programme",end="")
        time.sleep(0.25)
        print(".",end="")
        time.sleep(0.25)
        print(".",end="")
        time.sleep(0.25)
        print(".",end="")
        time.sleep(0.25)