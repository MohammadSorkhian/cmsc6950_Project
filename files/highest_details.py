import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

numLastDays = 30
numTopCountires = 10

# Calculate mean of top countries in lastDays
df_NewCasesLastDays = pd.read_csv('df_newCasesLastDays.csv', parse_dates=['Date_reported'], index_col='Date_reported')
df_TopCountries = df_NewCasesLastDays.sum().sort_values(ascending=False).head(numTopCountires)    # Sorte and select top countries
list_TopCountriesName = list(df_TopCountries.keys())    # Extract name of these top countries
df_NewCasesLastDaysTop = df_NewCasesLastDays[list_TopCountriesName]    # Extract these top countries into a dataframe
se_NewCasesLastDaysTopMean = df_NewCasesLastDaysTop.mean()    # Calculate mean for these countries
# Calculate mean of top countries in lastPeriod
df_NewCasesLastPeriod = pd.read_csv('df_newCasesLastPeriod.csv', parse_dates=['Date_reported'], index_col='Date_reported')
df_NewCasesLastPeriodTop = df_NewCasesLastPeriod[list_TopCountriesName]    # Extract these top countries into a dataframe
se_NewCasesLastPeriodTopMean = df_NewCasesLastPeriodTop.mean()    # Calculate mean for these countries

# Line Grath: last month in detail
df_NewCasesLastDaysTop.plot.line(figsize=(12,5))
plt.title(f'New detected Covid-19 in top {numTopCountires} countries over last {numLastDays} days')
plt.ylabel('Number of New Cases')
plt.xlabel('Date')
plt.legend(bbox_to_anchor=(1, 1.02))
plt.tight_layout()
plt.savefig('images/TopCountries.png')

# Bar Grath: Top countries MOM
lastDays = list(se_NewCasesLastDaysTopMean)
lastPeriod = list(se_NewCasesLastPeriodTopMean)
x = np.arange(len(list_TopCountriesName))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x + width/2, lastDays, width, label='Last Month')
rects2 = ax.bar(x - width/2, lastPeriod, width, label='A Month before Last')
ax.set_title(f'Month over Month new detected Covid-19 cases in top {numTopCountires} countries')
ax.set_ylabel('Number of New Cases')
ax.set_xticks(x)
for tick in ax.get_xticklabels():
    tick.set_rotation(80)
ax.set_xticklabels(list_TopCountriesName)
ax.legend()
fig.tight_layout()
plt.savefig('images/TopCountriesCompare.png')