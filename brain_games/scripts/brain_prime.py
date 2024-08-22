import random
import prompt


def is_prime(n):
    """Проверяет, является ли число простым."""

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def prime_games():
    """Проверяет, является ли число простым."""

    counter_answer = 0
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while counter_answer <= 2:
        n = random.randint(2, 1000)
        print('Question:', n)
        answer = prompt.string("Your answer: ")
        if is_prime(n) and answer == 'yes':
            print('Correct!')
            counter_answer = counter_answer + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{n}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


def main():
    prime_games()


if __name__ == "__main__":
    main()
