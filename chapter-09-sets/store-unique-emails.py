'''
Write a program to read through the data/mbox-short.txt and figure out a non-repeating collection of emails. 
You can pull the emails from lines that start with "From ".
'''

set_of_emails = set()

file_path = 'data/mbox-short.txt'

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('From '):
            words = line.split()
            email = words[1]
            set_of_emails.add(email)

for email in set_of_emails:
    print(email)

assert "gopal.ramasammycook@gmail.com" in set_of_emails, "You did not filter out all emails!"
assert "wagnermr@iupui.edu" in set_of_emails, "You did not filter out all emails!"
assert len(set_of_emails) == 11, "Your collection is not non-repeating!"
