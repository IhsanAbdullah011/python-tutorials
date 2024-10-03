gender = input("please enter your gender (M/F)")

if gender == "M":
    mosquePrayer = int(input("how many salahs do you pray in the mosque"))
    if mosquePrayer <5:
        print("u need to pray at least all 5 salahs in the mosque")
    gym = input("how often do you go gym")
    food = input("what does ur wife cook")


elif gender == "F":
    hoover = int(input("how often do u hoover"))
    if hoover < 1:
        print("your getting sent back")
    cleaning = input("how often do you clean the KITCHEN")
    cooking = input("what do u cook")

else:
    print("invalid")