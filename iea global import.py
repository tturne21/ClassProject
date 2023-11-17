import pandas as pd
import numpy as np
import matplotlib as plot
import openpyxl
#do this second
df1= pd.read_csv('IEA_Global_EV_2030_Projections_Data_2023.csv')
df2= pd.read_excel('StatePopulations.xlsx')
df3= pd.read_excel('mv-registration-counts-by-state.xlsx')
df4= pd.read_excel('ev-registration-counts-by-state_6-30-22(altered).xlsx')




df4.drop(['Unnamed: 0', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace= True)
9:41
df4.rename(columns={'Unnamed: 1': 'state', 'Unnamed: 2': 'population'}, inplace=True)


#fixes index
df4.reset_index(drop=True, inplace=True)
#drops that state row
df4.drop([0],inplace= True)



df1['region'].value_counts()
#(what is happening in pandas is it takes the entire dataframe and selects only (aka indexes) against the region column, after that it creates basically a series, where the region is the indesx and the second column is the values of that index)