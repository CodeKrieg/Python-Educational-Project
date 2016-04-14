def compound_interest():
# 
    principal = input('Please enter your initial deposit: $')
    rate = input('Please enter the interest rate: ')
    rate = rate / 100.0
    time = input('Please enter the number of years it will be saved: ')
    time += 1
    compound = input('How many times is the interest compounded a year?: ')

    print "Year %21s" % "Amount on deposit"

    for time in range(1, time):
        formula = principal * (1.0 + rate)** time
        formula = formula - principal
        print "%4d%21.2f" % (time, formula)
        # print formula

def start():
    print "Lets start compounding your interest."
    compound_interest()

start()


# In the above code we are trying to calculate the compund interest
# We start by defining a function (compound_interest)

# Then we are asking for a couple of inputs:
# Initial deposit, rate (which we divide by 100), the number of years(incrementing it by 1 each year), then we are asking for the number of times you wantto calculate the CI in a particular year

# We are then printing two strings, year and amount on deposit, the first string also adds space with %21s, just to keep it clean and simple.

# The next step we are doing a for loop with time, we are calculating the principal * 1.0 + rate ** time. 
# And then printing the result (time is the year, and formula is the result)

# In the second function we are defining start and then we are calling the compound_interest
# And our last step is to call start outside the function and start the program
