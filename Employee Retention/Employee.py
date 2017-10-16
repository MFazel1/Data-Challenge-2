#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:11:46 2017

@author: fazelanjom
"""

import numpy as np
import pandas as pd


Data=pd.read_csv('employee_retention_data.csv',sep=',')

Data['Has-quit']=~Data['quit_date'].isnull()

#Columns=Index(['employee_id', 'company_id', 'dept', 'seniority', 'salary', 'join_date',
#       'quit_date', 'Has-quit'],
#      dtype='object')

Data['company_id'].value_counts()
Company_id_Retention_rate=Data.groupby(['company_id'])['Has-quit'].value_counts(normalize=True).rename('percentage').mul(100).reset_index()
#Data['Has-quit'].value_counts(normalize=True).rename('percentage').mul(100).reset_index()

Seniority_Retention_rate=Data.groupby(['seniority'])['Has-quit'].value_counts(normalize=True).rename('percentage').mul(100).reset_index()
Seniority_Retention_rate['Has-quit'].value_counts()
Seniority_Retention_rate_quit=Seniority_Retention_rate[Seniority_Retention_rate['Has-quit']==True]

Seniority_Retention_rate_quit=Seniority_Retention_rate_quit.drop(Seniority_Retention_rate_quit.index[[30,29]])


Company_id_dep_Retention_rate=Data.groupby(['company_id','dept'])['Has-quit'].value_counts(normalize=True).rename('percentage').mul(100).reset_index()
Company_id_dep_Retention_rate=Company_id_dep_Retention_rate[Company_id_dep_Retention_rate['Has-quit']==True]
Company_id_dep_Retention_rate['dept'].value_counts()
#customer_service    12
#engineer            12
#data_science        12
#marketing           11
#sales               11
#design              10

Company_id_dep_Retention_rate['company_id'].value_counts()
#10    6
#9     6
#8     6
#7     6
#6     6
#5     6
#4     6
#3     6
#2     6
#1     6
#12    4
#11    4

import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 2

customer_service =list(Company_id_dep_Retention_rate[Company_id_dep_Retention_rate['dept']=='customer_service'].percentage)
engineer = list(Company_id_dep_Retention_rate[Company_id_dep_Retention_rate['dept']=='engineer'].percentage)
data_science = list(Company_id_dep_Retention_rate[Company_id_dep_Retention_rate['dept']=='data_science'].percentage)
marketing = list(Company_id_dep_Retention_rate[Company_id_dep_Retention_rate['dept']=='marketing'].percentage)
sales = list(Company_id_dep_Retention_rate[Company_id_dep_Retention_rate['dept']=='sales'].percentage)
design = list(Company_id_dep_Retention_rate[Company_id_dep_Retention_rate['dept']=='design'].percentage)
Company_id= [1,2,3,4,5,6,7,8,9,10,11,12]
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, customer_service, bar_width,
                 alpha=opacity,
                 color='b',
                 label='customer_service')
 
rects2 = plt.bar(index + bar_width, engineer, bar_width,
                 alpha=opacity,
                 color='g',
                 label='engineer')
 
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('customer_service', 'engineer'))
plt.legend()
 
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
plt.plot(Seniority_Retention_rate_quit['seniority'], Seniority_Retention_rate_quit['percentage'], 'ro')
#plt.axis([0, 6, 0, 20])
plt.show()


#==============================================================================
# The feature to add
#==============================================================================
AVG_Salary_DEP=Data.groupby(['dept']).agg({'salary':'mean'}).reset_index()
Data['Below_average_Salary']=Data[Data.salary<(df1.text.values)]

mergeddf = pd.merge(df2,df1, how="left")
AVG_Salary_DEP['dept'].isin(Data['dept'])

def Check_salary:
    if()

Data.apply (lambda row: Check_salary (row),axis=1)


Data['join_date'] = pd.to_datetime(Data['join_date'])
