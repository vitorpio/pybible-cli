import pytest
from . import constants
from pybible import pybible_load
from pybible.classes.bible import Bible
from pybible.classes.bible_without_apocrypha import BibleWithoutApocrypha
from pybible.classes.book import Book
from pybible.classes.chapter import Chapter
from pybible.classes.verse import Verse


@pytest.fixture
def bible():
    return pybible_load.load()


def test_init(bible):
    assert isinstance(eval(repr(bible)), Bible)


def test_len(bible):
    assert len(bible) == constants.BIBLE_SIZE_TEST


def test_str(bible):
    assert str(bible) == constants.BIBLE_NAME_TEST


def test_index_book_by_position(bible):
    book = bible[constants.POS_TEST]
    assert isinstance(book, Book)
    assert str(book) == constants.BOOK_NAME_TEST


def test_index_book_by_position_error(bible):
    with pytest.raises(SystemExit):
        return bible[constants.POS_TEST_ERROR]


def test_index_book_by_name(bible):
    book = bible[constants.BOOK_KEY_TEST]
    assert isinstance(book, Book)
    assert str(book) == constants.BOOK_NAME_TEST


def test_index_book_by_name_error(bible):
    with pytest.raises(SystemExit):
        return bible[constants.BOOK_KEY_TEST_ERROR]


def test_ot(bible):
    ot = bible.ot()
    assert len(ot) == constants.OT_SIZE_TEST
    assert ot[constants.FIRST_POSITION].title \
        == constants.OT_FIRST_BOOK_TITLE_TEST
    assert ot[constants.LAST_POSITION].title \
        == constants.OT_LAST_BOOK_TITLE_TEST


def test_nt(bible):
    nt = bible.nt()
    assert len(nt) == constants.NT_SIZE_TEST
    assert nt[constants.FIRST_POSITION].title \
        == constants.NT_FIRST_BOOK_TITLE_TEST
    assert nt[constants.LAST_POSITION].title \
        == constants.NT_LAST_BOOK_TITLE_TEST


def test_books_names(bible):
    assert len(bible.books_names) == constants.BIBLE_SIZE_TEST
