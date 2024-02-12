#9/08/2023-Wednesday

import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df)

''
def add_3(x):
    return x+3
df2=df.apply(add_3)
df2
df2=((df.A).apply(add_3))
df2
#Or used folowing method
df2=df.apply(lambda x: x+3)

#using apply function single column 
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]

#Apply to multiple column 
##when u'r going to apply function for multiple column u have pass the list of columns

df[['A','B']]=df[['A','B']].apply(add_4)
df

#Apply lambda function to each column 
df2=df.apply(lambda x : x+ 10)
df2

#using pandas.DataFrame .trnsform() to apply function column 
#using DataFrame.tarnsfrorm()
import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df) 

def add_2(x):
    return x+2
df =df.transform (add_2)
print(df)

#using pandas.DataFrame .map() to single column 
import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df) 

df['A']=df['A'].map(lambda A:A/2)
df 

#using numpy function on single column 
#using DataFrame.apply() & [] operator
import numpy as np 
import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df) 
#for single column 
df['A'] =df['A'].apply(np.square)
df
#for multiple column 
df[['A','B']]= df[['A','B']].apply(np.square)
df

#using numpy.sauare() method
#using numpy.square() and [] operator
import numpy as np 
import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}
df=pd.DataFrame(data)
print(df) 
df['A'] =np.square(df['A'])
print(df)

#pandas groupby() with example
import pandas as pd
import numpy as np
technologies={'courses':["spark","pyspark","hadoop","python","pandas","hadoop","spark","python","NA"],
              'fee':[22000,25000,23000,24000,26000,25000,25000,22000,15000],
              'duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
              'discount':[1000,2300,1000,12000,25000,np.nan,14000,1600,0]}
df=pd.DataFrame(technologies)
print(df)
 
#use groupby() to compute the sum 
df2=df.groupby(['courses']).sum()
print(df2) 

#Group by multiple column 
df2=df.groupby(['courses','duration']).sum()
print(df2) 

#Add index too the grouped data 
#Add Row  index to the group byb result 
df2=df.groupby(['courses','duration ']).sum().reset_index()
print(df2)








































