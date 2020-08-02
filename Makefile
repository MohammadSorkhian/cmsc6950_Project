
main.pdf: files/main.tex files/images/autorank.png files/images/TopCountries.png files/autorankResult.txt
	cd files && latexmk -pdf main.tex	

files/images/autorank.png: files/fetchDataFromCSV.py files/WHO-COVID-19-global-data.csv
	cd files && python3 fetchDataFromCSV.py

files/images/TopCountries.png: files/fetchDataFromCSV.py files/WHO-COVID-19-global-data.csv
	cd files && python3 fetchDataFromCSV.py

files/autorankResult.txt: files/fetchDataFromCSV.py files/WHO-COVID-19-global-data.csv
	cd files && python3 fetchDataFromCSV.py

files/WHO-COVID-19-global-data.csv:
	make clean
	cd files && wget https://covid19.who.int/WHO-COVID-19-global-data.csv
	
	

.PHONY: almost_clean clean

almost_clean:
	cd files && latexmk -c
	
clean: almost_clean
	cd files && rm -f main.pdf autorankResult.txt *.csv*
	cd files/images && rm -f *

