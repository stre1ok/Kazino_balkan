from random import *


def game_is_start():
    max_range_number = 999999 # Максимальное угадываемое число
    attempts = 0 # Количество угадываний числа
    number_of_attempts = 10000 # Количество попыток на ошибку
    print('Добро пожаловать в числовую угадайку')
    answer_for_range = input('Угадываем от 1 до 100 или до вашего числа?(Да/Нет)')
    
    def input_user_range_number_is_valid():
        # Ввод пользователем значения максимального диапазона угадывания. Проверка числа на целостность.
        user_range_number = input(f'Вводите своё максимальное число!(Максимально возможное число {max_range_number})')
        if user_range_number.isdigit() and 1 <= int(user_range_number) <= max_range_number:
            number_of_range = int(user_range_number)
            return number_of_range
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            return input_user_range_number_is_valid()
            
    if answer_for_range.lower() == 'да':
        number_of_range = input_user_range_number_is_valid()
        random_number = randint(1, number_of_range)  # Random number between 1 and user_range_number.
        print(f'Загадано случайное целое число от 1 до {number_of_range}. Попробуй угадать!')
    else:
        random_number = randint(1, 100)  # Random number between 1 and 100.
        print('Загадано случайное целое число от 1 до 100. Попробуй угадать!')

    def input_user_number_is_valid(number):
        # Проверка введённого пользователем числа на целостность.
        return number.isdigit() and 1 <= (int(number)) <= max_range_number   
    
    while True:
        player_number = input("Угадывай число: ")
        if input_user_number_is_valid(player_number):
            if int(player_number) == random_number:
                print(f'ВЫ ПОБЕДИЛИ!!! Количество попыток: {attempts}')
                again = input('Хотите сыграть ещё раз?(Да/Нет)')
                if again.lower() == 'да':
                    game_is_start()
                else:
                    break
            else:
                attempts += 1
                number_of_attempts -= 1
                print(f'Вы не угадали. Осталось попыток: {number_of_attempts}')
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            
game_is_start()            
