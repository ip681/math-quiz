import random
import tkinter as tk

#---tkinter star testing
# master = tk.Tk()
# tk.Label(master, text="Condition").grid(row=0)
# tk.Button(master, text='Submit').grid(row=1, column=0)
# tk.Label(master, text="Answer").grid(row=2)
#
# e1 = tk.Entry(master)
#
# e1.grid(row=0, column=1)
#
# master.mainloop()

#---tkinter end testing

QUESTIONS_COUNT = 6
correct_answers_count = 0
all_answers_count = 0

while all_answers_count < QUESTIONS_COUNT:

    num_1 = random.choice(range(1, 99))
    num_2 = random.choice(range(1, 99))
    operation = random.choice(["+", "-", "*", "/"])

    if operation == "+":

        result = num_1 + num_2
        answer = int(input(f"{num_1} + {num_2} = "))

        if answer == result:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"Wrong! Correct answer is {result}")

    elif operation == "-":

        result = num_1 - num_2
        answer = int(input(f"{num_1} - {num_2} = "))

        if answer == result:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"Wrong! Correct answer is {result}")

    elif operation == "*":
        num_1 = int(num_1 / 10 + 1)
        num_2 = int(num_2 / 10 + 1)
        result = num_1 * num_2
        answer = int(input(f"{num_1} * {num_2} = "))

        if answer == result:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"Wrong! Correct answer is {result}")

    elif operation == "/":
        num_2 = int(num_2 / 10 + 1)
        num_1 = num_2 * random.choice(range(2, 10))
        result = int(num_1 / num_2)
        answer = int(input(f"{num_1} / {num_2} = "))

        if answer == result:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"Wrong! Correct answer is {result}")

    all_answers_count += 1
    print(f"Question {all_answers_count} of {QUESTIONS_COUNT}")
    print("_________________________________________________")

print(f"You have {correct_answers_count} correct answers")
print(f"You have {int(correct_answers_count / all_answers_count * 100)} %")
