computer_choice = "rock"
user_choice = input("Enter rock, paper, or scissors: ") 

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("You lose! Paper covers rock.")
    else:
        print("You win! Rock crushes scissors.")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("You lose! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("You lose! Rock crushes scissors.")
    else:
        print("You win! Scissors cut paper.")