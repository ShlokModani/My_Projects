import random

def main() :
    choices = ["rock", "paper", "scissors"]
    wins = losses = draws = 0

    print("\n---- Rock Paper Scissors ----")

    while True :
        player = input(
            "\nChoose rock, paper, scissors (or quit) : "
        ).strip().lower()

        if player == "quit" :
            break

        if player not in choices :
            print("Invalid choice. Try again.")
            continue

        computer = random.choice(choices)
        print("Computer chose:", computer)

        if player == computer :
            print("It's a draw!")
            draws += 1
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print("You win!")
            wins += 1
        else :
            print("Computer wins!")
            losses += 1

        print(f"Score: Wins={wins}, Losses={losses}, Draws={draws}")

    print("\nFinal score : ")
    print(f"Wins : {wins} | Losses : {losses} | Draws : {draws}")

if __name__ == "__main__" :
    main()