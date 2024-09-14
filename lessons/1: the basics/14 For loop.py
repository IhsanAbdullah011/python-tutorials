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

for i in range(0,10):
    print("i wont miss my homework")

# 'i' is a variable that starts at 0 (because in the range function the firs tnumebr is 0),
# each time the loop starts again it will increase by 1 we can see the value of 'i'
# by printing it out in the loop

for i in range(0,10):
    print(f"value of 'i': {i}")

print("")

# we can change the name of 'i' to make it asier to understand. lets call it 'counter' instead

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

for counter in range(0,12,2):
    print(f"value of 'counter': {counter}")