from fonction import menu_1, grille_jeu_losange, menu_logo

menu_logo()
choice1="0"
while choice1!="3":
    choice1 = menu_1()
    #if choice1 =="1":



    if choice1 == '2':
        grille_jeu_losange()