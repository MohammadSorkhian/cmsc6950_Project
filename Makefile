
main.pdf: files/main.tex files/images/autorank.png files/autorankReport.txt files/images/TopCountries.png files/images/TopCountriesCompare.png
	cd files && latexmk -pdf main.tex && mv main.pdf ../

files/autorankReport.txt: files/autorank_report.py files/df_newCasesLastDays.csv
	cd files && python3 autorank_report.py > temp.txt
	cd files && fold -w60 temp.txt > autorankReport.txt && rm -f temp.txt

files/images/autorank.png: files/autorank_report.py files/df_newCasesLastDays.csv
	cd files && python3 autorank_report.py > temp.txt
	cd files && fold -w60 temp.txt > autorankReport.txt && rm -f temp.txt

files/images/TopCountriesCompare.png: files/highest_details.py files/df_newCasesLastDays.csv files/df_newCasesLastPeriod.csv
	cd files && python3 highest_details.py

files/images/TopCountries.png : files/highest_details.py files/df_newCasesLastDays.csv files/df_newCasesLastPeriod.csv
	cd files && python3 highest_details.py

files/df_newCasesLastDays.csv: files/fetchDataFromCSV.py files/WHO-COVID-19-global-data.csv
	cd files && python3 fetchDataFromCSV.py

files/df_newCasesLastPeriod.csv: files/fetchDataFromCSV.py files/WHO-COVID-19-global-data.csv
	cd files && python3 fetchDataFromCSV.py

files/WHO-COVID-19-global-data.csv:
	cd files && wget https://covid19.who.int/WHO-COVID-19-global-data.csv
	
	

.PHONY: almost_clean clean

almost_clean:
	cd files && latexmk -c
	
clean: almost_clean
	cd files && rm -f autorankReport.txt *.csv*
	cd files/images && rm -f *

