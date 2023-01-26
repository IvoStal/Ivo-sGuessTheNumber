import random
while True:

    computer_number = random.randint(1, 100)

    while True:
        player_number = input('The computer chose a number between 1 and 100. Try to guess it: ')

        if not player_number.isdigit():
            print('Please, stop kidding. Try again.')
        player_number = int(player_number)
        if player_number > computer_number:
            print('This number is too big, try again.')
        elif player_number < computer_number:
            print('This number is too small. Try again.')
        else:
            print('You nailed it! Congratulations!')
            choice = input('Do you want to play again? Type [y]es or [n]o: ')
            if choice == 'y':
                print('Here we go!')
                break
            elif choice == 'n':
                raise SystemExit('Have a nice day! See you next time!')
            else:
                raise SystemExit('Incorrect answer! Enough for today.')
