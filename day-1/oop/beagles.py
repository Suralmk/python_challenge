import random

NUMBER_DIGITS = 3
MAX_GUESS = 10



def generate_secret_number():
    """Generates a secret number of digit NUMBER_DIGIT and returns it"""

    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNumber = ""
    for i in range(NUMBER_DIGITS):
        secretNumber += numbers[i]
    return secretNumber


def get_clues(guess, secret_num):
    """
        Returns pico, fermi and beagles
    """
    if guess == secret_num:
        return "You got the number!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")
    if len(clues) == 0:  return "Beagles"
    else: 
        clues.sort()
        return ' '.join(clues)

def beagles():

        while True:
            secret_num = generate_secret_number()
            print(f"You have {MAX_GUESS}")

            num_guess = 1
            while num_guess <= MAX_GUESS:
                guess = ""
                while len(guess) != NUMBER_DIGITS and not guess.isdecimal():
                    print(f"Guess #{num_guess}")
                    guess = input("-> ")
                
                clues = get_clues(guess, secret_num)
                print(clues)
                num_guess += 1

                if guess == secret_num:
                    break

                if num_guess > MAX_GUESS:
                    print("You run out of guesses")
                    break 

            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break

if __name__ == "__main__":
    beagles()