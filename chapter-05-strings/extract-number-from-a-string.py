'''
Write code using find() and string slicing to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475"

colon_index = text.find(':')

number_string_with_spaces = text[colon_index + 1 : ]    # '    0.8475'

number_string_without_spaces = number_string_with_spaces.strip()    # '0.8475'

number = float(number_string_without_spaces)    # 0.8475

print(number)