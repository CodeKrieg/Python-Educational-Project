# Alright, so you've learned how to say 'Hello World' in Python, you learned how to do math and print certain things.
# You've learned what arrays are and how to use them and also hashes a.k.a dictionaries
# VERY GOOD. Now, lets go into something more advanced... branches and functions

# Lets start with if-statements. here is an example:

humans = 20
dinosaurs = 30
pterodactyls = 25

if humans < dinosaurs:
    print "Dinosaurs are alive! We've done it, now they are going to eat us!"
    
if humans > dinosaurs:
    print "We were not able to bring dinosaurs back.. how sad"

if humans < pterodactyls:
    print "Is that a plane? Is that a helicopter? Is that superman? NO! Its a pterodactyl!"
    
if humans > pterodactyls:
    print "This one failed as well... he can't fly."
    
# What is an if-statement? An if-statement creates what is called a branch in the code. The if-statement tells your script "If this expression is True, then run the code under it. otherwise skip it"
# In order to create a branch (like the if statement above) you need to have a colon at the end of the line, and also the code inside it needs to be indented 4 spaces.
# Do not forget that Python is very picky, so it won't accept syntax errors, having 4 spaces of indentation is a must with branches

# Lets work with else and if, we will start again with an example:

humans = 15
cats = 20
dogs = 15


if cats > humans:
    print "Its over. The cats have conquired the earth!"
elif cats < humans:
    print "We won, the cats are not a danger anymore!"
else:
    print "We are still fighting them!"


if dogs > cats:
    print "The neverending fight between dogs and cats is over! Dogs have won!"
elif dogs < cats: 
    print "The neverending fight between dogs and cats is over! The cats have won, long life Prince Miaw!"
else:
    "Same old story, they are fighting again"

# Alright, so here is our example. Lets explain what it does:
# The same as my example with the if-statement, if A is true then print A. if A is false then print B. But that was on one line, if we want something more complex we can use the elif and else statements. 
# the above says : If A is true then print A. If A is not true and B is true, then print B. And if neither A nor B are true, print C 


# Functions
# Functions do three things:
# 1- They name piece of code the way variables name strings and numbers.
# 2- They take arguments.
# 3- Using and 2 they let you make your own "mini-scripts" or "tiny commands"

# Example:
def print_two_arg(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1
    
print_two_arg("Odin", "Thor")
print_one("Here is only one argument")

# Above we have two functions, the first one takes two arguments (We pass in Odin and Thor) and the second one takes only one argument
# What is def? Def stands for define. So you are defining a function to let your compiler know what it is actually doing at this point or what it needs to do whenever this function is called upon
# What names can we use as functions? The same with variables, you can use any name you want