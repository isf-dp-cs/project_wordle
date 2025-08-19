# python word_finder.py good_words bad_words

from list_of_words import five_letter_words
import sys 

def get_possible_words(good_letters, bad_letters, word_list): 
    # finish this function

    return


if __name__ == "__main__":
    good_letters = ""
    bad_letters = ""

    if len(sys.argv) == 3:
        good_letters = sys.argv[1]
        bad_letters = sys.argv[2]

    possible_words = get_possible_words(good_letters, bad_letters, five_letter_words)

    print(possible_words)
     
        