import pandas as pd
import numpy as np

df=pd.read_csv("C:/2-dataset/Seeds_data.csv.xls")
print(df)

df.describe()

# Program to get the first three rows of a given DataFrame
df2 = df.iloc[:3]
df2

#Pandas.DataFrame.query()
# Query all rows with Area equals to 14.29
df2=df.query("Area == 14.29")
print(df2)

########################

# not equals condition
df2=df.query("Area != 14.29")
df2


######################################################

# Derive new column fron existing column

df2 = df.assign(area_Percent=lambda x: x.length * x.Width / 100)
print(df2)


#######################################################


# Get the number of rows in DataFrame
rows_count = len(df.index)
rows_count

rows_count = len(df.axes[0])
rows_count

column_count = len(df.axes[1])
column_count

########  Another Method  ########

row_count = df.shape[0]  #Returns number of Rows
column_count = df.shape[1]   #Returns number of columns
print(row_count)
print(column_count) 

rows_count = len(df.index[0:2])
print("total number of rows: "+str(rows_count))

rows_count = len(df.axes[0])
print("total number of rows: "+str(rows_count))

###############################################################

# Program to select name and score columns from given dataframe
df2 = df.iloc[:,:2]
df2

########## Another Method ###################
df2 = df.loc[:,['Area','Compactness']]
df2


# Program to select the specified columns and rows from a given data
df2 = df.iloc[1:4,[1,3]]
df2

# Program to select rows where width is greater than 2
print(df[df['Width']>2])



# Program to select rows the area is between 13.06 and 15.57
print("Rows where the area is between 13.06 and 15.57: ")
print(df[df['Area'].between(13.06, 15.57)])


# Program to select number of rows where the area is less than 13 and length greater than 5
print(df[(df['Area']< 13) & (df['length']>5)])


# Program to change the Area in row 4 to 13
df.loc[4,'Area'] = 13  # Area = column name   and  4 = row name
df


# program to calculate sum of length
print(df['length'].sum())


# Program to calculate mean of area
print(df['Area'].mean())


# Program to append new row 215 to dataframe with the given
# values for each column
df.loc[215]= [16.77,14.13,1.22,2.567,5.234,8.22,4.123,3]
df


# program to sort the dataframe first by 'Area' in descending order
# then by 'len_ker_grove' in ascending order
df=df.sort_values(by=['Area'],ascending=[False])
print(df)
df = df.sort_values(by=['len_ker_grove'],ascending=[True])
print(df)


# To replace the Type column contain the value 1 by 1.1,
# 2 by 2.22 and 3 by 3.03
df['Type']=df['Type'].map({1 : 1.1, 2 : 2.22, 3 : 3.03})
df


# Program to change the value 2.699 to 15 in Assymetry_coeff
# column of the dataframe
df['Assymetry_coeff']=df['Assymetry_coeff'].replace(2.699,15)
print(df)


# Program to iterate over rows in dataframe
for index, row in df.iterrows():
    print(row['Assymetry_coeff'],row['Width'])



   
 















