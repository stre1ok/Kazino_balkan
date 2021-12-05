from random import *

print('Добро пожаловать в числовую угадайку')
random_number = randint(1, 100)  # Random number between 1 and 100.
print('Загадано случайное целое число от 1 до 100. Попробуй угадать!')

def is_valid(number):
    # Проверка введённого числа на целостность.
   return number.isdigit() and 1 <= (int(number)) <= 100

while True:
    player_number = input("Ну чо:")
    if is_valid(player_number):
        player_number = int(player_number)
        print(player_number)
        break
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

# just for test


