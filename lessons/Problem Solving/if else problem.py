"""

Task
Given an integer, , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

"""

def answers(n):
    if n%2 != 0:
        print("Weird")
        
    elif (n%2 == 0):
        if (2<=n<=5):
            print("Not Weird")
        elif (6<=n<=20):
            print("Weird")
        elif (n>20):
            print("Not Weird")

answers(int(input("enter a number for n ")))