#Цикл
#Создать список из десяти целых чисел.
listing = [1,2,3,4,5,6,7,8,9,0]
print (listing)
#Вывести на экран каждое число, увеличенное на 1.
for i in range(len(listing)):
    listing[i] += 1
print(listing)

#Цикл
#Ввести с клавиатуры строку.
string= input('Введите строку: ')
#Вывести эту же строку вертикально: по одному символу на строку консоли.
def vertical_convert(str1):
    words = str1.split()
    word_long=max(map(len,words))
    print("\n".join(" ".join(c[i] for c in [i+" "*(word_long-len(i)) for i in words]) for i in range(word_long)))
vertical_convert(string)


#Оценки
#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
school_classes= [
                {'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '5b', 'scores': [5,2,3,5,4]},
                {'school_class': '6a', 'scores': [4,5,2,4,3]}
                ]

#Посчитать и вывести средний балл по всей школе.
def average_school (list1):
    print ('bla1')
average_school(school_classes)
#Посчитать и вывести средний балл по каждому классу.
def average_class (list1):
    print ('bla2')
average_class (school_classes)