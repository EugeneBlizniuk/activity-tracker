import logging

from aiogram import Bot, Dispatcher, executor, types

import category
import activity
import exceptions

API_TOKEN = "2071085913:AAHU8wD4dywZD-1IlgLeGGjZOVKbWVc3kFA"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    """This handler will be called when user sends `/start` or `/help` command"""
    await message.answer(
        "Hello there!\n"
        "I'm here to collect your activity statistics and drink beer.\n"
        "As you can see my bottle is empty already\n\n"
        "Enter /help to get a list of commands"
    )


@dp.message_handler(commands=["help"])
async def get_help(message: types.Message):
    """Return a list of existing commands"""
    await message.answer(
        "/start - light me up\n"
        "/help - list of existing commands\n"
        "/categories - list of existing categories\n\n"
        "new commands are coming..."
    )


@dp.message_handler(commands=["categories"])
async def categories_list(message: types.Message):
    """Return a list of existing categories"""
    categories = category.CategoryService().get_all_categories()
    answer = "List of existing categories:\n\n* " + \
             ("\n* ".join([c.name + ' (' + ", ".join(c.aliases) + ')' for c in categories]))
    await message.answer(answer)


@dp.message_handler()
async def add_activity(message: types.Message):
    """Add new activity"""
    try:
        added_activity = activity.add_activity(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    answer = f"{added_activity.name} has been added\n{added_activity.amount} minutes have been spent"
    await message.answer(answer)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
