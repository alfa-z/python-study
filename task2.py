#TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
number = int(input('Enter number: '))
if number%2==0 and number%4!=0:
    print('the number is even')
elif number%4==0:
      print('divisible by 4')
else:
        print('the number is odd')