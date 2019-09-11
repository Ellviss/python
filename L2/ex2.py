#Практика: Сравнение строк
#Написать функцию, которая принимает на вход две строки
def string_check(str1,str2):
#Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0
    if type(str1) != str or type(str2) !=str :
        return "0"
#Если строки одинаковые, вернуть 1
    elif str1 == str2:
        return "1"
#Если строки разные и первая длиннее, вернуть 2
    elif str1 != str2 and len(str1)>len(str2) and str2 !='learn':
        return "2"
#Если строки разные и вторая строка 'learn', возвращает 3
    elif str1 != str2 and str2 == 'learn':
        return "3"        
#Вызвать функцию несколько раз, передавая ей разные параметры и выводя на экран результаты

ans=string_check('blabla',12)
print(ans)
ans=string_check('blabla','blabla')
print(ans)
ans=string_check('blablabla','blabla')
print(ans)
ans=string_check('blabla','learn')
print(ans)