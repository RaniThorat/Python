#17 AUGUST



###########################################################

#extracting some information
import re
text1='''Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family'''

def get_pattern_match(pattern,text1):
    matches=re.findall(pattern,text1)
    if matches:
        return matches[0]

get_pattern_match(r'age \d+', text1)
get_pattern_match(r'Born(.*)\n', text1).strip()
get_pattern_match(r'Born(.*)\n', text1).strip()
get_pattern_match(r'Born.*\n(.*)\(age',text1).strip()
get_pattern_match(r'\(age.*\n(.*)', text1)


###############################################################

#making dictionary from extracted information

import re
text1='''Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family'''

def get_pattern_match(pattern,text1):
    matches=re.findall(pattern,text1)
    if matches:
        return matches[0]


def extract_personal_info(text1):
    age=get_pattern_match('age (\d+)', text1)
    full_name=get_pattern_match('Born(.*)\n', text1)
    birth_date=get_pattern_match(r'Born.*\n(.*)\(age',text1).strip()
    birth_place=get_pattern_match(r'\(age.*\n(.*)', text1)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_info(text1)

#########################################################

text3='''Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''

def get_pattern_match(pattern,text1):
    matches=re.findall(pattern,text1)
    if matches:
        return matches[0]

def extract_personal_info(text3):
    age=get_pattern_match('age (\d+)', text3)
    full_name=get_pattern_match('Born .*\n', text3)
    birth_date=get_pattern_match(r'Born.*\n(.*)\(age',text3).strip()
    birth_place=get_pattern_match(r'\(age.*\n(.*)', text3)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_info(text3)

############################################################


#TOKENIZATION
txt='welcome to the new year 2023'
x=txt.split()
print(x)

#removing special characters from text
import re
def remove_special_characters(text):
    pattern=r'[^a-zA-Z0-9.]' #^=(not), other will remove 
    return re.sub(pattern,' ',text)
remove_special_characters('007 Not sure@ if this % was #fun ! 7564 thing to do.?/:;')


#removing numbers from text
import re
def remove_numbers(text):
    pattern=r'[^a-zA-Z.,!?/:;\"\'\$]' #^=(not), other will remove 
    return re.sub(pattern,' ',text)
remove_numbers('007 Not sure@ if this % was #fun ! 7564 thing to do.?/:;')

#
txt='welcome: to the, new year 2023!'
txt.split()


##########################################################

#AFTERNOON

#removing punctuation
import string
text='Article: @First sentence of some, (important) article having lot of ~ punctuations, and another one;!'
def remove_punctuation(text):
    text=''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation(text)


#stemming
import nltk
def get_stem(text):
    stemmer=nltk.porter.PorterStemmer()
    text=' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem('We are eating and swimming; we have been eating and swimming; he eats and swims; he ate and swam')


##########################################################################################################

#21/08/2023-Monday

#lammetization
import re
line='asdf fjdk; afed,fjek,asdf, foo'
re.split(r'(?:,/;|\s)/s*',line)

pattern=r'(?:,|;|\s)/s*'
x=re.split(pattern,line)
print(x)

#matching text at the start or end of string
filename='spam.txt'
filename.endswith('.txt')

area_name='6th lane west andheri'
area_name.startswith('west andheri')

choices=('http:','ftp:')
url='http://www.python.org'
url.startswith(choices)

#slicing a string
#positive indexing
s='ABCDEFGHI'
print(s[2:7])

#negative indexing
s='ABCDEFGHI'
print(s[-7:-2])

#positive & negative indexing
s='ABCDEFGHI'
print(s[2:-5])

#in step of 2
s='ABCDEFGHI'
print(s[2:7:2])

#reverse step of 2
s='ABCDEFGHI'
print(s[6:1:-2])

#slice of beginning and end
s='ABCDEFGHI'
print(s[:3])

s='ABCDEFGHI'
print(s[6:])

#reversing the string
s='ABCDEFGHI'
print(s[::-1])


#similar operations can be done with slices
filename='spam.txt'
filename[-4:]==('.txt')

url='http://www.python.org'
url[:5]=='http:' or url[:6]=='https:' or url[:4]=='ftp:'

#pip install fnmatch
from fnmatch import fnmatch,fnmatchcase
names=['Dat1.csv','Dat2.csv','config.ini','foo.py']
[name for name in names if fnmatch(name,'Dat*.csv')]

from fnmatch import fnmatch,fnmatchcase
names=['andheri east','parle east','dadar west']
[name for name in names if fnmatch(name,'* east')]


from fnmatch import fnmatch,fnmatchcase
names=['data1','data2','data3','rani','chiu']
[name for name in names if fnmatch(name,'data*')]

addresses=[
    '5412 N CLARK ST',
    '1000 N ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADAWAY']
from fnmatch import fnmatchcase
[addr for addr in addresses if fnmatchcase(addr, '*ST')]

text='yeah, but no,but yeah, but no,but yeah '
#exact match 
text=='yeah'

#match at start or end 
text.startswith('yeah') #true
text.endswith('no') #false

#search for the location of the first occurance
text.find('no')

################################################################################

text1='11/27/2012'
text2='Nov 27,2012'

import re
#simple matching : \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

#output-yes
    
if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')
  #output-no  

#Another method 

datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text1):
    print('yes')
else:
    print('no')


datepat=re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text2):
    print('yes')
else:
    print('no')

###########################################################################

#searching and replacing text 
text='yeah, but no,but yeah, but no,but yeah '
text.replace('yeah','yep')

###############################################################################

#if you have dates in format 11/27/2012 want to convert 2012-
text='Today is 11/27/2012. pycon starts 3/13/2013.'
import re 
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
#3 3rd group,\1 is 1st group 
#today is 2012-11-27 .pycon starts 2013-3-13

########################################################################

#if u want to know how many substitution are made in text then u can use subn() method

newtext,n=datepat.subn(r'\3-\1-\2',text)
newtext
n #how many substitution we have done 

###############################################################################

text='UPPER PYTHON, lower python, Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)

#to substitude
re.sub('python','snake',text,flags=re.IGNORECASE)
#Ouput='UPPER snake, LOWER snake, MIXED snake '

#########################################################################

#The last exmple reveals a limitation that replacing text won't match the case of
# the matched text If u need to the fix this, u might have to use a support function ,as in the following:

import re
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
text3=re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
text3            

#Another method to findout  the pattern 

str_pat=re.compile(r'\"(.*)\"')
text1='computer says "no."'
str_pat.findall(text1)

#however if we have text as below (Drawback)
text2='computer says "no." phone says "yes."'
str_pat.findall(text2)

#extract only no and yes 
str_pat=re.compile(r'\"(.*?)\"')
str_pat.findall(text2)

########################################################################

comment=re.compile(r'/\*(.*?)\*/')
text1='/* this is a comment */'
comment.findall(text1)
#output-[' this is a comment ']

text2='''/* this is a
 multiple comment */'''
comment.findall(text2)



comment=re.compile (r'/\*((?:.|/n)*?)\*/')
comment.findall(text2)



comment=re.compile(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)

###################################################################################################
s1='spicy Jalape\u00f10'
s2='spicy Jalapen\u3030'
print(s1)
print(s2)
s1==s2



import unicodedata
t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
t1==t2

























