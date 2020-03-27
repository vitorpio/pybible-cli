import jsonpickle
import sys
import importlib
from pybible.classes.bible import Bible

try:
    from importlib.resources import open_text
except ImportError:
    from importlib_resources import open_text

JSON_EXT = ".json"
RESOURCES_PACKAGE = 'pybible.resources.bibles_json'


def load(bible_name: str = "kj", book_name: str = "kj") -> Bible:
    try:
        package_module = RESOURCES_PACKAGE if bible_name == book_name \
            else f'{RESOURCES_PACKAGE}.{bible_name}'
        package = importlib.import_module(package_module)

        json_file = open_text(package, book_name + JSON_EXT)

        return jsonpickle.decode(json_file.read())
    except ImportError:
        print(f"Bible \"{bible_name}\" not found")
        print('Use --help for the available bibles')
        sys.exit(1)
    except FileNotFoundError:
        available_books = [book.replace(JSON_EXT, '')
                           for book in importlib.resources.contents(package)
                           if book.endswith(JSON_EXT)]
        print(f"Book \"{book_name}\" not found")
        print(f"Available books for {bible_name} are: {available_books}")
        sys.exit(2)
