# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:32:19 2023

@author: Sanchita Gunjal
"""

# write python prog. to all the item in the list


def sum_list(items):
    sum = 0
    for x in items:
        sum = x+sum
    return sum
print(sum_list([2, 2, 2,4]))



def sum_of(items):
    sum=0
    for x in items:
        sum=x+sum
    return sum
print(sum_of([2,3,4]))



def mul_of(items):
    mul=1
    for x in items:
        mul=x*mul
    return mul
print(mul_of([2,3]))

# write prog. to multiply all the item in the list
def multiply_list(items):
    tot = 1
    for x in items:
        tot = tot*x
    return tot
print(multiply_list([2, 2, 2]))

# write prog. for to get the largest no. from a list
list1 = [12, 6666, 89, 76, 0, 23]
print(max(list1))

# write prog. for to get the smallest no. from a list
list1 = [12, 6666, 89, 76, 0, 23]
print(min(list1))

# to count the number of string which satisfies
# condition string length is 2 or more and the first and last char from a given list of string

def match_words(words):
    ctr=0 #counter is 0
    for i in words:
        if len(i)>2 and i[0]==i[-1]:
            ctr +=1
    return ctr
print(match_words(['abc','xyz','aba','1221']))
        
#write prog. to get a list sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
#sample list:[(2,5),(1,2),(4,4),(2,3),(2,1)]
#Expected result : [(2,1),(1,2),(2,3),(4,4),(2,5)]

def last (n):
   #last is function
   return n[-1]

def sort_list_last(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

#write a python prog. to remove dublicates from list
a=[10,20,30,20,10,50,60,40,80,50,40]
lst1=[10,20,30,20,10,50,60,40,80,50,40]
st1=set(lst1)
#since set removes duplicate item 
print(st1)
lst2=list(st1)
print(lst2)

#write a program to clone or copy a list
original_list=[10,22,44,23,4]
new_list=list(original_list)
print(original_list)
print(new_list)

#write prog. to find list of words that are longer than 3 from a given list of words.
def long_words(n,str):
    word_len=[]
    txt = str.split(" ")
    for x in txt :
        if len(x)>n:
            word_len.append(x)
    return word_len
print(long_words(3,"The quick brown fox jumps over the lazy dog"))

#write python function that takes two list and return 
#True if they have at least one common member

def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
print(common_data([1,2,3,4,5],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))
  
#write prog.to calculate the difference between the two lists

list1=[1,3,5,7,9]
list2=[1,2,4,6,7,8]
diff1=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
total_diff=diff1+diff2
print(total_diff)

#write a python program to convert  list of characters into string.
s=['a','b','c','d']
str1=''.join(s)
print(str1)
  
#write python prog.to find the index of an item in a specified list.
#used in NLP
#
num=[10,30,4,6]
print(num.index(6))

#write python prog. to append a list to the second list
list1=[1,2,3,4]
list2=[3,4,5,5]
final_list=list1+list2
print(final_list)
















