# This file contains all the attempted challenges.


# Compound Interest #CH2 Q14
""" 
# Chapter 2, Question # 14, p. 116, Compound Interest

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
# Chapter 3, Question # 14, p. 163, Body Mass Index

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
# Chapter 4, Question # 6, p. 214 Celsius to Fahrenheit

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
# Chapter 4, Question # 10, p. 215, Tuition Increase

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
# Chapter 5, Question # 15, p. 297, Test Average and Grade

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


# Odd/Even Counter #CH5Q16
"""
# Chapter 5, Question # 297, p. 297, Odd/Even Counter

# Pseudocode
# import the random module
# define a function to check for even or odd numbers and return true or false
# define a function to count to 100 and generate a random number on each iteration
# check if the random number is even or odd using the even_checker function
# declare two variables to be used as accumulators for each count of even or odd numbers
# return the accumulated value of both even and odd numbers
# display the result.

import random

# check if number is even or odd
def even_checker(number):
    if (number % 2) == 0:
        status = True
    else:
        status = False
    return status

# function to generate 100 random numbers and count the odd and even numbers
def random_generator():
    even_count = 0
    odd_count = 0

    # loop to generate 100 random numbers and return the count of odd and even numbers
    for count in range(100):
        random_number = random.randint(1,100)
        print(random_number, end=", ")

        #check if random number is even or odd and count
        if even_checker(random_number):
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# declare the main function
def main():
    # get the results from the random_generator() function
    even, odd = random_generator()

    # display the result
    print(f'\nCount of numbers generated: {100}')
    print(f'Count of even numbers: {even}')
    print(f'Count of odd numbers: {odd}')

# call the main function
if __name__ == '__main__':
    main()
"""


# Future Value #CH5Q19
"""
#Chapter 5, Question # 19, p. 298, Future Value

# Pseudocode
# Define the future_value function to calculate and return the future value using the formula (a * ((1 + b) ** c))
# Get the present amount of the user and typecast to float after validating the input
# Get the monthly interest rate, validate the input, typecast to float and divide by 100
# Get the period from the user, validate the input and typecast to int
# Determine the future value by calling the future_value function
# Display the result.

# Generate future value

def future_value(a,b,c):
    fval = (a * ((1 + b) ** c))
    return fval

def main():

    # Get present value in account
    get_present_value = input("Enter the present amount in the account: ")

    # test for float by replacing one '.' from input value and check if it returns a digit
    a = get_present_value.replace('.', '', 1)

    # request new input while current input is invalid
    while a.isdigit() == False:
        print("Present amount should be in digits")
        get_present_value = input("Enter present amount in the account: ")
        a = get_present_value.replace('.', '', 1)

    # cast input to float and assign to variable
    present_value = float(get_present_value)

    # Get monthly interest
    get_monthly_interest = input("Enter the monthly interest rate (e.g. 5 for 5% not 0.05): ")

    # test for float by replacing one '.' from input value and check if it returns a digit
    b = get_monthly_interest.replace('.', '', 1)

    # request new input while current input is invalid
    while b.isdigit() == False:
        print("Interest rate should be in digits")
        get_monthly_interest = input("Enter the monthly interest rate (e.g. 5 for 5% not 0.05: ")
        b = get_monthly_interest.replace('.', '', 1)

    # cast input to float, divide by 100 and assign to variable
    monthly_interest = float(get_monthly_interest)/100

    # get the total number of months
    get_time = input("Enter the total number of months: ")

    # input validation
    while get_time.isdigit() == False:
        print("Total number of months should be in digits")
        get_time = input("Enter the total number of months ")
    time = int(get_time)

    # Calculate future value with the future_value function
    f_value = future_value(present_value,monthly_interest,time)

    # Display result
    print(f'\n***************\nThe future value of the account is ${f_value:.2f}')

# Call the main function
if __name__ == '__main__':
    main()
"""


# Golf Scores #CH6Q10

# Chapter 6, Question # 10, p. 359, Golf Scores

# main function
def main():
    write_to_file()
    #read_from_file()


def write_to_file():
    # get the number of players in the team
    num_players = int(input("How many players are in your team: "))

    # open new file with name 'golf.txt'
    golf_file = open('golf.txt', 'w')

    # write the first line as header
    golf_file.write('\n===============\nPLAYER NAME\t\tPLAYER SCORE\n')

    # get the name and score of each player and write it to file
    for count in range (1, num_players + 1):
        # get the name and score
        player_name = input(f"Enter the name of player #{count}: ")
        player_score = float(input(f"Enter the score of player #{count}:"))

        # write name and score to file
        golf_file.write(f'{player_name}\t\t\t{player_score}\n')

    # close the file
    golf_file.close()

def read_from_file():
    try:
        # open the file to for reading
        golf_file = open('golf.txt', 'r')

        # assign first line to display
        display = golf_file.readline()

        # print each line till the end of the file
        while display != '':
            print(f'{display}')
            # read next line
            display = golf_file.readline()

        # close file
        golf_file.close()

    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('An error occured trying to process the file data.')

    except:
        print('An error occured.')