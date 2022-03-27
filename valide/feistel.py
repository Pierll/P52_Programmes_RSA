
def getDico():
	nbr_dicos = int(input("nbr fonctions ?"))
	nbr_bits  = int(input("nbr bit par fonctions ?"))
	dicos = []
	for i in range(0, nbr_dicos):
		d = {}
		for y in range(0, nbr_bits):
			print("Fonction f", i+1, " (", "bit ", y+1, ")", ":")
			b1 = input()
			b1 = int(b1, 2)
			b2 = input()
			b2 = int(b2, 2)
			d[b1] = b2
		dicos.append(d)
	return dicos

def decoupe(M, bits):
	n = int(bits/2)
	decouper = [M[i:i+n] for i in range(0, len(M), n)]
	for i in range(len(decouper)):
		decouper[i] = int(decouper[i], 2)
	return decouper

def intToBin(i):
	resultat = str(bin(i))[2:]
	if(resultat == "0" or resultat == "1"):
		resultat = "0" + resultat
	return resultat

def feistel(paquets, dicos):
	g = paquets[0]
	d = paquets[1]
	
	for i in range(len(dicos)):
		print("--------------------------")
		print("i = ", i, ":")
		temp = d
		print("g", i, "=", intToBin(g), " et d", i, "=", intToBin(d))
		d = g ^ dicos[i][d]
		print("d", i+1, "=", intToBin(g), " XOR f", i+1, "(", intToBin(temp), ")")
		g = temp

	temp = g
	
	g = intToBin(d)
	d = intToBin(temp)
	return(g, d)

choix = 0
d = getDico()
while choix == 0:
	m = str(input("Saisissez votre message : "))
	bits = int(input("Nombre de bits : "))
	res = feistel(decoupe(m, bits), d)
	print("Votre mot est : ", res)
	choix = int(input("Voulez-vous refaire un mot ? (0 oui, 1 non)"))

