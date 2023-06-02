import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6287800146:AAHrDuh9OmfYwRrlan5V7P093yYsEt6P1vo'

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
    wikipedia.set_lang("ru")
    javob = wikipedia.summary(message.text)
    await message.answer(javob)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)