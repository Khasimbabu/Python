#*************************************************************************
# PYTHON PANDAS
#*************************************************************************
import numpy as np
import pandas as pd
list1 = [10,20,30,40]
print(list1)
print(type(list1))
print('*********')
list1_panda = pd.Series(list1)
print(list1_panda)
print(type(list1_panda))
print('*********')
data = ['SumanRao','Indian','Hyderabad']
label = ['Name','Nationality','Place_Of_Origin']
res = pd.Series(data, index=label)
print(res)
print('*********')
# convert Python dictionary into Panda series
data1 = {"Name":"Suman","Place":"Hyderabad","Pincode":500032}
res1 = pd.Series(data1)
print(res1)
print('*********')
res2 = pd.Series(data1, index=['Name','Pincode'])
print(res2)
print('*********')
# DataFrame of Pandas
data2 = {
    "total_corona_cases":[500,600,700],
    "total_active_cases":[100,200,300],
    "total_corona_deaths":[50,60,70]
}
res3 = pd.Series(data2)
print(res3)
print('*********')
res4 = pd.DataFrame(data2)
print(res4)
print(res4.loc[0])
print('*********')
date = ['1-July-2021','2-July-2021','3-July-2021']
res5 = pd.DataFrame(data2, index=date)
print(res5)
print(res5.loc['1-July-2021'])
print(res5.loc['1-July-2021']['total_corona_deaths'])
print('*********')
#******** Write a program to get the Total_corona_cases,Total_deaths,Total_active_cases with its % increase each
# with respect to other day.
total_cases = sum(res4.loc[:]['total_corona_cases'])
total_active = sum(res4.loc[:]['total_active_cases'])
total_deaths = sum(res4.loc[:]['total_corona_deaths'])
print(total_cases)
print(total_active)
print(total_deaths)
print('*********')
for i in date:
    print(i)
    print(((res5.loc[i]['total_corona_cases'])/total_cases) * 100)
    print(((res5.loc[i]['total_active_cases'])/total_active) * 100)
    print(((res5.loc[i]['total_corona_deaths'])/total_deaths) * 100)
print('*********')