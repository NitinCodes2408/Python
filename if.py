
is_male  = True

if is_male:
    print("You are male")
else:
    print("You are not male")
    
is_male = False
is_tall = True

if is_male and is_tall :
    print("You are tall male")
elif is_male and not(is_tall):
    print("You are short male")
elif not(is_male) and is_tall:
    print("You are not male but are tall")
else :
    print("You are either not male or not tall or both")




a = int(input("Enter your percent : ")) 
if a >= 75 :
    print("You will Distinction")
else :
    print("You are fail")

# if statements and comparisons


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3,0,7)) 

