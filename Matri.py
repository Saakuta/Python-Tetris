nmb = int(input("Entrez un nombre de ligne entre 19 et 26: "))
while (nmb >= 27 or nmb <= 18):
    nmb = int(input("Entrez un nombre de ligne entre 19 et 26: "))
nmb += 2
M = []
m = 0
L = []
L.append(" ")
L.append(" ")
for j in range(nmb-2):
    if m < 26:
        L.append(chr(97+m))
    m += 1
L.append(" ")
M.append(L)
L = []
L.append(" ")
L.append("╔")
for k in range(nmb-2):
    L.append("═")
L.append("╗")
M.append(L)
n = 0
for l in range(2, nmb):
    L = []
    if n < 26 :
        L.append(chr(65 + n))
    else:
        L.append(n)
    n += 1
    L.append("║")
    for m in range(nmb-2):
        L.append("0")
    L.append("║")
    M.append(L)
L = []
L.append(" ")
L.append("╚")
for h in range(1, nmb-1):
    L.append("═")
L.append("╝")
M.append(L)


for a in range(nmb+1):
    for b in range(nmb+1):
        print(M[a][b], end=" ")
    print()

