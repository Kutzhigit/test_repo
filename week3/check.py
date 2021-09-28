# Дан словарь, в котором ключом является имя студента, а значением
# словарь с его оценками по 3 предметам. Замените оценки названием
# предмета, по которому студент имеет высший балл. Например: a = {'John':
# {'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature':
# 81},
# 'Kelly': {'history': 84, 'math': 85, 'literature': 87}}
# Результат: {'John': 'math', 'Rose': 'math', 'Kelly': 'literature'}

# a = {'John':{'history': 90, 'math': 95, 'literature': 91}, 
# 'Rose': {'history': 92, 'math': 96, 'literature':81},
# 'Kelly': {'history': 84, 'math': 85, 'literature': 87}}
# a ={k1:v1 for k1,v1 in a.items() for k2, v2 in v1.items() if v1(max(values))== v2}
# print(a)

# 3) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
# list_ = [1, 2, 3, 4]
# print(sum(list_))

# # Дан список с числами. Отфильтруйте этот список, оставив только четные числа.
# list_ = [1, 2, 3, 4,5,6,7,8,9]
# for i in list_:
#     if i % 2 == 0:
#         list_.append(i)
# print(list_)

import functools
list_ = [1, 2, 3, 4,5,6,7,8,9]
list_ = functools.reduce(lambda x,y: x+y, list_)
print(list_)

