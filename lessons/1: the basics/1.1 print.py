
print("Hello World")
print('Hello world')

# "" vs ''
print('he said "shush" ')
print("he said \"shush\" ")

# concatination
print("hi" + "there")
print("hi","there")

#concatinating strings with integers
# print("i am" + 5)      # using the '+' opperator
print("i am", 5)         # using the ',' sign
print("i am" + str(5))   #using type coverter: str()

print("5 + 5")
print(5 + 5)

# print(5+"5")
print(5+int(5))          #using type coverter: int()

print(8.5 + 5)           #what "type" is this?
print(8.0 + 5)

# print(int('8.5')+5)
print(float('8.5')+5)

print("this is some tex" "\nthis is some text on a new line\n\nyou can use two backslash n's to make an empty line\n")

"""
summary:

- we use the print function to display information to the terminal
- to do this we write print followed by brackets, we put the information we want to display within the brackets

- if we put "" inside oft he brackets, whatever is inside of the brackets are known as "strings"
- a "string" is a type of data, there are others such as integers, floats and bools
- when printing we need to be careful of "mixing" different data "types" and how it may affect what is displayed

- concatination is when you combine two data types together. in python you cna do this by using '+' or ','
- combining two strings together litterelly puts them side by side. 
 e.g: "hi" + "friend" --> hifriend
      "hi " + "friend" --> "hi friend"

- careful!: concatinating a string and an integer using '+' can cause an error
 e.g "this is a string because of the speech marks" + 5

- to soolve this issue instead of using the '+' sign we can use ','
- alternatively we cna change the "type" of the integer 5 into a string by either  putting a "" arround it or by using a type converter
 e.g "string" , "5"
 e.g "string" + "5"
 e.g "string" + str(5)

 data types:
 - str: (A.K.A strings) anything surrounded in (" ") or in (' '), its just plain and simple text
 - int: (A.K.A integers) whole numbers
 - float: (A.K.A floating point numbers) decimal numbers

 type converters:
 - str()
 - int()
 - float()
"""