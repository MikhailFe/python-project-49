import prompt
import random



def is_nimber_even():
    "Функция, котороя проверяет является ли чсило четным"
    
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter_answer = 0

    while counter_answer <= 2:
        random_number = random.randint(1, 100)
        print('Question:', random_number)
        answer = prompt.string('Your answer: ')

        if (answer == 'yes' and random_number % 2 == 0) or \
           (answer == 'no' and random_number % 2 != 0):
            counter_answer = counter_answer + 1
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


def main():
    is_nimber_even()


if __name__ == "__main__":
    main()
