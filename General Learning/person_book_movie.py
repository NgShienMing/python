"""Learning classes"""
from calc_day_in_year import calc_day_in_year

def month_to_num(month: str):
    """Convert month in string to number"""
    month = month.lower()
    month_arr = ["january", "february", "march", "april", "may", "june", "july",
                 "august", "september", "october", "november", "december"]
    for month_str in month_arr:
        if month == month_str:
            month_num = month_arr.index(month_str) + 1
            break
    return month_num

class Person:
    """Person class"""
    def __init__ (self, name, birthday, birthmonth, birthyear):
        self.name = name
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear

    def to_string(self):
        """Print the details of the person in a string"""
        print(f"{self.name}'s birthday is on {self.birthday} {self.birthmonth} {self.birthyear}.")

    def day_of_birthday(self):
        """Print the day in the year where the person's birthday is on"""
        year = self.birthyear
        month = month_to_num(self.birthmonth)
        day = self.birthday
        day_in_year = calc_day_in_year(year, month, day)
        suffix = "th"
        if day_in_year == 1:
            suffix = "st"
        elif day_in_year == 2:
            suffix = "nd"
        elif day_in_year == 3:
            suffix = "rd"
        print(f"{self.name}'s birthday is the {day_in_year}{suffix} day in the year.")

class Book:
    """Book class"""
    def __init__(self, title, author, publisher, pages):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages

    def book_author(self):
        """Print book title and author"""
        print(f"{self.title} is written by {self.author}.")

    def num_of_pages(self):
        """Print book title and total pages"""
        print(f"{self.title} has {self.pages} pages.")

class Movie:
    """Movie class"""
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.set_rating(rating)

    def set_rating(self, rating):
        """Rating setter"""
        if rating in ("U", "PG-13", "18"):
            self.rating = rating
        else:
            self.rating = "NR"

    def movie_info(self):
        """Print movie title and director"""
        print(f"{self.title} is directed by {self.director}.")

p1 = Person("Ng Shien Ming", 2, "June", 2002)
p1.to_string()
p1.day_of_birthday()

hpbook1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "Bloomsbury", 223)
hpbook2 = Book("Harry Potter and the Chamber of Secrets", "J. K. Rowling", "Bloomsbury", 251)
hpbook3 = Book("Harry Potter and the Prisoner of Azkaban", "J. K. Rowling", "Bloomsbury", 317)
hpbook4 = Book("Harry Potter and the Goblet of Fire", "J. K. Rowling", "Bloomsbury", 636)
hpbook5 = Book("Harry Potter and the Order of the Phoenix", "J. K. Rowling", "Bloomsbury", 766)
hpbook6 = Book("Harry Potter and the Half-Blood Prince", "J. K. Rowling", "Bloomsbury", 607)
hpbook7 = Book("Harry Potter and the Deathly Hallows", "J. K. Rowling", "Bloomsbury", 607)
hpbook7.book_author()
hpbook7.num_of_pages()

movie1 = Movie("Shang-Chi and The Legend of The Ten Rings", "Destin Daniel Cretton", "PG-13")
movie2 = Movie("Spider-Man: No Way Home", "Jon Watts", "PG-13")
movie2.movie_info()
