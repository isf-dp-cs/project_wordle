import random

def wordle():
    """
    A basic command-line Wordle game.
    """
    try:
        with open("words5.txt", "r") as f:
            all_words = f.readlines()
    except FileNotFoundError:
        print("Error: 'words5.txt' not found.")
        return

    five_letter_words = []
    for line in all_words:
        word = line.strip()
        if len(word) == 5:
            five_letter_words.append(word.lower())
    
    if not five_letter_words:
        print("Error: 'words5.txt' does not contain any 5-letter words.")
        return

    # Select a random word from the list
    secret_word = random.choice(five_letter_words)

    # ANSI escape codes for colors
    green_bg = "\033[42m"  # Green background
    yellow_bg = "\033[43m" # Yellow background
    grey_bg = "\033[47m"   # Grey background
    reset = "\033[0m"      # Reset colors

    print("Welcome to Wordle! Try to guess the 5-letter word.")
    print("You have 6 attempts.")

    for attempt in range(1, 7):
        guess = input(f"\nAttempt {attempt}: ").strip().lower()

        # Input validation
        while len(guess) != 5 or not guess.isalpha():
            guess = input("Please enter a valid 5-letter word: ").strip().lower()

        if guess == secret_word:
            print(f"Congratulations! You guessed the word: {secret_word.upper()}")
            break

        feedback = ""
        secret_word_list = list(secret_word)
        guess_list = list(guess)
        
        # First pass: Check for green letters (correct letter in the correct position)
        for i in range(5):
            if guess_list[i] == secret_word_list[i]:
                feedback += f"{green_bg}{guess_list[i].upper()}{reset}"
                secret_word_list[i] = None # Mark as checked to handle duplicates
                guess_list[i] = None
        
        # Second pass: Check for yellow and grey letters
        for i in range(5):
            if guess_list[i] is not None:
                if guess_list[i] in secret_word_list:
                    feedback += f"{yellow_bg}{guess_list[i].upper()}{reset}"
                    # Mark the first occurrence of the letter as checked in the secret word list
                    secret_word_list[secret_word_list.index(guess_list[i])] = None
                else:
                    feedback += f"{grey_bg}{guess_list[i].upper()}{reset}"
        
        print(feedback)

    else: # This block executes if the loop finishes without a 'break'
        print(f"\nSorry, you're out of attempts. The word was {secret_word.upper()}.")

if __name__ == "__main__":
    wordle()