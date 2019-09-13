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

def vert_str(str1):
    letter=str1.split()
    for letter in str1:
        print(letter)

vertical_convert(string)
vert_str(string)


#Оценки
#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
school_classes= [
                {'school_class': '4a', 'scores': [3,4,4,5,2]},
                {'school_class': '5b', 'scores': [5,2,3,5,4]},
                {'school_class': '6a', 'scores': [4,5,2,4,3]}
                ]

#Посчитать и вывести средний балл по всей школе.
def average_school (dict_list):
    for item in dict_list:
        class_res=0
        len_avg=0
        class_res +=sum(item.get('scores'))
        len_avg +=len(item.get('scores'))
     
    res = class_res/len_avg
    print ('Classes average: '+str(res) )
average_school(school_classes)
#Посчитать и вывести средний балл по каждому классу.
def class_avr(dict_list):
    for item in dict_list:
        school_class= item.get('school_class')
        res =  sum(item.get('scores'))/len(item.get('scores'))
        print ('Class: '+school_class+' average: '+str(res) )
class_avr(school_classes)
