from random import randint
import art

Easy_Turn = 10
Hard_Turn = 5

# function to check user's guess against actual number

def check_answer(user_guess,actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too High!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it!, the answer is {actual_answer}")



# function to set difficulty
def set_difficulty():
    guess_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if guess_difficulty == "easy":
        return Easy_Turn
    else:
        return Hard_Turn


def game():
    print(art.logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a umber between 1 and 100.")
    answer = randint(1,100)
    print(f"pass the correct answer {answer}")



    # let the user guess the number
    turns = set_difficulty()


    # repeat the guessing functionality if they get it wrong
    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("Make a Guess: "))

        # track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != answer:
            print("Guess again.")


game()




