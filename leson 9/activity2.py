# 1) Display a menu asking the user to select a ride
print("Select a ride:")
print("1 for Bike")
print("2 for Car")

# 2) Take the user’s input and store it in choice
choice = input("Enter your choice (1 or 2): ")

# 3) If choice is 1 (Bike)
if choice == "1":
    # a) Show bike options
    print("\n Bike Options:")
    print("1 for Scooty")
    print("2 for Scooter")
    # b) Take the user’s input for bike type
    choice2 = input("Enter bike type (1 or 2): ")
    # c) Print the selection
    if choice2 == "1":
        print("you have selected motercycle")
    else:
        print("you have selected scooter")

# 4) Else if choice is 2 (Car)
elif choice == "2":
    # a) Show car options
    print("\nCar Options:")
    print("1 for Sedan")
    print("2 for XUV")
    print("3 for SUV")
    print("4 for Luxury car")
    # b) Take the user’s input for car type
    choice3 = input("Enter car type (1, 2, 3 or 4): ")
    # c) Print the selection
    if choice3 == "1":
        print("you have selected sedan")
    elif choice3 == "2":
        print("you have selected xuv")
    elif choice3 == "3":
        print("you have selected suv")
    else:
        print("you have selected luxury car")

# 5) Else (if choice is not 1 or 2)
else:
    print("Wrong choice!")

 