import random
class GuessingGame:
    def __init__(self):
        self.__secret_number = random.randint(1, 100)
    @property
    def secret_number(self):
        return self.__secret_number
    @property
    def attempts(self):
        return self.__attempts
    def reset_game(self):
        self.__secret_number = random.randint(1, 100)
        self.__attempts = 0

    def guess(self, user_guess):
        self.__attempts += 1
        if user_guess < self.__secret_number:
            return 'Число больше'
        elif user_guess > self.__secret_number:
            return 'Число меньше'
        else:
            return 'Вы угадали число!'

if __name__ == "__main__":
    game = GuessingGame()
    print(f'Число: {game.secret_number}')

    while True:
        user_input = int(input('Угадайте число от 1 до 100: '))
        result = game.guess(user_input)
        print(result)
        if result == 'Вы угадали число!':
            print(f'Количество попыток: {game.attempts}')
            break

    game.reset_game()
    print(f'Перезапуск игры! Новое число: {game.secret_number}')