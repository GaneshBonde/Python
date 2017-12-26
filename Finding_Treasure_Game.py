from sys import exit
# Created by : Ganesh Bonde
# This program cannot be used for making commercial benefits.
# Contact me at ganeshbonde@gmail.com if you want to use it for commercial
# purposes.
# This method is the starting point of the Game.
def start():
    print("You are in a forest.")
    print("You can enter '1' to cross bridge")
    print("You can enter '2' to ride on a horse present on your left.")
    print("You can enter '3' to take boat on your right to search for the treasure. ")

    choice = input("> ")

    if choice == "1":
        cross_bridge()
    elif choice == "2":
        ride_horse()
    elif choice == "3":
        ride_boat()
    else:
        start()

# The player is next to the bridge. The player can either cross bridge or
# go back to forest.
def cross_bridge():
    print("You are on the bridge.")
    print("You can enter '1' to cross over the bridge and reach Castle.")
    print("You can enter '2' to go back in forest.")

    choice = input("> ")

    if choice == "1":
        entrance()
    else:
        start()

# This directs the player to entrance of the Castle.
def entrance():
    print("You are at the entrance of the Castle where treasure is hidden")
    print("Enter '1' to enter the Castle")
    print("Enter '2' to cross bridge and reach the forest.")

    choice = input("> ")

    if choice == "1":
        room2_entrance()
    else:
        cross_bridge()

# The player rides a boat in the sea.
def ride_boat():
    print("You are riding a boat in sea.")
    print("Enter '1' to keep riding in sea")
    print("Enter '2' to ride boat back towards forest.")

    choice = input("> ")

    if choice == "1":
        ride_boat2()
    else:
        start()

# This method directs the player to ride boat deep into sea and can
# redirect to forest.
def ride_boat2():
    print("You are riding a boat in sea.")
    print("Enter '1' to keep riding in sea")
    print("Enter '2' to ride boat back towards forest.")

    choice = input("> ")

    if choice == "1":
        ride_boat2()
    else:
        ride_boat()

# This method directs the player to ride boat deep into sea and can
# redirect to ride_boat2.
def ride_boat3():
    print("You are riding a boat in sea.")
    print("Enter '1' to keep riding in sea")
    print("Enter '2' to ride boat back towards forest.")

    choice = input("> ")

    if choice == "1":
        ride_boat4()
    else:
        ride_boat2()

# This method directs the player to ride boat deep into sea and can
# redirect ride_boat3 position.
def ride_boat4():
    print("You are riding a boat in sea.")
    print("Enter '1' to keep riding in sea")
    print("Enter '2' ride boat back towards forest.")

    choice = input("> ")

    if choice == "1":
        ride_boat4()
    else:
        ride_boat3()

#This method directs the player to ride horse in dessert
# or redirect towards forest.
def ride_horse():
    print("You are riding a horse in a dessert.")
    print("Enter '1' to keep riding in dessert")
    print("Enter '2' to ride horse towards forest.")

    choice = input("> ")

    if choice == "1":
        ride_horse2()
    else:
        start()

# This method directs the player to ride horse from position 2 of dessert
# to either position 1 or 3 of the dessert.
def ride_horse2():
    print("You are riding a horse in a dessert.")
    print("Enter '1' to keep riding in dessert")
    print("Enter '2' to ride horse towards forest.")

    choice = input("> ")

    if choice == "1":
        ride_horse3()
    else:
        ride_horse()

#This method directs the player to ride horse from position 3 of dessert
#to either position 2 or 4.
def ride_horse3():
    print("You are riding a horse in a dessert.")
    print("Enter '1' to keep riding in dessert")
    print("Enter '2' to ride horse towards forest.")

    choice = input("> ")

    if choice == "1":
        ride_horse4()
    else:
        ride_horse2()

# This method directs the player to ride horse from postion 4 of dessert
# to either postion 3 of dessert or side balcony of the Castle.
def ride_horse4():
    print("You are riding a horse in a dessert.")
    print("Enter '1' to access Castle from side entrance.")
    print("Enter '2' to ride horse towards forest.")

    choice = input("> ")

    if choice == "1":
        balcony_room4()
    else:
        ride_horse3()

