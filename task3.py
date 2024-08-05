#TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”


number = input('Enter phone number: ')
if 9<= len(number) <= 13:
    if number.startswith('+254') or number.startswith('254') or number.startswith('07') or number.startswith('7') or number.startswith('01') or number.startswith('1'):
        print('+254' + number.lstrip('+254').lstrip('254').lstrip('07').lstrip('7').lstrip('01').lstrip('1')) #string.lstrip removes characters from the left
    else:
        print('Phone number does not start with the expected prefix.')
else:
    print('invalid number')