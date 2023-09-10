'''
Open the file data/romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
'''

unique_words = []

file_path = 'data/romeo.txt'

with open(file_path, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word not in unique_words:
                unique_words.append(word)

unique_words.sort()

for word in unique_words:
    print(word)
