#Python functions
#it allows you to create blocks of code to be re-used.
#perform a specific task
#it takes in some input of data
#performs some operation on the data
#returns the output
#examples of input function;
#*print() => display data in the terminal
#*input() => input the data of the user
#*int
#*range
#*float
#*str

#custom function
#begin with a key wor def then name of the function e.g login,()
#To form a block of code in python, we need a full colon (:)
#then it must be indented.
#the function cannot be executed unless it has been called.
#a function is called by a name ()

#parameters => variables used inside a function (for reusing a function)

#arguments => are exact values passed into a function when calling

def hello():
    name = 'Ojijo'
    print(f'Hello {name}')

hello() #cannot be shown on the terminal because it is not called i.e it is not inside the indentation


#create a function to calculate the area of a triangle.
def area_triangle():
    base = 20
    height = 10
    area = (base*height)*0.5
    print(area)

area_triangle() #calling the function


#create a function that calculates the area of a rectangle take users input.

def area_rectangle():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    area = length*width
    print(area)

area_rectangle()

# create a function that takes input from a user of a num and checks if a number is even number or odd number

def even_num():
    num = int(input('Enter number: '))
    if num%2==0:
        print('even')
    else:
            print('odd')
even_num()


#Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

def phone_number():
     number = input('Enter phone number: ')
     if 9<= len(number) <= 13:
         if number.startswith('+254') or number.startswith('254') or number.startswith('07') or number.startswith('7') or number.startswith('01') or number.startswith('1'):
             print('+254' + number.lstrip('+254').lstrip('254').lstrip('07').lstrip('7').lstrip('01').lstrip('1'))
         else:
            print('Incorrect format')
     else:
        print('invalid')
phone_number()


#Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.

def car_speed():
    speed = int(input('Enter speed: '))
    speed_limit = 70
    if speed <=70:
        print('ok')
    else:
        demerit_points = (speed - speed_limit) / 5
        demerit_points = int(demerit_points)
        if demerit_points<=12:
            
            print(f'{demerit_points} demerit points')
        else:
                print('license suspended')
car_speed()


# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.

def prods():
    prods = [['omo','30kshs','300'], ['milk','50kshs','200'],['bread','45kshs','359'], ['coffee','5kshs','79']]
    total_stock = 0
    for i in prods:
        total_stock += int(i[-1])
    print(f'total_stock {total_stock}')  #print outside the loop
prods()




#task 3, 8, 10, 12, 13