# This method directs the player from room 1 and door 1 position.
# towards other rooms in the Castle.
def room1_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on left.")
    print("You can enter '2' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room8_door1()
    elif choice == "2":
        room2_door1()
    else:
        print("You are still in the same room.")
        room1_door1()

# This method directs the player from room 1 and door 2 position
# towards other rooms in the Castle.
def room1_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on right.")
    print("You can enter '2' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room2_door1()
    elif choice == "2":
        room8_door1()
    else:
        print("You are still in the same room.")
        room1_door2()

# This method directs the player from room 2 entrance position of the
# Castle into the Castle.
def room2_entrance():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to get outside Castle.")

    choice = input("> ")

    if choice == "1":
        room7_door1()
    elif choice == "2":
        room1_door1()
    elif choice == "3":
        room3_door1()
    elif choice == "4":
        entrance()
    else:
        print("You are still in the room.")
        room2_entrance()

# This method directs the player from room 2 and door 1 position
# towards other rooms in the Castle.
def room2_door1():
    print("This room is empty.")
    print("There are two doors.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room3_door1()
    elif choice == "2":
        room7_door1()
    elif choice == "3":
        room1_door1()
    else:
        print("You are stil in the same room.")
        room2_door1()

# This method directs the player from room 2 and door 2 position
# towards other rooms in the Castle.
def room2_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room1_door1()
    elif choice == "2":
        room7_door1()
    elif choice == "3":
        room3_door1()
    else:
        print("You are stil in the same room.")
        room2_door2()

# This method directs the player from room 2 and door 3 position
# towards other rooms in the Castle.
def room2_door3():
    print("This room is empty.")
    print("You can enter '1' to enter entrance point.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        entrance()
    elif choice == "2":
        room3_door1()
    elif choice == "3":
        room1_door1()
    elif choice == "4":
        room7_door1()
    else:
        print("You are stil in the same room.")
        room2_door3()

# This method directs the player from room 3 and door 1 position
# towards other rooms in the Castle.
def room3_door1():
    print("There is a bear in the room.")
    print("The bear has killed you.")
    print("Game Over")
    print("You can enter '1' to restart the game.")
    print("You can enter '2' to exit.")

    choice = input("> ")

    if choice == "1":
        start()
    elif choice == "2":
        exit()
    else:
        exit()

# This method directs the player from room 3 and door 2 position
# towards other rooms in the Castle.
def room3_door2():
    room3_door1()

# This method directs the player from room 4 and door 1 position
# towards other rooms in the Castle.
def room4_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        balcony_room4()
    elif choice == "2":
        room5_door1()
    elif choice == "3":
        room3_door2()
    else:
        print("You are stil in the same room.")
        room4_door1()

# This method directs the player from balcony of room 4
# towards other rooms in the Castle.
def balcony_room4():
    print("You are standing in a balcony.")
    print("There is a big dessert infront of you.")
    print("You cannot go in the dessert from the balcony.")
    print("You can enter '1' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room4_door2()
    else:
        print("You are stil in the balcony.")
        balcony_room4()

# This method directs the player from room 4 and door 2 position
# towards other rooms in the Castle.
def room4_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room3_door2()
    elif choice == "2":
        room5_door1()
    elif choice == "3":
        balcony_room4()
    else:
        print("You are still in the same room.")
        room4_door2()

# This method directs the player from room 4 and door 3 position
# towards other rooms in the Castle.
def room4_door3():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on right.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        balcony_room4()
    elif choice == "2":
        room3_door2()
    elif choice == "3":
        room5_door1()
    else:
        print("You are still in the same room.")
        room4_door3()

# This method directs the player from balcony of room 5
# towards other rooms in the Castle.
def balcony_room5():
    print("You are standing in a balcony.")
    print("There is a big dessert infront of you.")
    print("You cannot go in the dessert from the balcony.")
    print("You can enter '1' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room5_door3()
    else:
        print("You are stil in the balcony.")
        balcony_room5()

# This method directs the player from room 5 and door 1 position
# towards other rooms in the Castle.
def room5_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room12_door1()
    elif choice == "2":
        room6_door2()
    elif choice == "3":
        balcony_room5()
    else:
        print("You are still in the same room.")
        room5_door1()

# This method directs the player from room 5 and door 2 position
# towards other rooms in the Castle.
def room5_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        balcony_room5()
    elif choice == "2":
        room12_door1()
    elif choice == "3":
        room4_door3()
    else:
        print("You are still in the same room.")
        room5_door2()

# This method directs the player from room 5 and door 3 position
# towards other rooms in the Castle.
def room5_door3():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room6_door2()
    elif choice == "2":
        room4_door3()
    elif choice == "3":
        room12_door1()
    elif choice == "4":
        balcony_room5()
    else:
        print("You are still in the same room.")
        room5_door3()

# This method directs the player from room 5 and door 4 position
# towards other rooms in the Castle.
def room5_door4():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room4_door3()
    elif choice == "2":
        balcony_room5()
    elif choice == "3":
        room6_door2()
    elif choice == "4":
        room12_door1()
    else:
        print("You are still in the same room.")
        room5_door4()

# This method directs the player from room 6 and door 1 position
# towards other rooms in the Castle.
def room6_door1():
    print("There is a clue in this room to find a treasure.")
    print("The clue is that, ")
    print("the treasure is near the room having red bricks.")
    print()
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room5_door2()
    elif choice == "2":
        room11_door1()
    elif choice == "3":
        room7_door3()
    else:
        print("You are still in the same room.")
        room6_door1()

# This method directs the player from room 6 and door 2 position
# towards other rooms in the Castle.
def room6_door2():
    print("There is a clue in this room to find a treasure.")
    print("The clue is that, ")
    print("the treasure is near the room having red bricks.")
    print()
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room7_door3()
    elif choice == "2":
        room11_door1()
    elif choice == "3":
        room5_door2()
    else:
        print("You are still in the same room.")
        room6_door2()

# This method directs the player from room 6 and door 3 position
# towards other rooms in the Castle.
def room6_door3():
    print("There is a clue in this room to find a treasure.")
    print("The clue is that, ")
    print("the treasure is near the room having red bricks.")
    print()
    print("You can enter '1' to enter in the room on right.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room5_door2()
    elif choice == "2":
        room7_door3()
    elif choice == "3":
        room11_door1()
    else:
        print("You are still in the same room.")
        room6_door3()

# This method directs the player from room 7 and door 1 position
# towards other rooms in the Castle.
def room7_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on right.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room8_door2()
    elif choice == "2":
        room6_door1()
    elif choice == "3":
        room2_door3()
    else:
        print("You are still in the same room.")
        room7_door1()

# This method directs the player from room 7 and door 2 position
# towards other rooms in the Castle.
def room7_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room6_door1()
    elif choice == "2":
        room2_door3()
    elif choice == "3":
        room8_door2()
    else:
        print("You are still in the same room.")
        room7_door2()

# This method directs the player from room 7 and door 3 position
# towards other rooms in the Castle.
def room7_door3():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront of you.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room8_door2()
    elif choice == "2":
        room2_door3()
    elif choice == "3":
        room6_door1()
    else:
        print("You are still in the same room.")
        room7_door3()

# This method directs the player from room 8 and door 1 position
# towards other rooms in the Castle.
def room8_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on left.")
    print("You can enter '2' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room7_door2()
    elif choice == "2":
        room1_door2()
    else:
        print("You are still in the same room.")
        room8_door1()

# This method directs the player from room 8 and door 2 position
# towards other rooms in the Castle.
def room8_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on right.")
    print("You can enter '2' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room1_door2()
    elif choice == "2":
        room7_door2()
    else:
        print("You are still in the same room.")
        room8_door2()

# This method directs the player from room 9 and door 1 position
# towards other rooms in the Castle.
def room9_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on left.")
    print("You can enter '2' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room16_door1()
    elif choice == "2":
        room10_door1()
    else:
        print("You are still in the same room.")
        room9_door1()

# This method directs the player from room 9 and door 2 position
# towards other rooms in the Castle.
def room9_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on right`.")
    print("You can enter '2' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room10_door1()
    elif choice == "2":
        room16_door1()
    else:
        print("You are still in the same room.")
        room9_door2()

# This method directs the player from room 10 and door 1 position
# towards other rooms in the Castle.
def room10_door1():
    print("You have found the treaseure")
    print("The room is full of Diamonds, Gems and Gold.")
    print ("-----------------------------------")
    print ("-----------------------------------")
    print ("-----------------------------------")
    print("      Congratulations !!!!!!!!!!!!!!!!")
    print("      You Won   !!!!!!!!!!!!!!!!!!!!!!")
    print ("-----------------------------------")
    print ("-----------------------------------")
    print ("-----------------------------------")

# This method directs the player from room 11 and door 1 position
# towards other rooms in the Castle.
def room11_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront you.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room14_door1()
    elif choice == "2":
        room12_door2()
    elif choice == "3":
        room6_door3()
    else:
        print("You are still in the same room.")
        room11_door1()

# This method directs the player from room 11 and door 2 position
# towards other rooms in the Castle.
def room11_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on right.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room6_door3()
    elif choice == "2":
        room14_door1()
    elif choice == "3":
        room12_door2()
    else:
        print("You are still in the same room.")
        room11_door2()

# This method directs the player from room 11 and door 3 position
# towards other rooms in the Castle.
def room11_door3():
    print("This room is empty.")
    print("You can enter '1' to enter in the room on infront.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room6_door3()
    elif choice == "2":
        room12_door2()
    elif choice == "3":
        room14_door1()
    else:
        print("You are still in the same room.")
        room11_door3()

# This method directs the player from room 12 and door 1 position
# towards other rooms in the Castle.
def room12_door1():
    print("There is tiger in the room.")
    print("It has eatten you.........")
    print("Game Over")
    print("Enter '1' to restart the game.")
    print("Enter '2' to exit.")

    choice = input("> ")

    if choice == "1":
        start()
    elif choice == "2":
        exit()
    else:
        print("You are still in the same room.")
        room12_door1()

# This method directs the player from room 12 and door 2 position
# towards other rooms in the Castle.
def room12_door2():
    room12_door1()

# This method informs the player that he/she has fallen in the valley
# and the game is over.
def valley():
    print("After opening the door you saw a big valley.")
    print("You fell in the valley and have died`")
    print("Game Over")
    print("Enter '1' to restart the game.")
    print("Enter '2' to exit.")

    choice = input("> ")

    if choice == "1":
        start()
    elif choice == "2":
        exit()
    else:
        print("Game Over. Restarting the Game ..........")
        start()

# This method directs the player from room 13 and door 1 position
# towards other rooms in the Castle.
def room13_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room  infront.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        balcony_room13()
    elif choice == "2":
        valley()
    elif choice == "3":
        room14_door3()
    else:
        print("You are still in the same room.")
        room13_door1()

# This method directs the player from room 13 and door 2 position
# towards other rooms in the Castle.
def room13_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room  infront.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room14_door3()
    elif choice == "2":
        valley()
    elif choice == "3":
        balcony_room13()
    else:
        print("You are still in the same room.")
        room13_door2()

# This method directs the player from balcony of room 13
# towards other rooms in the Castle.
def balcony_room13():
    print("You are standing in a balcony.")
    print("There is a big dessert infront of you.")
    print("You cannot go in the dessert from the balcony.")
    print("You can enter '1' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room13_door2()
    else:
        print("You are stil in the balcony.")
        balcony_room13()

# This method directs the player from room 14 and door 1 position
# towards other rooms in the Castle.
def room14_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        valley()
    elif choice == "2":
        room15_door2()
    elif choice == "3":
        room13_door1()
    elif choice == "4":
        room11_door3()
    else:
        print("You are still in the same room.")
        room14_door1()

# This method directs the player from room 14 and door 2 position
# towards other rooms in the Castle.
def room14_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room13_door1()
    elif choice == "2":
        valley()
    elif choice == "3":
        room11_door3()
    elif choice == "4":
        room15_door2()
    else:
        print("You are still in the same room.")
        room14_door2()

# This method directs the player from room 14 and door 3 position
# towards other rooms in the Castle.
def room14_door3():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter in the room on left.")
    print("You can enter '4' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room15_door2()
    elif choice == "2":
        room11_door3()
    elif choice == "3":
        valley()
    elif choice == "4":
        room13_door1()
    else:
        print("You are still in the same room.")
        room14_door3()

# This method directs the player from room 15 and door 1 position
# towards other rooms in the Castle.
def room15_door1():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront.")
    print("You can enter '2' to enter in the room on right.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room14_door2()
    elif choice == "2":
        valley()
    elif choice == "3":
        room16_door2()
    else:
        print("You are still in the same room.")
        room15_door1()

# This method directs the player from room 15 and door 2 position
# towards other rooms in the Castle.
def room15_door2():
    print("This room is empty.")
    print("You can enter '1' to enter in the room infront.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room16_door2()
    elif choice == "2":
        valley()
    elif choice == "3":
        room14_door2()
    else:
        print("You are still in the same room.")
        room15_door2()

# This method directs the player from room 16 and door 1 position
# towards other rooms in the Castle.
def room16_door1():
    print("This room is full of red bricks.")
    print("You can enter '1' to enter in the room infront.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        valley()
    elif choice == "2":
        room15_door1()
    elif choice == "3":
        room9_door2()
    else:
        print("You are still in the same room.")
        room16_door1()

# This method directs the player from room 16 and door 2 position
# towards other rooms in the Castle.
def room16_door2():
    print("This room is full of red bricks.")
    print("You can enter '1' to enter in the room on right.")
    print("You can enter '2' to enter in the room on left.")
    print("You can enter '3' to enter room behind you.")

    choice = input("> ")

    if choice == "1":
        room9_door2()
    elif choice == "2":
        valley()
    elif choice == "3":
        room15_door1()
    else:
        print("You are still in the same room.")
        room16_door2()

# Calling start method to start the Game.
start()
