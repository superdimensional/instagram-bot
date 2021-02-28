import random


def nameGen():
    n = random.randint(0, 100) # chooses random number between 0 and 100
    n * 10
    botName = "offworld.agent." + str(n) # adds the generated number to the end of the name
    return botName

def passGen():
    n = random.randint(10000000, 1000000000) # chooses a random number between  10 thousand and 1 million
    return n
#* in the future make a better password thing using actual letters ?

def emailGen():
    botMail = nameGen() + "@gmail.com" # takes generated name and makes it an email
    return botMail
