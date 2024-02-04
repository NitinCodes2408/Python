# variables & data types

character_name = "Nitin" #variables name
character_age = "19"
isMale = True
#is_male = False
print("There once was a man named " + character_name +", ")
print("he was " + character_age +" years old. ") 

character_name = "Lokesh"
character_age = "20"
print("He really like the name " + character_name +", ")
print("but didn't like being " + character_age + ".")


#Working with Strings

print("Giraffe\nAcademy")   # \n for next line
print("Giraffe\"Academy")   
phrase = "Giraffe Academy"
print(phrase + " is cool")   # +"string" is attached to another String
print(phrase. lower())       # for small text
print(phrase. upper())       # for capitalize the text
print(phrase.upper().isupper())
print(len(phrase))           # for counting the length
print(phrase [3])            # checking the character with index
#print(phrase [7])
print(phrase.index("A"))     # checking the index number of char
print(phrase.replace("Academy", "Classes"))    # for replace the strings


#Working with Numbers

print(-2.0987)     #Displaying simple numbers
print(3+5)         #Any operation calculation
print(4+5.5)       #Addition
print(10-5)        #Subtraction
print(10*2)        #Multiplication
print(12/2)        #Division
print(3*4+5)

#Math Functions
from math import *

my_num = 5+10
print(str(my_num) + " is my favorite number")    #Displaying Number with string

my_num = -10
print(abs(my_num))    #Displaying absolute value of -ve numbers
print(pow(3, 2))      #Displaying power of any number
print(max(10,20))     #Finding max number 
print(min(40, 30))    #Finding min number
print(round(3.5))     #Displaying round figure number
print(sqrt(100))      #Displaying square root

#Getting input from users

name = input("Enter your name: ")
age = input("Enter your age: ")
print("My name is " + name +"!")
print("and my age is " + age +"!")
print("Hello " + name + "! You are " + age)

#Building a basic calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# result = int(num1) + int(num2)     # for calculating simple number
result = float(num1) + float(num2)   # for caclulating decimal number

print(result)                        # this is commun


# Mad Libs Games

color = input("Enter a color:")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")


print("Rose are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)


