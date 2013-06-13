# -*- coding: utf-8 -*-
# Maïeul ROUQUETTE ; Annette von STOCKHAUSEN
# GPL 3
# https://www.gnu.org/licenses/gpl-3.0.html
# default file configuration

#reading
hyphen		= ("‑","-")			# the ≠ type of hyphen
line_number_r 	= "\([0-9]*\)" 			# the regexp to test the line number
ellipsis  	= "([γδ(δι)θλμπρτφ])’"		# the regexp to prevent transforming ellipsis to endquot 
begin_quote_r	= "[‘“«]"			# the regexp to find begining of quotation
end_quote_r	= "[’”»]"			# the regexp to find end of quotation
paragraph_r	= "\((\w+?)\.\) "		# the regexp to find a paragraph number
chapter_r	= "(\d+?\.)"			# the regexp to find a chapter number
ndash_r		= "—"				# the ndash in reading
begin_insert_r 	= "<"				# the symbol at begining of insert.
end_insert_r	= ">"				# the symbol at end of insert.
par_break_r	= "^( )"			# the begining of paragraph
empty_line_r	= ("","\r","\n")		# the empty lines
#writing
par_break_w	= "\r\n"			# the begining of paragraph
begin_quote_w	= "\enquote{"			# the begining of quotation
end_quote_w	= "}"				# the end of quotation
paragraph_w	= r"\\marginnote{\1}"		# the paragraph number
chapter_w	= r"\n\\textbf{\1}"		# the chapter number
unicode_normalize = False			# to normalize or not to normalize the Unicode characters ? See the documentation of unicodedata.normalize() on http://docs.python.org/2/library/unicodedata.html. The value :
						    #False : not normalize ?
						    #"NFC"
						    #"NFKC"
						    #"NFD"
						    #"NFKD"
ellipsis_back 	= "’"				# the ellipsis symbol
ndash_w		= "--"				# the ndash in writing
begin_insert_w	= r"\\textins{"			# the begining of insert.
end_insert_w	= "}"				# the end of insert.
empty_line_w	= "\r"
line_number_w	= ""				# the line number at end
last_regexp	= False				# rexgep which are applied at last (("find1","replace1"),("find2","replace2"))
#import the config file.

try :
    from config import *
except:
    pass