'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly. 
Print your computed pay.
'''

# START YOUR CODE HERE.
hours_str = input("Enter hours worked: ")
hours = float(hours_str)

rate_str = input("Enter hourly rate: ")
rate = float(rate_str)

if hours <= 40:
    gross_pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * (1.5 * rate)
    gross_pay = regular_pay + overtime_pay

print('Gross pay:', gross_pay)