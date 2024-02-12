# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:32:22 2023

@author: Admin
"""

#One hat encoder
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()

df=pd.read_csv("C:/Datasets/ethnic diversity.csv")
df.columns
#We have salaries and age as numerical col let us make them
#1 and 0th pos so to make furuther data processing is easy
df=df[['Salaries','age','Position','State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus','Department','Race']]
#check the dataframe in the variable explore
#We want only nominal data and ordinal data for preprocessing

enc_df=pd.DataFrame(enc.fit_transform(df.iloc[:,2:]). toarray())


###############################################################3
#Label encoder
from sklearn.preprocessing import LabelEncoder
#Creating instance of label encoder
labelencoder=LabelEncoder()
#Split your data into input and output values
x=df.iloc[:,0:9]
y=df['Race']
df.columns


x['Sex']=labelencoder.fit_transform(x['Sex'])
x['MaritalStatus']=labelencoder.fit_transform(x['MaritalDesc'])
x['CitizenDesc']=labelencoder.fit_transform(x['CitizenDesc'])


#Label encoder y
y=labelencoder.fit_transform(y)
#This is going to create an array hence convert it bakc to dataframe
y=pd.DataFrame(y)

df_new=pd.concat([x,y],axis=1)

#If you willl see the vairableexplore ,y do not have the col name
#Henace rename the col 
df_new=df_new.rename(columns={0:'Race'})



###################################################################
import pandas as pd 
im
