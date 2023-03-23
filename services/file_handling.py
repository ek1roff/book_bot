import re

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 750

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    page = re.sub(r'[.,!?:;]\.+$', '', text[start:start+size])
    edit_page = re.findall(r'(?s).+[.,!?:;]', page)
    return *edit_page, len(*edit_page)


def prepare_book(path: str) -> None:
    with open(path, 'r', encoding="utf-8") as file:
        txt = file.read()
        start = 0
        num_page = 1
        while len(tuple(txt)) != start:
            txt_out, symbol = _get_part_text(txt, start, PAGE_SIZE)
            start += symbol
            book[num_page] = txt_out.lstrip()
            num_page += 1


prepare_book(BOOK_PATH)
