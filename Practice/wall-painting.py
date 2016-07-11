"""Wall Painting practice excercise"""
import math
SQ_FT_PER_GALLON = 400
total_sqft = 0.0  # has to be initialized or else we can't add to it later
again = True
while again:
    print('What is the width of your wall in feet? ')
    width = float(input())
    print('What is the height of your wall in feet')
    height = float(input())

    wall_sqft = width * height
    total_sqft += wall_sqft  # keeps a running total
    print('Do you wish to enter another wall?')
    selection = input()
    if selection == 'n':
        again = False

print('How much does the paint cost per gallon?')
price = float(input())
print('How many coats of paint do you want?')
coats_paint = int(input())
cost_dollars = math.ceil(total_sqft / SQ_FT_PER_GALLON) * price * coats_paint

print('It will cost ${:.2f}'.format(cost_dollars))
