import pickle
import sys
from pybible.classes.bible import Bible
from importlib.resources import open_binary
import pybible.resources.bibles_serialized


def load(bible_name: str = "kj") -> Bible:
    try:
        pickle_file = open_binary(pybible.resources.bibles_serialized, bible_name)
        return pickle.load(pickle_file)
    except OSError:
        print(f"Could not load \"{bible_name}\" pickle file, check if it exists and is structure correctly as "
              f"described in the docs.")
        sys.exit(1)
