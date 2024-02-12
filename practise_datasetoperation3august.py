import pandas as pd
import numpy as np
df=pd.read_csv("loan.csv")
df
#to accessing the shape
df.shape
#(39717, 111)
#to accessing the size 
df.size
#4408587
#accessing the columns
df.columns

#to accessing the column.values
df.columns.values

df.index
#RangeIndex(start=0, stop=39717, step=1)

df.dtypes

#Accessing one column contents(used single [] brackets)
df['id']
#Or
df['term']

#Accessing two columns conent(used single double brackets)
df[['id','term']]

#pandas to manipulate DataFrame
#describe DataFrame
#Describe dataframe for all numberic columns(only float, integer)
#it will show 5 number summary
#imp.for intrview
df.describe()

df=df.rename({'id':'c1','term':'c2'},axis=1)

df=df.rename({'memebr_id':'c3','loan_amnt':'c4'},axis='columns')

##############################################
##when we have default indexing 
df=df.drop(0)
df 
 
#drop columns by name

#another method for read the file
import pandas as pd
import numpy as np
df=pd.read_csv("C:/2-dataset/loan.csv")
df

############################################################

import pandas as pd
import numpy as np
df=pd.read_csv("C:/2-dataset/crime_data.csv.xls")
df

#to accessing the shape
df.shape
#(50, 5)

#to accessing the size 
df.size
#250

#accessing the columns
df.columns
#Index(['Unnamed: 0', 'Murder', 'Assault', 'UrbanPop', 'Rape'], dtype='object')

#to accessing the column.values
df.columns.values
#array(['Unnamed: 0', 'Murder', 'Assault', 'UrbanPop', 'Rape'], dtype=object)
     
df.index
#RangeIndex(start=0, stop=50, step=1)

df.info

df.dtypes #string data type
'''Unnamed: 0     object
Murder        float64
Assault         int64
UrbanPop        int64
Rape          float64
dtype: object'''


#Accessing one column contents(used single [] brackets)
df['Murder']
#OR
df['Rape']

#Accessing two columns conent(used single double brackets)
df[['Murder','Rape']]

#pandas to manipulate DataFrame
#describe DataFrame
#Describe dataframe for all numberic columns(only float, integer)
#it will show 5 number summary
#imp.for intrview
df.describe()

#rename the columns
df=df.rename({'Murder':'GG','Rape':'GP'},axis=1)

df=df.rename({'Assault':'c3','UrbanPop':'c4'},axis='columns')

df=df.drop(0)

##############################################################
import pandas as pd
import numpy as np
df=pd.read_csv("C:/2-dataset/bank_data.csv.xls")
df
#to accessing the shape
df.shape
#(45211, 32)

#to accessing the size 
df.size
#1446752

#accessing the columns
df.columns
'''Index(['age', 'default', 'balance', 'housing', 'loan', 'duration', 'campaign',
       'pdays', 'previous', 'poutfailure', 'poutother', 'poutsuccess',
       'poutunknown', 'con_cellular', 'con_telephone', 'con_unknown',
       'divorced', 'married', 'single', 'joadmin.', 'joblue.collar',
       'joentrepreneur', 'johousemaid', 'jomanagement', 'joretired',
       'joself.employed', 'joservices', 'jostudent', 'jotechnician',
       'jounemployed', 'jounknown', 'y'],
      dtype='object')'''

#to accessing the column.values
df.columns.values

#to check the index 
df.index 
#RangeIndex(start=0, stop=45211, step=1)

df.info

#Checking the string data type
df.dtypes 

#Accessing one column contents(used single [] brackets)
df['age']
df['loan']
df['default']

#Accessing two columns conent(used single double brackets)
df[['age','loan','default']]

#pandas to manipulate DataFrame
#describe DataFrame
#Describe dataframe for all numberic columns(only float, integer)
#it will show 5 number summary
#imp.for intrview
df.describe()

#rename the columns
df=df.rename({'age':'A1','default':'A2'},axis=1)
 #OR
df=df.rename({'balance':'A3','housing':'A4'},axis='columns')

#Select certain rows and assign it to another dataframe([rows:columns])
df2=df[356:]
df2

#substacting specific value from a column
df['balance']=df['duration']-200
df['balance']








