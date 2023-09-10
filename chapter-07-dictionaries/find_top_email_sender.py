'''
Write a program to read through the data/mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

sender_counts = {}

file_path = 'data/mbox-short.txt'

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('From '):
            words = line.split()
            sender = words[1]
            sender_counts[sender] = sender_counts.get(sender, 0) + 1

top_sender = None
max_count = 0

for sender, count in sender_counts.items():
    if count > max_count:
        top_sender = sender
        max_count = count

if top_sender is not None:
    print(f"The top sender is {top_sender} with {max_count} messages.")
else:
    print("No 'From ' lines found in the file.")