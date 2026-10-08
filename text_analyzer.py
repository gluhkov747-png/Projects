#_____Анализатор текста_____
def clean_text(text):
    text = text.lower()

    for mark in ".,!?;:-":
        text = text.replace(mark, "")

    text = text.split()

    if len(text) != 0:
        return text

    else:
        print("Список слов пуст")
        return list()


def word_stat(words):
    stat = {}
    for word in words:
        if word in stat:
            stat[word] += 1
        else:
            stat[word] = 1
    return stat


def top_words(stat, n = 5):
    dct_top_words = sorted(stat.items(), key = lambda x: (-x[1], x[0]))
    dct_top_words = [i[0] for i in dct_top_words][:n]
    return dct_top_words


text = input()
#"Python is great. Python is powerful. I love Python."

words = clean_text(text)\

print(words)
print(word_stat(words))

stat = word_stat(words)


try:
    n = int(input("Введите число для определения колличества популярных слов "))
    print(top_words(stat, n))
    
except ValueError:
    print("Вы ввели не тот тип данных")
    n = 3
    dct_top_words = top_words(stat, n)
    print(dct_top_words)