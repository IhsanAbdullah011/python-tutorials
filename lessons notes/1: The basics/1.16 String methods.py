"""
  Basic String Methods in Python
  Strings are one of the most commonly used data types in Python.
  They come with various built-in methods that allow you to manipulate 
  and interact with string data easily.
"""
# String Methods Overview

# 1. len()
# Description: Returns the length of the string.
text = "Hello, World!"
length = len(text)
print(length)  # Output: 13

# 2. str.lower()
# Description: Converts all characters in the string to lowercase.
text = "Hello, World!"
lower_text = text.lower()
print(lower_text)  # Output: "hello, world!"

# 3. str.upper()
# Description: Converts all characters in the string to uppercase.
text = "Hello, World!"
upper_text = text.upper()
print(upper_text)  # Output: "HELLO, WORLD!"

# 4. str.strip()
# Description: Removes any leading and trailing whitespace from the string.
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

# 5. str.replace(old, new)
# Description: Replaces all occurrences of a substring with another substring.
text = "Hello, World!"
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Output: "Hello, Python!"

# 6. str.split(separator)
# Description: Splits the string into a list using the specified separator.
text = "Hello, World!"
words = text.split(", ")
print(words)  # Output: ["Hello", "World!"]

# 7. str.join(iterable)
# Description: Joins elements of an iterable (like a list) into a single string with a specified separator.
words = ["Hello", "World"]
joined_text = ", ".join(words)
print(joined_text)  # Output: "Hello, World"

# 8. str.find(substring)
# Description: Returns the index of the first occurrence of the substring. Returns -1 if not found.
text = "Hello, World!"
index = text.find("World")
print(index)  # Output: 7

# 9. str.startswith(prefix)
# Description: Checks if the string starts with the specified prefix. Returns True or False.
text = "Hello, World!"
result = text.startswith("Hello")
print(result)  # Output: True

# 10. str.endswith(suffix)
# Description: Checks if the string ends with the specified suffix. Returns True or False.
text = "Hello, World!"
result = text.endswith("World!")
print(result)  # Output: True

# Practical Application Example: Email Validation
# In real-world applications, you often need to validate email addresses.
# You can use string methods to check if the input meets certain criteria.

email = input("Enter your email: ").strip()

if email.find("@") != -1 and email.endswith(".com"):
    print("Valid email address.")
else:
    print("Invalid email address. Make sure it contains '@' and ends with '.com'.")

# Activity: Practice with String Methods
# 1. Create a string variable that contains your full name.
# 2. Use string methods to:
#    - Count the number of characters in your name (excluding spaces).
#    - Convert your name to uppercase and print it.
#    - Replace any part of your name (e.g., a nickname) with another string and print the result.
#    - Split your name into a list of words.
#    - Join the list back into a string with hyphens (-) as the separator.
# 3. Bonus Challenge: Write a function that takes a string and checks if it is a palindrome (reads the same backward as forward).
