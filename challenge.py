# This file contains all the attempted challenges.


# Compound Interest #CH2 Q14
""" 
# Chapter 2, Question # 14, p. 116, Compound Interest
# ICS 698

# Pseudocode
# Ask the user to enter the initial capital
# Ask the user to enter the interest rate in percentages and divide by 100
# Ask the user to enter the number of times the interest will compound annually
# Ask the user to enter the number of years the interest will compound
# Calculate the compound interest rate using the formula (principal * ((1 + (rate / num_of_times)) ** (num_of_times * period)))
# Display the result

# Get user data for all required variables
principal = float(input("Enter initial deposit or capital: "))
rate = float(input("Enter interest rate in percentage (e.g. 5 for 5%): ")) / 100
num_of_t = float(input("Enter the number of times per yer the interest is compounded "
                       "(e.g. 12 if monthly and 4 if quarterly): "))
period = float(input("Enter the number of years the interest will span: "))

# Calculate the compound interest
compound = (principal * ((1 + (rate / num_of_t)) ** (num_of_t * period)))

# Display the compound interest
print("\n************************")
print(f'Your compound interest on ${principal:.2f} after {period:.0f} years at an annual rate of {rate:.0%} is ${compound:.2f}')
"""