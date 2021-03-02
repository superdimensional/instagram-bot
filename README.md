# PLAN:

### 1) Create outlook email
### 2) Print email credentials to "emailToFile.txt"
### 3) Use emails from "emailToFile.txt" to create instagram account
### 4) Print insta account credentials to "instaToFile.txt"
### 5) Use insta credentials to sign in 

# Function of each file:

"outlookEmail.py" makes emails and prints the output to file "botEmails.txt".
"accCred.py" is just a module I have created to generate usernames, passwords, and emails.
It also contains the function to write <email>:<password> combos.
"createAcc.py" creates instagram accounts.
"insta.py" takes the accounts created and signs into them and does an action in instagram.
