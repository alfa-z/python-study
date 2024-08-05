# Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .

while True: #used to run a condition continously until it is true
        num1 = input('Enter num1: ')
        num2 = input('Enter num2: ')

        if num1.isdigit() and num2.isdigit(): #isdigit is used to check if a number is integer
                num1 = int(num1)
                num2 = int(num2)
                sum = num1 + num2
                print(sum)
                break
        
        else:
                print('invalid character entered')