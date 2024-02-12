
"""write a pandas programn to create a datafrane from dictionary and display 
sample data :{'X':[78,85,96,80,86], 'Y':[84,94,89,83,86], 'Z':[86,97,96,72,83]} 
"""

import pandas as pd
d={'X':[78,85,96,80,86],
    'Y':[84,94,89,83,86],
    'Z':[86,97,96,72,83]}

df=pd.DataFrame(d)
print(df)
  

'''
Write a pandas program to create and display A Dataframe from the specific  dictionary data which has 
Sample Python dictionary data and list  lables:
    exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
                'score':[12.5,9,16.5,np.nan,9,20],
                'attempt':[1,3,2,3,2,3],
                'qualify':['yes','no','yes','no','yes','no'],
                
               }
    lables=['a','b','c','d','e','f']
    
'''
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df

print("Summary of the basic information about the dataframe and its ")
print(df.info())
df.describe()


#----------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
 
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
    'score':[12.5,9,16.5,np.nan,9,20],
    'attempt':[1,3,2,3,2,3],
    'qualify':['yes','no','yes','no','yes','no'],
    }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df
 
print("First three row of the dataframe : ")
print(df.iloc[:3])


#-------------------------------------------------------------------------------------
#Write a pandas program to select the 'name' and 'score' columns from dataframe
import pandas as pd
import numpy as np
 
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
    'score':[12.5,9,16.5,np.nan,9,20],
    'attempt':[1,3,2,3,2,3],
    'qualify':['yes','no','yes','no','yes','no'],
    }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df
 
print("select the 'name' and 'score' columns : ")
print(df[['Name','score']])

#--------------------------------------------------------------------------------------------
#write a pandas program  to  select the specific column and rows from the a dataframe
'''
Expected output
   score qualify
a   12.5     yes
b    9.0      no
c   16.5     yes 
d    NaN      no
e    9.0     yes
f   20.0      no

'''
import pandas as pd
import numpy as np

exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df

print(" select the specific column and rows : ")
print(df[['score','qualify']])
########################################################
#Afternoon session 8/8/2023
#write pandas prog. to select row no. attempts in the examination is greter than 2
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df
print("no. attempts in the examination is greter than 2:")
print(df[df['attempt']>2])

#or we can also used following technique instead of above
df2=df.loc[df.attempt>2]
df2
###########################################################
#write pandas prog. to count the number of row and column of DataFrame

import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df
#for rows 
rows_count=len(df.axes[0])
rows_count
#for column 
column_count=len(df.axes[1])
column_count
print("no.of row:"+str(rows_count))
print("no.of column:"+str(column_count))

###############################################################
#write pandas prog. to select rows where the score is missing,i.e. is NaN

import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df
print("Rows where acore is missing:")
df2=(df[df['score'].isnull()])

############################################################
#write pandas prog. to select rows between 15 and 20(inclusive)
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om'],
   'score':[12.5,9,16.5,np.nan,9,20],
   'attempt':[1,3,2,3,2,3],
   'qualify':['yes','no','yes','no','yes','no'],
   }
lables=['a','b','c','d','e','f']

df=pd.DataFrame(exam_data, index=lables)
df
print("Rows where score between 15 and 20 (inclusive):")
df2=(df[df['score'].between(15,20)])

##################################################################
#write pandas prog. to select the rows where no. of attempts in the examination is less than 2 and score greater than 15
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("no. of attempt in the examination is less than 2 and score greater than 15:")
df2=(df[(df['attempt']<2) & (df['score']>15)])

###############################################################
#write a search pandas prog. to change the score in row 'd' to 11.5
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("\nchange the score in row 'd' to 11.5:")
df.loc['d','score'] = 11.5 #'d' is rows name and 'score ' is column name
print(df)

############################################################
#write pandas prog. to calculate the sum of the examination attempts by the student
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("\nsum of the examination attempts by the student:")
print(df['attempt'].sum())

#############################################################
#write a pandas prog. to cal. the mean of all student 'score'
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("\nmeans value of student:")
print(df['score'].mean())

#write pandas prog. to append to new row 'k' to DataFrame with given value for each column
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("original rows:")
print(df)
print("\n append a new row:")
df.loc['k']=['GP','20.5','2','no']
print("print all recoed after insert a new record:")
print(df)

#############################################################
#write pandas prog. to sort the DataFrame first by 'name' in decending order,then by 'score' in ascending order

import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("original rows:")
print(df)
df=df.sort_values(by=['Name','score'],ascending=[False,True]) #name is the descending order & score is ascending order
print()
print("sort the DataFrame first by 'name' in decending order,then by 'score' in ascending order:")
print(df)

#OR 

import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("original rows:")
print(df)
df=df.sort_values(by=['Name'],ascending=[False]) 
print(df)
df=df.sort_values(by=['score'],ascending=[True]) 
print(df)
print("sort the DataFrame first by 'name' in decending order,then by 'score' in ascending order:")
print(df)


###########################################################
#write pandas prog. to replace the 'qualify'column contain the values 'yes' and 'no' with True and False
#imp. for interview
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("original rows:")
print(df)
print("\nreplace the 'qualify'column contain the values 'yes' and 'no' with True and False:")
df['qualify']=df['qualify'].map({'yes':True,'no':False})
print(df)

################################################################
#write pandas prog. to change the name 'GG' to 'james' in name column of the DataFrame.
#imp
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
print("original rows:")
print(df)
print("\nchange the name 'GG' to 'james':")
df['name']=df['Name'].replace('GG','james') #GG is old name & james is new name 
print(df)

##############################################################
#write a search pandas prog. to insert a new column in existing DataFrame 
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
color=['Red','Blue','Orange','Red','white','Blue','Green']
df['color'] = color
print("\ninsert a new column in existing DataFrame i.e. color :")
print(df)

##############################################################
#write pandas prog. to iterate over rows in a DataFrame(imp)
import pandas as pd
import numpy as np
exam_data={'Name':['Ram','Sham','Ghansham','Babubhai','Krishna','Om','GG'],
   'score':[12.5,9,16.5,np.nan,9,20,21],
   'attempt':[1,3,2,3,2,3,1],
   'qualify':['yes','no','yes','no','yes','no','yes'],
   }
lables=['a','b','c','d','e','f','g']

df=pd.DataFrame(exam_data, index=lables)
df
for index,row in df.iterrows():
    print(row['Name'],row['score'])

################################################################


























































































































































































































