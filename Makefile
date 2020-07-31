
main.pdf: outputImages_Text
	cd files && pdflatex main.tex

outputImages_Text: clearData covid_19_WHO
	cd files && python3 fetchDataFromCSV.py


covid_19_WHO:
	cd files && wget https://covid19.who.int/WHO-COVID-19-global-data.csv

clearData:
	cd files && rm -f *.csv*
