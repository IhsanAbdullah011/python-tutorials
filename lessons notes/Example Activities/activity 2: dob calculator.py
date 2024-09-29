name = input("please enter your name: ")
age = int(input("please enter your age: "))
day = input("please enter the day number you were born: ")
month = input("please enter your month number you were born: ")
year = 2024-age

print("hi "+name)
print("you were born in", day+ "/" + month + "/" +str(2024 - int(age))) #option 1
print("you were born in", day+ "/" + month + "/",2024-age) #option 2


print(f"you were born in {day}/{month}/{year}")
