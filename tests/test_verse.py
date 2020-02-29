import pytest
from . import constants
from pybible import pybible_load


@pytest.fixture
def verse():
    return pybible_load.load()[constants.BOOK_KEY_TEST][constants.POS_TEST][constants.POS_TEST]


def test_len(verse):
    assert len(verse) == constants.VERSE_SIZE_TEST


def test_str(verse):
    assert str(verse) == constants.VERSE_TEXT_TEST
