input("tell me what to print! ")
print(input("tell me what to print! "))

name = input("what is your name? ")
age = input("how old are you? ")

print("you're name is "+name+" and you are "+age+" years old")
#note: the input will store infromation by default as a string

print(age,20)
# print(age+20)

age = int(input("how old are you? "))
print(age+20)


"""
something to notice/think about:

- in python you have things called built in functions. theyre like ley words that tell the computer what you want to do
  notice in vscode it colours the built in fucntions in yellow.
- up until this lesson we only learnt one built in function: 'print'
- today we learnt a new function called input

- you can combine functions within functions for example print(input())
  print(input("question")) -> print is saying display, then inside of print we have input, this is saying get some information from the user,
  inside input there is some text, this is a prompt and will be displayed, this essentialy describes to the user what they need to write or input.
    
    1) so it will do input first (display the promt)
    2) user will type an answer
    3) the users response will be given to the print function
    4) the print function will display it

- another example: int(input("how old are you"))
  
    1) input function displays the prompt "how old are you"
    2) user enters the response
    3) the response is stored as a string by defaut
    4) the int() function converts the response into an int

- last example: age = int(input("how old are you"))
  
    1) input function displays the prompt "how old are you"
    2) user enters the response
    3) the response is stored as a string by defaut
    4) the int() function converts the response into an int
    5) the response whihc is now an int is finally stored into a variable called "age"

"""

"""
activity 1: Mad libs generator

- a mad libs genrator is very simple. it will help you to jsut practice inputs and concatination
- it starts fo by promting the user to input answers to a few questions
- it then uses the answers to fill in the blanks to make a funny story

- heres an example:

program:

- please enter an adjective
- please enter an adjective
- please enter an type of bird
... all the way tot he end

the final output will be what the user put in:

It was a [adjective] cold November day. I woke up to the [adjective] smell of [type of bird] 
roasting in the [room in a house] downstairs. I [verb (past tense)] down the stairs to see if
I could help [verb] with the dinner. My mom said, "See if [relative's name] needs a fresh [noun]." 
So, I carried a tray of glasses full of [a liquid] into the [verb ending in -ing] room.
When I got there, I couldn't believe my [part of the body (plural)]; there were [plural noun]
[verb ending in -ing] on the [noun]!

"""

"""
activity 2: DOB calculator

- make a simple program that asks the user for their name, age, what month and day they were born
- the program should say "hi [name]"
- the program should then use the age, month and day entered to figure out their DOB and display the following:
  "you were born in [date of birth]/[month of birth]/[year of birth]"

hints:
- you will need to use input()
- you will need to use int()
- you will need vairables
- you will need concatination

"""

"""
activity 3: Arithmetic Practice

Task: Write a Python program that:
1. Asks the user for two numbers (integers or floats).
2. Performs the following operations on those two numbers and prints the results:
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)
   - Exponentiation (**)
   - Integer division (//)
   - Modulus (%)
   
Example output:
Enter the first number: 10
Enter the second number: 3

Results:
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Exponentiation: 1000
Integer division: 3
Modulus: 1
"""