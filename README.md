![test](https://github.com/vitorpio/pybible-cli/workflows/test/badge.svg?branch=master)

# Pybible-cli  - Bible reference

The **pybible-cli** is a basic module for referencing the bible's books, chapters and verses. Using the command line, it is possible to reference the [King James Bible](https://www.sacred-texts.com/bib/osrc/index.htm). 

## Installation

You can install the pybible-cli from PyPI: `pip install pybible-cli`

This module requires at least Python version 3.

## How to use

The **pybible-cli** is a command line application, named `pybible`. To reference (print on your terminal) verses, chapters, books and even the whole bible simply call the command:
    
    $ pybible
    In the beginning God created the heaven and the earth.
    ...
    The grace of our Lord Jesus Christ be with you all. Amen.

It's possible to reference the whole bible as above or just parts of it, some examples are:

Reference the old testament:

    $ pybible -ot
    In the beginning God created the heaven and the earth.
    ...
    And he shall turn the heart of the fathers to the children, and the heart of the children to their fathers, lest I come and smite the earth with a curse
    
Reference the new testament:

    $ pybible -nt
    The book of the generation of Jesus Christ, the son of David, the son of Abraham.
    ...
    The grace of our Lord Jesus Christ be with you all. Amen.

Reference the book of John:

    $ pybible --book john
    In the beginning was the Word, and the Word was with God, and the Word was God.
    ...
    And there are also many other things which Jesus did, the which, if they should be written every one, I suppose that even the world itself could not contain the books that should be written. Amen.
    
Reference the third chapter from the book of John:

    $ pybible --chapter john 3
    There was a man of the Pharisees, named Nicodemus, a ruler of the Jews:
    ...
    He that believeth on the Son hath everlasting life: and he that believeth not the Son shall not see life; but the wrath of God abideth on him.
    
Reference the fourth verse of the third chapter from the book of John:

    $ pybible --verse john 3 4
    Nicodemus saith unto him, How can a man be born when he is old? can he enter the second time into his mother's womb, and be born?

Get a random verse with the `--qotd` argument:

    $ pybible --qotd
    "And the house which I build is great: for great is our God above all gods." - 2 Chronicles 2:5 (King James Bible)    

It is possible to add parameters to include the reference on the output(`-r`, `--reference`) and count the size(`-s`, `--size`) of what is been referenced.

For help, execute:

    $ pybible -h
    usage: pybible [-h] [--bible BIBLE]
                   [-ot | -nt | --qotd | --book BOOK_NAME | --chapter BOOK_NAME CHAPTER_NUMBER | --verse BOOK_NAME CHAPTER_NUMBER VERSE_NUMBER]
                   [-r] [-s]
    
    Bible reference
    
    optional arguments:
      -h, --help            show this help message and exit
      --bible BIBLE         Bible version to use
      -ot, --old_testament  Reference the old testament
      -nt, --new_testament  Reference the new testament
      --qotd                Quote a single, random verse
      --book BOOK_NAME      Reference book
      --chapter BOOK_NAME CHAPTER_NUMBER
                            Reference book and chapter
      --verse BOOK_NAME CHAPTER_NUMBER VERSE_NUMBER
                            Reference book, chapter and verse
      -r, --reference       Include book, chapter number and verse reference
      -s, --size            Size of bible, book, chapter or vere referenced
    
    ✞

You can also use `pybible-cli` in your on python code for referencing the bible, just import the `pybible_load` module from the `pybible` package:

    >>> from pybible import pybible_load
    >>> bible = pybible_load.load()
    >>> bible.name
    'King James Bible'
    
## Contributing

If you like this module feel free to contribute and make the `pybible-cli` module a pythonic bible reference module (that is the goal).

At this point there is only one bible version available (King James Version), you can help add more versions of the bible to this module, just follow the OOP structure inside the `classes` package and pickle it into a single file.

There are some performance issues involving unpickling, you can help with that too ;)

Feel free to reach out to me for new features and ideas ...
