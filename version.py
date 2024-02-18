# import sys
# print("Python Version")
# print(sys.version)
# print("Version Info")
# print(sys.version_info)


#practical 2

# name = input ("enter your name :")
# print("hello, "+ name + "!" )


# print("MSBTE")


#practical 3

# print("Conversion of Us dollar to Indian Rupees note:1$= 70INR")
# usDollar=int(input("Enter Doller Amount="))
# inr=usDollar*71.27
# print("INR=",inr)

# print("Conversion of bites to MB,GB,TB") 
# bits=int(input("Enter no of bits")) 
# byte=bits/8 
# kb=byte/1024 
# mb=kb/1024 
# gb=mb/1024 
# tb=gb/1024 
# print("Megabites=",mb) 
# print("Gigabites=",gb) 
# print("Terabites=",tb)


# num = float(input("Enter a number: "))
# sqrt_result = math.sqrt(num)
# print(f"The square root of {num} is: {sqrt_result}")


# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))

# # Calculate the area of the rectangle
# area = length * width

# # Output: Display the result
# print(f"The area of the rectangle is: {area}")



# side = float(input("Enter the side length of the square: "))

# # Calculate the area and perimeter of the square
# area = side * side
# perimeter = 4 * side

# # Output: Display the results
# print(f"The area of the square is: {area}")
# print(f"The perimeter of the square is: {perimeter}")


# radius = float(input("Enter the radius of the cylinder: "))
# height = float(input("Enter the height of the cylinder: "))

# # Calculate the surface area and volume of the cylinder
# surface_area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height
# volume = math.pi * radius**2 * height

# # Output: Display the results
# print(f"The surface area of the cylinder is: {surface_area}")
# print(f"The volume of the cylinder is: {volume}")


# x = float(input("Enter the value of variable 'x': "))
# y = float(input("Enter the value of variable 'y': "))

# # Swap the values without using a temporary variable
# x, y = y, x

# # Output: Display the swapped values
# print(f"After swapping, the value of 'x' is: {x}")
# print(f"After swapping, the value of 'y' is: {y}")


# number = int(input("Enter a number: "))

# # Check if the number is even or odd
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")


# number = float(input("Enter a number: "))

# # Calculate the absolute value using abs()
# absolute_value = abs(number)

# # Output: Display the absolute value
# print(f"The absolute value of {number} is: {absolute_value}")



# Input: Get three numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# Check the largest number
# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3

# # Output: Display the largest number
# print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")



# Input: Get a year from the user
# year = int(input("Enter a year: "))

# # Check if the year is a leap year
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# # Input: Get a number from the user
# number = float(input("Enter a number: "))

# # Check if the number is positive, negative, or zero
# if number > 0:
#     print(f"{number} is a positive number.")
# elif number < 0:
#     print(f"{number} is a negative number.")
# else:
#     print(f"{number} is zero.")


# Input: Get marks for each subject from the user
# subject1 = float(input("Enter marks for Subject 1: "))
# subject2 = float(input("Enter marks for Subject 2: "))
# subject3 = float(input("Enter marks for Subject 3: "))
# subject4 = float(input("Enter marks for Subject 4: "))
# subject5 = float(input("Enter marks for Subject 5: "))

# # Calculate average marks
# average_marks = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

# # Display the average marks
# print(f"Average Marks: {average_marks}")

# # Determine the grade based on average marks
# if average_marks >= 90:
#     grade = 'A+'
# elif average_marks >= 80:
#     grade = 'A'
# elif average_marks >= 70:
#     grade = 'B'
# elif average_marks >= 60:
#     grade = 'C'
# elif average_marks >= 50:
#     grade = 'D'
# else:
#     grade = 'F'

# # Output: Display the grade
# print(f"Grade: {grade}")




# practical 5

# Program to print even numbers from 1 to 100 using a while loop

# Initialize the counter
# number = 1

# # Loop through numbers from 1 to 100
# while number <= 100:
#     # Check if the number is even
#     if number % 2 == 0:
#         # Print the even number
#         print(number, end=' ')

#     # Increment the counter
#     number += 1

# # Output: 2 4 6 8 10 ... 98 100


# Program to find the sum of the first 10 natural numbers using a for loop

# Initialize the sum
# sum_of_numbers = 0

# # Loop through the first 10 natural numbers
# for number in range(1, 11):
#     # Add the current number to the sum
#     sum_of_numbers += number

