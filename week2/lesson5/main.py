# range([s], s, [s])
# for i in range(1, 61, 2):
#     print(i)

# lst1 = list(range(1,100))
# print(lst1)

# lst2 = []
# for i in range(1,101):
#     lst2.append(i)

# newlist = [Exception for item in ]

# lst3 = [i for i in range(1,101)]
# print(lst3)

# lst = ['apple','potato','banan','tomato']
# # lst = [elem for elem in lst if elem != 'potato']
# lst = [i for i in lst if i != 'tomato' and i != 'banan']
# print(lst)

# numlist = list(range(1 ,21))
# # strlist = ['chet' if i % 2 ==0 else 'nechet' for i in numlist]
# # print(strlist)
# # num_lst2 = 
# lst_odd = [i for i in numlist if not i % 2 == 0]
# print(lst_odd)

# lst = ['hello', 'john','worls']
# lst = [i.upper() for i in lst]
# print(lst)


# dct = {x: x **2 for x in range(6)}
# print(dct)

# dct = {x**2: x**3 for x in range(11)}
# print(dct)

# dct = {1: None,2: None,3: None,4: None,5: None,}
# dct1 = {k:'chet' if k%2==0 else 'nechet' for k, v in dct.items()}
# print(dct1)

# lst = ['aplle','heloo world','sas']
# dct = {k: len(k) for k in lst if len(k) > 6}
# print(dct)

# import random
# lst = ['Asa','Mark','Tom','Nick','Jack']
# lst_order = random.sample(range(1,10), len(lst))
# guest_order_stack = {lst[i]:lst_order[i] for i in range(len(lst))}
# # print(guest_order_stack)
# for v in guest_order_stack:
#     if k, v in guest_order_stack.items()
#     if 

# nums = input('enter nums')
# nums = nums.split(",")
# list_ = []
# for i in nums:
#     list_.append(i)
# print(sorted(list_))