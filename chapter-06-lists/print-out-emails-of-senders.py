'''
Open the file data/mbox-short.txt and read it line by line. 
When you find a line that starts with "From " like the following line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
Then print out a count at the end. 

Hint: make sure not to include the lines that start with "From:".
'''

number_of_emails = 0

file_path = 'data/mbox-short.txt'

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('From '):
            words = line.split()
            if number_of_emails + 1 < 10:
                print('Sender', number_of_emails + 1, ' :', words[1])
            else:
                print('Sender', number_of_emails + 1, ':', words[1])
            number_of_emails += 1

print("There were", number_of_emails, "lines in the file with 'From ' as the first word.")