# try / except

# try:
#     # (logic expression)
#     a = 'ASa'
# except NameError:
#         print(a)
# try:
#     num = 1
#     num2 = 0
#     print(num/num2)
# except ZeroDivisionError:
#     print('done')

# try:
#     a = int(input('Enter num:'))
#     b = input('Enter some:')
#     print(a+b)
# except TypeError:
#     print('OK')

# except ZeroDivisionError:
#     print('Ok2')


# try:
#     a = int(input('Enter num:'))
#     b = input('Enter some:')
#     print(a+b)
# except TypeError:
#     print('OK')

# except ZeroDivisionError:
#     print('Ok2')

# try:
#     num1 = int(input('enter first'))
#     operation = input("choose: '-','+','*','/': ")
#     num2 = int(input('enter second'))
#     operation_dict = {'-':num1-num2,'+':num1+num2,'*':num1*num2,'/':num1/num2}
#     print(operation_dict[operation])
# except:
#     print('Arithmeric error occured!')
# else:
#     print('Worked')
# finally:
#     print('Good job')

a = set()
a.update('Hello world!')
print(a)
