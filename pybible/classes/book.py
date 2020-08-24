import sys


class Book:
    """
    A class used to represent a book from the bible.
    """

    def __init__(self, title: str, full_title: str, author: str,
                 chapters: tuple):
        """
        Initialize a `Book` object.

        :Parameters:
            - `title`: string with the book's title.
            - `full_title`: string with the book's title.
            - `author`: string with the book's author.
            - `chapters`: tuple of chapters in the book.
        """
        self.__title = title.strip()
        self.__full_title = full_title.strip()
        self.__author = author.strip()
        self.__chapters = chapters

    def __len__(self):
        return len(self.chapters)

    def __getitem__(self, item):
        try:
            return self.chapters[item]
        except IndexError:
            print(f"Chapter number {item + 1} not found in {self.title}.")
            sys.exit(6)

    def __repr__(self):
        return f'Book(\"{self.title}\", \"{self.full_title}\", ' \
               f'\"{self.author}\", {self.chapters})'

    def __str__(self):
        return f'{self.title} by {self.author}'

    @property
    def title(self):
        """String with the title of the book."""
        return self.__title

    @property
    def full_title(self):
        """String with the fulltitle of the book."""
        return self.__full_title

    @property
    def author(self):
        """String with the author of the book."""
        return self.__author.strip()

    @property
    def chapters(self):
        """Tuple of `Chapter` objects inside the book."""
        return self.__chapters
