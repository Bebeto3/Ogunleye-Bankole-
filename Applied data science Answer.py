# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 12:18:59 2022

@author: HP
"""


import pandas as pd
import matplotlib.pyplot as plot


UK = pd.read_csv('\Users\HP\Downloads\Population/GBR_Data.csv',delim_whitespace=True)
print(UK)
header = UK.columns
print(header)
print(UK.loc['Rural_population'])

# represent Population_total as 'pol'
# ,, Rural_population as 'rur'
# ,, Urban_population as 'urb'
# ,, Population_female as 'poF'
# ,, Population_male as 'pom'
# ,, Death_rate_crude as 'drC'
# ,, infant_deaths as 'ID'
data = {
        "pol": UK.loc['Population_total'],
        "rur": UK.loc['Rural_population'],
        "urb": UK.loc['Urban_population'],
        "poF": UK.loc['Population_female'],
        "poM": UK.loc['Population_male'],
        "drC": UK.loc['Death_rate_crude'],
        "iD": UK.loc['infant_deaths']
        }

# For Bar Chart
GBR = pd.DataFrame(data = data,index=UK.columns);

GBR.plot.bar(rot = 0,title='United kingdom Population Estimate & projections');
plot.yticks([100000000,200000000,300000000])
plot.draw();


# For Pie Chart

pieUK = pd.DataFrame({'population': UK.columns,
                      'rural population': UK.loc['Rural_population']})
Ruralplot = plot.subplot(121, aspect='equal')
print(pieUK)
pieUK.groupby(['population']).sum().plot(kind='pie',y='rural population',labels=pieUK['population'],ax=Ruralplot, autopct='%1.1f%%', 
 startangle=90, shadow=False,fontsize=8,legend = False)

pieGBR = pd.DataFrame({'population_year': UK.columns,
                      'urban population': UK.loc['Urban_population']})
Urbanplot = plot.subplot(121, aspect='equal')
print(pieGBR)
pieGBR.groupby(['population_year']).sum().plot(kind='pie',y='urban population',labels=pieGBR['population_year'],ax=Urbanplot, autopct='%1.1f%%', 
 startangle=90, shadow=False,fontsize=8,legend = False)



# For LINE Graph
Year = UK.columns
female_pop = UK.loc['Population_female']


plot.plot(Year, female_pop,label="female population")

plot.xlabel('Year')
plot.ylabel('Population')
plot.title('UK Female population projections')
plot.xticks(Year)
plot.yticks([90000000,100000000,110000000])
#plot.show()


male_pop = UK.loc['Population_male']
print(male_pop)

plot.plot(Year, male_pop,label='male projections')

plot.xlabel('Year')
plot.ylabel('Population')
plot.title('UK population projections')
plot.xticks(Year)
plot.yticks([90000000,100000000,110000000])
plot.legend()
plot.show()
