""" Typing Test implementation """

from utils import *
from ucb import main
import simplejson as json

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
def lines_from_file(path):
    """
    Open txt and turn it into Stream
    Content:(list of String)
    content can be saved by readlines(stream)
    Remove the trailing and leading white space
    """
    file = open(path)
    content = readlines(file)
    return [strip(x) for x in content]

def new_sample(path, i):
    """
    Return String from the list
    """
    assert i >= 0
    return lines_from_file(path)[i]

def analyze(samp, typed, start, end):

    def w_per_m(samp, typed, start, end):

        time_used = (end - start) / 60
        num_char = len(typed)
        res = (num_char / 5) / time_used

        return res

    def accuracy(samp, typed):
        samp_list = split(samp)
        typed_list = split(strip(typed))

        len_samp = len(samp_list)
        len_typed = len(typed_list)

        if len_typed == 0:
            return 0.0


        if len_typed >= len_samp:
            i = 0
            count = 0
            while i < len_samp:
                if samp_list[i] == typed_list[i]:
                    count += 1
                i += 1
            return count / len_samp * 100
        elif len_typed < len_samp:
            i = 0
            count = 0
            while i < len_typed:
                if samp_list[i] == typed_list[i]:
                    count += 1
                i += 1
            return count / len_typed * 100

    return [w_per_m(samp, typed, start, end), 
    accuracy(samp, typed)]

# Q3

# def pig_latin(word):

#     # First letter
#     def is_vowel(s):
#         if s == 'a' or s == 'e' or s =='i' or s == 'o' or s == 'u':
#             return True
#         else:
#             return False

#     # First letter
#     def is_consonant(s):
#         return not is_vowel(s)

#     # Check if contain vowel
#     def contain_vowel(s):
#         return 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s


#     if is_vowel(word[0]):
#         return word + 'way'
#     elif contain_vowel(word):
#         for i in range(len(word)):
#             if is_vowel(word[i]):
#                 return word[i:] + word[:i] + 'ay'
#     else:
#         return word + 'ay'




# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6
    
    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________ 
        substitute_char = ______________ 
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8
