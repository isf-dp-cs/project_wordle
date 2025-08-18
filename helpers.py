from list_of_words import five_letter_words


def create_letter_ranking(word_list): 
    frequency_dictionary = {}

    for word in word_list:
        for letter in word:
            if letter not in frequency_dictionary:
                frequency_dictionary[letter] = 1
            else:
                frequency_dictionary[letter] += 1

    print(frequency_dictionary)
    sorted_freq = sorted(frequency_dictionary.items(), key=lambda x: x[1], reverse = True)
    
    letter_rank = []
    for item in sorted_freq:
        letter_rank.append(item[0])

    print(sorted_freq)
    return letter_rank

# rank = create_letter_ranking(five_letter_words)
# print(rank)
# print()

def score_words(letter_rank, word_list, current_word = None):
    words_to_score = {} 
    

    # do not score duplicate letter words
    for word in word_list:
        if len(set(word)) == len(word):
            words_to_score[word] = 0

    for word, score in words_to_score.items():
        for letter in set(word):
            words_to_score[word] += letter_rank.index(letter)

    # print(words_to_score)

    top_words = sorted(words_to_score.items(), key=lambda x: x[1])[0:20]
    return top_words

# print(score_words(rank, five_letter_words))


def get_possible_words(good_letters, bad_letters, word_list): 
    possible_words = []
    for word in word_list: 
 
        if set(good_letters).issubset(set(word)):
            count_bad = 0
            
            for letter in bad_letters: 
                if letter in word:    
                    count_bad += 1

            if count_bad == 0:
                possible_words.append(word) 

    return possible_words

print(get_possible_words('ig', 'swnapple', five_letter_words))
     
        