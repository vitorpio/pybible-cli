import argparse
import sys
from pybible import pybible_load
import random
from collections import namedtuple

Reference = namedtuple("Reference", ["verse_text", 'book_title',
                                     'chapter_number', 'verse_number',
                                     'bible_name'])

parser = argparse.ArgumentParser(description='Bible reference',
                                 epilog="\u271e")


def configure_arg_parser():
    parser.add_argument("--bible", metavar="BIBLE",
                        help="Bible version to use", choices=["kj"],
                        default="kj")

    reference_group = parser.add_mutually_exclusive_group()
    reference_group.add_argument("-ot", "--old_testament",
                                 help="Reference the Old Testament",
                                 action="store_true")
    reference_group.add_argument("-nt", "--new_testament",
                                 help="Reference the New Testament",
                                 action="store_true")
    reference_group.add_argument("-qotd", "--qotd",
                                 help="Quote a single, random verse",
                                 action="store_true")
    reference_group.add_argument("--book", metavar="BOOK_NAME",
                                 help="Reference a book")
    reference_group.add_argument("--chapter", metavar=("BOOK_NAME",
                                                       "CHAPTER_NUMBER"),
                                 help="Reference a book and chapter", nargs=2)
    reference_group.add_argument("--verse", metavar=("BOOK_NAME",
                                                     "CHAPTER_NUMBER",
                                                     "VERSE_NUMBER"),
                                 help="Reference a book, chapter and verse",
                                 nargs=3)

    options_group = parser.add_mutually_exclusive_group()
    options_group.add_argument("-r", "--reference",
                               help="Include book, chapter and verse "
                                    "reference",
                               action="store_true")
    options_group.add_argument("-s", "--size",
                               help="Size of the bible, book, chapter or vere "
                                    "referenced",
                               action="store_true")


def process_arguments():
    args = parser.parse_args()

    if args.old_testament:
        response = process_ot_arguments(args)
    elif args.new_testament:
        response = process_nt_arguments(args)
    elif args.book:
        response = process_book_arguments(args)
    elif args.chapter:
        response = process_chapter_arguments(args)
    elif args.verse:
        response = process_verse_arguments(args)
    elif args.qotd:
        response = process_qotd_arguments(args)
    else:
        response = process_bible_arguments(args)

    if args.reference:
        return (f"{reference.verse_text} - {reference.book_title} "
                f"{reference.chapter_number}:{reference.verse_number}"
                f" ({reference.bible_name})"
                for reference in response)
    else:
        if args.size:
            return response
        return (f"{reference.verse_text}" for reference in response)


def process_ot_arguments(args: argparse.Namespace):
    bible = pybible_load.load(args.bible)
    if args.size:
        yield f"The Old Testament has {len(bible.ot())} books"
    else:
        for reference in (Reference(verse.text, book.title, chapter.number,
                                    verse.number, bible.name)
                          for book in bible.ot()
                          for chapter in book.chapters for verse
                          in chapter.verses):
            yield reference


def process_nt_arguments(args: argparse.Namespace):
    bible = pybible_load.load(args.bible)
    if args.size:
        yield f"The New Testament has {len(bible.nt())} books"
    else:
        for reference in (Reference(verse.text, book.title, chapter.number,
                                    verse.number, bible.name)
                          for book in bible.nt()
                          for chapter in book.chapters for verse
                          in chapter.verses):
            yield reference


def process_book_arguments(args: argparse.Namespace):
    bible = pybible_load.load(args.bible, args.book)
    book = bible[0]
    if args.size:
        yield f"{book.title} has {len(book)} chapters"
    else:
        for reference in (Reference(verse.text, book.title, chapter.number,
                                    verse.number, bible.name)
                          for chapter in book.chapters for verse
                          in chapter.verses):
            yield reference


def process_chapter_arguments(args: argparse.Namespace):
    bible = pybible_load.load(args.bible, args.chapter[0])
    book = bible[0]
    chapter = book[cast_integer_argument(parser, args.chapter[1],
                                         "--chapter", "CHAPTER_NUMBER")]
    if args.size:
        yield f"Chapter {chapter.number} of {book.title} " \
              f"has {len(chapter)} verses"
    else:
        for reference in (Reference(verse.text, book.title, chapter.number,
                                    verse.number, bible.name)
                          for verse in chapter.verses):
            yield reference


def process_verse_arguments(args: argparse.Namespace):
    bible = pybible_load.load(args.bible, args.verse[0])
    book = bible[0]
    chapter = book[cast_integer_argument(parser, args.verse[1], "--verse",
                                         "CHAPTER_NUMBER")]
    verse = chapter[cast_integer_argument(parser, args.verse[2], "--verse",
                                          "VERSE_NUMBER")]
    if args.size:
        yield f"Verse {verse.number} of Chapter {chapter.number} " \
              f"of {book.title} has {len(verse)} characters"
    else:
        yield Reference(verse.text, book.title, chapter.number,
                        verse.number, bible.name)


def process_qotd_arguments(args: argparse.Namespace):
    bible = pybible_load.load(args.bible)
    book = random.choice(bible)
    chapter = random.choice(book.chapters)
    verse = random.choice(chapter.verses)
    yield Reference(verse.text, book.title, chapter.number,
                    verse.number, bible.name)


def process_bible_arguments(args: argparse.Namespace):
    bible = pybible_load.load(args.bible)
    if args.size:
        yield f"{bible.name} has {len(bible)} books"
    else:
        for reference in (Reference(verse.text, book.title, chapter.number,
                                    verse.number, bible.name)
                          for book in bible.books
                          for chapter in book.chapters for verse
                          in chapter.verses):
            yield reference


def cast_integer_argument(my_parser: argparse.ArgumentParser, argument: str,
                          argument_name: str, argument_metavar: str) -> int:
    try:
        position_one_based_numbered = int(argument) - 1
        if position_one_based_numbered < 0:
            raise argparse.ArgumentTypeError()
        return position_one_based_numbered
    except (argparse.ArgumentTypeError, ValueError):
        my_parser.print_usage()
        print(f"{my_parser.prog}: error: argument {argument_name}: "
              f"{argument_metavar} must be an integer number greater then 0")
        sys.exit(3)


def output_response(response):
    for line in response:
        print(line)


def main():
    configure_arg_parser()
    references = process_arguments()
    output_response(references)


if __name__ == "__main__":
    main()
