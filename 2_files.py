"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
def main():
    with open('referat.txt', 'r', encoding='utf-8') as f: #Чтение содержимого файла
        content = f.read()
    
    string_length = len(content) # Считаем длину строки
    print(f"Длина строки: {string_length} символов")

    word_count = len(content.split()) #Подсчет количества слов
    print(f"Количеество слов: {word_count}")

    modified_content = content.replace('.', '!') #Замена точек на восклицательные знаки

    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(modified_content)
    print("Данные успешно обработаны и сохранены в файл referat2.txt")

if __name__ == "__main__":
    main()
