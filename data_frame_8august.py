#8/8/2023-tuesday
import pandas as pd
technologies={'courses':["spark","pyspark","hadoop","python","pandas"],
              'fee':[20000,25000,26000,22000,24000],
              'duration':['30days','40days','35days','40days','60days'],
              'discount':[11.8,23.7,13.4,15.7,12.5]}
row_labels=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_labels)
print(df)

#pandas .Dataframe .query() by example
#query all rows with courses equal "spark"
df2=df.query("courses == 'spark'")
print(df2)

#Not equal continon 
df2=df.query("courses ! = 'spark'")
print(df2)
################################################################3
import pandas as pd
technologies={'courses':["spark","pyspark","hadoop","python","pandas"],
              'fee':[20000,25000,26000,22000,24000],
              'duration':['30days','40days','35days','40days','60days'],
              'discount':[11.8,23.7,13.4,15.7,12.5]}

df=pd.DataFrame(technologies)
print(df)


#pandas add column to Dataframe 
#add new column to the data frame

tutors=['ram','sham','ghansham','ganesh','ramesh']
df2=df.assign(TutorAssigned=tutors)
print(df2)

#add multiple column to the datframe 
MNCCompanies = ['TATA','HCL','INFOSYS','GOOGLE','AMAZON']
df2=df.assign(MNC=MNCCompanies,tutorAssigned=tutors)
df2

#derive new column from existing column 
df=pd.DataFrame(technologies)
df2=df.assign(Discount_percent=lambda x:x.fee * x.discount / 100)
print(df2)


#Append column to Existing pandas Datframe 
#Add new column to the existing dataframe 
df= pd.DataFrame(technologies)
df["MNCCompanies"]=MNCCompanies
print(df)


#Add new column ata specific position 
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors) #tutors are list
print(df)

#Quick example of get the number of rows in DataFrame 
rows_count=len(df.index)
rows_count
 
rows_count=len(df.axes[0])
rows_count

column_count=len(df.axes[1])
column_count

###########################################################
df=pd.DataFrame(technologies)
rows_count=df.shape[0] #retrun the no. row
column_count=df.shape[1] #retuen the no. column 
print(rows_count) #output is 5
print(column_count)  #output  is 3


 




















