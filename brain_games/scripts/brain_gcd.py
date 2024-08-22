import random
import math


def gcd_game():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("Find the greatest common divisor of given numbers.")

    score = 0
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        user_answer = int(input("Your answer: "))

        correct_answer = math.gcd(num1, num2)
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again,", user_answer + '!')
            break

    if score == 3:
        print(f"Congratulations, {user_name}!")


def main():
    gcd_game()


if __name__ == "__main__":
    main()
