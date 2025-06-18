import random

def name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"

print("Welcome To The Game (Rock, Paper, Scissors)")
print("Choices are:\n1. Rock (Enter '1')\n2. Paper (Enter '2')\n3. Scissors (Enter '3')\n4. Exit (Enter '0')")
print("Total Rounds : 10")
print("Let's Begin")
try:
    round = 1
    total_1 = 0  # Player score
    total_2 = 0  # Computer score

    while round <= 10:
        print("\nRound:", round)
        choice = int(input("Enter Your Choice: "))
        
        if choice == 0:
            print("Let's Play Later")
            break

        if choice not in [1, 2, 3]:
            print("ERROR (Enter a number between 0 and 3)")
            continue

        computer_choice = random.randint(1, 3)

        print("Your Choice:", name(choice))
        print("My Choice:", name(computer_choice))

        if choice == computer_choice:
            print("Ahh! It's a tie.")
        elif (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 3) or (choice == 3 and computer_choice == 1):
            print("Yeah! I won.")
            print("Better luck next time, dude.")
            total_2 += 1
        else:
            print("You won!")
            total_1 += 1

        round += 1

    print("\nFinal Scores:")
    print("Your Score:", total_1)
    print("My Score:", total_2)

    if total_1 > total_2:
        print("Great, the luck is with you!")
    elif total_1 < total_2:
        print("Heee! You lose.")
    else:
        print("Wow! It's a tie overall.")

except ValueError:
    print("Enter only numbers (0–3)")
finally:
    print("Thank you for playing!")

    
