from fonctions import *
print("mon second fichier")
#*print("prénom : ")
#x = input("entrer votre prénom : ")
#print(type(x))
#y=20
#print("le prénom est : ",x,y)
#ch='Bonjour'
#print('Hello world'[3:7])
# print('Hello world'[4:])
# nom, age = 'Benjamin', 31
# print('Bonjour, {0} tu as {1}', nom, age)
# txt = "Hello World"
# x = txt[2:5]
# print(x)
# nom, réponse = 'Benjamin', 42.89098765
# chaine = f'La réponse de {nom} est {réponse}.'
# print(chaine)
# Phrase = input("Entrez une phrase: ")
# mots=Phrase.split(" ")
# print("le nombre de mots dans la phrase est : ", len(mots))
# print("le nombre de mots dans la phrase est : {}".format(len(mots)))
# # print("le nombre de mots dans la phrase est : %d" % (len(mots)))
# ChoixOperation = input("""Choisissez une opération :
#     1. Addition
#     2. Soustraction
#     3. Multiplication
#     4. division \n""")
# if ChoixOperation=='1' or ChoixOperation=='2' or ChoixOperation=='3' or ChoixOperation=='4' :
#     Operande1 =  input("Entrez le premier nombre : ")
#     Operande2 =  input("Entrez le second nombre : ")
#     validation = True
#     if ChoixOperation=='1':
#         resultat = float(Operande1) + float(Operande2)
#     elif ChoixOperation=='2':
#         resultat = float(Operande1) - float(Operande2)
#     elif ChoixOperation=='3':
#         resultat = float(Operande1) * float(Operande2)
#     elif ChoixOperation=='4':
#         if float(Operande2)==0 :
#             validation = False
#             print("erreur division par Zéro")
#         else:
#             resultat = float(Operande1) / float(Operande2)
#     # else:
#     #     validation = False
#     if validation==True:
#         print("Résultat : %.2f" %resultat )
# une annee en seconde = 3,156e+7
v = 31556952 / 31557600
print("le nombre d\' annees : %d" % int(v))
reste = 31556952 - (31557600 * int(v))
print("le reste est : %d" %reste)
semaines = reste / 604800.02
print("le nombre de semaines : %d" % int(semaines))
restesemaine = reste - (604800.02 * int(semaines))
print("le reste est : %d" %restesemaine)
print(f"resultat de la fonction : {estNombreDansIntervalle(10, 30,20)}")
print(type(estNombreDansIntervalle(10, 30,20)))
