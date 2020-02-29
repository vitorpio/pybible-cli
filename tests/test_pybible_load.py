import pytest
from . import constants
from pybible import pybible_load
from pybible.classes.bible import Bible


def test_load():
    bible = pybible_load.load(constants.BIBLE_NAME_ARG_TEST)
    assert isinstance(bible, Bible)


def test_load_fail():
    with pytest.raises(SystemExit):
        bible = pybible_load.load(constants.BIBLE_NAME_ARG_TEST_ERROR)
        assert isinstance(bible, Bible)
