'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking or bad user data. Print your computed pay.
'''

hours_string = input("Enter hours: ")
hours_float = float(hours_string)

rate_per_hour_string = input('Enter hourly rate: ')
rate_per_hour_float = float(rate_per_hour_string)

gross_pay = hours_float * rate_per_hour_float

print('Gross pay:', gross_pay)