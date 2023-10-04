#ecrire un programme qui va lire les donnees d'employe a partir du clavier
#identifiant,nom,salaire,adresse,marié
identifiant= int(input("saisir un identifiant"))
nom = input("saisir un nom")
salaire= float(input("saisir un salaire"))
adresse = input("saisir une adresse")
status= bool(input("marie ou non[true or false]"))
print("svp confirmer les infos : ")
print("Lidentifiant de l'employé est : ",identifiant)
print("Le nom de l'employé est : ",nom)
print("L'adresse' de l'employé est : ",adresse)
print("la situation de l'employe est est : ",status)
