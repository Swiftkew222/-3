def A(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
def append_to_file(text, file):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
file = "Text1.txt"
print("Исходный содержимое файла:")
A(file)
append_to_file("добавление строки ", file)
print("\nОбновленное содержимое файла:")
A(file)
