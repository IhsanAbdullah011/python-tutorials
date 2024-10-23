"""
introduction to loops: For loop

- A loop allows you to repeat a bunhc of code multiple times.
- real life example:"
    teacher: "in your detention i want you to write the follwoing lines 100 times"
             'I will never misbehave ever again'

- to code that, rather than typing out print("i will never..."), we can use a for loop
  that says to the computer, do the specified code FOR 100 repetitions

"""

# introduce 0 indexing
# introduce range (start,stop) function

for i in range(100):
    print("i wont miss my homework")


for i in range(4,11):
    print("i wont miss my homework")
    

numbers = [2,4,7,8,10,12,14,16,18,20]

for i in range(10): #this is saying the loop will loop 10 times, and i starts from 0 and ends at 9

    print(i) # output: 5
    print(numbers[i]) # output: 12


# 'i' is a variable that starts at 0 (because in the range function the firs tnumebr is 0),
# each time the loop starts again it will increase by 1 we can see the value of 'i'
# by printing it out in the loop


for i in range(0,10):
    print(f"value of 'i': {i}")


print("")

# we can change the name of 'i' to make it esier to understand. lets call it 'counter' instead

for counter in range(0,10):
    print(f"value of 'counter': {counter}")

print("")

# by changing the first number in the range function we can change the starting value of 'counter'
for counter in range(3,10):
    print(f"value of 'counter': {counter}")

print("")

# by adding a third number in the range function it will increase its 'step', this means instead of
# increasing by 1 each time the loop loops, it iwll increase by the step number.
# range(start,stop,step)

for counter in range(0,12,3):
    print(f"value of 'counter': {counter}")


#uses for loops
totalPrice = 0.00

itemsBaught = [10.99, 3.99, 2.40, 11.60, 2.99, 5.99]

for i in range(len(itemsBaught)):
    totalPrice = totalPrice + itemsBaught[i]


print(totalPrice)

for i in itemsBaught:
    totalPrice = totalPrice+i

print("your total is",totalPrice)