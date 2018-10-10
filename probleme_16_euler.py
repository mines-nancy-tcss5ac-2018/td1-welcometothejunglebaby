def solve_pb_16(nombre):
    liste=str(nombre)              #on convertit en str
    longueur = len(liste)
    S=0
    for i in range(longueur):
        S+=int(liste[i])           #on somme tous les chiffres composant nombre
    return S
