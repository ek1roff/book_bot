from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON
from services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    kp_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button in sorted(args):
        kp_builder.row(InlineKeyboardButton(
            text=f'{button} - {book[button[:100]]}',
            callback_data=str(button)))
    kp_builder.row(InlineKeyboardButton(
                        text=LEXICON['edit_bookmark_button'],
                        callback_data='edit_bookmarks'),
                   InlineKeyboardButton(
                        text=LEXICON['cancel'],
                        callback_data='cancel'),
                   width=2)
    return kp_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    kp_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button in sorted(args):
        kp_builder.row(InlineKeyboardButton(
            text=f'{LEXICON["del"]} {button} - {book[button][:100]}',
            callback_data=f'{button}del'))
    kp_builder.row(InlineKeyboardButton(
                        text=LEXICON['cancel'],
                        callback_data='cancel'))
    return kp_builder.as_markup()
