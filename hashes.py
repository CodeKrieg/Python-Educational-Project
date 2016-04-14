# Hashes, or dictionaries, are just like arrays. They are containers for data, but hashes are a lot more complex and you are able to do a lot more stuff with them.
# The uses of a dictionary
# Dictionaries ,just like lists, are one of the most commonly used data structures in programming
# A dictionary is used to map or associate things you want to store to keys you need to get them.

# An arrays lets you do this:
cities = ['London', 'Rome', 'Bucharest', 'Amsterdam', 'Moscow']
print cities[2]
# This will print Bucharest

cities[1] = 'Stockholm'
print cities[1]
# This will be Stockholm now, instead of Rome. 

print cities
# this will give London, Stockholm, Bucharest, Amsterdam, Moscow. Since we changed Rome to Stockholm above.


# You can use numbers to index into a list, meaning you can use numbers (like we used 1 and 2 above) to find out what's in lists. 
# What a dictionary does is that it lets you use anything, not just numbers. Lets see an example: 

odin = {'name': 'Odin', 'age': 6000, 'height': 3 * 3 + 9 / 5}
print odin['name']
# This will print Odin

print odin['age']
# This will print 6000

print odin['height']
# This will print 10

# We can also add things to our hashes on the fly. Lets see an example:
odin['city'] = 'Asgard'

print odin['city']
# This will print the beautiful city of Asgard

print odin
# This will print the whole hash

# Ok, so we've seen that we can use strings in order to get information's out of a hash. But, if you want to use integers (numbers) you can do like so: 

thor = {1: 'Thor', 2: '2000', 3: 'Asgard'}

# Alright, now that we have our hash. Lets see if it works
print thor[1]

# This will give us Thor

print thor[2]
# This will give us 2000

print thor[3]
# This will give us Asgard


# Now, what do we do if we put somethign we do not need inside a dictionary and we want to delete it? 
# Simple, we use the del keyword

del thor[2]
print thor
# Simple, right?


# Lets create an awesome dictionary.

# We will create a dictionary of how the days of the week got their name
days = {
    'Sunday': 
        """
        Sun's Day. 
        The Sun gave people light and warmth every day. 
        They decided to name the first (or last) day of the week after the Sun.
        """,
    'Monday': 
        """
        Moon's Day. 
        The Moon was thought to be very important in the lives of people and their crops.
        """,
    'Tuesday': 
        """
        Tiw's Day. 
        Tiw, or Tyr, was a Norse god known for his sense of justice
        """,
    'Wednesday': 
        """
        Woden's Day. 
        Woden, or Odin, was a Norse god who was one of the most powerful of them all
        """,
    'Thursday': 
        """
        Thor's Day. 
        Thor was a Norse god who wielded a giant hammer.
        """,
    'Friday': 
        """
        Frigg's Day. 
        Frigg was a Norse god equal in power to Odin.
        """
}

print '=' * 15
print "The name of the last/first day of the week, Sunday, comes from: ", days['Sunday']
print "The the name of the first/second day of the week, Monday, comes from: ", days['Monday']
print "The name of the second/third day of the week, Tuesday, comes from: ", days['Tuesday']
print "The name of the third/forth day of the week, Wednesday, comes from: ", days['Wednesday']
print "The name of the forth/fifth day of the week, Thursday, comes from: ", days['Thursday']
print "The name of the fifth/sixth day of the week, Friday, comes from: ", days['Friday']
