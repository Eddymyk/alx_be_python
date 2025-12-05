from book_class import Book

def main():
    my_book = Book("Oscar", "Eddy Mike", 1995)

    print(my_book)

    print(repr(my_book))

    del my_book

if __name__ == "__main__":
    main()
