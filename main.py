import random

def roll_dice():
    no = random.randint(1, 6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[ 0   ]")
        print("[  0  ]")
        print("[   0 ]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[ 0 0 ]")
        print("[  0  ]")
        print("[ 0 0 ]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[ 0 0 0 ]")
        print("[       ]")
        print("[ 0 0 0 ]")
        print("[-----]")

# Main loop
while True:
    print("\n1. Roll the dice")
    print("2. Exit")
    choice = input("What do you want to do? Enter 1 or 2: ")

    if choice == "1":
        roll_dice()
    elif choice == "2":
        print("Exiting the Dice Simulator.")
        break
    else:
        print("Invalid input. Please enter 1 or 2.")
