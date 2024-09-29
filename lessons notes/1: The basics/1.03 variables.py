"""
A variable is a named location that is used to store information,
this information can be called and used in different parts of the program,
variables store information but that information can be changed.

a good example would be a box:
    imagine we have a box called "toy box". i can put things inside the box,
    for example i can put toys inside of it. when i want my toys i can 'call/bring' 
    my toy box and take out whats inside of it. i can also chaneg the toys that are inside
    the toy box. for example a toy car cna be repalced with lego
"""

#difining variables



name = "Abdullah"
age = 10

#printing variables
print(name)
print(age)

print("hello",5)
print("hello"+5)




#concatinating with variables
print("string followed by 'name' variable: "+ name)
# print("strign followed by 'age' variable: "+ age)
print("strign followed by 'age' variable: " , age)
print("strign followed by 'age' variable: "+ str(age))
print("strign followed by 'age' variable: "+ "age")
print(type(age))
print(f"strign followed by 'name' variable: {name}")



# maths with variables
numOne = 10
numTwo = 20


print(5+5)

numOne+numTwo = 30

print(numOne + numTwo)  #30
print(numOne + numOne)  #20

total = numOne + numTwo
print(total)

#my first number is [variable 1], my second number is [variable 2]. 
#[variable 1] + [variable 2] = [total]

# +
# -
# /
# *


#re-assigning values to existing variables
print(numOne)
numOne = 15
print(numOne)

# a cool feature
var_1, var_2, var_3 = ("content for variable 1", "content for variable 1", 3)
print(var_1)
print(var_2)
print(var_3)


"""
summary:

- vairables are used to store data
- to make a variable (define a variable) you just write a variable name
- to give a value (assign a value) to the variable you add an '=' sign after the name and then put the data
- python will automatically knwo what type the variable is based ont he 'type' of data you enter (i.e str, int, float)

- you can use the print function and variables together
- print(name) -> python sees you our displaying something, it recognises you put a variable called name, it then displays
  whatever is inside of the variable called 'name'
- if you dont difine a variable and then tell python to print it it will give an error

- last lesson we learn about concatination and arithmetic opperations. you are able to do this using vairables in the exact same way
- you can concatinate varaibles
- you can concatinate varaibles and use it in print()
- you can perform mathematical opperations using variables and store it in another variable
- just as you need to pay attention to types when concatinating, you need to do the same for variables

- you can overwrite exisitng variables, meaning you cna reset what a variable is storing
- you cna difine multiple variables in one line. first write all the different variabel names using a ',' to separate the variables
  then add the '=' sign followed by what you want to put in each variable using a ',' to separate the content. note names and
  content need to be equal. meaning 3 variable names need to have 3 bits of information. not 2. not 4.
  
"""