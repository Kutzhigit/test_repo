# словари 
#  {key:value,key:value}
# dct = {}
# dict.clear()
# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# # print(dct['age'])
# print(dct['hobby'][1])

# dict.copy()
# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# # dct1 = dct.copy(), 

# # dict.fromkeys(seq[,value])
# lst = ['name','age', 'hobby']


# # dict.get(key[,default])
# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# print(dct.get(['name']))

# dict.items()
# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# lst = list(dct.items())
# print(lst[0])

# dict.keys() list from key
# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# print(dct.keys())

# dict.values() - list from values

# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# print(dct.values())


# # dict.pop(key[,default]) -  delete elem from key if not key 'keyerrror'
# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# remove_elem = dct.pop('age')
# print(f'This deleted elem {remove_elem} \n this dict{dct}')

# dict.popitem() - delete random key;value
# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# remove_elem = dct.popitem()
# print(remove_elem)

# dict.setdefault(key[, default])  - give value from key if not   
# dct = {'name':'John', 'age':25, 'hobby':['fishing','footbal','auto']}
# elem = dct.setdefault('surname', 'jackson')
# print(elem, dct)

# dict.update(other) -
# dct = {'name':'John', 'age':25}
# dct.update({'surname': 'jackson','hobby':['fishing','footbal','auto']})
# print(dct)


# cycle in dict

# dct = {'name':'John', 'age':25,'surname':'jackson'}
# for k, v in dct.items():
#     print(k, v)

# dct = {'name':'John', 'age':25,'surname':'jackson'}
# lst_k = []
# lst_v = []
# for k, v in dct.items():
#     lst_k.append(k)
#     lst_v.append(v)
# print(lst_k, lst_v)

# tuple
# tpl = ()

# tpl = ('hello',[1 , 2])
# # tpl[1].append('3')
# # print(tpl[1][2])

# for i in  tpl:
#     print(i)

# tpl = ('hello',1 , 2, 'world')
# print(tpl.count('hello'))
# print(tpl.index('hello'))

# frozenset
# st = {'hello', 1 , 2,'world'}
# fst = frozenset(st.copy())