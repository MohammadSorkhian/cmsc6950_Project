TopCountries.png: covid_19_WHO
	python3 fetchDataFromCSV.py

covid_19_WHO:
	wget https://covid19.who.int/WHO-COVID-19-global-data.csv

