#python program to create one dimensional array
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)

#write a pandas prog. to convert a pandas module series to python list and it's type
#IMP. for intrview 
import pandas as pd
ds=pd.Series([2,4,6,8,10])
print(ds)
print(type(ds))
print("Convert pandas Series to python list")
print(ds.tolist())
print(type(ds.tolist())) 

#write prog. to add, substact,multiple and divide two series
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
ds=ds1+ds2
print("Add two series")
print(ds)
print("Subtract two series")
ds=ds1-ds2
print(ds)
print("Multiple two series")
ds=ds1*ds2
print(ds)
print("Divide two series")
ds=ds1/ds2
print(ds)

#write pandas prog. to compared the element
import pandas as pd
ds1=pd.Series([2,4,6,8,10])
ds2=pd.Series([1,3,5,7,9])
print("Series1:") 
print(ds1)
print("Series2:")
print(ds2)
print("Compared the elment of the  said series:")
print("Equal")
print(ds1==ds2)
print("Greater than:")
print(ds1>ds2)
print("less thann")
print(ds1<ds2)
    
#write pandas prog. to convert a dictionry to a pandas series
import pandas as pd
d1={'a':100,'b':200,'c':300,'d':400,'e':800}
print("Original dictionary:")
print(d1)
new_series=pd.Series(d1)
print('converted series:')
print(new_series)


#write pandas prog. to convert a numpy array to pandas series
import numpy as np
import pandas as pd
n_a=np.array([10,20,30,40,50])
print("Numpy array")
print(n_a)
new_series=pd.Series(n_a)
print("converted pandas series")
print(new_series)


#write a pandas prog. to change  the data type of given column or series
import pandas as pd
s1=pd.Series(['100','200','python','300.12','400'])
print("original data series:") 
print(s1)
print("change the said data type to numeric:")
s2=pd.to_numeric(s1,errors='coerce')
print(s2)

#write pandas prog to convert first column of dataframe as series
#imp. for intview 
import pandas as pd
d={'col1':[1,2,3,4,7,11],'col2':[4,5,6,9,5,0],'col3':[7,5,8,12,1,11]}
df=pd.DataFrame(data=d)
print("Original Data frame")
print(df)
s1=df.iloc[:,0] #all rows and 0th column 
print("\n1st column as a series")
print(s1)
print(type(s1)) 

##########################################
import pandas as pd
s = pd.Series([['red','green','white'],['red','black'],['yellow']])
print("original series of list")
print(s)
s=s.apply(pd.Series).stack().reset_index(drop=True)
print("one series")
print(s) 



#stack() function is used to stack the prescribed level(s) from column to  index
import pandas as pd
s = pd.Series([['red','green','white'],['red','black'],['yellow']])
print("original series of list")
print(s)
s1=s.apply(pd.Series)
s2=s1.stack()
s3=s2.reset_index(drop=True)
print("one series")
print(s3)
          
###########################################################

#write pandas  prog. to some data to an exiting series 
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("original data series:")
print(s)
print("\nData science after adding some data")
new_s=pd.concat([s,pd.Series([500,"php"])],ignore_index=True)
print(new_s)

#write pandas prog. to sort a given series
import pandas as pd
s=pd.Series(['100','200','python','300.12','400'])
print("original data series:")
print(s)
new_s=pd.Series(s).sort_values()
print(new_s)

#write pandas change the order of index of given series
import pandas as pd
s=pd.Series(data=[1,2,3,4,5],index=['A','B','C','D','E'])
print("original data series")
print(s)
s=s.reindex(index=['B','A','C','D','E'])
print("data science after changing the order of index:")
print(s)


            
            








































