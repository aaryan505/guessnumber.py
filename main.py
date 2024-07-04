import random
import log from art
def guess_num():
    return random.randint(1, 100)

def check_num(user_num, num):
    if user_num == num:
        print("You win!")
        return True
    elif user_num > num:
        print("Too high")
    else:
        print("Too low")
    return False

def clear():
    # Clear the screen for most terminal/console interfaces
    print("\033[H\033[J", end="")

def thegame():
    num = guess_num()
    difficulty = input("Choose a difficulty (easy or hard): ").lower()
    attempts = 10 if difficulty == "easy" else 5

    while attempts > 0:
        user_num = int(input("Guess a number between 1 to 100: "))
        is_right = check_num(user_num, num)
        if is_right:
            break
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left. Guess again.")
        else:
            print("You've run out of attempts. Better luck next time!")

print("Welcome to the Number Guessing Game!")

while True:
    thegame()
    again_play = input("Do you want to play again (y or n)? ").lower()
    if again_play != 'y':
        print("Thank you for playing!")
        break
    clear()
