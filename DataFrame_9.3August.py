#9/08/2023-wednesday

#pandas shuffle DataFrame Rows
import pandas as pd
import numpy as np
technologies={'courses':["spark","pyspark","hadoop","python","pandas","oracle","java"],
              'fee':[20000,25000,26000,22000,24000,21000,22000],
              'duration':['30days','40days','35days','40days','60days','50days','55days'],
              'discount':[1000,2300,1500,1200,2500,2100,2000]}
df=pd.DataFrame(technologies)
print(df)

#pandas shuffle DataFrame Rows 
#shuffle the DataFrame rows & retrun all rows
df1=df.sample(frac=0.5)
print(df1)

#or
df1=df.sample(frac=1)
print(df1)

#create a new index starting from zero 
df1=df.sample(frac=1).reset_index()
print(df1)

#Drop shuffle index
df1=df.sample(frac=1)
print(df1)

#joins
import pandas as pd
import numpy as np
technologies1={'courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,30000],
              'duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index=index_labels)
print(df1)

technologies2={'courses':["spark","java","python","Go"],
              'discount':[2000,2500,1200,2000],
             }
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
print(df2)


#pandas inner join is mostly used join 
#it is used to join two DataFrame on indexs.
#when indexes don't match the rows get dropped from both DataFrame 

#pandas join by default it will join the tables left join 
df3=df1.join(df1,lsuffix="_left",rsuffix="_right")
df3

#pandas Inner join DataFrame 
df3=df1.join(df1,lsuffix="_left",rsuffix="_right",how='inner')
df3

#pandas left join DataFrame
df3=df1.join(df1,lsuffix="_left",rsuffix="_right",how='left')
df3

#pandas Right join on column 
df3=df1.join(df1,lsuffix="_left",rsuffix="_right",how='right')
df3

#pandas join column 
df3=df1.set_index('courses').join(df2.set_index('courses'),how='inner')
print(df3) 

#pandas left join DataFrame
df3=df1.set_index('courses').join(df2.set_index('courses'),how='left')
print(df3) 

#pandas Right join on column 
df3=df1.set_index('courses').join(df2.set_index('courses'),how='right')
print(df3) 

##################################################################################

#Pandas merge DatFrame-used as inner join
import pandas as pd
import numpy as np
technologies1={'courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,30000],
              'duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index=index_labels)
print(df1)

technologies2={'courses':["spark","java","python","Go"],
              'discount':[2000,2500,1200,2000],
             }
index_labels2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_labels2)
print(df2)

#using pandas.merge 
df3=pd.merge(df1,df2)
df3

#using DataFrame.merge()
df3=df1.merge(df2)
df3
##############################################################################
#use pandas.concat() to concat two DataFrame
import pandas as pd 
df=pd.DataFrame({'courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,24000]})

df1=pd.DataFrame({'courses':["pandas","hadoop","hyperion","java"],
              'fee':[25000,25200,245000,24900]})

#using pandas.concat() to concat two DataFrames
data = [df,df1]
df2=pd.Concat(data)
df2
##################################################################################
#concatenate multiple DataFrame using pandas.concat()
import pandas as pd 
df=pd.DataFrame({'courses':["spark","pyspark","python","pandas"],
              'fee':[20000,25000,22000,24000]})

df1=pd.DataFrame({'courses':["pandas","hadoop","hyperion","java"],
              'fee':[25000,25200,245000,24900]})

df2=pd.DataFrame({'duration':['30days','40days','35days','50days'],
            'discount':[2000,2500,1200,2000]})

#appending  multiple DataFrame
df3=pd.concat([df,df1,df2])
print(df3)

########################################################################































