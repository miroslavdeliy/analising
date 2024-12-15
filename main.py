#Функция ввода и модификации строки
def enter_text():
    words = input("Введите любой текст: ")
    signs = [',', '.', ':', ';', '!', '?']
    new_words = []
    words_low = words.lower() #Переводим строку в нижний регистр
    for word in words_low.split():
        for sign in signs:
            word = word.replace(sign, "") #Удаляем из списка слов знаки препинания
        new_words.append(word)
    return new_words #Возвращает измененный список слов из строки


#Функция определения самого длинного слова
def most_long(words):
    length = 0
    for word in words:
        if len(word) > length:
            length = len(word)
            longest = word
    return longest


#Функция подсчета гласных
def count_glas(words):
    glas = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    glas_count = 0
    for word in words:
        for symbol in glas:
            glas_count += word.count(symbol)
    return glas_count


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
print("Самое длинное слово: " + (most_long(new_text)))
#Количество гласных
print(f"Количество гласных {str(count_glas(new_text))}")
#Список с количеством вхождений
print(count_word(new_text))






