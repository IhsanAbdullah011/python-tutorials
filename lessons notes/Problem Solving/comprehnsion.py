"""
how to read and comprehend code in an easy to udnerstand manner

1) try your best to not read code in a "technical way"
2) read it in a way where its as close to english as you can possibly make it
3) read the code, not according to how english flows meaning dont jsut read from top to bottom left to right,
   rather read according to how the program runs, so if it goes from top to bottom and then right to left, then read it like that
4) also think about what the program does and the order it does things in detail!

in the rest of this file i'll write some tips or common internal dialogues you should think about when you see certain things to help with that
"""

# we said whenevr we see a comparison opperator we think of the word "check" and the sentance "if its true then do a", "otherwise do b"

#example 1:
a = 1
b = 2

a == b # read like this: im "checking" if a is the same as b, since there is no function here we dont ened to worry about what it will do

#example 1.1:
a = 1
b = 2

if a == b: # im "checking" if a is the same as be, if "true" then go to line 26
    print("a is equal to be")

else: #otherwise if "false" go to line 29
    print("a is not equal to b")

#example 1.2:
a = 0
b = 10
while a != b: # checking if a is not the same as b if that true go to line 35 otherwise go to line 36
    print("a is not b")
    a = a+1 # step 1: retrieve whats inside of a which is 0, step 2:  0+1, step 3: put it in a


#example 1.3:
# whenever you see an elif think: im "checking" if the previous if was "false", if it was false then do the 2nd check after it, otherwise skip
# whenever you see an else think: im "checking" if EVERYTHING before was "false", if it was then do the next line, otherwise jump to the end

if a == b: # im "checking" if a is the same as be, if "true" then go to line 26
    print("a is equal to be")

elif a<b:
    print("a is less than b")

else: #otherwise if "false" go to line 29
    print("a is not equal to b")

#uses for loops
totalPrice = 0.00
itemsBaught = [10.99, 3.99, 2.40, 11.60, 2.99, 5.99]

for i in range(len(itemsBaught)):
    totalPrice = totalPrice + itemsBaught[i]

print(totalPrice)

