import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from autorank import autorank, create_report, plot_stats, latex_table
from pprint import pprint

df = pd.read_csv('WHO-COVID-19-global-data.csv', parse_dates=['Date_reported'])
days = 5
grouped_country = df.groupby(' Country')
dic_lastDays = {"Date_reported":list(df['Date_reported'].tail(days))}
for x, item in grouped_country:
    dic_lastDays[x] = list(item[' New_cases'].tail(days))
pd.set_option('display.max_columns', 10)
df_newCases_lastDays = pd.DataFrame(dic_lastDays)
res = autorank(df_newCases_lastDays.iloc[:, 1:5], alpha=0.05, verbose=False)
print(df_newCases_lastDays.iloc[:, :5])
print(res)