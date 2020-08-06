import pandas as pd
from autorank import autorank, create_report, plot_stats, latex_table
import matplotlib.pyplot as plt

numTopCountires = 10
df_NewCasesLastDays = pd.read_csv('df_newCasesLastDays.csv', parse_dates=['Date_reported'], index_col='Date_reported')
df_TopCountries = df_NewCasesLastDays.sum().sort_values(ascending=False).head(numTopCountires)    # Sorte and select top countries
list_TopCountriesName = list(df_TopCountries.keys())
df_NewCasesLastDaysTop = df_NewCasesLastDays[list_TopCountriesName]
result = autorank(df_NewCasesLastDaysTop, alpha=0.05, verbose=False)    # Calculate autorank for these top countries
plot_stats(result)    # Utilise aoutorank built-in plotting function
plt.savefig('images/autorank.png')
create_report(result)    # Print report