import datetime
from typing import NamedTuple, Optional

import pytz

import db
import exceptions
from category import CategoryService


class Message(NamedTuple):
    """Message structure"""
    activity_name: str
    amount: int


class Activity(NamedTuple):
    """Activity structure"""
    id: Optional[int]
    name: str
    amount: int


def add_activity(raw_message: str) -> Activity:
    """Add new activity"""
    parsed_message = _parse_message(raw_message)
    category = CategoryService().get_category(parsed_message.activity_name)
    inserted_row_id = db.insert("activity", {
        "name": category.name,
        "amount": parsed_message.amount,
        "created": _get_now_formatted(),
        "category_name": category.name,
        "raw_text": raw_message
    })
    return Activity(id=inserted_row_id,
                    name=category.name,
                    amount=parsed_message.amount)


def _parse_message(raw_message: str) -> Message:
    """Parse incoming message"""
    result = raw_message.split()
    if not result or not result[0] or not result[1]:
        raise exceptions.NotCorrectMessage(
            "I don't get it, check the message pattern, "
            "example:\nworkout 90")

    activity_name = result[0].strip().lower()
    amount = result[1].replace(" ", "")
    return Message(activity_name=activity_name,
                   amount=int(amount))


def _get_now_formatted() -> str:
    """Return properly formatted date"""
    return _get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")


def _get_now_datetime() -> datetime.datetime:
    """Return UTC datetime"""
    tz = pytz.timezone("UTC")
    now = datetime.datetime.now(tz)
    return now
