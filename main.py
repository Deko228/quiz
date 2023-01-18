def game_start():
    input("Добро пожаловать! Чтобы начать, нажмите Enter: ")

game_start()

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Введите вариант ответа (A, B, C, или D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("ВЕРНО!")
        return 1
    else:
        print("НЕВЕРНО!")
        return 0

def display_score(correct_guesses, guesses):

    k = []
    n = []
    f = []

    print("-------------------------")
    print("РЕЗУЛЬТАТЫ")
    print("-------------------------")

    print("Ваши ответы: ", end="")
    for i in guesses:
        print(i, end=" ")
        k.append(i)
    print()

    print("Правильные ответы: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
        n.append(questions.get(i))
    print()

    for key in questions:
        f.append((key))


    score = int(correct_guesses)*50
    total = int(len(questions))*50
    print("Ваш счёт: "+str(score)+" / "+str(total))

    my_file = open("Result.txt", "w+")
    my_file.write("РЕЗУЛЬТАТЫ\n-------------------------\nВопросы: "+str(f)+"\nВаши ответы: "+str(k)+"\nПравильные ответы: "+str(n)+"\nВаш счёт: "+str(score)+" / "+str(total))
    my_file.close()


def play_again():

    response = input("Хотите сыграть ещё раз? (да или нет): ")
    response = response.upper()

    if response == "ДА":
        return True
    else:
        return False

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]


new_game()
while play_again():
    new_game()

print("Спасибо за игру!")
