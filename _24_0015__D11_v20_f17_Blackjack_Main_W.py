# D11v20f15
import random, decimal, time

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

points_counter = 0

def playing_again():
    print(logo)
    print("The dealer dealt your first card")

    global points_counter
    continue_playing = True
    player_busted = False  # Flag to check if player has busted

    while continue_playing:
        drawn_random_card = random.randint(2, 14)

        if drawn_random_card == 1 or drawn_random_card == 11:
            face_card = "Ace"
            Ace_choice = int(input(f"Nice! You got an {face_card}. You can pick to add 1 or 11 to your total. (1 or 11): "))
            True_point_value = Ace_choice
            points_counter += True_point_value
        elif drawn_random_card >= 2 and drawn_random_card <= 10:
            print(f"\nYou got dealt a {drawn_random_card}")
            points_counter += drawn_random_card
        elif drawn_random_card == 12:
            print("\nYou got dealt a Jack")
            points_counter += 10
        elif drawn_random_card == 13:
            print("\nYou got dealt a Queen")
            points_counter += 10
        elif drawn_random_card == 14:
            print("\nYou got dealt a King")
            points_counter += 10

        if points_counter >= 22:
            print("Womp womp. You went over 21. Bust. You lose")
            player_busted = True
            break

        print(f"Your points so far this round is {points_counter}")

        Hit_or_Stay = input(f"Do you want to Hit or Stay? (H or S): ").upper()
        if Hit_or_Stay != "H":
            break

    # Computer's turn to play, only if player hasn't busted
    if not player_busted:
        computer_points_counter = 0
        cards_dealt_to_you_per_round = 0

        computer_continue_playing = True
        while computer_continue_playing == True:

            # def start_a_new_round():
            # Dealing of the cards:
            drawn_random_card = random.randint(2, 14)

            # Ace (use if other block doesn't work)
            # if drawn_random_card == 1:
            #     face_card = "Ace"
            #     print(f"You got dealt an {face_card}")
            #     Ace_choice = input("Please pick either 1 or 11 to apply to the total. (1 or 11): ")      #choose A.1 OR A.11
            #     if Ace_choice == 1:
            #         points_counter += 1
            #     elif Ace_choice == 11:
            #         points_counter += 11

            # for card_range_iteration in range(2-9):
            # 2
            # if drawn_random_card == card_range_iteration:
            #     face_card = card_range_iteration
            print("The dealer flips over their next card")
            time.sleep(1.5)
            if drawn_random_card == 1 or drawn_random_card == 11:
                face_card = "Ace"
                True_point_value = 11
                print(f"It drew an Ace. That's {True_point_value} points!")

                computer_points_counter += True_point_value
                if computer_points_counter >= 22:
                    print("Computer went over! You win!")
                    computer_continue_playing = False
                    continue_playing = False
                elif computer_points_counter >= 14 and computer_points_counter < 22:
                    print(f"The dealer points so far this round is {computer_points_counter}")
                    computer_continue_playing = True



            elif drawn_random_card == 2 or drawn_random_card == 3 or drawn_random_card == 4 or drawn_random_card == 5 or drawn_random_card == 6 or drawn_random_card == 7 or drawn_random_card == 8 or drawn_random_card == 9 or drawn_random_card == 10:
                print(f"\nIt got dealt a {drawn_random_card}")
                computer_points_counter += drawn_random_card
                if computer_points_counter >= 22:
                    print("Computer went over! You win!")
                    computer_continue_playing = False
                    continue_playing = False
                elif computer_points_counter >= 14 and computer_points_counter < 22:
                    print(f"The dealer points so far this round is {computer_points_counter}")
                    computer_continue_playing = True


            elif drawn_random_card == 12:
                face_card = "Jack"
                print(f"\nIt got dealt a {face_card}")
                computer_points_counter += 10
                if computer_points_counter >= 22:
                    print("Computer went over! You win!")
                    computer_continue_playing = False
                    continue_playing = False
                elif computer_points_counter >= 14 and computer_points_counter < 22:
                    print(f"The dealer points so far this round is {computer_points_counter}")
                    computer_continue_playing = True
            # TODO                # else: #missing this last statement ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            elif drawn_random_card == 13:
                face_card = "Queen"
                print(f"\nIt got dealt a {face_card}")
                computer_points_counter += 10
                if computer_points_counter >= 22:
                    print("Computer went over! You win!")
                    computer_continue_playing = False
                    continue_playing = False
                elif computer_points_counter >= 14 and computer_points_counter < 22:
                    print(f"The dealer points so far this round is {computer_points_counter}")
                    computer_continue_playing = True


            elif drawn_random_card == 14:
                face_card = "King"
                print(f"\nIt got dealt a {face_card}")
                computer_points_counter += 10
                if computer_points_counter >= 22:
                    computer_continue_playing = False
                    continue_playing = False
                elif computer_points_counter >= 14 and computer_points_counter < 22:
                    print(f"The dealer points so far this round is {computer_points_counter}")
                    computer_continue_playing = True
                elif computer_points_counter >= 17 and computer_points_counter < 22:
                    print(f"The dealer Stays at {computer_points_counter} points")
                    Hit_or_Stay = "S"
                    computer_continue_playing = False
                    if computer_continue_playing == False and Hit_or_Stay == "S":
                        if computer_points_counter > points_counter:
                            print(
                                f"The dealer beat you, score of {computer_points_counter} to your score of: {points_counter}")
                            print("Sorry but the dealer beat you with a higher score. Better luck next time.")
                            continue_playing = False
                            break
                        elif computer_points_counter == points_counter:
                            print("It looks like it's a Draw! You tied")
                            continue_playing = False

        if computer_points_counter >= 22:
            print("Bahahaha. The computer went Bust. What a loser it must be. Good job, human!")
            computer_continue_playing = False
            continue_playing = False
        else:
            print("Womp womp. You went over 21. Bust. You lose")
            player_busted = True
            game_on=True





if points_counter >= 22:
    print("Bust: Sorry, you lose.")
    # computer_continue_playing = False  #these 3 here and below are not needed
    # continue_playing = False
# else:
# Game Loop
game_on = True
while game_on:
    playing_again()
    # game_on = True
    while True:
        keep_playing = input(f"Do you want to play again? (Y or N): ").upper()
        if keep_playing == "Y" or keep_playing == "y":
            # global points_counter
            points_counter = 0
            # playing_again()
            break
            # continue_playing = True
        elif keep_playing == "N" or keep_playing == "n":
            # continue_playing = False
            print("Ok, thanks for playing! Have a great day! :)")
            game_on = False
            break
        else:
            print("Please enter 'Y' for Yes or 'N' for No.")

# playing_again()
