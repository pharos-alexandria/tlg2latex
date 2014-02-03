all:
	rm -f *.pdf
	rm -f ../tlg2latex.zip
	rm -rf tlg2latex
	mkdir tlg2latex
	pandoc README.md -o README.pdf
	rm -f test/.DS_Store
	cp -r default.py tlg2latex.py *pdf test tlg2latex
	cp README.md tlg2latex/README
	zip -r ../tlg2latex.zip tlg2latex