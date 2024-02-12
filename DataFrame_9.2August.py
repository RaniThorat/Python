#9/08/2023-wednesday
#pandas get colummn names from dataframe 
import pandas as pd
import numpy as np 
technologies={'courses':["spark","pyspark","hadoop","python","pandas"],
              'fee':[22000,25000,23000,24000,26000],
              'duration':['30days','50days','30days',None,np.nan],
              'discount':[1000,2300,1000,12000,25000]}
df=pd.DataFrame(technologies)
print(df)

df.columns
#get the list of all column names from headers
column_headers = list(df.columns.values)
print("The column Header :",column_headers)

#using list(df) to get column header as list 
column_headers=list(df.columns)
column_headers

#using list(df) to get the list of all column Name 
column_headers=list(df)
column_headers
