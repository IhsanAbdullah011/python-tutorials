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
activity 1:

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