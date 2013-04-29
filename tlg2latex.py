# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE ; Annette von STOCKHAUSEN
# GPL 3
# https://www.gnu.org/licenses/gpl-3.0.html
# Ce script permet de transformer des textes issu du TLG en texte utilisable en LaTeX :
#    - suppression des numeros de lignes
#    - suppression des césures
#    - remplacement des guillemets par des \enquote{}
# Version 1.1.1
import re
import os
import default as config
import unicodedata
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
	if os.path.dirname(fichier)=="":
	    destination = "normal_" + os.path.basename(fichier)
	else:
	    destination = os.path.dirname(fichier) + os.sep + "normal_" + os.path.basename(fichier)
	file = codecs.open(destination,encoding='utf-8',mode='w')
	file.write(finale)
	file.close()

def normalise_ligne(ligne):
	'''On normalise ligne par ligne'''
	ligne = re.sub(config.line_number,"",ligne) 	# suppression du numero
	ligne = ligne.strip()			# suppression des espaces de début et fin
	
	# suppression des césures
	if ligne[-1] in config.hyphen:		
		ligne = ligne[:-1] + "%"
	
	# les guillemets
	ligne = re.sub(config.ellipsis,r"\1'",ligne) # replace ’ in Ellipsis with ', otherwise not discernable from single endquote
	ligne = re.sub(config.begin_quote_r,config.begin_quote_w,ligne)
	ligne = re.sub(config.end_quote_r,config.end_quote_w,ligne)
	ligne = re.sub("\'","’",ligne) # replace ’ back	
	
	# chapters and paragraphs
	ligne = re.sub(config.paragraph_r,config.paragraph_w,ligne) # paragraph number
	ligne = re.sub(config.chapter_r,config.chapter_w,ligne) #chapter number  
	
	# Unicode normalization
	if config.unicode_normalize:
	    ligne = unicodedata.normalize(config.unicode_normalize,ligne)
	return ligne

def test():
	"""Be sur any modification doesn't break compatibilty"""
	test = os.listdir("test") 	 #All the file of the test directory.
	import hashlib
	for file in test:
		if file[0] in ["0","1","2","3","4","5","6","7","8","9"]: #If it's a file to be tested.
		    md5 = hashlib.md5(open("test" + os.sep + "normal_" + file,"rb").read()).hexdigest()
		    normaliser_fichier("test" + os.sep + file)
		    
		    if md5 !=hashlib.md5(open("test" + os.sep + "normal_" + file,"rb").read()).hexdigest():
			    print ("Erreur sur le fichier" + file)
			    
		    else:
			    print ("Fichier "+file+ " OK")

def __main__():
	import sys
	import getopt
	option = getopt.getopt(sys.argv[1:],'')[1]
	if option == ['test']:
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
	

__main__()