import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6032377757:AAH4HfKWmw0qLMHxhJWD8KRoyV8qBX18ncs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Any text")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)