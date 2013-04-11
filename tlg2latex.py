# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE %%S
# http://geekographie.maieul.net/26
# Paternité  - Partage des Conditions Initiales à l'Identique 2.0 France (CC BY-SA 2.0)
# http://creativecommons.org/licenses/by-sa/2.0/fr/
# Ce script normalise la typo des textes extraits depuis la Library of Latin Texts : espace avant les signes de ponctuation double, majuscule en début de phrase
# Version 1.0
import re

def normaliser_typo_fichier(fichier):
	'''Normalise un fichier'''
	import codecs
	finale = ''
	debut_phrase = True
	file = codecs.open(fichier,encoding='utf-8')
	for ligne in file:
		ligne  = ligne.strip()
		if ligne!='':
			
			finale = finale + normalise_typo_ligne(ligne,debut_phrase)+'\n'
			if ligne[-1] in ['?','!','.']:
				debut_phrase = True
			else:
				debut_phrase = False
		else:
			finale = finale + '\n'
	file.close()
	file = codecs.open(fichier,encoding='utf-8',mode='w')
	file.write(finale)
	file.close()

def normalise_typo_ligne(ligne,debut_phrase=True):
	'''On normalise la typo, ligne par ligne'''
	# Une majuscule après les . ? !
	ligne = re.sub('[\s]{2,}',' ',ligne)		#suppression des espaces multiples
	
	majuscule_apres = ['?','!','.']
	
	for i in range(len(ligne)):
		if ligne[i] in majuscule_apres : 
			if i+1<len(ligne):
				if ligne[i+1] !=' ':
					ligne = ligne.replace(ligne[i]+ligne[i+1],ligne[i]+ligne[i+1].upper())
				else:				#il y a forcément quelquechose après, vu qu'on a striper
					ligne = ligne.replace(ligne[i]+' '+ligne[i+2],ligne[i]+' '+ligne[i+2].upper())
	
	
	# La ponctuation avant les signes doubles
	espace_avant = [':','?','!',';']
	for signe in espace_avant:
		ligne = ligne.replace(signe,' '+signe)
	# Si la ligne était en début de phrase :
	if debut_phrase == True:
		ligne = ligne[0].upper() + ligne[1:]
	
	return ligne
	
def principal():
	import sys
	import getopt
	option = getopt.getopt(sys.argv[1:],'')[1]
	print option
	if option == 'test':
		test()
		sys.exit()
	else:
		for fichier in option:
			try:
				normaliser_typo_fichier(fichier)
				print fichier + " normalisé"
			except:
				print "Impossible de normaliser "+ fichier
		sys.exit()
	
	
def test():
	''' Test unitaire -> oui je pourrais faire mieux, mais j'ai la flemme d'apprendre à utiliser le module de python'''
	tableau = [('ceci? est; un: test unitaire!','Ceci ? Est ; un : test unitaire !',True )]
	for i in tableau:
		if normalise_typo_ligne(i[0],i[2])	!= i[1]:
			print "erreur"
			print "Donné : \t"  + i[0]
			print "Attendu : \t" + '"' + i[1] + '"'
			print "Reçus : \t" + '"' +  normalise_typo_ligne(i[0])+ '"'
		else:
			print "ok"

principal()