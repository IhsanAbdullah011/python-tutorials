grade = int(input("Enter your mark (0-100): "))

if grade >= 90:
    print("You got an A! Excellent work!")
elif grade >= 80:
    print("You got a B! Great job!")
elif grade >= 70:
    print("You got a C! Good effort, but there's room to improve.")
elif grade >= 60:
    print("You got a D. You passed, but try harder next time.")
else:
    print("You got an F. Don't give up! Keep working and you'll improve.")