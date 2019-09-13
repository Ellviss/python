#Задание
#Перепишите функцию ask_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, 
#Писала пользователю "Пока!" и завершала работу при помощи оператора break
def ask_user():
    try:
        ask= ''
        while ask != 'Хорошо':
            ask=input('Как дела? ')
    except KeyboardInterrupt:
        print('Пока!')

#ask_user()

#Задание
#Перепишите функцию discounted(price, discount, max_discount=20)из урока про функции так, чтобы она перехватывала исключения,
#Когда переданы некорректные аргументы (например, строки вместо чисел).
def discounted(price, discount, max_discount=20):
    #price = abs(float(price))
    #discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    try:
        if max_discount > 99:
            return price
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except TypeError:
        print (f"Argument must be of type float")
    except ValueError:
        print (f'Слишком большая максимальная скидка')    
                      
res=discounted(20.0,8,10.0)
print (res)