"""
P1 adding until given number:

1) i need to ask the user what number they want to go up to
2) i need to keep on adding until i reach the number

example:
user says 6

program:

how?

total = 0


total = 0
number = int(input("please enter a number: "))

for i in range(1,number+1):
    total = total + i

print(total)

"""




"""
P2: printing all numbers between a range

input: 12
output: print all even numebrs between 1 and 12: example - 2,4,6,8,10

1) get number from user
2) loop: start from 2 and end at number
3) step up by 2
4) print the i

number = int(input("please enter your number: "))

for i in range(2,number,2):
    print(i)

1) get number from user
2) start from 1 and loop untill 12
3) if the numeber is even print it
4) if the number is odd dont print it

number = int(input("please enter a number: "))

for i in range(1,number):
    if i % 2 == 0:
        print(i)
"""

"""
P3: multiplication table printer

input: 4
print 1X4 = 4
print 2x4 = 8
...
print 12x4 = 48

1) get input for whihc number they want to see --> multiplier
2) loop: start from 0 until (including) 12
2.5) do the maths and store in answer
3) print "multiplier x i = answer"

multiplier = int(input("please enter a multiplication table you want to see: "))
answer = 0

for i in range(13):
    answer = multiplier * 2
    print(f"{multiplier} x {i} = {answer}")

"""

"""
user input: 1,2,3,4,5,6
store in list[]
list for looping

ask how long is ur list? 10
for 10 numbers:
    myList.append(int(input(whats ur number)))

#now we have our list

for i in range(len(list),-1):
    print(list[i])
______________

myList = []
lenList = int(input("please enter the lenght of your list:" ))

for i in range(lenList):
    myList.append(int(input("please enter the next number")))

for j in range(len(myList) -1,-1,-1):
    print(myList[j])
    
"""



number = int(input("please enter your number: "))

for i in range(2,number,2):
    print(i)
    