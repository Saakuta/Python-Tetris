Mirija Jonathan RAJOELIARIVONY ANDRIAMAHERY
Thomas BRANDY
Karim SHOUKRY

def print_grind(fichier):
    M = []
    m = 0
    L = []
    L.append(" ")
    L.append(" ")
    for j in range(19):
        if m < 26:
            L.append(chr(97 + m))
        m += 1
    L.append(" ")
    M.append(L)

    L = []
    L.append(" ")
    L.append("╔")
    for k in range(19):
        L.append("═")
    L.append("╗")
    M.append(L)

    n = 0
    for l in range(2, 21):
        L = []
        if n < 26:
            L.append(chr(65 + n))
        else:
            L.append(n)
        n += 1
        L.append("║")
        for ligne in fichier:
            for elem in ligne:
                if elem == 0:
                    L.append(" ")
                elif elem == 1:
                    L.append("•")
                elif elem == 2:
                    L.append("■")
            L.append("║")
        L.append("║")
        M.append(L)
    L = []
    L.append(" ")
    L.append("╚")
    for h in range(1, 20):
        L.append("═")
    L.append("╝")
    M.append(L)

    for a in range(22):
        for b in range(22):
            print(M[a][b], end=" ")
        print()
