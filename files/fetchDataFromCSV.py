import pandas as pd
import matplotlib.pyplot as plt
from autorank import autorank, create_report, plot_stats, latex_table

df = pd.read_csv('WHO-COVID-19-global-data.csv', parse_dates=['Date_reported'])
# country_names = list(df.groupby(' Country').groups.keys())
numLastDays = 30    # Number of last days that we want to know the stats of new cases
numTopCountires = 10    # Number of countries with the highest volume of detected new cases
# pd.set_option('display.max_columns', 8)
df_GroupedCountry = df.groupby(' Country')    # Groupe data by countries
dic_LastDays = {"Date_reported":list(df['Date_reported'].tail(numLastDays))}    # Create a dictionary with last {numLastDays} records
for x, item in df_GroupedCountry:    # To extracte {numLastDays} last records of Covid-19 new casesin each country
    dic_LastDays[x] = list(item[' New_cases'].tail(numLastDays))
df_NewCasesLastDays = pd.DataFrame(dic_LastDays)    # Create a panda dataframe from the dictionary    
df_TopCountries = df_NewCasesLastDays.iloc[:, 1:].sum().sort_values(ascending=False).head(numTopCountires)    # Sorte and select top countries
list_TopCountriesName = list(df_TopCountries.keys())    # Extract name of these top countries
df_NewCasesLastDaysTop = df_NewCasesLastDays[list_TopCountriesName]    # Extract these top countries into a dataframe
se_NewCasesLastDaysTopMean = df_NewCasesLastDaysTop.mean()    # Calculate mean for these countries
se_NewCasesLastDaysTopMean.plot(kind='bar')
plt.xlabel('Countries')
plt.ylabel('Number of New Cases per day')
plt.title(f'Top {numTopCountires} countries in last {numLastDays} days in terms of detected new Covid-19 cases')
plt.tight_layout()
plt.savefig('images/TopCountries.png')    # Save the plotted figure
res = autorank(df_NewCasesLastDaysTop, alpha=0.05, verbose=False)    # Calculate autorank for these top countries
plot_stats(res)    # Utilise aoutorank built-in plotting function  
plt.savefig('images/autorank.png')
f_result = open('autorankResult.txt','w')    # Save the result(res) in a txt file
f_result.write(str(res))
f_result.close()

