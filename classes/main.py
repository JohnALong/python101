from book import Book
from library import Library
from classes import Pizza

book_one = Book("J. K. Rowling", "Harry Potter and the Sorcerer's Stone")
book_one.current_page = 1

print(f'I am reading {book_one.title} by {book_one.author}')
book_two = dict()
print(type(book_one))
print(type(book_two))
print(isinstance(book_one, Book))
print(isinstance(book_two, Book))
print(isinstance(book_two, dict))

book_one.start_reading()

book_two = Book("J. K. Rowling", "Harry Potter and the Chamber of Secrets")

book_two.current_page = 197

book_two.start_reading()

nss_library = Library("The NSS Library")
print(nss_library.name)

nss_library.add_book(book_one)
nss_library.add_book(book_two)
nss_library.list_books()
nss_library.set_address("301 Plus Park Blvd")
# errors out if you have not given the library an address
print(nss_library.address)

my_pizza = Pizza()
my_pizza.set_size("24 inch")
my_pizza.set_crust("pan")
my_pizza.add_topping("italian sausuge")
my_pizza.add_topping("mushrooms")
my_pizza.descrbe_pizza()


