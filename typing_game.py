from prompts import prompt_list                                 # imports prompt list from prompts.py 
from random import choice
from helpers import print_slow, calculate_wpm, calculate_accuracy, generate_prompt
from time import time

print("-"*50)
print("Welcome to the ISF Typing Game")                         # print welcome to the game
print("-"*50)

print("     1. You will see the prompt")                        # print rules
print("     2. The timer will start")
print("     3. Type the prompt as fast as you can")
print("     4. Click 'enter/return' when you are done.\n")
input("> Press `enter/return` to start the game! ")                    # user input any key to start game

print("-"*30)
print("The game will start in...")
print_slow("3...2...1!", .1)
print("-"*30,"\n")


#### 💻 YOUR CODE GOES HERE 💻 ####
## translate this pseudocode into Python code
## feel to change it to make the most sense to you
##   (you may delete it for an extra challenege)

# initialize the variable chosen_prompt and store a random prompt from  prompt_list 
# print chosen_prompt
# initialize the variable start_time and store the current time 
# initialize the variable user_input_prompt and store user input prompt typing attempt 
# initialize the variable end_time and store the current time 
# initialize the variable user_wpm and store the return value of calculated_wpm() 
# print user_wpm
