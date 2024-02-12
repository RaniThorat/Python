import numpy as np
import pandas as pd
technologies=({'courses':["spark","pyspark","hadoop","python","pandas",None,"spark"],
              'fee':[20000,25000,26000,22000,24000,np.nan,25000],
              'duration':['30days','40days','35days','40days','60days','35days',''],
              'discount':[11.8,23.7,13.4,15.7,12.5,14.4,13.2],
              'time':['8am','9am','10am','5am','6am','8am']})
df3=pd.DataFrame(technologies)
print(df3)

df3.columns
df3.columns=['A','B','C','D','E']


