'''
Write a program to read through the data/mbox-short.txt and figure out the line indexes (starting at zero) that contain emails. 
Every line that contains an email starts with "From ". 
Store the indexes in a list called indexes.
'''

indexes = []

with open('data/mbox-short.txt', 'r') as file:
    for line_index, line in enumerate(file):
        if line.startswith('From '):
            indexes.append(line_index)

print(indexes)

assert len(indexes) == 27, "It seems as you did filter out not every line index!"
assert indexes[2] == 130, "You filtered out a wrong line!"
assert indexes[-1] == 1837, "Your filtered out a wrong line!"