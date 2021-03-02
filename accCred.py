import random


def nameGen():
    n = random.randint(0, 1000) # chooses random number between 0 and 100
    n * 10
    botName = "offworld." + str(n) # adds the generated number to the end of the name
    return botName

def passGen():
    n = random.randint(10000000, 1000000000) # chooses a random number between  10 thousand and 1 million
    passwd = str(n) + "AaAa$"
    return passwd
#* in the future make a better password thing using actual letters ?

def emailGen():
    botMail = nameGen() + "@outlook.com" # takes generated name and makes it an email
    return botMail

def toFile(email_valid, password_valid):
    with open('botEmails.txt', 'a+') as f:
        f.write(str(email_valid + "@outlook.com:" + password_valid + "\n"))