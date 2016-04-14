# Note: In order to run this file do these steps: 
# 1- type in your terminal ‘python’
# 2- import amortization
# 3- amortization.amortization(15000, 5, 350)
#                        (principal, rate, term)

from decimal import *
# Basically the Amortization consists of a lot of them decimal points. 
#  In order to get the decimals to exactly work, we had to import everything from pre made python modules called decimal
def amortization(principal, rate, term):
# firstly we defin a function which would call a function called amortization in order to populate our table. 
# We would need to define the fields that would be required from the user. (principal, rate and term)
# Prints the amortization table for a loan.
# Prints the amortization table for a loan given
# the principal, the interest rate, and
# the term (in months).
    payment = pmt(principal, rate, term)
    begBal = principal
# here the payment variable is called upon to hold the three values provided by the user as mentioned earlier
# Beginning balance will show the Principal amount that is being paid 
#  Time to Print headers of our Amortization table using print table. I will explain a few things used in this table 
    print 'Pmt no'.rjust(6), ' ', 'Beg. bal.'.ljust(13), ' ',
    print 'Payment'.ljust(9), ' ', 'Principal'.ljust(9), ' ',
    print 'Interest'.ljust(9), ' ', 'End. bal.'.ljust(13)
    print ''.rjust(6, '-'), ' ', ''.ljust(13, '-'), ' ',
    print ''.rjust(9, '-'), ' ', ''.ljust(9, '-'), ' ',
    print ''.rjust(9, '-'), ' ', ''.ljust(13, '-'), ' '
# the rjust and ljust are used to set the justification alignment for the table columns
# Okay now comes the time to Print data that we get from our calculations
    for num in range(1, term + 1):
    # there goes the for loop
        interest = round(begBal * (rate / (12 * 100.0)), 2)
        applied = round(payment - interest, 2)
        endBal = round(begBal - applied, 2)
    # Then we'll apply the formulas to calculate amortization using proper variables
        print str(num).center(6), ' ',
        print '{0:,.2f}'.format(begBal).rjust(13), ' ',
        print '{0:,.2f}'.format(payment).rjust(9), ' ',
        print '{0:,.2f}'.format(applied).rjust(9), ' ',
        print '{0:,.2f}'.format(interest).rjust(9), ' ',
        print '{0:,.2f}'.format(endBal).rjust(13)
    # In this example str changes the values that is in for loop of num 
    # 0:,.2f This value here is actually changing the results to 2 digits of decimal points. We are applying the .format to format it in the right column with right justifications
        begBal = endBal
    # At the end we are implying that begin balance should be same as the end balance
def pmt(principal, rate, term):
# Calculates the payment on a loan.
# Returns the payment amount on a loan given
# the principal, the interest rate
    
    ratePerTwelve = rate / (12 * 100.0) # here we define how we are calculating the amortization. 
    result = principal * (ratePerTwelve / (1 - (1 + ratePerTwelve) ** (-term)))
#  Once we have the rate per year calculated, we go calculate result applying the formula above. 
    result = Decimal(result)
    result = round(result, 2)
    return result
# Convert to decimal and round off to two decimal places.