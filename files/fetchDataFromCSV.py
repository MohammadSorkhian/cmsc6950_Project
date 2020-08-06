import pandas as pd
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
df_NewCasesLastDays.to_csv(r'df_newCasesLastDays.csv')

dic_LastPeriod = {"Date_reported":list(df['Date_reported'].tail(2*numLastDays).head(numLastDays))}    # Create a dictionary with last {numLastDays} records
for x, item in df_GroupedCountry:    # To extracte corresponding previous
    dic_LastPeriod[x] = list(item[' New_cases'].tail(2*numLastDays).head(numLastDays))
df_NewCasesLastDays = pd.DataFrame(dic_LastPeriod)    # Create a panda dataframe from the dictionary
df_NewCasesLastDays.to_csv(r'df_newCasesLastPeriod.csv')