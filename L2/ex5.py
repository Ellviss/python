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
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if not isinstance(price, float):
        raise TypeError(f"Argument save must be of type float, not {type(price)}")
    if not isinstance(discount, float):
        raise TypeError(f"Argument save must be of type float, not {type(discount)}")
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
                  
res=discounted(20.0,8,10.0)
print (res)