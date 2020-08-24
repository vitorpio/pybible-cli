import sys


class Chapter:
    """
    A class used to represent a chapter from a book of the bible.
    """

    def __init__(self, number: int, verses: tuple):
        """
        Initialize a `Chapter` object.

        :Parameters:
            - `number`: integer containing the number of the chapter.
            - `verses`: tuple of verses in the chapter.
        """
        self.__number = number
        self.__verses = verses

    def __len__(self):
        return len(self.verses)

    def __getitem__(self, item):
        try:
            return self.verses[item]
        except IndexError:
            print(f"Verse number {item + 1} not found in Chapter {self.number}.")
            sys.exit(7)

    def __repr__(self):
        return f'Chapter({self.number}, {self.verses})'

    def __str__(self):
        return f'Chapter {self.number}'

    @property
    def number(self):
        """Integer with the number of the chapter."""
        return self.__number

    @property
    def verses(self):
        """Tuple of `Verse` objects inside the chapter."""
        return self.__verses
