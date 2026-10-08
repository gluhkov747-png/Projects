#скрипт, который берёт папку с файлами, собирает их в один CSV и чистит пустые строки.
#берем папку с файлами, обходим файлы и добавляем текст в новый отдельный файл, далее убираем пустые строки
import os
import os.path
import csv
from pathlib import Path


encoding = "utf-8-sig"
#кодировка для безопасности (BOM от Excel)

data = ["id", "name", "amount"]
#список строк

name_file = "notes.csv"
#имя файла без пустых строк


with open(name_file, "w", encoding=encoding, newline="") as f:
    writer = csv.writer(f)
    writer.writerow(data)

name_folder = "data"
#имя папки с файлами

path_folder = Path(os.getcwd()) / name_folder
#путь к папке

for root, dirs, files in os.walk(path_folder):
    for file in files:
        try:
            path_file = Path(root) / file
            #путь к файлу из цикла

            if os.path.splitext(file)[1].lower() == ".csv" and os.path.getsize(path_file) != 0:

                with open(path_file, "r", encoding=encoding, newline="") as f:

                    reader = csv.reader(f)
                    #объект читатель для корректной работы со строкой csv файла

                    next(reader, None)
                    lst_strings = []
                    #общий список строк

                    for row in reader:
                        row = [c.strip() for c in row]
                        #c - элемент списка, из которого убираем пробелы и перенос строки

                        if all(not c for c in row):
                            continue
                            #проверка, что символы после чистки пробелов и переноса не стали пустыми

                        lst_strings.append(row)
                        #добавляем список в общий список строк        

                with open("notes.csv", "a", encoding=encoding, newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(lst_strings)

        except Exception as e:
            print(f"Ошибка: {e}")