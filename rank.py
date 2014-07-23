import math
# As I worked on a few examples, I noticed that the rank of a word can be
# determined by its relative rank to the strings that start with the same set
# of characters. For example, the rank difference between 'ab-cde' and 'ab-ced'
# is 1, while the rank difference between 'cde' and 'ced' is also 1, since the
# first 3 characters 'ab-' don't affect their relative rank. Therefore, this
# function calculates all the relative ranks for each index of the string
# relative to the first word in the dictionary, and the sum is the actual rank.


# Create dictionary to hold the numbers of repetition for all 'characters left'
# Each time take away one character from 'characters left' going left to right.
def enum(word):
    chars_num = {}
    for i in range(len(word)):
        if word[i] in chars_num:
            chars_num[word[i]] += 1
        else:
            chars_num[word[i]] = 1
    return chars_num


# Create dictionary to hold number of all 'characters left' that come before
# that character in the alphabet.
def index(left_chars):
    indexes = {}
    for current_char in left_chars.keys():
        char_index = 0
        for char in left_chars.keys():
            if (char < current_char):  # alphabetic comparison
                char_index += left_chars[char]
        indexes[current_char] = char_index
    return indexes


def permute(word, chars_left):  # number of all permutations for the string
    permutation = math.factorial((len(word)))
    for value in chars_left.values():  # now account for repeated characters
        permutation /= math.factorial(value)
    return permutation


# Main function that calculates the rank of a word among its permutations
def calculate_rank(word):
    chars_left = enum(word)
    char_indexes = index(chars_left)
    num_permutation = permute(word, chars_left)
    word_rank = 1  # First word in the dictionary has index 1
    num_chars = len(word)
    for i in range(len(word)):
        current = word[i]
        # word rank increased according to the 'current' character at index i
        # relative to the alphabetically first character at index i
        word_rank += num_permutation / num_chars * char_indexes[current]
        # permutation updated according to elimination of the 'current' char
        num_permutation *= chars_left[current]
        num_permutation /= num_chars
        # update characters left and character indexes
        chars_left[current] -= 1
        for char in char_indexes.keys():  # for loop inside for time efficiency
            if (char > current):
                char_indexes[char] -= 1
        num_chars -= 1
    return word_rank

# Input function depends on the python version! This one works for version 2.7.
USER_INPUT = raw_input("Please type in the word you want to rank: ")
print calculate_rank(USER_INPUT)
