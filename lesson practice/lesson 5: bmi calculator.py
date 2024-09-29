height = int(input("how tall are you in cm? "))
weight = float(input("how much do you weigh in kg? "))

height = height/100
bmi = weight/(height*height)

print(round(bmi,2))

