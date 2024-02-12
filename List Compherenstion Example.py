# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:17:46 2023

@author: Sanchita Gunjal
"""

#find all the number from 1-1000 that are divisible 7

div=[n for n in range(1,1000) if n%7==0]
print(div)


#find all the number from 1-1000 that have a 3 in them
num=[n for n in range(0,1000) if '3' in str(n)]
print(num)

#count the number of spaces in string
some_string='The slow solid squid swam sumptuously through the slimy swamp'
spaces=[s for s in some_string if s==' ']
print(len(spaces))

#Create a list of all the consonants in the string
sentence='''yellow yaks like yelling and yawning and yesturday they while eating yuky yams'''
result=[letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(result)

#find common no. in two  list (without using a tupleor set) list

list_a=[1,2,3,4]
list_b=[2,3,4,5]
common=[a for a in list_a if a in list_b ]
print(common)
####################################
#ready reference code 
#used in NLP
#Get only the number in sentence like'In 1884  there were 13 instances of s protest
sentence='In 1884  there were 13 instances of a protest with over 1000 people attending'
words=sentence.split()
result=[number for number in words if not number.isalpha()]
print(result)

#Given 
result=[]
for n in range (20):
    if n %2==0:
        result.append('Even')
    else:
        result.append('odd')
print(result)
        
#List comrehension 
result=['even' if n%2==0 else 'odd' for n in range (20)]
print(result)
        
##################################################
#produce a list if tuple consisting of only matching number
list_a=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
result=[(a,b) for a in list_a for b in list_b if a==b]
print(result)      

#find all of the words in string that are less than 4 letters
sentence='On a summer day Ramnath sonar went swimming in the sun and his red skin stung'
examine=sentence.split()
result=[word for word in examine if len(word) <=4]
print(result)

#find all of the words in string that are greater than 4 letters
sentence='On a summer day Ramnath sonar went swimming in the sun and his red skin stung'
examine=sentence.split()
result=[word for word in examine if len(word) >=4]
print(result)

#Write prog. to print a specified list after removing the 0th,4th,5th element
color=['Red','Green','white','black','pink','yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

########################################################
#Home Work 
#compare two sentences and find out common word in that sentences

def sentence_to_list(sentence1):
    word=sentence1.split()
    return word

sentence1 ="This is very big news related with data science field"

list_a=sentence_to_list(sentence1)
#print(list_a)


def sentence_to_list(sentence2):
    word=sentence2.split()
    return word

sentence2 ="Our Aim is to Find out data science field"

list_b=sentence_to_list(sentence2)
#print(list_b)


common = [a for a in list_a if a in list_b]
print(common)













