import random
import sys
from list_of_words import five_letter_words

# Get a random word from the list
secret_word = random.choice(five_letter_words)


# ANSI escape codes for colors
green_bg = "\033[42m"
yellow_bg = "\033[43m"
yellow_bg = "\u001b[48;5;226m"
grey_bg = "\033[47m"
reset = "\033[0m"

found = False
attempts = 0
max_attempts = 6

print("Enter a 5-letter word")

while attempts < max_attempts and not found:
    input_word = input()
    
    if input_word == secret_word:
        print("Well done! You guessed the word!")
        found = True
    else:
        output = ""
        for j in range(len(input_word)):
            guess_letter = input_word[j]
            formatted_letter = grey_bg + guess_letter + reset

            if secret_word[j] == guess_letter:
                formatted_letter = green_bg + guess_letter + reset
            else:
                for h in range(len(secret_word)):
                    if secret_word[h] == guess_letter:
                        formatted_letter = yellow_bg + guess_letter + reset
                        break
            output = output + formatted_letter
        
        print(output)
        attempts += 1

if not found:
    print("Sorry, you ran out of attempts. The word was: " + secret_word)