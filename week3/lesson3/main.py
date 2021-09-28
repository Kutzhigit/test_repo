#  function
# def add_func():
#     print(10+5)
# add_func()

# def add_num(num1,num2):
#     print(num1+num2)

# num1= int(input('first'))
# num2= int(input('second'))

# add_num(num1,num2)

# def add_num(num1,num2):
#     return num1+num2
# result = add_num(10,100)
# print(result)


# def hello(name,surname, age):
#     print(f'Hello {name} {surname}! Your age {age} !')
# name,surname,age = input('enter name'),input('enter surname'),input('enter age')
# hello(name,surname,age)

# def hello(name ='non',surname='none', age):
#     print(f'Hello {name} {surname}! Your age {age} !')

# hello(age=23)

# def func(*args, **kwargs):
#     print(f'this args{args}')
#     print(f'this kwargs{kwargs}')

# func('hello',1,3, name='alex',age=23)


# def add_func(num1,num2):
#     return num1 + num2

# def sub_func(num1,num2):
#     return num1 - num2

# def mult_func(num1,num2):
#     return num1 * num2

# def dev_func(num1,num2):
#     return num1 / num2

# def handler(operation,num1,num2):
#     switcher = {
#         '+': add_func(num1,num2),
#         '-': sub_func(num1,num2),
#         '*': mult_func(num1,num2),
#         '/': dev_func(num1,num2),
#     }
#     return switcher[operation]

# num1 = int(input('enter num1'))
# operation = input('choose')
# num2 = int(input('enter num'))
# result = handler(operation,num1,num2)
# print(result)


# string = input('enter string').lower()
# def translate_str(string):
#     intab = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
#     outtab = 'йцукенгшщзхъфывапролджэячсмитьбю.'
#     trantab = str.maketrans(intab,outtab)
#     return string.translate(trantab)

# result = translate_str(string)

# print(result)           

# def foo():
#     var = 'переменная foo'
#     def bar():
#         var = 'переменная bar'
#         # print("переменная в foo: ", var)
#     bar()
# print("переменная в foo: ", var)
# foo()
# print("переменная в foo: ", var)