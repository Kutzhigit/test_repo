# # 1.
# # lst = [i if i % 3 and i %5 ==0 else 'none' ]
# # lst= list(range(1,101))
# lst = [i for i in lst if i % 3 and i % 5 == 0 else 'none' for i in range(1,101))]
# print(lst)

# 2.
# dct = {'hello':None, 'word':None, 'programmer':None}
# dct = {k:len(k) for k,v in dct.items()}
# print(dct)

# 3.
# db = {'john':23, 'jack':34, "alex":23}
# def create():
#     global db
#     name = input('enter name: ')
#     age = input('enter age: ')
#     if name in db:
#         print('this name has')
#     else:
#         db[name] = age
#         print('name register')
#         print(f'now list {db}')

# def read():
#     # global db
#     print(f'now list {db}')


# def update():
#     global db 
#     name = input('enter name for change: ')
#     age = input('enter age: ')
#     if name in db:
#         db[name]= age
#         print('done')
#         print(f'now list {db}')
# # update()
# def delete():
#     global db
#     name = input('enter name for delete: ')
#     if name in db:
#         db.pop(name)
#         print('done')
#         print(f'now list {db}')
#     else:
#         print('error')
# delete()


