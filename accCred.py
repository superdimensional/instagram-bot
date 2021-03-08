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
                                            # TODO: in the future make a better password thing using actual letters ?

def emailGen():                             # takes generated name and makes it an email
    botMail = toEmail(nameGen())            # TODO: fix inconcistancy, it creates a name for an email that has a diffrent name!
    return botMail                          # TODO: add an input for the function and pass the name of the account through it

def toEmail(username):
    email = str(username) + "@outlook.com"
    return email

def emailToFile(email_valid, password_valid):                                      # ! deprecated 
    with open('credentials/botEmails.txt', 'a+') as f:
        f.write(str(toEmail(email_valid) + ":" + password_valid + "\n"))           # ! replaced by credToJson function 

def instaToFile(username_valid, password_valid):                                   # ! deprecated
    with open('credentials/botInsta.txt', 'a+') as f:                               
        f.write(str(username_valid + ":" + password_valid + "\n"))                 # ! replaced by credToJson function

def credToJSON(username_valid, password_valid):
    credentials = []
    credentials.append({
        'username':username_valid,
        'email':toEmail(username_valid),
        'password': password_valid
    })
    with open('credentials/botCred.json', 'a+') as outfile:
        json.dump(credentials, outfile)

def JSONToUsername(entryNumber):
    input_file = open ('credentials/botCred.json')
    json_array = json.load(input_file)
    store_list_username = []

    for item in json_array:
        stored_username = {"username":None}
        stored_username['username'] = item['username']
        store_list_username.append(stored_username)

    username_login = str(store_list_username[entryNumber])
    return username_login

def JSONToPassword(entryNumber):
    input_file = open ('credentials/botCred.json')
    json_array = json.load(input_file)
    store_list_password = []

    for item in json_array:
        stored_password = {"password":None}
        stored_password['password'] = item['password']
        store_list_password.append(stored_password)

    password_login = str(store_list_password[entryNumber])
    return password_login