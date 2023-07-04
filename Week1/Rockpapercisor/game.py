import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if choice in ['rock', 'paper', 'scissors', 'q']:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    draw_count = 0

    while True:
        print("\n--- New Round ---")
        user_choice = get_user_choice()

        if user_choice == 'q':
            break

        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")

        if user_choice == computer_choice:
            draw_count += 1
        else:
            winner = determine_winner(user_choice, computer_choice)
            if winner == "You win!":
                user_score += 1
            elif winner == "Computer wins!":
                computer_score += 1

        print(f"Result: {winner}")
        print(f"Score - You: {user_score} | Computer: {computer_score} | Draws: {draw_count}")

    print("\n--- Game Over ---")
    print(f"Final Score - You: {user_score} | Computer: {computer_score} | Draws: {draw_count}")

# Start the game
play_game()
