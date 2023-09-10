'''
Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following scheme: 
>= 0.9 A; >= 0.8 B; >= 0.7 C; >= 0.6 D; < 0.6 F. 
For the test, enter a score of 0.85.
'''

while True:
    score_str = input("Enter a score between 0.0 and 1.0: ")

    try:
        score = float(score_str)
        if score < 0.0 or score > 1.0:
            raise ValueError  # Raise an error for out-of-range scores
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value between 0.0 and 1.0.")
        continue  # Prompt the user again

    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

    break  # Exit the loop when a valid score is provided
