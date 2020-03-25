import jsonpickle
import sys
import importlib
from pybible.classes.bible import Bible

try:
    from importlib.resources import open_text
except ImportError:
    from importlib_resources import open_text

JSON_EXT = ".json"


def load(bible_name: str = "kj", json_name: str = "kj") -> Bible:
    try:
        bible_package = importlib.import_module(
            f'pybible.resources.bibles_serialized.{bible_name}')
        json_file = open_text(bible_package, json_name
                              + JSON_EXT)
        return jsonpickle.decode(json_file.read())
    except ImportError:
        print(f"Could not load \"{json_name}\" json file, check if it exists "
              f"and is structure correctly as described in the docs.")
        sys.exit(1)
