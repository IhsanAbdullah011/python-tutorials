#comparison opperators: ==, !=, <, >, <=, >=

x = 5
y = 7

if x>y:
    print("x is greater than y")

if x<y:
    print("x is less than y")

if x==y:
    print("x is equal than y")

if x != y:
    print("x is not equal to y")

z = 12

if (z>x>y):
    print("z is greater than x, and x is greater than y. therefroe z is the biggest and y is the smallest")


age = int(input("how old are you?"))

if (age < 18):
    print("you are not an adult by western standards...")

if age > 18 :
    print("you are an adult by western standards...")

if age == 18:
    print("you just turned into an adult by western standards")

weight = int(input("how many kg do you weigh?"))

if (weight >= 150):
    print("Akhi im worried for your health. you got to hit gym asap and lose some weight!!!")

if (weight <= 50):
    print("Akhi im worried for your health. you got to hit gym asap and put on some muscle!!!")

favFood = input("whats ur favourite food? ")

if (favFood == "burger"):
    print("you have good taste")
    print("we should go out to eat some time. i heard smash burger is really good")