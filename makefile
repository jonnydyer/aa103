SpecificImpulseEff.pdf : SpecificImpulseEff.tex
	pdflatex SpecificImpulseEff
	#bibtex SpecificImpulseEff
	pdflatex SpecificImpulseEff
	pdflatex SpecificImpulseEff

clean:
	rm *.log
	rm *.aux
