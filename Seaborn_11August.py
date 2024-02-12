#11/08/2023-Friday

#How to used Seaborn for Data Visulization 
#pip install seaborn 

import seaborn as sns 
import pandas 
import matplotlib.pyplot as plt
#seaborn has 18 in-built datasets that can be found useing the following command 
sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head()

sns.countplot(x='sex',data=df)
#x- The name of the column 
#data -The dataframe 

sns.countplot(x='sex',hue='survived',data=df,palette='Set1') #palette used for set of color 

sns.countplot(x='sex',hue='survived',data=df,palette='Set2')

sns.countplot(x='sex',hue='survived',data=df,palette='Set3')

######################################################################

#KDE Plot 
#A kernal Density Estimate (KDE) plot is used 
#to plot the distribution of continuous data 
sns.kdeplot(x='age',data=df,color='black')

######################################################################
#Distribution plot 
sns.displot(x='age',kde=True,bins=6,data=df)

#kde -It is set 
sns.displot(x='age',kde=True,bins=5,hue=df['survived'],palette='Set1',data=df)

######################################################################
#Scatter Plot 
#First ,we will need to load the iris dataset 

df=sns.load_dataset('iris')
df.head()

#scatter plot help understand co-relation between data,
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')

###########################################################################

#joint plot

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')

sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')

############################################################################

#pair plot 
sns.pairplot(df)

#########################################################################

#heat map 
#it is ised for  to visualize confusion ,matrices,& correlation 

corr = df.corr()
sns.heatmap(corr)




