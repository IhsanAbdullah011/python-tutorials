"""

Task: Car Insurance Premium Calculator
Write a program that calculates the monthly insurance premium for a person based on their age, driving experience, car type, and accident history. The rules are as follows:

If the person is 25 years old or older:
If they have 5 or more years of driving experience:
If their car is a sports car:
If they have had an accident in the past 2 years, their premium is $200.
Otherwise, their premium is $150.
If their car is not a sports car:
If they have had an accident in the past 2 years, their premium is $120.
Otherwise, their premium is $100.
If they have less than 5 years of driving experience:
If their car is a sports car:
If they have had an accident in the past 2 years, their premium is $250.
Otherwise, their premium is $200.
If their car is not a sports car:
If they have had an accident in the past 2 years, their premium is $180.
Otherwise, their premium is $150.
If the person is under 25 years old:
If they have 5 or more years of driving experience:
If their car is a sports car:
If they have had an accident in the past 2 years, their premium is $300.
Otherwise, their premium is $250.
If their car is not a sports car:
If they have had an accident in the past 2 years, their premium is $220.
Otherwise, their premium is $180.
If they have less than 5 years of driving experience:
If their car is a sports car:
If they have had an accident in the past 2 years, their premium is $350.
Otherwise, their premium is $300.
If their car is not a sports car:
If they have had an accident in the past 2 years, their premium is $270.
Otherwise, their premium is $220.

Input:
age (integer): Age of the person.
driving_experience (integer): Years of driving experience.
car_type (string): Either "sports car" or "regular car".
accident_in_past_two_years (boolean): True if the person has had an accident in the past two years, False otherwise.
This task requires 4 levels of nested if statements and helps to practice handling multiple layers of logic based on different conditions!

"""

#implementation

age = int(input("Enter your age: "))
experience = int(input("How many years have you been driving for?: "))
carType = input("What type of car do you have? \n1) sports car \n2) regular car\ncar type: ")
hadAccident = input("Have you had a car accident in the last 2 years? Yes / No ")
cost = 0

if age >= 25:
    if experience >= 5:
        if carType == "sports car":
            if hadAccident == "No":
                cost = 150
            elif hadAccident == "yes":
                cost = 200
            else:
                print("you may have written a incorrect input/answer")
        elif carType == "regular car":
            if hadAccident == "No":
                cost = 100
            elif hadAccident == "yes":
                cost = 120
            else:
                print("you may have written a incorrect input/answer")
        else:
            print("you may have written a incorrect input/answer")
    elif experience < 5:
        if carType == "sports car":
            if hadAccident == "No":
                cost = 200
            elif hadAccident == "yes":
                cost = 250
            else:
                print("you may have written a incorrect input/answer")
        elif carType == "regular car":
            if hadAccident == "No":
                cost = 150
            elif hadAccident == "yes":
                cost = 180
            else:
                print("you may have written a incorrect input/answer")
        else:
            print("you may have written a incorrect input/answer")
    else:
        print("you may have written a incorrect input/answer")

elif age < 25:
    if experience >= 5:
        if carType == "sports car":
            if hadAccident == "No":
                cost = 250
            elif hadAccident == "yes":
                cost = 300
            else:
                print("you may have written a incorrect input/answer")
        elif carType == "regular car":
            if hadAccident == "No":
                cost = 180
            elif hadAccident == "yes":
                cost = 220
            else:
                print("you may have written a incorrect input/answer")
        else:
            print("you may have written a incorrect input/answer")
    elif experience < 5:
        if carType == "sports car":
            if hadAccident == "No":
                cost = 300
            elif hadAccident == "yes":
                cost = 350
            else:
                print("you may have written a incorrect input/answer")
        elif carType == "regular car":
            if hadAccident == "No":
                cost = 220
            elif hadAccident == "Yes":
                cost = 270
            else:
                print("you may have written a incorrect input/answer")
        else:
            print("you may have written a incorrect input/answer")
    else:
        print("you may have written a incorrect input/answer")

else:
    print("you may have written a incorrect input/answer")

if cost != 0:
    print(f"The price of your insurance is: ${cost}.00")
