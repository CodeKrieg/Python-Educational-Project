#Modifying an existing Array
# Sometimes you might want to modify what you already have in that array or just add more to the array data. 
# in your IDE create a new file modifyarray.py (you can name it anything)
# We will look into it in this section. 
newArray = ["Mashrur", "NewYork", "mashrur@gmail.com"]
print newArray
newArray[1] = "Germany"
# In above example I have modified the second value of the array from New York to Germany.
print "Array is Modified, New Array is: "
print newArray
#let's see one more example 
newArray[2] = "mashrur@metacode.com"
print newArray
#This is how you actually modify the elements within an array
# But what if you want to add something to the array? Let's see how it is done. 
# we are going to modify newArray.
# In new array we have 3 elements at position: 0, 1 and 2. Now we would like to add another thing to position 3. 
# So How we gonna do it? well lets see the example
newArray.append("edinburgh")
print newArray
#Here you can see we've just added a value to the exisiting array. Please note with append, you will only be able to add one value. well can I add more than one value? Yes, you can.
# let's try adding more than one value of different typecodes using extend
newArray.extend(["gold", 12, 1.5])
print newArray
#the above example extends the array to any extend, along with the values you might need to add. These can be of any typecode. 
# Removing the data in an array
# let's say we want to remove the second element from the array, so let's try the same in following example
newArray.remove("gold")
# so in above example we wanted to remove one of the elements of newArray, which is "gold". So we've used .remove with the .remove function with the element that we want to remove. 
print newArray
# That's basically it about modifying the arrays. Try out a few by your own by creating new Arrays and modifying them. 