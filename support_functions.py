from contextlib import nullcontext

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
    for i in keys_list:
        if i in sentence:
            return database[i]



