shoppingList = ["banana", "apple", "pear", "pineapple"] 


print(shoppingList) #prints full list

print(shoppingList[0]) #prints 1st item/element
print(shoppingList[1]) #prints 2nd item/element
print(shoppingList[2]) #prints 3rd item/element
print(shoppingList[3]) #prints 4th item/element

print("")











#list methods

#Example 1: append: adds to the end of the list
shoppingList.append("coconut")
print(f"\n{shoppingList}")




#Example 2: sorts the list alphabetically
shoppingList.sort()
print(shoppingList)





#Example 3: reverses the order of the items in the list
shoppingList.reverse()
print(f"\n {shoppingList}")






#Example 4: removes the last item in the list
shoppingList.pop(2)
print(f"\n {shoppingList}")








#Example 5: removes whatever is specified inside of the brackets
shoppingList.remove("banana")
print(f"\n {shoppingList}")





#Example 6: inserts a value into the index specified -> .insert(index, value)
shoppingList.insert(2,"orange")
print("inserted orange in index 2 -> position 3:")
print(f"\n {shoppingList}")



print(len(shoppingList))




