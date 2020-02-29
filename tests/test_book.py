import pytest
from . import constants
from pybible import pybible_load
from pybible.classes.chapter import Chapter


@pytest.fixture
def book():
    return pybible_load.load()[constants.BOOK_KEY_TEST]


def test_len(book):
    assert len(book) == constants.BOOK_SIZE_TEST


def test_str(book):
    assert str(book) == constants.BOOK_NAME_TEST


def test_index_chapter_by_position(book):
    chapter = book[constants.POS_TEST]
    assert isinstance(chapter, Chapter)
    assert chapter.number == constants.POS_TEST + 1


def test_index_by_position_error_positive(book):
    with pytest.raises(SystemExit):
        return book[constants.POS_TEST_ERROR]
