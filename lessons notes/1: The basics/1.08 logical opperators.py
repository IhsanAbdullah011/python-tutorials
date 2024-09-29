#logical opperators: and, or, not

"""

- and: first thing AND second thing need to be true
- or:  first thing OR second thing need to be true, i.e. one or both of them must be true
       but boht of them cant be false
- not: converts whatevr is inside into the opposite, so if its true it will make it false,
       if it is false it will mkae it true

"""

x = 10
y = 5
z = 2

#Example 1: and opperator - what will it print? True or False
print("\nAND opperator - what will it print? True or False\n")
print(x<y and y<z)
print(x>y and y<z)
print(x<y and y>z)
print(x>y and y>z)

#Example 2: or opperator - what will it print? True or False
print("\nOR opperator - what will it print? True or False\n")
print(x<y or y<z)
print(x>y or y<z)
print(x<y or y>z)
print(x>y or y>z)

x = 10
y = 5
z = 2


#Example 3: Not opperator - what will it print? True or False
print("\nNOT opperator - what will it print? True or False\n")
print(not(x == y))
print(not(x != y))
