#list

# ['sdgfs'],34,'rgtfe', [3,5,7,['hello']]

# lst = [1, 2, 3, ['hello', 'world']]
# for i in lst:
#     # if isinstance(i, (list)):
#         print(i)
# # lst = ['h', ' r', 'l']
# print('k' in lst)

# names = input('enter names:').lower().split()
# guest = input('enter name').lower()
# if guest in names:
#     print('done')
# # else:
# #     print('error')
# list_of_friens = ['tom','asa', 'max']
# for friend in list_of_friens:
#     print(f'welcome to party, {friend}')


# metod list
# lst= ['some1', 'some2']
# new_data = input('enter data')
# lst.append(new_data)
# print(lst)

# # lst.extend()
# lst1= ['some1', 'some2']
# lst2= ['some3', 'some4']
# lst1.extend(lst2)
# print(lst1)

# # list.insert(i, x)  по индексу
# lst= ['some1', 'some2']
# lst.insert(0, 'some3')
# print(lst)

# list.remove(x) удаляет первое вхождение
# lst= ['some1', 'some2']
# lst.remove('some1')
# print(lst)

# list.pop([i]) удаляет и возвращает по индексу
# lst= ['some1', 'some2']
# lst.pop(0)
# print(lst)


# # list.index(x.[star, end])
# lst= ['some1', 'some2', 2, 5]
# print(lst.index(2))


# # # list.count() подсчет элемента
# lst= ['h', 'e', 'l','l']
# print(lst.count('e'))

# # list.sort([key =funk])
# lst = [1,5 ,3 ,4 ,2]
# lst.sort()
# print(lst)

# # list.reverse() reverze list
# lst = [1,5 ,3 ,4 ,2]
# lst.reverse()
# print(lst)

# list.clear() clear list
# lst = [1,5 ,3 ,4 ,2]
# lst.clear()
# print(lst)


# # list.copy() copy list
# lst1 = [1,5 ,3 ,4 ,2]
# lst2 = lst1.copy()
# print(lst2)

# n = int(input())
# a = ord('a')
# z = ord('z')
# A = ord('A')
# Z = ord('Z')
# if a <= n <= z or A <= n <= Z:
#     print("Это буква", chr(n))
# else:
#     print("Это не буква, а символ", chr(n))


# lst = [1, 2, 3, 'hello', [1, 'data', 4]]
# for i in lst:
#     print('Это элемент первого списка')
#     if isinstance(i, (list)):
#         print('это элемент второго')




# name_of_list = ['helloworld']
# second = name_of_list[0][(len(name_of_list[0])-1)//2+1:]
# first = name_of_list[0][:(len(name_of_list[0])-1)//2+1]
# # print(len(name_of_list[0]))
# print(first, second)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in nums:
#     if i < 5:
#         print(i)

# nums = input('enter nums')
# list_ = []
# for i in nums:
#     list_.append(i).sort()
#     list_.sort()
# print(list_)
# # print(list_)