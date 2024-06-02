"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
def main():
    employers = [
        {'name': 'Max', 'age': 23, 'job': 'Engineer'},
        {'name': 'Andrei', 'age': 25, 'job': 'Designer'},
        {'name': 'Svetlana', 'age': 43, 'job': 'Manager'},
        {'name': 'Vasilisa', 'age': 31, 'job': 'Analyst'}

    ]
    with open('peolpe.csv', 'w', newline='') as f:
        fieldnames = ['name', 'age', 'job'] #Указываем ключи, которые будут заголвками столбцов
        writer = csv.DictWriter(f, fieldnames=fieldnames) #Создаем объект writer
        writer.writeheader() #Записываем заголовок
        for epmloyee in employers:
            writer.writerow(epmloyee)
if __name__ == "__main__":
    main()