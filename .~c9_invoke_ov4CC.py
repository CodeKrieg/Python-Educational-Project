def compound_interest():
# 
    principal = input('Please enter your initial deposit: $')
    rate = input('Please enter the interest rate: ')
    rate = rate / 100.0
    time = input('Please enter the number of years it will be saved: ')
    time = time + 1
    compound = input('How many times is the interest compounded a year?: ')

    print "Year %21s" % "Amount on deposit"

    for time in range(1, time):
        formula = principal * (1.0 + rate) ** time
        formula = formula + principal
        print "%4d%21.2f" % (time, formula)

def start():
    print "Lets start compounding your interest."
    compound_interest()

start()


# In the above code we are trying to calculate the compund interesting
# We are starting by defining an object (compound_interest)

# Then we are asking for a couple of inputs:
# Initial deposit, rate (which we divide by 100), the number of years (which we add +1), then we are asking for the compund

# We are then printing two strings, year and amount on deposit, the first string also adds space with %21s, just to keep it clean and simple.

# The next important step is to do a loop, we are doing a foor loop
# Then we are asking for the initial deposit amount (in USD)
# We are asking for the rate and then we dividing the rate to 100.0
# After that we are asking for the amount of time 