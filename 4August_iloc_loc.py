import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","python","pandas",None,"spark"],
              'fee':[20000,25000,26000,22000,24000,np.nan,25000],
              'duration':['30days','40days','35days','40days','60days','35days',''],
              'discount':[11.8,23.7,13.4,15.7,12.5,14.4,13.2]})
row_labels=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

df=df.drop(['r1','r2'])
df

#deletd Row by index rane


#when u have default index for rows
df=pd.DataFrame(technologies)
df=df.drop(0)
df
df=pd.DataFrame(technologies)
df=df.drop([0,3]) #it will deleted rows0 and rows3
df
df=df.drop(range(0,2)) #it will deleted 0 and 1
df

########################################

import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","python","pandas",None,"spark"],
              'fee':[20000,25000,26000,22000,24000,np.nan,25000],
              'duration':['30days','40days','35days','40days','60days','35days','60days'],
              'discount':[11.8,23.7,13.4,15.7,12.5,14.4,13.2]})
df=pd.DataFrame(technologies)
print(df)



#drop coluns by index
print(df.drop(df.columns[1],axis=1))
df =pd.DataFrame(technologies)


#using inplace=True
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

######################################################
df=pd.DataFrame(technologies)
#drop 2 or more columns by lebel name
df=df.drop(["courses","fee"],axis=1)
print(df)

#drop 2 or more colums by index
df=pd.DataFrame(technologies)
df=df.drop(df.columns[[0,1]],axis=1)
print(df)

#drop columns from list of columns
df=pd.DataFrame(technologies)
df.columns
liscol=["courses","fee"]
df2=df.drop(liscol,axis=1)
print(df2)
###############################################################

#iloc=for index
#loc=for  slect the rw and columns
#imp. for intrview

import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","python","pandas",None,"spark","python"],
              'fee':[20000,25000,26000,22000,24000,np.nan,25000,22000],
              'duration':['30days','40days','35days','40days','60days','35days','60days','80days'],
              'discount':[11.8,23.7,13.4,15.7,12.5,14.4,13.2,12.4]})
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

#df.iloc[startrow:endrow,startcolumns:endcolumns]

df=pd.DataFrame(technologies,index=row_labels)
#below are quick example
#for columns
df2=df.iloc[:,0:2]
df2
#this line is used slicing to get Dataframe
#item by index
#the first slice [:] indicates to return all rows
#the second slice specified that onlu column between 0 and 2 (excluding 2) should be returned.

#for roes 
df2=df.iloc[0:2,:]
df2
#in this case the first slice indicate [0:2] 
###############################################
#slicing specified rows and columns using iloc 
df3=df.iloc[1:2,1:3] #it means that the only one row and 2 columns in that 
df3
######################################################

#select Rows by integer index
df2=df.iloc[2] #select row by index
df2

df2=df.iloc[[2,3,6]] #in double it select the row by index list
df2=df.iloc[1:5] #select rows by integer index range
df2=df.iloc[:1] #select First Rows
df2=df.iloc[:3] #select the first 3 rows
df2=df.iloc[-1:] #select the last Rows
df2=df.iloc[-3:] #select the last 3 Rows
df2=df.iloc[::2] #select the alternate rows
df2=df.iloc[::4] #select the alternate by rows

###################################3
#select Rows by index labels
df2=df.loc['r2'] #select Row by label
df2=df.loc[['r2','r3','r6']] #select the rows by index label in double 
df2=df.loc['r1':'r5']  #it include the 5th row also 
df2=df.loc['r1':'r5':2] #select alternate rows with index

#########################################################################################
#using loc[] to take columns slice
#loc[] syntax to slice columns
#df.loc[:,stat:stop:step]

import pandas as pd
import numpy as np
technologies=({'courses':["spark","pyspark","hadoop","python","pandas",None,"spark","python"],
              'fee':[20000,25000,26000,22000,24000,np.nan,25000,22000],
              'duration':['30days','40days','35days','40days','60days','35days','60days','80days'],
              'discount':[11.8,23.7,13.4,15.7,12.5,14.4,13.2,12.4]})
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
#select multiple columns
df2=df.loc[:,["courses","fee","duration"]]
#select ramdom columns
df2=df.loc[:,["courses","fee","discount"]]
#select columns between two columns
df2=df.loc[:"fee":"discount"]
#select colunmn by range
df2=df.loc[:,"duration"]
#select columns by range 
#all columns upto 'duration'
df2=df.loc[:,:'duration']
df2







































