import runcode
#Jack Chidlaw: Greet user, include name in greeting if it is given.
def get_greetings(name):
    if name == "":
        return "Greetings!"
    else:
        return "Greetings "+ str(name) + "! I am Avery. How may I help?"

#Jack Chidlaw: get all the keys from the database dict, check if keyword is in sentence and if so return element from database using found keyword
def get_reply(sentence, lines_of_code, database):
    keys = database.keys()
    keys_list = list(keys)
    j = 0
    if sentence == "code" or lines_of_code != [] and sentence != "run":
        return ""
    elif sentence == "run":
        return runcode.run(lines_of_code)
    else:
        sentence = sentence.lower()
        sentence_no_punc = ""
        for char in sentence:
            # Check if the character is not a punctuation mark (using a simple list of punctuation marks)
            if char not in ".,!?;:'\"()[]{}<>-_/$@#%^&*":
                sentence_no_punc += char

        for i in keys_list:
            if i in sentence_no_punc.split():
                j += j
                return database[i]
        if j != 1:
            return database["None of the above"]





