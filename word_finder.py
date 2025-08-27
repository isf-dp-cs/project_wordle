from list_of_words import five_letter_words
import sys 

def get_possible_words(good_letters, bad_letters, word_list): 
    possible_words = set()
    for word in word_list: 
 
        if set(good_letters).issubset(set(word)):
            count_bad = 0
            
            for letter in bad_letters: 
                if letter in word:    
                    count_bad += 1

            if count_bad == 0:
                possible_words.add(word) 

    return possible_words


if __name__ == "__main__":
    possible_words = get_possible_words(sys.argv[1], sys.argv[2], five_letter_words)
    print(possible_words)
     
        