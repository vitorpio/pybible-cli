class Verse:
    """A class used to represent a verse from the bible."""

    def __init__(self, text: str, number: int):
        """
        Initialize a `Verse` object.

        :Parameters:
            - `text`: sting containing the text of the verse.
            - `number`: integer with the number of the verse.
        """
        self.__text = text.strip()
        self.__number = number

    def __len__(self):
        return len(self.text)

    def __repr__(self):
        return f'Verse(\"{self.text}\", {self.number})'

    def __str__(self):
        return self.text

    @property
    def text(self):
        """String with the text of the verse."""
        return self.__text

    @property
    def number(self):
        """Integer with the verse's number."""
        return self.__number
