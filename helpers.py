import sys
import time
from random import choice, randint
from prompts import common_words

def print_slow(message,seconds):
    # prints one character at time from `message`
    # pauses for `seconds` in between each character

    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(seconds)
    sys.stdout.write('\n')


def calculate_wpm(user_typed_prompt, start_time, end_time):
    # returns the number of words per minute
    # rounds wpm to 1 decimal point 

    total_time_minutes = (end_time - start_time)/60             # calculates total time elapsed 
    user_total_keys_pressed = len(user_typed_prompt)            # stores length of total characters the user typed

    total_num_words = user_total_keys_pressed/5                 # calculated total number of words user typed
    wpm = total_num_words/total_time_minutes                    # calculates total words per minute typed

    return round(wpm,1)                                         # returns wpm rounded to 1 decimal point 


def calculate_accuracy(chosen_prompt, user_typed_prompt):
    # returns the accuracy of the user's input as a decimal
    # be sure to round the quotient to 1 decimal point
    #
    # 🤔 it's up to you to define accuracy 
    #       - is it how similar each letter is?
    #       - is it how similar each word is?
    #       - is it case sensitive? puncutation sensitive? 

    #### 💻 YOUR CODE GOES HERE 💻 ####


    return 





###### EXTENSION #######

def generate_prompt():
    # returns a prompt of random words
    # prompt should be a random length between 10-15 words 
    # (e.g. monday sound speed lose wall probable arrange make absolute department base thing)
    
    random_prompt = ""

    #### 💻 YOUR CODE GOES HERE 💻 ####



    return random_prompt
