import random


def generate_progression():
    """Генерация случайного списка."""

    a = random.randint(0, 10)
    d = random.randint(0, 10)
    n = random.randint(5, 15)
    return [a + i * d for i in range(n)]


def arithmetic_progression_game():
    """Логика арифметической последовательности."""

    # print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('What number is missing in the progression?')
    counter_answer = 0

    while counter_answer <= 2:
        sequence = generate_progression()
        new_value = '..'
        remove_value = random.choice(sequence)
        index = sequence.index(remove_value)
        sequence.pop(index)
        sequence.insert(index, new_value)
        line = ' '.join(map(str, sequence))
        print('Question:', line)
        answer = int(input("Your answer: "))
        if answer == remove_value:
            print('Correct!')
            counter_answer = counter_answer + 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{remove_value}'.")
            print(f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


def main():
    arithmetic_progression_game()


if __name__ == "__main__":
    main()
