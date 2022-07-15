#Limit the number of guesses
#catch when somone submits a non-integer value
#print "too high" or "too low" messages for bad gusses
#Let ppl play again.
import random

#generate a random number between 1 and 10
secret_number = random.randint(1,10)


def run_game():

    guesses =[]
    guess = 0

    while True:
        #safely make an int
        try:
            #get a number guess from player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number! ".format(guess))
        else:

            #compare guess with secret number
            if guess == secret_number:
            #print hit/miss
                print("You Win! my number was {}".format(secret_number))
                break
            elif guess < secret_number:
                print("My number is higher than {}".format(guess))
            elif guess > secret_number:
                print("My number is lower than {}".format(guess))
            else:
            #print hit/miss
                print("No")
        guesses.append(guess)

    else:
        print("You didn't get it! My number was {}".format(secret_number))

    play_again = input("Do you want to play again? [Y/n]")
    if play_again.lower() != 'n':
        run_game()
    else:
        print("Bye!")
    play_again = input("DO you want to play again? [Y/n]")
    if play_again.lower() != 'n':
        run_game()
    else:
        print("Bye!")
run_game()




            

    

