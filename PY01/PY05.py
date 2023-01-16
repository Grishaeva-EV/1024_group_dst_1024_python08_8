'''
Skillfactory | Задача по Python
5.1 7.17
Напишите функцию sort_ignore_case(ls), которая принимает на вход список ls и сортирует его без учёта регистра по алфавиту.

Функция возвращает отсортированный список.

Пример:


print(sort_ignore_case(['Acc', 'abc']))
# ['abc', 'Acc']
'''

def sort_ignore_case(ls):
    ls.sort(key=lambda word: word.lower())
    return ls

'''
Skillfactory | Задача по Python
Напишите функцию exchange(usd, rub, rate), которая может принимать на вход сумму в долларах (usd), сумму в рублях (rub) и обменный курс (rate). Обменный курс показывает, сколько стоит один доллар. Например, курс 85.46 означает, что один доллар стоит 85 рублей и 46 копеек.

В функцию должно одновременно передавать два аргумента. Если передано менее двух аргументов, должна возникнуть ошибка ValueError('Not enough arguments'). Если же передано три аргумента, должна возникнуть ошибка: ValueError('Too many arguments').

Функция должна находить третий аргумент по двум переданным. Например, если переданы суммы в разных валютах, должен возвращаться обменный курс. Если известны сумма в рублях и курс, должна быть получена эквивалентная сумма в долларах, аналогично — если передана сумма в долларах и обменный курс.

Пример:

print(exchange(usd=100, rub=8500))
# 85.0

print(exchange(usd=100, rate=85))
# 8500

print(exchange(rub=1000, rate=85))
# 11.764705882352942

print(exchange(rub=1000, rate=85, usd=90))
# ValueError: Too many arguments

print(exchange(rub=1000))
# ValueError: Not enough arguments

'''

def exchange(usd = None, rub = None, rate = None):
    none_count = 0
    for i in [usd, rub, rate]:
        if i == None:
            none_count += 1
    if none_count < 1:
        raise ValueError('Too many arguments')
    if none_count > 1:
        raise ValueError('Not enough arguments')
    
    if usd == None:
        return rub / rate
    if rate == None:
        return rub / usd
    if rub == None:
        return rate * usd