# # Print the result
# print("Sum of the first 10 natural numbers:", sum_of_numbers)



# Program to print Fibonacci series

# Function to generate Fibonacci series up to n terms
# def fibonacci(n):
#     fib_series = []
#     a, b = 0, 1

#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a + b

#     return fib_series

# # Get the number of terms from the user
# num_terms = int(input("Enter the number of terms for Fibonacci series: "))

# # Print the Fibonacci series
# result = fibonacci(num_terms)
# print("Fibonacci series up to", num_terms, "terms:", result)



# Program to calculate the factorial of a number

# Function to calculate factorial
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Get the number from the user
# num = int(input("Enter a number to calculate its factorial: "))

# # Check for non-negative input
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     # Calculate and print the factorial
#     result = factorial(num)
#     print(f"The factorial of {num} is: {result}")



# Program to reverse a given number

# Function to reverse the number
# def reverse_number(number):
#     reversed_num = 0

#     while number > 0:
#         digit = number % 10
#         reversed_num = (reversed_num * 10) + digit
#         number = number // 10

#     return reversed_num

# # Get the number from the user
# num = int(input("Enter a number to reverse: "))

# # Reverse the number and print the result
# result = reverse_number(num)
# print(f"The reversed number is: {result}")


# practical 6


# def sum_of_list(numbers):
#     total = sum(numbers)
#     return total

# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# result = sum_of_list(my_list)
# print(f"The sum of the list {my_list} is: {result}")


# def multiply_list_elements(lst):
#     result = 1
#     for item in lst:
#         result *= item
#     return result

# # Example usage:
# my_list = [2, 3, 4, 5]
# result = multiply_list_elements(my_list)

# print(f"The product of all elements in the list {my_list} is: {result}")  


# 



# def get_smallest_number(numbers):
#     if not numbers:
#         return None  # Return None for an empty list
    
#     smallest = numbers[0]  # Assume the first number is the smallest
    
#     for num in numbers:
#         if num < smallest:
#             smallest = num  # Update the smallest number
    
#     return smallest

# # Example usage:
# numbers_list = [5, 3, 8, 2, 1, 7]
# result = get_smallest_number(numbers_list)

# if result is not None:
#     print(f"The smallest number in the list is: {result}")
# else:
    # print("The list is empty.")
    
    
    
# def reverse_list(input_list):
#     return input_list[::-1]

# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# reversed_list = reverse_list(my_list)
# print(reversed_list)



# def find_common_items(list1, list2):
#     return [item for item in list1 if item in list2]

# # Example usage:
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# common_items = find_common_items(list1, list2)
# print("Common items:", common_items)


# def select_even_items(input_list):
#     return [item for item in input_list if item % 2 == 0]

# # Example usage:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_items = select_even_items(my_list)
# print("Even items:", even_items)




list = [1, 2, 3, 4, 5]
print(list [2])

thisList = ["Nitin","Pritam","Lokesh","Vipul","Ganesh","Bhaumik","Aryan","Yash","Anuj"]
print(thisList[ -4:-1])



Thislist = ["apple","banana","chery","kiwi"]
Thislist[2] = "Mango"
print(Thislist)



List1 = ["Tata","Birla","Ambani","Adani"]
List1 [0:2] = ["Ashok","Leyland"]
print(List1)



import keyword

print(keyword.iskeyword('if'))  # True
print(keyword.iskeyword('hello'))  # False



# # Example of if-elif-else statement

# # User input for age
# age = int(input("Enter your age: "))

# # Checking the age category
# if age < 0:
#     print("Invalid age. Please enter a valid age.")
# elif age < 18:
#     print("You are a minor.")
# elif age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")


# Python program to reverse a word

# Function to reverse a word
# def reverse_word(word):
#     reversed_word = word[::-1]
#     return reversed_word

# # Get input from the user
# user_input = input("Enter a word: ")

# # Call the function to reverse the word
# reversed_input = reverse_word(user_input)

# # Display the reversed word
# print("Reversed word:", reversed_input)


a=input("enter a word :")
for I in range(len(a)-1,-1,-1):
    print(a[I],end="")
    

# for i in range (1,5):
#     for j in range (1,5):
#         if j<=i:
#             print("*",end='')
#         else:
#             print(" ")
#         print()



# for i in range (1,6):
#     print('*', end=" ")
# for j in range (1,6):
#     print('*', end=" ")
    
# for i in range (5,0,-1):
#     for j in range(i)
#     print('*', end=" ")
#     print()