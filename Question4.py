import pandas as pd
import numpy as np

data = pd.read_csv('country_vaccination_stats.csv')


naIndex = list(data["daily_vaccinations"].index[data["daily_vaccinations"].apply(np.isnan)])

for i in naIndex :    
    minVal = data["daily_vaccinations"][data["country"] == data["country"][i]].dropna().min()
    data["daily_vaccinations"][i] = minVal
    
data.fillna(0,inplace = True)   

#data.to_csv("country_vaccination_stats_filledNA.csv",index = False)

