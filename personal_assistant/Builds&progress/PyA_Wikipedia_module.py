##this is the wikipedia module alone

import wikipedia

while True:
    input = raw_input("Question: ")
    print wikipedia.summary(input, sentences = 2)
