# Kaun Bane ga Crore Pati
# Practice
questions = [
    [
        "Which language was used to build Character ?", "Heart", "Brain",
        "emotions", "Pain", 4
    ],
    [
        "Which language was used to build Character ?", "Heart", "Brain",
        "emotions", "Pain", 4
    ],
    [
        "Which language was used to build Character ?", "Heart", "Brain",
        "emotions", "Pain", 4
    ],
    [
        "Which language was used to build Character ?", "Heart", "Brain",
        "emotions", "Pain", 4
    ],
]

levels = [
    1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000
]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestions for Rs.  {levels[i]}")

    print(f"a. {question[1]}                   a. {question[2]}")
    print(f" c. {question[3]}                   d. {question[4]}")
    reply = int(input("Please enter the number between (1-4): "))
    if (reply == question[-1]):
        print("Correct Answer, You Have won: {levels[i]} ")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
    else:
        print("Wrong Answe")
        break
