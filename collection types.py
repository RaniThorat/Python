# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:32:55 2023

@author: Sanchita Gunjal
"""

#python collection type-1>Tuple=is used to stored multiple item in single varible
#writen in round bracket
tup1=(1,3,5,7)
#Accesing elements of a tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:\t',tup1[1])
print('tup1[2]:\t',tup1[2])
print('tup1[3]:\t',tup1[3])


#Tuple can hold different types
tup2=(1,'john',True,-23.45)
print(tup2)

#Iterating over tuples
tup3=('apple','orange','plum','apple')
for x in tup3:
    print(x) 
#length of tuple 
tup3=('gg','gayatri',True,"pinki","smart")
len(tup3)

#u can count how many time specified value 
#a tuples allow duplicates

tup4=('apple','orange','gg','apple','apple')
tup4.count('apple')
print(tup4.index('apple'))
print(tup4.index('gg'))
#checking if an elements exits
tup3=('apple','banana','plum',"orange")
if 'orange' in tup3:
    print('orange is in Tuple')
else:
    print('orange is not in Tuple')

#Nested Tuples
tuple1=(1,3,5,7)
tuple2=('joh','denis','phoebe','adam')
tuple3=(42,tuple1,tuple2,5.5)
print(tuple3)
#it is not possible to add or remove
#elements from a tuple;they are immutable


#2>List=mutable
#creating list
lst1=['john','paul','George','Ringo']
#u also have the nested list
lst1=[1,43.5,True]
lst2=['apple','orange','31']
root_list=['john' ,lst1,lst2,'gg']
print(root_list)

#Accessing elements from list
lst1=['john','paul','gg','Rongo']
print(lst1[-1])
lst1[0]
lst1[-2]
#append of list 
lst4=[1,2,3,4,5,6]
lst4.append(4)
print(lst4)
#sum of list
lst4=[1,2,3,5,2,2]
print(sum(lst4))

############################################
lst1=['john','paul','george','Ringo']
print('lst1[1]:',lst1[-1])
print('lst1[-1]:',lst1[-1])
print('lst1[1:3]:',lst1[1:3])
print('lst1[1:]:',lst1[1:])

#Adding a list
lst1=['john','paul','gh','ringo']
lst1.append('gayatri')
print(lst1)
#extend a list
lst1=['gg','paul','gg','ringo','pete']
lst1.extend(['gayatri','gggg'])
print(lst1)

#Inserting a list
a_list=['aaa','madonna','gg']
print(a_list)
a_list.insert(1,"gayatri")
print(a_list)

#
lst1=[1,2,5,6]
lst1.insert(2,3)  #we putting th element 3 in second indexing number
print(lst1)

##list concantenation
lst1=[3,2,1]
lst2=[6,5,4]
lst3=lst1+lst2
print(lst3)



######################################################
#Assignment
#1>Take 5 no.in list and find minimum of the list
list1=[5,44,35,3,87,90]
min_numb=min(list1)
print("mininum number:",min_numb)


#2>Take 5 no. on list find maximum of the list
list2=[2000000000000000000,233,11,444444444444,34]
max_num=max(list2)
print("maximum value:",max_num)


#3>Take 5 string in list and make it revesed
list3=["gayatri","GG","sai","PG","RRty"]
reversed_list=[string[::-1] for string in list3]
print("reversed:",reversed_list)

########insert 
list3.insert(2,"sanjivani")
print(list3)

#4>Take 10 no. in list write script to searched for a value
lst4=[3,5,7,8,9,12,34,56,47,]
i=int(input(print("enter a no.:")))
if i in lst4:
    print("exits")
else:
    print("not exits")
#5>take 10 no. in list inseart some duplicated no.write to find duplicated
list4=[1,2,11,12,14,11,2,4,5,4,]
l1=[]
for i in list4:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')

#6>take vowels in list and non vowels letter find out no. of vowels in list

lst5=['a','r','w','v','u','x','o','g','e','l']
count=0
for i in lst5:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(f"Total vowels present in list are {count}")

################################################################
#27/07/2023
#Removing from list
another_list=['grey','mark','robbie','jason','howard']
print(another_list)
another_list.remove('robbie')
print(another_list)

#The pop() method 
lst6=['once','upon','a','time']
print(lst6)
print(lst6.pop(2))
print(lst6)

#Inserting into a list
a_list=['gg','gp','mn','ji']
print(a_list)
a_list.insert(1,'gayatri')
print(a_list)


#3>Creating Set
#do not allow to dublicate element
basket={'apple','orange','apple','pear','orange','banana','banana'}
print(basket)

#Accessing elements in a set
for item in basket:
    print(item)

#Adding item to set
basket={'apple','orange','banana'}
basket.add('apricot')
print(basket)

# want to add multiple element in set 
basket={'apple','orange','banana'}
basket.update(['apricot','mango'])
print(basket) 
#obtaining the length of set
basket={'apple','orange','apple','pear','orange'}
print(len(basket))

#obtaining the max and min value in set
basket2={23,45,67,12,456}
print(max(basket2))
print(min(basket2))

#Removing item from set
basket={'apple','banana','apple'}
basket.remove('apple')
print(basket)

#set operation
s1={'apple','orange','banana'}
s2={'grapefruit','lime','banana'}
print('union:',s1 | s2) 
print('Intersection:',s1 &s2)
print('Difference:',s1 - s2)

#Dictionaries
capital={'Maharashtra':'mumbai',
         'Gujrat': 'ahmadbad',
         'up':'Lakhnow',
         'karnataka':'banglore',
         'Andhrapradesh':'hydrabad'}
print(capital)
#Accessing item via keys
print('capital[Maharashtra]:',capital['Maharashtra'])
#Adding a New Entry 
capital['west_bengal']='kolkatta'
print(capital)
#changing a key value
capital['Gujrat']='gandhinagar'
print(capital)
#removing an entry
capital.pop('karnataka')
print(capital)
#deleting element
del capital['up']
print(capital)
#Interating over keys
capital={'Maharashtra':'mumbai',
         'Gujrat': 'ahmadbad',
         'up':'Lakhnow',
         'karnataka':'banglore',
         'Andhrapradesh':'hydrabad'}
for state in capital:
    print(state,end=',')

for state in capital:
    print(state,end=',')
    print(capital[state])
   ###################### 
capital={'Maharashtra':'mumbai',
         'Gujrat': 'ahmadbad',
         'up':'Lakhnow',
         'karnataka':'banglore',
         'Andhrapradesh':'hydrabad'} 
for state in capital:
    print(state,end=',')
    print(capital[state])   
    
    
#values,keys,item
capital={'Maharashtra':'mumbai',
         'Gujrat': 'ahmadbad',
         'up':'Lakhnow',
         'karnataka':'banglore',
         'Andhrapradesh':'hydrabad'} 
print(capital.values())
print(capital.keys())
print(capital.items())

#checking the key membership
print('karnataka'in capital)
print('bihar' not in capital)
#ontaning the lenghth of a dictionary 
print(len(capital))
#to get value of key in dictionaries
print(capital.get('up'))
#Dictionaries can have values in tuple
seasons={'summer':('feb','mar','apr','may'),
         'Rainy':('june','july','august','sept'),
         'Winter':('oct','nov','december','january')}
print(seasons['Rainy'])
print(seasons['Rainy'][0])
print(seasons['Winter'])
print(seasons['summer'])

#Dictionary method 
#get()is useful method to access 
#Dictionaries can not have two item with the same key
dict2={
       'brand':"maruti",
       'model':"breeza",
       'year':2021,
       'year':2020
       }
print(dict2)

#loop through a dictionary ,it will show thw key 
for x in dict2:
    print(x)
#print all value in dictionary 
for x in dict2:
    print(dict2[x])

#write python prog. to all the item in the list
def sum_list(items):
    sum=0
    for x in items:
        sum=x+sum
    return sum 
print(sum_list([2,2,2,]))

      
    
    
    













