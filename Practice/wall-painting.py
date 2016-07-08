"""Wall Painting practice excercise"""
import math

cost = 0
totalarea = 0.0
again = True
while again == True:
    print('What is the width of your wall in feet? ')
    width = float(input())
    print('What is the height of your wall in feet')
    height = float(input())



    area = width * height
    totalarea = totalarea + area
    print('Do you wish to enter another wall?')
    selection = input()
    if selection == 'n':
        again = False
        break
    else:
        again == True

print('How much does the paint cost per gallon?')
price = float(input())
print('How many coats of paint do you want?')
coats = int(input())
cost = cost +math.ceil(totalarea/400) * price* coats

print('It will cost $' + str(cost))
