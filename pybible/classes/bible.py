import sys


class Bible:
    """
    A class used to represent a real world bible
    (not including apocrypha books).
    """
    OLD_TESTAMENT_BOOKS = 39
    APOCRYPHA_BOOKS = 7

    def __init__(self, name: str, language: str, books: tuple,
                 apocrypha_books_included: bool = False):
        """
        Initialize a `BibleWithoutApocrypha` object.

        :Parameters:
            - `name`: string with the bible's name.
            - `language`: string with the language in witch the bible
            was written.
            - `books`: tuple of books contained bible
            (not including apocrypha books).
        """
        self.__name = name.strip()
        self.__language = language.strip()
        self.__books = books
        self.__ot_last_book = self.OLD_TESTAMENT_BOOKS
        if apocrypha_books_included:
            self.__ot_last_book += self.APOCRYPHA_BOOKS

    def __getitem__(self, key):
        try:
            return self.books[key]
        except IndexError:
            print(f"Book number {key} not found in {self.name}.")
            sys.exit(4)

    def __repr__(self):
        return f'BibleWithoutApocrypha(\"{self.name}\", ' \
               f'\"{self.language}\", {self.books})'

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return self.name

    def ot(self) -> tuple:
        return self.books[:self.__ot_last_book]

    def nt(self) -> tuple:
        return self.books[self.__ot_last_book:]

    @property
    def name(self):
        """String with the name of the bible."""
        return self.__name

    @property
    def language(self):
        """String with the language in witch the bible was written."""
        return self.__language

    @property
    def books(self):
        """Tuple of `Book` objects inside the bible."""
        return self.__books
