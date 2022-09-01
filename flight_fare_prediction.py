# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings


dfflight=pd.read_excel(r"D:\spc\archive\Data_Train.xlsx")
print(dfflight.head(2)) 


 
#removing unwanted columns

print(dfflight.columns)


dfflight.drop(['Route','Additional_Info'], axis=1, inplace=True) 

print(dfflight.columns)

#checking Nan values


print(dfflight.isna().sum())

dfflight.dropna(inplace=True)



#convert departure time in hrs and minuts

print(dfflight['Dep_Time'])

dfflight["Dep_hr"] = pd.to_datetime(dfflight['Dep_Time']).dt.hour
print(dfflight['Dep_hr']) 

dfflight['Dep_min']=pd.to_datetime(dfflight['Dep_Time']).dt.minute
print(dfflight['Dep_min'])


dfflight['Arr_hr']=pd.to_datetime(dfflight['Arrival_Time']).dt.hour
print(dfflight['Arr_hr'])

dfflight['Arr_min']=pd.to_datetime(dfflight['Arrival_Time']).dt.minute
print(dfflight['Arr_min']) 


 

 
dfflight["journey_date"]=pd.to_datetime(dfflight['Date_of_Journey'], format=("%d/%m/%Y")).dt.day

print(dfflight['journey_date'])

dfflight['journey_month']=pd.to_datetime(dfflight['Date_of_Journey'], format='%d/%m/%Y').dt.month

print(dfflight['journey_month'])