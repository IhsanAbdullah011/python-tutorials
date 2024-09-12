age = 25

if age >= 0:
    if age < 2:
        print("Infant")
    elif age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 65:
        print("Adult")
    else:
        print("Senior")
else:
    print("Invalid age")

"""
activity 3: Text-Based Adventure Game

Description:
In this activity, you will create a simple text-based adventure game. The user will be presented
with different scenarios and given a few options to choose from. Each choice will affect the
progression of the story. The game should include at least 3 decision points with different
outcomes based on the user's input.

Instructions:
1. Start by setting the scene for the adventure.
2. Present the user with two or more options using input().
3. Based on the user's choice, display the next part of the story.
4. Continue the game until the user reaches an ending.

Example path one:

You find yourself in a dark forest. There's a path leading left and right.
Do you go left or right? (left/right): left

You encounter a wild wolf! Do you fight or run?
Do you fight or run? (fight/run): fight

You bravely fight off the wolf and continue on your journey! After a while, you come across a cave.
Do you enter the cave or keep walking? (enter/walk): enter

Inside the cave, you find a treasure chest! As you approach, you hear a noise behind you.
Do you open the chest or run away? (open/run): open

You open the chest and find it filled with gold and jewels! Congratulations, you've completed your adventure and found the treasure!

Example path 2:

You find yourself in a dark forest. There's a path leading left and right.
Do you go left or right? (left/right): right

You find a small village. The villagers invite you to rest. Do you accept or continue your journey? 
Do you rest or continue? (rest/continue): continue

You continue your journey, feeling tired but determined. After a while, you come across a steep mountain.
Do you climb the mountain or follow the valley path? (climb/follow): climb

As you reach the top, you are rewarded with a breathtaking view and discover an ancient artifact hidden in the rocks. You've completed your adventure and found a rare treasure!

"""