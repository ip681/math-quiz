import random

QUESTIONS_COUNT = 3
correct_answers_count = 0
all_answers_count = 0

while all_answers_count < QUESTIONS_COUNT:

    num_1 = random.choice(range(1, 99))
    num_2 = random.choice(range(0, 99))

    result = num_1 + num_2

    print(f"{num_1} + {num_2} = ")

    answer = int(input())

    if answer == result:
        print("Correct!")
        correct_answers_count += 1
    else:
        print(f"Wrong! Correct answer is {result}")

    all_answers_count += 1

print(f"You have {correct_answers_count} correct answers")
print(f"You have {int(correct_answers_count / all_answers_count * 100)} %")
