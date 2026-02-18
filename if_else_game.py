name = input('Enter your name: ')
print ('Hello',name,'. Welcome to my game!!')
should_we_play = input("Do you want to play? ").lower()

if should_we_play == 'yes' or should_we_play == 'y':
    print('we are going to play')
    #weapon = input('Choose a weapon(sword/axe): ').lower()
    direction = input('do you want to go left or right?(left/right) ').lower()
    if direction == "left" or direction == "l":
        print("You went left and fell off a cliff---game over, try again.")
    elif direction == 'right':
        print("WE GO RIGHT")
        choice = input("You now see a bridge. Do you want to cross it or swim under it?(swim/cross): ")
        if choice == 'swim':
            print("You got eaten by an alligator. Game over")
        else:
            print("You found the treasure.. You won the game!!")
    else:
        print("Sorry not a valid reply, END")
else:
    print("we are not playing...")