
main.pdf: files/main.tex files/images/autorank.png files/images/TopCountries.png files/autorankResult.txt files/main.tex
	cd files && latexmk -pdf main.tex	

files/images/autorank.png: files/WHO-COVID-19-global-data.csv
	cd files/images && python3 fetchDataFromCSV.py

files/images/TopCountries.png: files/WHO-COVID-19-global-data.csv
	cd files/images && python3 fetchDataFromCSV.py

files/autorankResult.txt: files/WHO-COVID-19-global-data.csv
	cd files && python3 fetchDataFromCSV.py

files/WHO-COVID-19-global-data.csv:
	cd files && wget https://covid19.who.int/WHO-COVID-19-global-data.csv