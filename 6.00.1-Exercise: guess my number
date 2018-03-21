low = 0
high = 100

mid = (high + low) //2
print('Please think of a number between 0 and 100!')
while True:
    print('Is your secret number %d?' %mid)
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if answer == 'c':
        print('Game over. Your secret number was: ' + str(mid))
        break
    elif answer == 'h':
        high = mid
    elif answer == 'l':
        low = mid
    else:
        print('Sorry, I did not understand your input.')
    mid = (high + low) //2
