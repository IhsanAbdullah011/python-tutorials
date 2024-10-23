#hint: set condition to true, start the while loop and wirte condiiton, make a way to make the ocndiiton eventually false

"""
1) get input
2) set condition for while
3) make the while loop
4) do the adding
5) get close to breaking out of the while loop
"""

number = int(input("please enter a number that you wan tot add to"))
counter = 0
total = 0

while counter <= number:
    total = total+counter
    counter = counter+1
    print(f"total = {total}+{counter}")

print(total)