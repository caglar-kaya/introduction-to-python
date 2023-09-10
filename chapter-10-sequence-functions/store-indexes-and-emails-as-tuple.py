'''
Write a program to read through the data/mbox-short.txt and figure out emails as well as their line indexes. 
Lines that contain emails start with "From ". 
Store the pairs in a list of tuples named pairs that have the format (index, email). 
Sort this list with regard to the emails in alphabetical order.
'''

pairs_of_index_and_email = []

with open('data/mbox-short.txt', 'r') as file:
    for index, line in enumerate(file):
        if line.startswith('From '):
            words = line.split()
            email = words[1]
            pairs_of_index_and_email.append((index, email))
            
pairs_of_index_and_email = sorted(pairs_of_index_and_email, key = lambda x: x[1])

print(pairs_of_index_and_email)

assert len(pairs_of_index_and_email) == 27, "It seems as you did not filter out every pair!"
assert pairs_of_index_and_email[2][0] == 493, "You filtered out a wrong pair!"
assert pairs_of_index_and_email[-1][0] == 904, "Your filtered out a wrong pair!"