def adventure_game():
    print("You find yourself in a dark forest. There's a path leading left and right.")
    choice1 = input("Do you go left or right? (left/right): ")

    if choice1 == "left":
        print("\nYou encounter a wild wolf! Do you fight or run?")
        choice2 = input("Do you fight or run? (fight/run): ")

        if choice2 == "fight":
            print("\nYou bravely fight off the wolf and continue on your journey!")
            print("After a while, you come across a cave.")
            choice3 = input("Do you enter the cave or keep walking? (enter/walk): ")

            if choice3 == "enter":
                print("\nInside the cave, you find a treasure chest!")
                print("As you approach, you hear a noise behind you.")
                choice4 = input("Do you open the chest or run away? (open/run): ")

                if choice4 == "open":
                    print("\nYou open the chest and find it filled with gold and jewels!")
                    print("Congratulations, you've completed your adventure and found the treasure!")
                else:
                    print("\nYou ran away, missing out on what could have been a great treasure. The adventure ends.")
            else:
                print("\nYou walk past the cave and continue your journey, but find nothing exciting.")
                print("The adventure ends uneventfully.")

        else:
            print("\nYou run away from the wolf, escaping into the forest.")
            print("The adventure ends here, without any great discoveries.")
    
    elif choice1 == "right":
        print("\nYou find a small village. The villagers invite you to rest.")
        choice2 = input("Do you rest or continue your journey? (rest/continue): ")

        if choice2 == "rest":
            print("\nYou rest with the villagers and enjoy their hospitality.")
            print("After a peaceful night, your journey ends, but you feel content.")
        else:
            print("\nYou continue your journey, feeling tired but determined.")
            print("After a while, you come across a steep mountain.")
            choice3 = input("Do you climb the mountain or follow the valley path? (climb/follow): ")

            if choice3 == "climb":
                print("\nAs you reach the top, you are rewarded with a breathtaking view.")
                print("You discover an ancient artifact hidden in the rocks!")
                print("Congratulations, you've completed your adventure and found a rare treasure!")
            else:
                print("\nYou follow the valley path, but nothing remarkable happens.")
                print("The adventure ends quietly.")

    else:
        print("\nInvalid choice. Please start again.")

# Run the game
adventure_game()
