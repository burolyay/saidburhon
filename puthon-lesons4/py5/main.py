import logging

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



@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def echo(message: types.Message):
    await message.answer("You send me sticker")

@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def echo(message: types.Message):
    await message.answer("You send me audio")

@dp.message_handler(content_types=types.ContentTypes.ANIMATION)
async def echo(message: types.Message):
    await message.answer("You send me gif")

@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def echo(message: types.Message):
    await message.answer("You send me video")

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def echo(message: types.Message):
    await message.answer("You send me photo")

@dp.message_handler(content_types=types.ContentTypes.POLL)
async def echo(message: types.Message):
    await message.answer("You send me poll")


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo(message: types.Message):
    await message.answer("You send me text")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)