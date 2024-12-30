import random

Random_food_generator = random.randint(1,8)
Food_choices = ''

if Random_food_generator == 1:
    Food_choices = 'Chick fil a'
if Random_food_generator == 2:
    Food_choices = 'Tacobell'
if Random_food_generator == 3:
    Food_choices = 'Dominos'
if Random_food_generator == 4:
    Food_choices = 'Chipotle'
if Random_food_generator == 5:
    Food_choices = 'Pdq'
if Random_food_generator == 6:
    Food_choices = 'Papa johns'
if Random_food_generator == 7:
    Food_choices = 'Popeyes'
if Random_food_generator == 8:
    Food_choices = 'Subway'
print(Food_choices)