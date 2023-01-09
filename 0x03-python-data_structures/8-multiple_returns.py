#!/usr/bin/python3

# a function that returns a tuple with the length of a string and its
# first character
def multiple_returns(sentence):
    length = len(sentence)
    # If the sentence is empty, the first character should be equal to None
    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]
    tpl = (len(sentence), first)

    return tpl
