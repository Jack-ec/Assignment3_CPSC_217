from contextlib import nullcontext

#Jack Chidlaw: Greet user, include name in greeting if it is given.
def get_greetings(name):
    if name == "":
        return "Greetings!"
    else:
        return "Greetings "+ str(name) + "! I am Avery. How may I help?"
    