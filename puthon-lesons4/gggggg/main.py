@dp.message_handler(text="soqqa")
async def echo(message: types.Message):
    # Making our request
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}%7Bcity%7D&appid=%7Bkey%7D")

    data = response.json
    temp_celsium = data ['main']['temp']-273.15
    humidity = data['main']['humtdity']
    wind_speed = data ['wind']['speed']
    long = data ['coord']['lon']
    lat = data ['coord']['lat']
    answer_text=f""
Shahar:{message.text}
Harorat : {temp_celsium}
Namlik: {humidity}

