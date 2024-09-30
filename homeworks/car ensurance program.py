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