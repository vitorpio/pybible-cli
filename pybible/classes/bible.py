from abc import ABC, abstractmethod


class Bible(ABC):
    """
    A class used to represent a real world bible.
    """

    def __init__(self, name: str, language: str, books: tuple):
        """
        Initialize a `Bible` object.

        :Parameters:
            - `name`: string with the bible's name.
            - `language`: language in witch the bible was written.
            - `books`: tuple of books contained in the bible.
        """
        self.__name = name.strip()
        self.__language = language.strip()
        self.__books = books

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return self.name

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

    @abstractmethod
    def ot(self) -> tuple:
        """
        Return the old testament tuple.

        :Return:
            - Tuple of `Book` objects in the old testament.
        """
        raise NotImplementedError

    @abstractmethod
    def nt(self) -> tuple:
        """
        Return the new testament tuple.

        :Return:
            - Tuple of `Book` objects in the new testament.
        """
        raise NotImplementedError
