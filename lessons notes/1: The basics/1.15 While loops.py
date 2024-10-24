
condition = 25

while condition > 10:
    print("the numebr inside the condition variable is greater than 10")
    print("condition =",condition)
    condition = condition -1  #this is my way to break out of the loop eventually



isClever = False
while isClever == False:

    print("you're dumb. go study")
    number = int(input("what is 9 + 10"))

    if number != 19:
        print("you are wrong")
    elif number == 19:
        print("correct")
        isClever = True
    else:
        print("invalid response")


#while loop example 1:
print("\n\n shopping list price calculator\n\n")

totalPrice = 0.00
itemsBaught = []
done = False

while done == False:
    finish = input("would you like to add a price to your order? 'yes' or 'no'")
    if finish == "yes":
        itemsBaught.append(float(input("please enter the price (0.00) format\nprice: ")))
    elif finish == "no":
        done = True
    else:
        print("invalid input. try again")

for i in itemsBaught:
    totalPrice = totalPrice+i

print("your total is",totalPrice)





#while loop example 2
print("\n\n steak doneness input\n\n")

print("\n\nWhat is your preferred doneness of steak")

answer = input("Please enter a number:\n\n1) Rare \n2) Medium Rare \n3) Medium \n4) Well Done\nSelection: ")
valid = False

while valid == False:
    
    if answer in ["1", "2", "3", "4"]:
        valid = True
    else:
        print("\nYou have not entered a valid answer.")
        answer = input("Please enter a number:\n\n1) Rare \n2) Medium Rare \n3) Medium \n4) Well Done\nSelection: ")

if answer == "1":
    print("you chose rare")
elif answer == "2":
    print("you chose medium rare")
elif answer == "3":
    print("you chose medium")
elif answer == "4":
    print("you chose well done")

print("your order is coming")

name = "abdullah"

while name in ["musa","yahya","esa"] != True:
    print("name isnt in ")