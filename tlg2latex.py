# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE 
# GPL 3
# https://www.gnu.org/licenses/gpl-3.0.html
# Ce script permet de transformer des textes issu du TLG en texte utilisable en LaTeX :
#    - suppression des numeros de lignes
#    - suppression des césures
#    - remplacement des guillemets par des \enquote{}
# Version 1.0
import re

def normaliser_fichier(fichier):
	'''Normalise un fichier'''
	import codecs
	finale = ''
	debut_phrase = True
	file = codecs.open(fichier,encoding='utf-8')
	for ligne in file:
		ligne  = ligne.strip()
		if ligne!='':
			finale = finale + normalise_ligne(ligne)+'\n'
	file.close()
	file = codecs.open("normal_"+fichier,encoding='utf-8',mode='w')
	file.write(finale)
	file.close()

def normalise_ligne(ligne):
	'''On normalise ligne par ligne'''
	ligne = re.sub("\([0-9]*\)","",ligne) 	# suppression du numero
	ligne.strip()				# suppression des espaces de début et fin
	
	# suppression des césures
	if ligne[-1] == "‑":
		ligne = ligne[:-1] + "%"
	
	# les guillemets
	ligne = ligne.replace("“","\enquote{")
	ligne = ligne.replace("”","}")
	return ligne
	
def principal():
	import sys
	import getopt
	option = getopt.getopt(sys.argv[1:],'')[1]
	if option == 'test':
		test()
		sys.exit()
	else:
		for fichier in option:
			try:
			    normaliser_fichier(fichier)
			    print (fichier + " normalisé")
			except:
			    print ("Impossible de normaliser "+ fichier)
		sys.exit()
	


principal()