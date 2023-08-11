import random

words = ["code", "bit", "dict", "list", "soul", "next", "little", "snake", "well played"]

MORSE_CODES = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": " "
}
answers = []


def get_word():
    """
    Рандомно выбирает слово из предложенного списка
    :return: слово из списка
    """
    return random.choice(words)


def morse_encode():
    """
    кодирует данное слово в последовательность точек и тире
    :return: последовательность точек и тире
    """
    word_encode = []
    for letter in random_word:
        word_encode.append(MORSE_CODES[letter])
    return " ".join(word_encode)


def print_statistic():
    """
    Подсчитывает кол-во верных и неверных ответов
    :param:
    :return:
    """

    print(f"Всего задачек: {len(answers)}")
    print(f"Отвечено верно: {sum(answers)}")
    print(f"Отвечено неверно: {len(answers) - sum(answers)}")


print("Сегодня мы потренируемся расшифровывать азбуку Морзе.")
input("Нажмите Enter и начнем\n")
for i in range(1, len(words) + 1):
    random_word = get_word()
    words.remove(random_word)
    current_encoded = morse_encode()
    user_answer = input(f"Слово {i} - {current_encoded}\n")
    if user_answer.lower() == random_word:
        print(f"Верно, {random_word.title()}!")
        answers.append(True)
    else:
        print(f"Неверно, {random_word.title()}!")
        answers.append(False)
print_statistic()
