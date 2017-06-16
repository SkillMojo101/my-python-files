##this is the wolframalpha module alone.

import wolframalpha

while True:
    input = raw_input("Question: ")
    app_id = "J8URQW-98EAUPHG7G"
    client = wolframalpha.Client(app_id)
    res = client.query(input)
    answer = next(res.results).text
    print answer
