# Methods

# Every string or number etc have operations of their own. We call them "Methods". Functions that are attached to the object, which are triggered with a call expression. Let's see an example here.
# let's make a file called methods.py under your cloud9 ide and put this code in your file. I will explain you the code in a second. 
S = 'parmesan'
print S.find('pa') # pa here is a substring
print S.replace('pa', 'XYZ')
# Ok so you must be thinking what this piece of code actually did here? Well here we set a variable S and set the value to "parmesan". Then we asked the compiler to look for offset of a substring. 
# It was not able fine any offset that's why it gave you "-1". 
# Now the last statement. what it's doing? well it Replace occurrences of a substring(PA) with another (XYZ)
line = 'aaaa,bbbbb,cccc,ddd,ee'
print line.split(',') # this splts the line in to a substring
print S.upper() #  transforms your substring in uppercase
print S.isalpha() # if content: isalpha or is of alphanumeric type? 
print S.isalpha() #if content: isdigit or int type?

#Now lets create a "line1" variable and try to do some tear down of it from here and there.  I am going to use

line1 = 'aaa,bbb,ccc,ddd,eee\n'

print line1
# from above piece of code you will get the following outcome
#aaa,bbb,ccc,ddd,eee                                                                                                                                                                               
# if you will observe it carefully, you will see that there is a new line space. 
# Now the strip() method comes comes very handy in this case. All you have to do is use l and r with strip to trim down the whitespaces from the desired side of the whole line. 
# lets do try chopping out the white space from the right side. How?
# Put the following code in your the methods.py file. 
print line1.rstrip()
#the outcome of above method will be no line spaces at all. 
#now lets try stripping the whitespaces from left. let's see and example

line1 = '\naaa,bbb,ccc,ddd,eee'

# lets do try chopping out the white space from the left side. How?
# Put the following code in your the methods.py file. 
print line1.lstrip()

#When you will run the code above, you shall get the output like this 
#aaa,bbb,ccc,ddd,eee                                                                                                                                                                               
#aaa,bbb,ccc,ddd,eee 

# You can see all the available methods that are available for string datatypes using following in your console or just put this in your methods.py file
S = 'Mozarella'
print dir(S)

#This will show you all the methods available for the S variable you just defined. 
# Well you must be wondering if I can use any integer here or a float or a mixed? string method operations work only on strings, and nothing else. So answer is no
# Let's see what method does a integer provides and work our way down and see the majority of those methods.
# Put this in your file
N = 1, 2, 3, 4, 5, 6
print N
print dir(N)

#The dir function simply gives the method names. To ask what they do, you can pass them to the help function:
#Type this into the file. I am going explain the code in a bit. 
print help(S.index)
# here we are using "help" to get to know how the index method would work. so let us run the file   
# You will get the output something like this 
#Help on built-in function index:
#index(...)
#    S.index(sub [,start [,end]]) -> int
#    Like S.find() but raise ValueError when the substring is not found.

#You can run the help on each method that has been listed when we ran dir(S)
