import pandas as pd
import numpy as np
import operator


data = pd.read_csv('country_vaccination_stats_filledNA.csv')


country_median = {}
for i in data['country'].unique():
   country_median[i] = data['daily_vaccinations'][data['country'] == i].median()
   
   
sorted_dict = sorted(country_median.items(), key=operator.itemgetter(1))
print(sorted_dict[-3:])