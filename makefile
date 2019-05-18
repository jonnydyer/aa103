RocketPerformance.pdf : RocketPerformance/RocketPerformance.tex
	pdflatex RocketPerformance/RocketPerformance
	bibtex RocketPerformance
	pdflatex RocketPerformance/RocketPerformance
	pdflatex RocketPerformance/RocketPerformance

Combustion.pdf : Combustion/Combustion.tex
	pdflatex Combustion/Combustion.tex
	bibtex Combustion
	pdflatex Combustion/Combustion.tex
	pdflatex Combustion/Combustion.tex

ElectricPropulsion.pdf : ElectricPropulsion/ElectricPropulsion.tex
	pdflatex ElectricPropulsion/ElectricPropulsion.tex
#	bibtex ElectricPropulsion
#	pdflatex ElectricPropulsion/ElectricPropulsion.tex
#	pdflatex ElectricPropulsion/ElectricPropulsion.tex

FinalProject.pdf : FinalProject/FinalProject.tex
	pdflatex FinalProject/FinalProject.tex
#	bibtex ElectricPropulsion
#	pdflatex ElectricPropulsion/ElectricPropulsion.tex
#	pdflatex ElectricPropulsion/ElectricPropulsion.tex
clean:
	rm *.log
	rm *.aux
	rm *.bbl
	rm *.blg
	rm *.out
	rm RocketPerformance/*.log
	rm RocketPerformance/*.aux
	rm Combustion/*.log
	rm Combustion/*.aux
