from datetime import datetime
my_name, my_surname = input('Name and Surname: ').split ()
age = input ('Your Age: ')
born_age = datetime.now().year-int(age)
print (f'Your name - {my_name} {my_surname}, and you bythday in {born_age} year')

v = input("Введите число от 1 до 10: ")
print (10+int(v))

name= input("Введите ваше имя: ")
print (f'Привет, {name}! Как дела?')

a=float('1')  # ???
b=int(2.5)  # ???
c=bool(1)  # ???
d=bool('')  # ???
e=bool(0)
print (a,b,c,d,e )