##this is the "functional" scrpit, no GUI jargon.

import wikipedia
import wolframalpha

while True:
    input = raw_input("Q: ")

    try:
        #wolfram
        app_id = "J8URQW-98EAUPHG7G"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer

    except:
        #wiki
        print wikipedia.summary(input)#, sentences = 2)
