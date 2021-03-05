import random
import json

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

def emailGen():                             # takes generated name and makes it an email
    botMail = nameGen() + "@outlook.com"    # TODO: fix inconcistancy, it creates a name for an email that has a diffrent name!
    return botMail                          # TODO: add an input for the function and pass the name of the account through it

def emailToFile(email_valid, password_valid):                                       # TODO: change from using .txt to .json
    with open('botEmails.txt', 'a+') as f:
        f.write(str(email_valid + "@outlook.com:" + password_valid + "\n"))

def instaToFile(username_valid, password_valid):
    with open('botInsta.txt', 'a+') as f:
        f.write(str(username_valid + ":" + password_valid + "\n"))