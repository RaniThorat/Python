#to update pandas to specific  or latest version
#conda install --upgrade pandas or conda install -c anaconda pandas
#update conda install update pandas==2.0.3 (to check update)
#

#To check the version version (imp. for intrview)
import pandas as pd
pd.__version__

# create using constuctor
#create pandas dataframe from list

import pandas as pd
technologies=[["spark",20000,"30days"],["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)

#since we have not given labels to columns and indexes,dataframe by default assigns incremental sequence no. as lebels to both


colum_names=["courses","fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=colum_names,index=row_label)
print(df)

##############################
#to check data type
df.dtypes

################################
#u can also assign custom data type to columns. 
#set custom  types to dataframe

import pandas as pd
technologies={'Courses':["spark","pyspark","Hadoop","python","pandas","oracle","java"],'Fee':[20000,25000,26000,22000,24000,21000,22000],'Duration':['30days','40days','35days','40dyas','60days','50days','55days'],'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]}
df=pd.DataFrame(technologies)
print(df.dtypes)
 

#convert object to string  used .dtypes
#convert all type to best possible type
df2=df.convert_dtypes()
print(df2.dtypes)

#change all columns to same type (to conver into object used astypes)(imp.)
df=df.astype(str)
print(df.dtypes)

#change type for one or multiple columns(imp)
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)

#convert data type for all columns in list
df=pd.DataFrame(technologies)
df
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df
#OR 
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes

#Ignore error
df=df.astype({"Courses":int},errors='ignore')
df.dtypes
#Generates error
df=df.astype({"Courses":int},errors='raise')




