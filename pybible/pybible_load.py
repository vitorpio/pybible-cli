import jsonpickle
import sys
from pybible.classes.bible import Bible
import pybible.resources.bibles_serialized
try:
    from importlib.resources import open_text
except ImportError:
    from importlib_resources import open_text

JSON_EXT = ".json"


def load(bible_name: str = "kj") -> Bible:
    try:
        json_file = open_text(pybible.resources.bibles_serialized, bible_name + JSON_EXT)
        return jsonpickle.decode(json_file.read())
    except OSError:
        print(f"Could not load \"{bible_name}\" json file, check if it exists and is structure correctly as "
              f"described in the docs.")
        sys.exit(1)
