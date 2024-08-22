import random
import prompt


def calc_games():
    """Логика игры калькулятор"""

    arithmetic_signs = ['-', '+', '*']
    counter_answer = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    random_signs = arithmetic_signs[random.randint(0, 2)]
    result = 0

    while counter_answer <= 2:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        result = 0

        print('Question:', first_number, random_signs, second_number)
        answer = int(prompt.string('Your answer: '))
        if random_signs == '+':
            result = first_number + second_number
            if answer == result:
                counter_answer = counter_answer + 1
                print('Correct!')
        elif random_signs == '-':
            result = first_number - second_number
            if answer == result:
                counter_answer = counter_answer + 1
                print('Correct!')
        elif random_signs == '*':
            result = first_number * second_number
            if answer == result:
                counter_answer = counter_answer + 1
                print('Correct!')
        if answer != result:
            print(f"'{result}' is wrong answer ;(. Correct answer was '{answer}'.")
            print("Let's try again,", name + '!')
            break
    else:
        print('Congratulations,', name)


def main():
    calc_games()


if __name__ == "__main__":
    main()
