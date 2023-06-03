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


# Test Average and Grade CH5Q15
"""
# Jacob Alebiosu
# Chapter 5, Question # 15, p. 297, Test Average and Grade
# ICS 698
# SU-2023

# Pseudocode
# define the calc_average function to find the average of grades using the formula average = (a + b + c + d + e)/5
# define the determine_grade function to return the grade of a score range
# define the main() function
# ask the user to enter the five grades
# call the "calc_average" function to find the average and assign it to average_grade
# display average grade
# display the equivalent grade of each score

# function to calculate average score
def calc_average(a,b,c,d,e):
    average = (a + b + c + d + e)/5
    return average

# function to classify a score and return its grade
def determine_grade(score):
    if 90 <= score <= 100 :
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    elif 0 <= score < 60:
        grade = "F"
    else:
        grade = "Invalid grade"
    return grade

def main():

    # get the five scores from user and cast to float
    # validate that the score is valid between 0 and 100

    first_score = float(input("Enter the first score: "))
    while (first_score < 0 or first_score > 100):
        print("Score should be a value between 0 and 100")
        first_score = float(input("Please enter the first score: "))

    second_score = float(input("Enter the second score: "))
    while (second_score < 0 or second_score > 100):
        print("Score should be a value between 0 and 100")
        second_score = float(input("Please enter the second score: "))

    third_score = float(input("Enter the third score: "))
    while (third_score < 0 or third_score > 100):
        print("Score should be a value between 0 and 100")
        third_score = float(input("Please enter the third score: "))

    fourth_score = float(input("Enter the fourth score: "))
    while (fourth_score < 0 or fourth_score > 100):
        print("Score should be a value between 0 and 100")
        fourth_score = float(input("Please enter the fourth score: "))

    fifth_score = float(input("Enter the fifth score: "))
    while (fifth_score < 0 or fifth_score > 100):
        print("Score should be a value between 0 and 100")
        fifth_score = float(input("Please enter the fifth score: "))
    
    # find the average by calling the average_score function 
    average_score = calc_average(first_score, second_score, third_score, fourth_score, fifth_score)
    
    # display the overall average score and grade for each student
    print(f'\t--------------------- \n The average score is {average_score}\n\t---------------------')
    print(f'Score \t \t Grade')
    print(f'{first_score} \t \t {determine_grade(first_score)}')
    print(f'{second_score} \t \t {determine_grade(second_score)}')
    print(f'{third_score} \t \t {determine_grade(third_score)}')
    print(f'{fourth_score} \t \t {determine_grade(fourth_score)}')
    print(f'{fifth_score} \t \t {determine_grade(fifth_score)}')

# call the function
if __name__ =='__main__':
    main()
"""