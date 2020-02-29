import pytest
from . import constants
from pybible import pybible_load
from pybible.classes.verse import Verse


@pytest.fixture
def chapter():
    return pybible_load.load()[constants.BOOK_KEY_TEST][constants.POS_TEST]


def test_len(chapter):
    assert len(chapter) == constants.CHAPTER_SIZE_TEST


def test_str(chapter):
    assert str(chapter) == constants.CHAPTER_NAME_TEST


def test_index_verse_by_position(chapter):
    verse = chapter[constants.POS_TEST]
    assert isinstance(verse, Verse)
    assert chapter.number == constants.POS_TEST + 1


def test_index_verse_by_position_error(chapter):
    with pytest.raises(SystemExit):
        return chapter[constants.POS_TEST_ERROR]
