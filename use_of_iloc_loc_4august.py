#SLICING OPERATORS
#use of iloc slicing operator 
import pandas as pd
technologies={'courses':["spark","pyspark","hadoop","python","pandas"],
              'fee':[20000,25000,26000,22000,24000],
              'duration':['30days','40days','35days','40days','60days'],
              'discount':[11.8,23.7,13.4,15.7,12.5]}
row_labels=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
 
#iloc used to extract some portion of dataframe by index
#df.iloc[startrow:endrow,startcol:endcol]
df=pd.DataFrame(technologies,index=row_labels)
df2=df.iloc[:,0:2] #it extracts all rows and 0 to 1 columns
df2

#same as above
df=pd.DataFrame(technologies,index=row_labels)
df2=df.iloc[0:2,:] #it extracts all columns and 0 to 1 rows
df2
#same as above
df2=df.iloc[0:2,0:2]#rows from 0 to 1 and columns from 0 to 1
df2 

df2=df.iloc[2] #only series of second row
df2
df2=df.iloc[[2,3,4]] #select rows by index of row
df2  
df2=df.iloc[1:5] #rows from 0 to 4 
df2
df2=df.iloc[:1] #only first row(r0)
df2
df2=df.iloc[:3] #first 3 row
df2
df2=df.iloc[-1:] #last row
df2
df2=df.iloc[-3:] #last 3 rows
df2
df2=df.iloc[::2]  #all the rows by jump of 2 means r1,r2,r4( select alternate row)
df2

#use of loc slicing operator
#select rows by labels
#when we access rows by labels it includes last row as well in range
df2=df.loc['r2'] #2nd row
df2
df2=df.loc[['r2','r3','r4']] #2nd,3rd,4th row
df2 
df2=df.loc['r2':'r4'] #row from 2 to 4
df2
df2=df.loc['r0':'r4':2] #row from r0 to r4 by jump of 2
df2


#SLICING OF COLUMNS
#df.loc[:,start:stop:step]
df2=df.loc[:,["courses",'fee','duration']] #all the rows with mentioned columns
df2 
df2=df.loc[:,'fee':'duration'] #columns between fee to duration
df2
df2=df.loc[:,'duration':] #all columns next to duration including duration
df2
df2=df.loc[:,:'duration'] #all columns upto duration
df2

#############################################################3















