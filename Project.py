import pandas as pd
from datetime import date

#fetching the preliminary data excel
df1 = pd.read_excel("Data.xlsx")

#taking the maximum value column into a list
max_value = df1['Max_Value']
#taking the minimum value column into a list
min_value = df1['Min_Value']
#taking the original value column into a list
orig_value = df1['Original_Price']

avg = list()
dep = list()

for i in range(len(min_value)):
    avg.append((max_value[i] + min_value[i]) / 2)
for i in range(len(min_value)):
    dep.append(orig_value[i] - avg[i])
# adding the column of average value and depreciation to the dataframe
df1['Avg_Value'] = avg
df1['Depreciation'] = dep

#saving the update data frame as a csv file
df1.to_csv(r'Data.csv')

df2 = pd.read_csv('Data.csv')
dep2 = []

#grouping the data by year
dep1 = df1.groupby('Year')
#finding the minimum depreciation for each year
dep2 = dict(dep1['Depreciation'].min())

years = list(dep2.keys())
dep_min = list(dep2.values())

make = []
#finding the corresponding make for the minimum depreciation foe all years
for i in range(9):
    make.append(df1['Make'].loc[(df1.Year == years[i]) & (df1.Depreciation == dep_min[i])].iloc[0])
    print(str(make[i]) + ' ' + str(int(date.today().year)-years[i]) + " " + str(dep_min[i]))

df3 = pd.DataFrame({'Year': years,'Brand': make , 'Minimum Depreciation': dep_min})

#saving the corealated brands, years and minimum depreciation
df3.to_csv(r'Data1.csv')
