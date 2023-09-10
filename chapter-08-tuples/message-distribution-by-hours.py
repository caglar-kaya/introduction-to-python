'''
Write a program to read through the data/mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour in the following format: Hour: Count.
'''

hours_and_counts = {}

file_path = 'data/mbox-short.txt'

with open(file_path, 'r') as file:
    for line in file:
        if line.startswith('From '):
            words = line.split()
            time = words[5]
            hour = time.split(':')[0]
            hours_and_counts[hour] = hours_and_counts.get(hour, 0) + 1

sorted_hours_and_counts = sorted(hours_and_counts.items())

for hour, count in sorted_hours_and_counts:
    print(f"Hour: {hour} Count: {count}")