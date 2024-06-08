from googletrans import Translator
import random


def play_game():
    translator = Translator()
    words = ["собака", "кошка", "яблоко", "дерево", "книга", "корова", "карандаш", "картина", "игра", "дом", "банан", "мяч", "сумка"]
    correct_answers = 0

    while True:
        word_to_translate = random.choice(words)
        translation = translator.translate(word_to_translate, src="ru", dest="en")
        translated_word = translation.text

        print(f"Переведите это слово на английский: {word_to_translate}")
        user_answer = input("Ваш ответ: ")

        if user_answer.lower() == translated_word.lower():
            print("Правильно!")
            correct_answers += 1
            play_again = input("Хотите попробовать следующее слово? (да/нет): ")
            if play_again.lower() != "да":
                break
        else:
            print(f"Неправильно. Правильный ответ: {translated_word}")
            play_again = input("Хотите сыграть еще раз? (да/нет): ")
            if play_again.lower() != "да":
                break

    print(f"Спасибо за игру! Количество правильных ответов: {correct_answers}")

print("Добро пожаловать в игру 'Переведи слово'!")
play_game()