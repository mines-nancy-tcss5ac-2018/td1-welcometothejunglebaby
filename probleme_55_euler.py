def est_palindrome(n):             #fonction booléenne qui renvoie True si n est un palindrome
    l=str(n)
    for k in range(len(l)//2+1):
        if l[k]!=l[len(l)-k-1]:
            return False
    return True


#calcul du nombre de nombres de Lichrel inférieurs à 10000
def solve_pb_55():
    c=0
    for i in range(10000):
        nb_itérations, B = 0, False              # B est un drapeau
        n1=i
        while nb_itérations<50 and B==False:     #passé 50 itérations, on est presque sûr que ça en est un
            l=str(n1)
            n2=''
            for p in range(len(l)):
                n2+=l[len(l)-1-p]               #on inverse l'ordre des chiffres
            n1=int(n1)+int(n2)
            if est_palindrome(n1):
                B=True              #la boucle s'arrête alors
                c+=1
            else:
                nb_itérations+=1
    return 10000-c
print(solve_pb_55())