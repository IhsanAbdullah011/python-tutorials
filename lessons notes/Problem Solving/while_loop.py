from random import randint

#hint: set values,using those values make a condiiton thats ture to start the while loop, make a way to make the those values eventually false

"""
counter = 0
while counter <=  10:
    print(counter)
    counter = counter+1
    # incrementing --> increasing a variable by a certain ammount
    # eventually counter will go form 0 upto 10 and hten the loop condition will be false and so it wont run

"""

"""
1) get input
2) set condition for while
3) make the while loop
4) do the adding
5) get close to breaking out of the while loop

start = int(input("Please enter a number to start from"))
end = int(input("please enter a number to end at"))
total = 0

while start <= end:
    total = total+start
    start = start+1
    
print(f"your total is: {total}")

"""

"""

randomInt = randint(0,10) #6
answer = int(input("guess my random number between 0 and 10: "))

while answer != randomInt:
    print("you guest wrong")
    answer = int(input("guess my random number between 0 and 10: "))#6

print("congrats u got my number:",randomInt)

"""

"""
hint: set values,using those values make a condiiton thats true to start the while loop, make a way to make the those values eventually false

1) get the user to tell us when to start the timer
2) isFinished = False
3) while isFinihsed is set to false loop
4) in the loop we can do timer minus 1 and print it
5) have an if statement: if timer is equal to 0 set isfinihsed to True
6) break out of loop. no mroe lines left. prorgam is done

isFinshed = False #making a variable i can use to ensure the loop is true and eventually ill make it false
timer = int(input("please enter a number to start the timer from"))

while isFinshed == False:
    print(timer)
    timer = timer-1

    if timer < 0:
        isFinshed = True

"""

timer = int(input("Please enter a numebr to start the timer form")) #6
stop = 0

while timer>=stop:
    print(timer)
    timer = timer-1


