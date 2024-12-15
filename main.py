#Функция ввода и модификации строки
import string


def enter_text():
    words = input("Введите любой текст: ")
    new_words = []
    for word in words.lower().split():
        for sign in string.punctuation:
            word = word.replace(sign, "") #Удаляем из списка слов знаки препинания
        new_words.append(word)
    return new_words #Возвращает измененный список слов из строки


#Функция определения самого длинного слова
def most_long_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


#Функция подсчета гласных
def vowel_counting(words):
    vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    number_vowels = 0
    for word in words:
        for symbol in vowel:
            number_vowels += word.count(symbol)
    return number_vowels


#Функция подсчета колчества вхождений
def count_word(words):
    dict_count = {}
    for word in words:
        dict_count[word] = words.count(word)
    return dict_count


#Основное тело программы
new_text = enter_text()

#Вывод количества слов
print(f"В данной строке {str(len(new_text))} слов")
#Вывод самого длинного слова
print("Самое длинное слово: ",most_long_word(new_text))
#Количество гласных
print("Количество гласных ", vowel_counting(new_text))
#Список с количеством вхождений
print("Количество вхождений каждого слова ", count_word(new_text))






