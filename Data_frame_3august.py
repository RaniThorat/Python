#create DataFrame from dictionary
import pandas as pd
technologies={'courses':["spark","pyspark","hadoop","python","pandas"],
              'fee':[20000,25000,26000,22000,24000],
              'duration':['30days','40days','35days','40days','60days'],
              'discount':[11.8,23.7,13.4,15.7,12.5]}
df=pd.DataFrame(technologies)
df

#convert dataframe to csv
df.to_csv('data_file.csv')

#To read csv file(to creat dataframe from csv file)
df=pd.read_csv('data_file.csv')
df

###################################################
#pandas DataFrame -Basic  operation
#create Dataframe with None/NUll to work with example

import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","python","pandas",None,"spark"],
              'fee':[20000,25000,26000,22000,24000,np.nan,25000],
              'duration':['30days','40days','35days','40days','60days','35days',''],
              'discount':[11.8,23.7,13.4,15.7,12.5,14.4,13.2]})
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
print(df) 

#dataframe properties
df.shape
#(7,4)

df.size
#28

df.columns
#Index(['courses', 'fee', 'duration', 'discount'], dtype='object')

df.columns.values
#array(['courses', 'fee', 'duration', 'discount'], dtype=object)

df.index
#Index(['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6'], dtype='object')

df.dtypes
#courses      object
#fee         float64
#duration     object
#discount    float64
#dtype: object

df.info
##########################################
#Accessing one column contents(used single [] brackets)
df['fee']

#Accessing two columns conent(used single double brackets)
df[['fee','duration']]

#Select certain rows and assign it to another dataframe([rows:columns])
#also writing as[str row:end row,str col:end col]
#where str row,col,end row,col=numbers/index
df2=df[4:]
df2

####################################
#Accessing certain cell from column 'duration'
df['duration'][3]

#substacting specific value from a column
df['fee']=df['fee']-500
df['fee'] 

#pandas to manipulate DataFrame
#describe DataFrame
#Describe dataframe for all numberic columns(only float, integer)
#it will show 5 number summary
#imp.for intrview
df.describe()

##########################################
#rename() -rename pandas DataFrame columns
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D'] #Assign new header by setting new columns names.
df


############################################
#Rename column Name using rename() method
#for accessing the row used axis=0 and accessing the column used the axis=1
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
#OR
df2=df.rename({'A':'c1','B':'c2'},axis=1)
#OR
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
#OR
df2=df.rename(columns={'A':'c1','B':'c2'})
#OR
df2=df.rename({'r0':'g1','r1':'g2'},axis=0) #for Rows 














