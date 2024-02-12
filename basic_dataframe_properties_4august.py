#basic dataframe properties
import pandas as pd
technologies={'courses':["spark","pyspark","hadoop","python","pandas"],
              'fee':[20000,25000,26000,22000,24000],
              'duration':['30days','40days','35days','40days','60days'],
              'discount':[11.8,23.7,13.4,15.7,12.5]}
df=pd.DataFrame(technologies)
df

#convert dataframe to csv
df.to_csv('data_file.csv')

#to read file
#create dataframe from csv file
df=pd.read_csv('data_file.csv')
df


#pandas dataframe - basic operation
#providing some null values
#EDA- Exploratory Data Analysis
import pandas as pd
import numpy as np
technologies={'courses':["spark","pyspark","hadoop",None,"python","pandas"],
              'fee':[20000,25000,26000,22000,24000,np.nan],
              'duration':['30days','','40days','35days','40days','60days'],
              'discount':[11.8,23.7,13.4,15.7,12.5,14.2]}
row_labels=['r0','r1','r2','r3','r4','r5']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
 
#dataframe properties
df.shape
#it returns number of rows and columns(6,4)

#multiplication of rows and columns
df.size

#returns column names
df.columns

#same as above
df.columns.values 

#returns index name of df
df.index

#returns type of column
df.dtypes 

#gives information about dataframe
df.info

#accessing one column contents
df['fee']

#accessing two column contents
df[['fee','duration']]

#select certain rows and assign it to another dataframe
#[rows:columns]
#also written as [str row:end row,str col:end col] 
#where str row,col,end row,col=numbers / index
df2=df[4:]
df2

#accessing certain cell from column 'duration'
df['duration'][3] 

#subtracting specific value from a column
#500 subtracted from all the elements of fee
df['fee']=df['fee']-500 
df['fee'] 

#pandas to manipulate dataframe
#describe dataframe
#describe dataframe for all numberic columns
#it will show 5 number summary it will required open () 
df.describe()

#renames pandas dataframe columns
#assign new header by setting new column names
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df
 
#rename column names using rename() method
df=df.rename({'A':'C1','B':'C2'},axis=1)
#OR
df2=df.rename({'C':'C3','D':'C4'},axis='columns')
#OR
df2=df.rename(columns={'A':'C1','B':'C2'})

#drop dataframe rows and columns
df=pd.DataFrame(technologies,index=row_labels)

#drop rows by labels
df1=df.drop(['r1','r2'])
df1 

#delete rows by index 
df1=df.drop(df.index[1])
df1

df1=df.drop(df.index[[1,3]])
df1

#delete rows by index range
df1=df.drop(df.index[2:])
df1

#when we have default indexing 
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1 
df=pd.DataFrame(technologies)
df1=df.drop([0,3]) #delete row 0 and 3 
df1
#OR
df1=df.drop(range(0,3)) #delete from 0 to 2
df1

#drop columns by name
df2=df.drop(['fee'],axis=1)
print(df2) 
#OR 
df2=df.drop(labels=['fee'],axis=1)
df2
#OR
df2=df.drop(columns=['fee'],axis=1)
df2

#drop column by index
print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(technologies)

#inplace=True
#when we want to make changes in original dataframe then
#we use inplace=True
#before we are making changes in dataframe and assign it 
#to new dataframe and original dataframe remains unchanged
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

#drop two or more columns by label
df=pd.DataFrame(technologies)
df2=df.drop(['courses','fee'],axis=1)
print(df2)

#drops two or more column by index
df=pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)

#drop columns from list of columns
df=pd.DataFrame(technologies)
df.columns
liscol=['courses','fee']
df2=df.drop(liscol,axis=1)
print(df2) 

