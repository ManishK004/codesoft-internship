import random
def guessing_game():

    print("\nROCK , PAPER , SCISSORS GAME")

    items=["paper","rock","scissor"]

    r=random.choice(items)
    attempts=0
    while True:
        user_choice=input("enter your choice").lower()
        if user_choice =="exit":
            print("game ended!")
            break

        elif user_choice== r:
            print("congratulations you won")
            print(f"you won the game by guessing correct output {user_choice} and in {attempts+1} attempts\n")
            play_again = input("if you want to play again, enter 'yes',else type 'exit' to quit:").lower()


            if play_again !='yes':
                   print("thank you")
            else:
                   guessing_game()
        else:
            print("try again")

            attempts=attempts+1


guessing_game()