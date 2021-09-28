
books = {'Pich and poor dad':'Robert Kiosaki','financial':'Theador Draiser',
'thin and get rich':'Napaleon Hill'}
reader = {}
def get_info():
    print(f'now list of books: {reader}')
    print(f'now list of books: {books}')
# get_info()
def manager():
    global books,reader
    ques = input(f'You want take or give book? if you mant take or give writ this:')
    if ques == 'take':
        name_book = input('wrinte name of book:')
        if name_book in books:
            books.pop(name_book)
            reader.pop(name_book)
    print(reader)
    print(books)
    # f'{name_books = input()}{name = input()}
manager() 
    