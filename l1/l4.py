def get_sum(one,two,delimiter='&'):
   one = str(one)
   two = str(two)
   #res = str(print(f'{one}{delimiter}{two}'))
   return f'{one}{delimiter}{two}'

get_sum("Learn","python",)
print (get_sum("Learn","python",))
print(get_sum("Learn","python").upper())

def format_price(price):
    price=int(price)
    return 'Цена: '+str(price)+' руб.'

print(format_price(56.24))