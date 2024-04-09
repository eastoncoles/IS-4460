#This is my comment

print('Easton') #This is a string object
print(3.3) #This is a float

A = 1
a = 2

print(A)
print(a)

user_name = "Easton"
gpa = 3.9

print(user_name)
print(gpa)

print("My name is " + user_name + " not Bill")
print(f"My name is {user_name} not Bill")

name = "Me"
name = 12

number = 123 * 654
print(str(number)[1:3]) #str() converts integer to string
# [] gets the set of numbers you would like

def addNumbers(a,b):
    output = a + b
    return output

print(addNumbers(1,2)) #positional arguments
print(addNumbers(b=6, a=3)) #named arguments

name = "Andy"
def say_hello():
    name = "Bob"
    return f"hello {name}"

print(say_hello())
