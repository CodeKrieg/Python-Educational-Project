# -*- coding: UTF8 -*-
#Arrays In Python
#what are arrays in python? you must be wondering. It is similar to arrays in any other languages such as C. Array is a collection of items which can be of any type(strings, integers etc.)
#Character Arrays: each character/array in python should be addressed by a variable let's see how
newArray = ["mashrur", "New York", "USA"]
print newArray
#Here the array has been assigned to a variable "newArray" you can choose anything and then is being printed using "print" command. 
#In order to Run it, All you have to do is this run the array.py using the following command in terminal. "python array.py"
#Unicode Arrays in Python: Unicode arrays are used to respond to the 'u' typecode corresponds to Python’s unicode character. 
#This won't work reason being, you need to define the encoding type at the start of your file like this "# coding=<encoding name>". 
#So go to the top of your array.py file and add "# coding=UTF8"
# On narrow Unicode builds this is 2-bytes, on wide builds this is 4-bytes. for example. 
uniArray = [u'hello', u'NewYork City']
print uniArray 
# In the code above, we passed on a unicode value for array, defining it using 'u' typecode. I will provide more typecodes as we proceed. So here u preceding 'hello' defines the encoding type of the datapassed along is that of unicode
# Then we printed it using 'print'
# The result of in terminal was like this 
# [u'hello', u'NewYork City']   
## Numerical Array 
#Now you must be thinking does python have things like signed and unsigned char? Yes it does. They are defined by the following 'b' for signed and 'B' for unsigned but the python type of these typecodes is "int".
# Let's see the Numerical Arrays now. The procedure is same as what we did with the last two, the only thing is you don't need ''. Below is an example
numArray = [1, 2, 3, 4, 5]
print numArray

# Let's see the Floating Array, Floating arrays are the ones that has contains decimals. 
floatArray = [1.0, 2.0, 3.0, 4.0, 5.0]
print floatArray
# You use floats integer but with float values. 

#Getting values from array. 
# Printing the specific values of an array can be performed by using the value position. for eg: 
print newArray[1] 
# In the above method, we printed the second value that is stored in "newArray". Any array always starts with "0". So let's say you want to call the first value of uniArray, you need to do something like this: 
print uniArray[0]
#Now Run the file and see the results


