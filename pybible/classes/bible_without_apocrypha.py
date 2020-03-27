from pybible.classes.bible import Bible
import sys


class BibleWithoutApocrypha(Bible):
    """
    A class used to represent a real world bible
    (not including apocrypha books).
    """
    __ot_last_book = 39
    """Last old testament book position in the bible
    (not including apocrypha books)."""
    __book_names = dict([(book, pos) for pos, book in enumerate((
        "genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua",
        "judges", "ruth", "1samuel", "2samuel", "1kings", "2kings",
        "1chronicles", "2chronicles", "ezra", "nehemiah", "esther", "job",
        "psalms", "proverbs", "ecclesiastes", "song of songs", "isaiah",
        "jeremiah", "lamentations", "ezekiel", "daniel", "hosea", "joel",
        "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk", "zephaniah",
        "haggai", "zachariah", "malachi", "matthew", "mark", "luke", "john",
        "acts", "romans", "1corinthians", "2corinthians", "galatians",
        "ephesians", "philippians", "colossians", "1thessalonians",
        "2thessalonians", "1timothy", "2timothy", "titus", "philemon",
        "hebrews", "james", "1peter", "2peter", "1john", "2john", "3john",
        "jude", "revelation"))])
    """Dictionary containing the book names in the bible
    (not including apocrypha books)."""

    def __init__(self, name: str, language: str, books: tuple):
        """
        Initialize a `BibleWithoutApocrypha` object.

        :Parameters:
            - `name`: string with the bible's name.
            - `language`: string with the language in witch the bible
            was written.
            - `books`: tuple of books contained bible
            (not including apocrypha books).
        """
        super().__init__(name, language, books)

    def __getitem__(self, key):
        try:
            if isinstance(key, str):
                return self.books[self.__book_names[key]]
            else:
                return self.books[key]
        except IndexError:
            print(f"Book number {key} not found in {self.name}.")
            sys.exit(4)
        except KeyError:
            print(f"Book \"{key}\" not found in {self.name}.\nAvailable book "
                  f"names for index: {list(self.__book_names.keys())}")
            sys.exit(5)

    def __repr__(self):
        return f'BibleWithoutApocrypha(\"{self.name}\", ' \
               f'\"{self.language}\", {self.books})'

    def ot(self) -> tuple:
        return self.books[:self.__ot_last_book]

    def nt(self) -> tuple:
        return self.books[self.__ot_last_book:]

    @property
    def books_names(self) -> tuple:
        """Tuple of book names inside the bible
        (not including apocrypha books)."""
        return tuple(self.__book_names.keys())
