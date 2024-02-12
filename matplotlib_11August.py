#11/08/2023-Friday 

#matplotlib is used for visulization & also used for  
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.show()

#output-LineChart
####################################################################
#multiline plots
import matplotlib.pyplot as plt
x=range (1,5)
plt.plot(x,[xi*1.5 for xi in x]) #list comprehension 
plt.plot(x,[xi*3.0 for xi in x]) #list comprehension 
plt.plot(x,[xi/3.0 for xi in x]) #list comprehension 
plt.show()

#output- chart in Three line

##################################################################
#Note how matplotlib automatically choose differant color for each line-green for the first line ,blue for second line,and red for the third one (from top to bottom) 

#Grid ,axes anf labels
#Adding a grid 
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0) #x - is used for x-axes and another value is used for y-axes
plt.grid(True)
plt.show()

###################################################################
#Handling axes
import matplotlib.pyplot as plt
import numpy as np 
x = np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.axis() #show the current axis limits values 
plt.axis([0,5,-1,13]) #set new axes limits
#[xmin,xmax,ymin,ymax]
#[0,5,-1,13]
plt.show()

#######################################################################3
#Adding lebels
import matplotlib.pyplot as plt 
plt.plot([1,3,2,4])
plt.xlabel('This is the X axis')
plt.ylabel('This is the Y axis')
plt.show()

##########################################################################
#Adding a Titles 
import matplotlib.pyplot as plt
plt.plot([1,3,2,4])
plt.title('simple plot')
plt.show()

#######################################################################
#adding a legend - scale of graph 
import matplotlib.pyplot as plt 
import numpy as np  
x = np.arange(1,5)
plt.plot(x,x*1.5,label='Normal')
plt.plot(x,x*3.0,label='Fast')
plt.plot(x,x/3.0,label='Slow')
plt.legend()
plt.show()

#########################################################################
#Control colors
'''color abbrevation -
color Name 
b     blue
c     cyan 
g     green 
k     black
m     magenta
r     red 
w     white 
y     yellow'''
import matplotlib.pyplot as plt 
import numpy as np 
y = np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()

##################################################################
#specifying styles in multiline plot
import matplotlib.pyplot as plt 
import numpy as np 
y = np.arange(1,3)
plt.plot(y,'y',y+1,'m',y+2,'c')
plt.show()

#control line style 
import matplotlib.pyplot as plt 
import numpy as np 
y=np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':')
plt.show()
    
###########################################################################
'''style abbravation style 
-  solid line 
-- dashed line 
-. dash-dot line 
: dotted line '''

#control marker style 
'''marker abbrevation marker style 
 . point marker 
 , pixel marker
 o circle marker 
 v triangle down marker
 ^ Triangle up marker 
 < triangle left marker 
 > Triangle right marker 
 1 Tripod down marker 
 2 Tripod up  marker
 3 Tripod left marker 
 4 Tripod right marker
 s pentagon marker
 * star marker 
 h Hexagon marker 
 H Rotated hexagon marker 
 + plus marker 
 x cross (x) marker 
 D Dimond marker 
d Thin diamond marker 
| Vertical line (vline symbol) marker 
  '''


import matplotlib.pyplot as plt 
import numpy as np 
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s')
plt.show()

#####################################################################
#Histogram chart 
import matplotlib.pyplot as plt 
import numpy as np 
y=np.random.randn(1000)
plt.hist(y); #important
plt.show()

#######################################################################
#Bar graph 
import matplotlib.pyplot as plt 
plt.bar([1,2,3],[3,2,5]); #used for trend and scale the particular range of time
plt.show()

#The bar() function is used to generate bar charts in matplotlib.
#The function excepts two lists of values:
#the x coordinates that are the position of the bar's laft margin and the heights of the bars:
    #As we can see the left margin of the bars start at the points specified in the first list,while their height are the values of the second list.
    
###################################################################
#Scatter Plot - used for to find the colinearity 
#istabilices the two variable colinearity 
''' Bivariate analysis 
Scatter plot display value for two sets of data.
The data visuslization is done as '''

import matplotlib.pyplot as plt 
import numpy as np 
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y)
plt.show()

size = 50*np.random.randn(1000)
colors=np.random.randn(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()

############################################################################
#Adding Text 
import matplotlib.pyplot as plt 
import numpy as np 
x=np.linspace(-4,4,1024)
y=.25 * (x+4.) * (x+1.) * (x-2.)
plt.text(-0.5,-0.25,'Brackmard minimum ')
plt.plot(x,y,c='k')
plt.show()


#How to used Seaborn for Data Visulization 
#pip install seaborn 































































