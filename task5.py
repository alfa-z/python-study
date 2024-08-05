# Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
num1 = input('Enter num1: ')
num2 = input('Enter num2: ')
num3 = input('Enter num3: ')
if num1>num2 and num1>num3:
    print(f'The largest is {num1}')
elif num2>num1 and num2>num3:
    print(f'The largest is {num2}')
else:
            print(f'The largest is {num3}')