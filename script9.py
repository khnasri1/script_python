## ecrire un programme qui choisit le plus grand nombre parmi 3 nombres saisis a partir du clavier
a= int(input("saisir un nombre a "))
b= int(input("saisir un nombre b "))
c= int(input("saisir un nombre c "))
if a > b and a > c:
    print("le nombre le plus grand est: ", a)
elif  b > c:
    print("le nombre le plus grand est: ", b)
else:
    print("le nombre le plus grand est: ", c)