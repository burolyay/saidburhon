import logging

from aiogram import Bot, Dispatcher, executor, types
from tugmalar import main_menu, Audio_menu
API_TOKEN = '   '

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom bu mening botim.", reply_markup=main_menu)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(text="Аудио")
async def echo(message: types.Message):
    await message.answer_audio(reply_markup=Audio_menu)


@dp.message_handler(text="1 Audio")
async def echo(message: types.Message):
    await message.answer_audio("https://t.me/edisonfamilia/887")
    
@dp.message_handler(text="2 Audio")
async def echo(message: types.Message):
    await message.answer_audio("https://t.me/edisonfamilia/887")
    
@dp.message_handler(text="3 Audio")
async def echo(message: types.Message):
    await message.answer_audio("https://t.me/edisonfamilia/887")
    
@dp.message_handler(text="4 Audio")
async def echo(message: types.Message):
    await message.answer_audio("https://t.me/edisonfamilia/887")

@dp.message_handler(text="Videolar")
async def echo(message: types.Message):
    await message.answer_audio("https://t.me/englishfocusuz/6497")


@dp.message_handler(text="Опросник")
async def echo(message: types.Message):     
    await message.answer_poll  (question="Гагда ды подился", 
                              options=["2005", "2010", "2015"],
                              is_anonymous=False,
                              correct_option_id=1,
                              type="quiz"
                             )
    await message.answer_photo("https://t.me/ichigoscripttw/1824")
    await message.answer_photo("https://t.me/my_park/2")
    await message.answer_video_note("https://telesco.pe/my_park/4")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)