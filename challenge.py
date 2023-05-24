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


# BMI Calculator CH3 Q14
"""
# Jacob Alebiosu
# Chapter 3, Question # 14, p. 163, Body Mass Index
# ICS 698
# SU-2023

# Pseudocode
# Ask the user to enter their weight and convert from "string" to "float"
# Ask the user to enter their height and convert from "string" to "float"
# Assign magic number 703 to k
# Calculate the BMI using the formula (weight * (k / (height ** 2)))
# Check if BMI is between 18.5 and 25 and display "Your weight is optimal" if true
# Else, check if BMI is greater than 25 and display "You are overweight"
# Else, display "You are underweight"

# Accept user weight and height
weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

# Assign constant k
k = 703

# Calculate BMI 
BMI = (weight * (k / (height ** 2)))

# Compare BMI against optimal value and display user's category
if 18.5 <= BMI <= 25:
    print("Your BMI is:", format(BMI,'.2f'), "Your weight is optimal")
elif BMI > 25:
    print("Your BMI is:", format(BMI,'.2f'), "You are overweight")
else:
    print("Your BMI is:", format(BMI,'.2f'), "You are underweight")
    print(f'Your BMI is: {BMI:.2f}. You are underweight')
"""


# Temp converter #CH4 Q6
"""
# Jacob Alebiosu
# Chapter 4, Question # 6, p. 214 Celsius to Fahrenheit
# ICS 698
# SU-2023

# Pseudocode
# Assign the value 32 to variable k
# Display the Celsius and Fahrenheit table headers
# Use the for loop's range function to iterate from 0 to 20 celsius
# Calculate the fahrenheit equivalent using the formula (((9/5) * i) + k)
# Display the Celsius and Fahrenheit values

# Assign 32 to constant k
k = 32

# Display table header
print("Celsius \t Fahrenheit")

# Initialize for loop
for i in range(21):
    # convert from celsius to fahrenheit
    fahrenheit = (((9/5) * i) + k)
    #print("For temp ", i, "Celsius, the Fahrenheit eqv is ", format(fahrenheit,'.2f'))
    
    # display result
    print(f'{i} \t \t \t  {fahrenheit:.1f}')
"""


# Tuition increase #CH4 Q10
"""
# Jacob Alebiosu
# Chapter 4, Question # 10, p. 215, Tuition Increase
# ICS 698
# SU-2023

# Pseudocode
# Assign 8000 to "tuition" variable as the initial tuition value
# Display initial tuition
# Initialize a for loop from range 1 to 6
# Calculate the new tuition with the increment using the formula (0.03 * tuition) + tuition
# Display the projected tuition and the corresponding year
# Repeat the loop and increment the tuition  until the iteration is complete

# Tuition fee
tuition = 8000

# Display initial tuition fee
print(f"The initial tuition for the Year is ${tuition:.2f}")

# initialize for loop to iterate from 1 to 6
for year in range(1, 6):
    tuition = (0.03 * tuition) + tuition
    print(f'The projected tuition for Year {year} is ${tuition:.2f}')

"""


