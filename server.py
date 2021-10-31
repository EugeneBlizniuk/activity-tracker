import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2071085913:AAHU8wD4dywZD-1IlgLeGGjZOVKbWVc3kFA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(
        "Hi there!\n I'm Activity Tracker!\n\n"
        "I'm here to collect your activity and calculate its statistics\n"
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
