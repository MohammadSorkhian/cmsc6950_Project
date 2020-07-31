import pandas as pd
import matplotlib.pyplot as plt
from autorank import autorank, create_report, plot_stats, latex_table

df = pd.read_csv('WHO-COVID-19-global-data.csv', parse_dates=['Date_reported'])
# country_names = list(df.groupby(' Country').groups.keys())
numLastDays = 5
numTopCountires = 10
pd.set_option('display.max_columns', 8)
df_GroupedCountry = df.groupby(' Country')
dic_LastDays = {"Date_reported":list(df['Date_reported'].tail(numLastDays))}
for x, item in df_GroupedCountry:
    dic_LastDays[x] = list(item[' New_cases'].tail(numLastDays))
df_NewCasesLastDays = pd.DataFrame(dic_LastDays)
df_TopCountries = df_NewCasesLastDays.iloc[:, 1:].sum().sort_values(ascending=False).head(numTopCountires)
list_TopCountriesName = list(df_TopCountries.keys())
df_NewCasesLastDaysTop = df_NewCasesLastDays[list_TopCountriesName]
se_NewCasesLastDaysTopMean = df_NewCasesLastDaysTop.mean()
se_NewCasesLastDaysTopMean.plot(kind='bar', y='Number of New Cases per Day', title=f'Top {numTopCountires} countries in last {numLastDays} days')
plt.savefig('TopCountries.png')
res = autorank(df_NewCasesLastDaysTop, alpha=0.05, verbose=False)
plot_stats(res)
plt.savefig('autorank.png')
f_result = open('result.txt','w')
f_result.write(str(res))
f_result.close()

