# Hello World 

# Python is a very fun and simple language, it also has a very straightforward syntax (which is always a good thing!)
# The simplest directive in Python is the "print" directive - it simply prints out a line (and also includes a newline, unlike in C).

# There are two main versions in Python (and there are big differences between them) python 2 and python 3. 
# one difference between Python 2 and 3 is the print statement. 

# In Python 2, the "print" statement is not a function, and therefore it is invoked without parentheses. 
# However, in Python 3, it is a function, and must be invoked with parentheses.

print("Hello World!")

# The print statement does exactly what its name says, it prints whatever you give to it. 

# Some examples:
# It can print strings
print("A string")

# it can print numbers
print(2)

# Python also has the ability to do simple math calculations
# Some examples:

print(1+2) # This should give us 3
print(5+5) # This should give us 10
print(8*6) # This should give us 48
print(25/4) # This should give us 6

# This is just basic math, but there is a lot more, Python is so powerful that you can do almost everything with it! 
# You should be very careful when you work with integers and strings. There is a very big difference between them

print("1") # This will print a string, so you can not do any math calculations with it
# print("1" + 1) 
# If you try anything like this, you will always receive an error.Reason being, you can't just add an string and an integer together. It has to be of same datatype.


# So far we've seen how to print a statement, how to do some math and we also seen what errors we might encounter when we have bad syntax.

# Lets continue to variables
# Short and simple, A variable is just a box that you can put stuff in. You can use variables to store all kinds of stuff

# So lets work with some strings and numbers once again, but this time, we will use variables

numberOne = 5
numberTwo = 5
print(numberOne + numberTwo)

# You might wonder "why don't we just do that math calculation without variables"
# Well, you see... later on you might want to use variables in order to store data, and that data be used again in another function. 

# Lets see how it would work with strings
greeting = "Hello there"
name = "John Doe"
print(greeting + ' ' + name) # As you can see, we are adding an empty string between the two variables, that is because it wouldn't have space if we just print it without that. 
                             # You can also add some space in one of the variables, its whatever you prefer



# String methods - formating

# Now that we covered integers, strings and variables, its time to go into something more advanced, string formating.
# String formating is quite a fun thing, simple put: there are a lot of methods made for strings that can be used, from capitalizing to split and replace and... ugh, there are a lot! 
# But right now we will concentrate on .format, which is quite fun to be honest! 

# Alright, lets create a simple program that will insert age and name. 
age = 26
name = "John Doe"

# "No, no, no! You told us that strings and integers do not work together." Well, they do not. put there is a way to overcome that. Allow me to show you
print("My age is " + str(age) + " years")
# You see, this str(age) transforms the data from the variable age (which, obviously, has an integer in) to a string. Quite fascinating indeed! 

# Very well, lets continue with our little program. 
print("My name is {0}, I am {1} years old".format(name, age))

# You might wonder what those brackets are for, well those are replacements fields. 
# Basically, 0 is the first one and 1 is the second one (and it keeps going as you add them) 
# and this way you do not need to add the data yourself, you add them in the format function and it all takes care by itself

# Lets work with some more formating
print("""This is how many days are in every month:
January     - {2}
February    - {0}
March       - {2}
April       - {1}
May         - {2}
June        - {1}
July        - {2}
August      - {2}
September   - {1}
October     - {2}
November    - {1}
December    - {2}""".format(28, 30, 31))


# Some more string formatting.
# We can play in multiple ways with our strings.  

# Lets say that we want our string to be on multiple lanes, how would we do that? 
# We can use the comand \n 

splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# We can also use the command \tb to tab the string
tabbedString = "a\tb\tc\td\t"
print(tabbedString)


# Lets say that we want to have a quote inside a string. if you write it like this
# print("Here is a quote "Quote"")
# This will fail. What you can do is either have one quote that surrounds the quote, or two quotes. Like this:
print('Example one: "I would take the awe of understanding over the awe of ignorance any day."')
print("Example two: 'That which can be asserted without evidence, can be dismissed without evidence'")

# But what if you have apostrophes for example: I'd. Then the syntax would have an error.. in that case we can do this: 
print('''Example three: "I'd take the awe of understanding over the awe of ignorance any day."''')
print("""Example four:
    Customer: 'Not much of a cheese shop really, is it?'
    Shopkeeper: 'Finest in the district, sir.'
    Customer: 'And what leads you to that conclusion?'
    Shopkeeper: 'Well, it's so clean.'
    Customer: 'It's certainly uncontaminated by cheese.'
    """)
# When you use three quotes not only it won't give you a sytnax error, but it will also start a new line when you write the code as we did above. Quite smart Python, quite smart.
