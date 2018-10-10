#probleme 22
def read():
    f=open('probleme022_names.txt','r')
    for ligne in f:
        words=ligne
    f.close()
    liste = words.split(',')
    liste.sort()
    return liste

L=read()                #L est la liste triée de tous les noms
 
def conv_lettre_chiffre(lettre): 
    """associe un nombre à chaque lettre de l'alphabet"""
    Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    i=1
    while lettre != Alphabet[i-1]:
        i+=1
    return i
    
def somme_word(word):
    somme=0
    for c in word:
        print(c)
        somme+=conv_lettre_chiffre(c)
    return somme

c=0     #compteur
for i in range(len(L)):     #on parcourt la liste des noms
    S=0
    for j in range(1,len(L[i])-1):         #car il y a les guillements au début et à la fin
        S+=conv_lettre_chiffre(L[i][j])    #c'est la jème lettre du mot numero i
    c+=S*(i+1)
print(c)    








    
    
    
    
    














