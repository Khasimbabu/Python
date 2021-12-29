### Custom definitions and classes if any ###
import os

print(os.getcwd())
os.chdir('C:\Khasim\DS\ipl2021Project')
print(os.getcwd())

import pandas as pd

df = pd.read_csv('335982.csv')
df.head()

'''
def predictRuns(testInput):
    prediction = 0
    ### Your Code Here ###
    return prediction
'''

df.columns=['venue','innings','batting_team','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']