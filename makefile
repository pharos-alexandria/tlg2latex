all:
	rm -f *.pdf
	rm -f ../tlg2latex.zip
	rm -rf tlg2latex
	mkdir tlg2latex
	pandoc README.md -o README.pdf --latex-engine=xelatex -V mainfont='Linux Libertine O'
	rm -f test/.DS_Store
	ln  default.py tlg2latex.py *pdf tlg2latex
	mkdir tlg2latex/test
	ln test/*txt tlg2latex/test
	ln README.md tlg2latex/README
	zip -r ../tlg2latex.zip tlg2latex
