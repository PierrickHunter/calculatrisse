##### Calculator

import os

def resultat(r1,ope,r2):
	r1 = input("Veuillez entrer le premier réel : ")
	ope = input("Choisissez une opération : ")
	r2 = input("Veuillez entrer le deuxième réel : ")
	resu = 0

	r1 = float(r1)
	r2 = float(r2)
		
	if ope == '+':
		resu = r1 + r2
		# %.4f permet d'afficher un réel avec 4 chiffres après la virgule
			
	elif ope == '-':
		resu = r1 - r2
	elif ope == '*':
		resu = r1 * r2
	elif ope == '/':
		if r2 != 0 :
			resu = r1 / r2
		else :
			print('Division par zéro')
	else : print('Opération invalide')
	print('Le résultat est ', resu)
	
	os.system("pause")
