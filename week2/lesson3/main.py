# a = {'hello', 1, 2,}
# for i in a;
#     print(i)

# lst = ['456', '325','456', '567', '976','325']
# a = set(lst)
# lst = list(a)
# print(lst)

#  операции множества 
# set.isdisjoint(other)  true/false
# a = {'hello', 1, 2}
# b = {'world', 5, 'john'}
# print(a.isdisjoint(b))

# set == other в set естьвсе элементы озер 
# a = {'hello', 1, 2}
# b = {'world', 5, 'john'}
# print(a == b)

# # set. issubset(other)  возвращает тру если б является подмножестаом а
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# print(b.issubset(a))
# print(b <= a)

# # set.issuperset(other)  возвращает тру если a является надмножестаом b
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# print(a.issuperset(b))
# print(a >= b)

# set.union(other, ...)  обядинение множеств
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# c = {15, 'jack'}
# # print(b.union(c,a))
# print(a|b|c)

# # set,intersection(other, ...)
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# c = {15, 'jack', 5}
# # print(b.intersection(a, c))
# print(b & c & a)

# # set.difference(other) разница
# a = {'world', 5, 'john','tom'}
# b = {'world', 5, 'john'}
# c = {15, 'jack', 5}
# # print(b.difference(c))
# print(b - c)

# set.symmetric_difference(other, ..)

# a = {'world', 5, 'john','tom'}
# b = {7, 5, 'hello'}
# c = {15, 'jack','tom'}
# print(b.symmetric_difference(c))
# print(b ^ c)

# # set.copy()
# a = {'world', 5, 'john','tom'}
# b = a.copy()
# print(b)

#  операции изменяющие множества

# set.update(other, ...)   обядинение изминение предыдущего
# a = {'world', 5, 'john','tom'}
# b = {7, 5, 'hello'}
# a.update(b)
# b |= c
# print(a)


# set.intersection_update(other, ...)   обновление пересечения
# a = {'world', 5, 'john','tom'}
# b = {7, 5, 'hello'}
# a.intersection_update(b)
# # b &= c
# print(a)


# set.diference_update(other, ...)   обновление разницы
# a = {'world', 5, 'john','tom'}
# b = {7, 5, 'hello'}
# c = {10, 52, 5}
# a.diference_update(b)
# # b -= c
# print(a)

# set.symmetric_diference_update(other, ...)   обновление разницы
# a = {'world', 5, 'john','tom'}
# b = {7, 5, 'hello'}
# c = {10, 52, 5}
# b.symmetric_diference_update(c)
# # b ^= c
# print(a)

# set.add(elem)
# b = {7, 5, 'hello'}
# b.add('hello')
# print(b)


# # set.remove(elem)  удаляет элемент если нет ошибка
# b = {7, 5, 'hello'}
# b.remove('hello')
# print(b)

# set.discard(elem)  удаляет если есть если нет то нет продолжает
# b = {7, 5, 'hello'}
# b.discard('h')
# print(b)

# set.pop()  удаляет любой рандомный элемент
# b = {7, 5, 'hello'}
# b.pop()
# print(b)


# set.clear() очистка множества
# b = {7, 5, 'hello'}
# b.clear()
# print(b)


# list_ = ['hello', 'rus']
# first = list_[1]
# second = list_[0]
# new_list = [second, first]
# print(new_list)

# suitcase = []
# suitcase.append('mask')
# suitcase.append('mask')
# print(suitcase)
# suitcase + []
# suitcase.append('mask')
# suitcase.append('mask')
# suitcase.append('mask')
# suitcase.append('mask')
# suitcase.append('mask')
# suitcase.pop()
# suitcase.insert(0, 'mark')
# print(suitcase)


# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}


# dict_ = {'timur':{'h':90,'m':95,'l':91},'vlad':{'m':93,'v':95, 'l':98}}
# dict_ = {k1:k2 for k1,v1 in dict_.items() for k2,v2 in v1.items() if max(v1.values())== v2}
# print(dict_)

# dict_ = {'first':{'a':1},'second':{'b':3}}
# dict_ = {k1:v2 for k1,v1 in dict_.items() for v2 in v1.values()}
# print(dict_)

# import random
# a = str(random.randrange(0, 10))
# while True:
#     num = input('enter num')
#     if num.lower()== 'exit':
#         print('game over')
#     elif int(a) > int(num):
#         print('big num')
#     elif int(a) < int(num):
#         print('low num')
#     elif int(a) == int(num):
#         print('win!')