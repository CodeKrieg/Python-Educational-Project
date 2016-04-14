#OOP'ng with Python
#Some of you might know that almost every language that we are using these days have a concept of OOP in it. Well so does the python. 
# let me explain you a bit as what OOP is. The concept of OOP is basically using objects to make the program much cleaner and more DRY. less the code is .. less is the confusion. 
# It's not just the "Class" that makes the any language OOP based. There are a lot of other ingredients to the recipe of OOP.
# OOP in python has two important aspects: 1) Inheritance 2) Composition. 
# Let me explain the both by means of an example. The Inheritance as the word explains itself is to "inherit" from its predecessor or the parent.
# So if any class or subclass is carrying over from it predecessors or parent, this nature of carrying over is called inheritance. 
# let say I have a class music and have nodes defined in it. Now I made another class called "Concert" and want the property of music to be added into it. So how am I suppose to do that. All I have to do is apply inheritance into it
# let's see an example

class Music:
    def notes(self, note):
        self.data = note
        
    def display(self):
        print self.data

x = Music()
y = Music()

x.notes("Do re mi fa so")
y.notes("so fa mi re do")

x.display()
y.display()

# you must be wondering what is going on in that piece of code. Well what we did here is we defined a class using Class object. 
# In the second line we defined the class methods using "def". 
# Then we added a self instance. Then we ended that method with pass.
# Then Again we've defined another class method to display the everthing from previous class method. Further, we've printed the self.data instance value. Let's see how this works. 
# Try running the same on the terminal and  see what result you get. To get into the Python Command shell type python in your terminal and hit enter
# Now let's see how the class that we've added right now would make it easier to get the work done. 
# so as we saw that we have our class, now we want to utilize it right. let's see how our "Inheritance concept would work here
# Try going through these lines in your IDE.
class Musician(Music):
    def display(self):
        print 'The notes are  = "%s"'% self.data

rex = Musician()
rex.notes("fa so do re mi")
rex.display()


# In the above example we inherited the Music class by adding it within () This would let us use the Music class elements in Musician class.
# Next we define the display class method for Musician
# Print the data using the self.data from Music class, which is  acting as a super class. Going further, we will print a random statement which would include self.data from parent class.
# The self.data that would be printed here will be the data we set in next step
# In next step we will set the empty instance rex, Then using notes function again in Musician class we set up a value rex. 