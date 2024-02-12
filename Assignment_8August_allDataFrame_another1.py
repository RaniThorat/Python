def prime_num(num):
    for i in range(2,num):
        if (num%i==0):
            return"The number is not prime"
            break
    return"The number is prime"
print(prime_num(11))


################# function without argument
def geet_user():
    #Display a simple greeting
    print("Hello")
geet_user()

#passing information to a function
def greet_user(username):
    #Display a simple greeting
    print(f"Hello, {username}!")
greet_user('Sanjivani AI')

#argument and parameter
def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name}.")
describe_pet('Dog','Moti')

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name}.")
describe_pet('Moti','Dog')


#####default values
## you can define a default value for each parameter 
def describe_pet(pet_name,animal_type='dog'):  ## dog is default value agrument
    print(f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='Moti')

##Avoiding argument error
def describe_pet(animal_type,pet_name):
    #display information about a pet
    print(f"nIhave s{animal_type}.")
    print(f"my {animal_type}'s name is {pet_name.title()}.")
describe_pet()


#Assignment=
#1>create prog using math and fstring and tell us how manydate,week and month we are left we willl leave until 80 yeras.
#2> write prog for roral coster see  if u are height is greate the 3cm then u can eligible
#3>if u are is under 18 then ticket will 20 ruppes and if u are age is greate than 18 then ticket wiil be 50 rupees  and if u are age less then 12 & height 120 cm ticket 10 rs and 12-18 age & height is 120cm ticket is 15  

#Roller coster 
print("Welcome to roller coster")
height=int(input("Please enter the height in cm"))
bill=0
if height>=120:
    print("You are eligible for roller coaster")
    age=int(input("please enter your age "))
    if age<12:
        print("child ticket are $5")
        bill=5
    elif age<=18:
        print("Your ticket are $7")
        bill=7
    else:
        print("Adult ticket are $12")
        bill=12
    want_photo=input("Do you want photo T OR N")
    if want_photo=='Y':
        bill+=3
        print(f"your total bill will be {bill}")
    else:
        print(f"you total bill {bill}")
else:
    print("sorry you need to grow taller")


#to create password
users=["admin","employee","manager","worker","staff"]
for user in users:
    if user=="admin":
        print("Hello admin, would you like to see a status report?")
    elif user=="employee":
        print("hello employee")
    elif user=="manager":
        print("hello manager")
    elif user=="worker":
        print("hello worker")
    else:
        print("hello")

##
import string
adjectives = ['sleepy','slow','smelly','wet','fat','red','orange','yellow','green','blue','purple','fluffy','white','proud','brave']
#pick the nouns
nouns = ['apply','dinosaur','ball','toaster','goat','dragon','hammer','duck','pandas',]

#pick the word
import random

adjectives  = random.choice(adjectives)
nouns = random.choice(nouns)
#select a num.
number= random.randrange(0,100)
#select a special_character

special_char = random.choice(string.punctuation)
#create the new secure password
password=adjectives + nouns + str(number) + special_char
print('your new password is: %s' %password)

#### using while loop 
print('welcome to password picker!') 
while True:
    adjectives = random.choice(adjectives)
    nouns = random.choice(nouns)
    number = random.randrange(1,100)
    special_char = random.choice(string.punctuation)
    password = adjectives + nouns +str(number) + special_char
    print('your new password is: %s' %password)
    response = input('would you like to generate another password? Type y or n: ')
    if response=='n':
        break

#password is good or not= have some condition
#1 it must have at least 8 char
#2 have at least one upper case letter
#3 one lower letter

def checkpassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    
    for  ch in  password:
        if ch>="A" and ch<="Z":
            has_upper=True
        elif ch>="a" and ch<="z":
            has_lower=True
        elif ch>="0" and ch<="9":
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
    
password=input("enter pass:")
checkpassword(password)


###
def checkpassword(password):
    has_upper=False
    has_lower=False
    has_num=False
    
    for  ch in  password:
        if ch>="A" and ch<="Z":
            has_upper=True
        elif ch>="a" and ch<="z":
            has_lower=True
        elif ch>="0" and ch<="9":
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
    
password=input("enter pass:")
a=checkpassword(password)
if a==True:
    print("strong")
else:
    print("weak")


####
print("what is your todays age")
years_today=input("years:")
months_today=input("months:")
days_today=input("days:")
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f"total age todays in days {total_days_today}")
print("Let us assume you are expected to live 90 years ")
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f"you remaining life in days  {remaining_days_to_live}")


###########################################################
#wrong prog.
print("welcome to pizza shope")
size_pizza=input("enter size of pizza,S,M,L")
add_pre=input("do u want to pre ? Y or N")
extra_cheese=input("do u want extra cheese ? Y or N")
bill=0
if size_pizza="S":
    print(the biil will be $15)
    bill=15
    if add_pre=='Y'or add_pre=='N':
        print("bill will be",biil+2)
    
        
    
    
elif size_pizza="M":
    print(the bill will be $20)
    bill=20
else:
    print(the bill will be $25)
    bill=25
if add_pre=='y':
    bill+=2
        
    ######################
def bill():
    s=15
    m=20
    L=25
    
    ps=2
    pmL=3
    ec=1
    
    a=input('enter the size of pizza:')
    if a=='s':
       print(bill will be $15) 
       b=input("want pepproni enter y or n:")
       if b=='y' or b=='n'
   
    
###################################################################

#26/07/2023
#returning dictionary
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('ram','sai')
print(musician)

#passing list
def greet_users(names):
    for name in names:
        mesg=f"Hello,{name.title()}!"
        print(mesg)
username=['sai','sanket','ram']
greet_users(username)


#passing an arbitrary no.of aguments
def make_pizza(*toppings):
    #print the list of toppings that have been requested
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')


#we replaced the print() call with loop that run through the
#list of toppings and describes the pizza being ordered
def make_pizza(*toppings):
    print("\nmakings the pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
        
#mixing positional and arbitrary arguments

def make_pizza(size,*toppings):
    print(f"\nmaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')

#####################

import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushroom','green peppers','extra cheese')

###########
#importing specific function
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')

######################
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushroom','green peppers','extra cheese')

###################
#using as to give a module an Alias

import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushroom','green peppers','extra cheese')

###############################
#importing all function in module 
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')

####################################
#scope of variable
x=x+1
x=6
print(x)
#u cannot reference a variable
#until it has assigned a value

###########
x=6
x=x+1
print(x)
#first intialized the variable

######################################
#lambda function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))

########### or

add=lambda a,b,c:a+b+c
add(4,5,6)

##########
def mul(a,b,c):
    multi=(a*b*c)
    return multi
print(mul(2,2,2))

####################################
#non keyword argument
val=lambda *args:sum(args)
val(1,2,3,5,6)
##############
val=lambda *args:sum(args)
val(1,2,3,5,6)
val(1,2,3,5,6,1,3)
#############
#keyword argument

def person(name,**data):
    print(name)
    print(data)
person(name='gayatri',age=12,place='mumbai',mob_no=123455)
     
#########################
def person(name,**data):
    print(name)
    for i ,j in data.items():
        print(i,j)
person(name='gayatri',age=12,place='mumbai',mob_no=123455)

######################################################
val=lambda **data:sum(data.values())
val(a=2,b=2,c=2,d=2)

#######################################################
#lambda function
max=lambda a,b:x if (a>b)
print(max(1,2)) #error

max=lambda a,b:x if (a>b)else b
print(max(1,2))
  #OR
max=lambda a,b:x if (a>b)else b
print(max(8,10))
        
        
            
            
    
    























    




























