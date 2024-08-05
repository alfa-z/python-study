# Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.

# Password = input('Enter Password: ')
# correct_password = 'admin@123'
# attempts = 4

# for i in range(attempts):
#     if Password == correct_password:
#         print('Access Granted')
#         break
#     else:
#         remaining_attempts = attempts - (i+1)
#         if remaining_attempts==3:
#             print(f'Incorrect password. {remaining_attempts} attempts left.')
#             if remaining_attempts==2:
#                 print(f'Incorrect password. {remaining_attempts} attempts left.')
#         else:
#                 print('Account is blocked')
        

correct_password = 'admin@123'
attempts = 4

# Loop for the number of attempts
for i in range(attempts):
    password = input('Enter Password: ')  
    
    if password == correct_password:
        print('Access Granted')
        break  # Exit the loop if the password is correct
    else:
        remaining_attempts = attempts - (i + 1)  # Calculate remaining attempts
        if remaining_attempts > 0:
            print(f'Incorrect password. You have {remaining_attempts} attempts left.')
        else:
            print('Account is blocked.')  # Block account after 4 incorrect attempts