import support_functions

################## Test case 1
your_result = support_functions.get_greetings("John")
expected_result = "Greetings John! I am Avery. How may I help?"

if your_result == expected_result:
    print("Test case 1 correct!")
else:
    print("Test case 1 not correct!")


################## Test case 2
sentence = "What is the First?"
lines_of_code = []
database = {"first": "Alpha", "second": "Beta", "third": "Gamma", "None of the above": "Nothing"}

your_result = support_functions.get_reply(sentence, lines_of_code, database)
expected_result = "Alpha"

if your_result == expected_result:
    print("Test case 2 correct!")
else:
    print("Test case 2 not correct!")


################## Test case 3
sentence = "What is the fourth?"
lines_of_code = []
database = {"first": "Alpha", "second": "Beta", "third": "Gamma", "None of the above": "Nothing"}

your_result = support_functions.get_reply(sentence, lines_of_code, database)
expected_result = "Nothing"

if your_result == expected_result:
    print("Test case 3 correct!")
else:
    print("Test case 3 not correct!")


################## Test case 4
sentence = "run"
lines_of_code = ["i = 5", "j = 6", "print(i+j)"]
database = {"first": "Alpha", "second": "Beta", "third": "Gamma", "None of the above": "Nothing"}

your_result = support_functions.get_reply(sentence, lines_of_code, database)
expected_result = "11\n"

if your_result == expected_result:
    print("Test case 4 correct!")
else:
    print("Test case 4 not correct!")
