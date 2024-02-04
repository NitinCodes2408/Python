
def say_hi():              # function name
    print("Hello User")
    
print("Top")
say_hi()                   # function calling
print("Bottom")

def say_hi(name):          # function value
    print("Hello " + name)
    
say_hi("Nitin")
say_hi("Sharu")


def say_hi(name, age):
    print("Hello " + name + ", you are " + age)
    
say_hi("Nitin", "19")
say_hi("Sharu", "20")