import logging

from aiogram import Bot, Dispatcher, executor, types

import category

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
        "Hello there!\nI'm Activity Tracker!\n\n"
        "I'm here to collect your activity and calculate its statistics\n\n"
    )


@dp.message_handler(commands=["categories"])
async def categories_list(message: types.Message):
    """Return a list of existing categories"""
    categories = category.CategoryService().get_all_categories()
    answer = "List of existing categories:\n\n* " + \
             ("\n* ".join([c.name + ' (' + ", ".join(c.aliases) + ')' for c in categories]))
    await message.answer(answer)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
