# Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

Email = input('Enter email: ')
if '@' in Email and Email.endswith('.com'):
    print('Valid email')
else:
    print('invalid email')