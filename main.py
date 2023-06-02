import requests
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types


def dt():
    now = str(datetime.now())[:10]
    timeStamp = datetime.strptime(now, "%Y-%m-%d").timestamp()
    return int(timeStamp)


def dt1():
    now = str(datetime.now())[:11] + "23:59:59"
    timeStamp = datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timestamp()
    return int(timeStamp)


bot = Bot(
    token={Token},
    parse_mode=types.ParseMode.HTML,
)
dp = Dispatcher(bot)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Северо-Запад", "ЧМЗ", "Центр", "Чурилово", "Все районы"]
keyboard.add(*buttons)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "<code>Привет 👋\n\nЯ помогу тебе узнать качество воздуха в твоем городе.\n"
        "\nОсновной показатель – ИКВ, это взвешенные частицы вещества, которые представляют собой широко распространенный загрязнитель атмосферного воздуха.\n"
        "\nСреднесуточная концентрация не допускает превышения порогового уровня 50 мкг/м3.\n"
        "\nЧтобы начать выбери свой район 🏡.\n</code>",
        reply_markup=keyboard,
    )


@dp.message_handler(text="Северо-Запад")
async def sz(message: types.Message):
    try:
        url = f"https://roseman.airalab.org/api/sensor/135fbacd20ff3ad0c8ebda98ca83fef6f1daa136448b1fffc1af3e2629b1a390/{dt()}/{dt1()}"
        r = requests.get(url).json()
        main = r.get("result")
        for data in main:
            pm10 = data.get("data").get("pm10")
            temp = data.get("data").get("temperature")
            time = datetime.fromtimestamp(data.get("timestamp"))
            humidity = data.get("data").get("humidity")
        if float(pm10) > 50:
            await bot.send_message(
                message.chat.id,
                f"<code>Дата: {time}\nРайон: Северо-Запад\nИКВ: {pm10} 🙊\nТемпература: {temp}°С\nВлажность: {humidity}%</code>",
                reply_markup=keyboard,
            )
        else:
            await bot.send_message(
                message.chat.id,
                f"<code>Дата: {time}\nРайон: Северо-Запад\nИКВ: {pm10} ☘\nТемпература: {temp}°С\nВлажность: {humidity}%</code>",
                reply_markup=keyboard,
            )
    except:
        await bot.send_message(
            message.chat.id,
            f"<code>Не могу обнаружить датчик 😬</code>",
            reply_markup=keyboard,
        )


@dp.message_handler(text="ЧМЗ")
async def chmz(message: types.Message):
    try:
        url = f"https://roseman.airalab.org/api/sensor/81c9bfbbe8c7bd0ac0670e435853a90008d84222b79c97e09d28214ae26eec03/{dt()}/{dt1()}"
        r = requests.get(url).json()
        main = r.get("result")
        for data in main:
            pm10 = data.get("data").get("pm10")
            temp = data.get("data").get("temperature")
            time = datetime.fromtimestamp(data.get("timestamp"))
            humidity = data.get("data").get("humidity")
        if float(pm10) > 50:
            await bot.send_message(
                message.chat.id,
                f"<code>Дата: {time}\nРайон: ЧМЗ\nИКВ: {pm10} 🙊\nТемпература: {temp}°С\nВлажность: {humidity}%</code>",
                reply_markup=keyboard,
            )
        else:
            await bot.send_message(
                message.chat.id,
                f"<code>Дата: {time}\nРайон: ЧМЗ\nИКВ: {pm10} ☘\nТемпература: {temp}°С\nВлажность: {humidity}%</code>",
                reply_markup=keyboard,
            )
    except:
        await bot.send_message(
            message.chat.id,
            f"<code>Не могу обнаружить датчик 😬</code>",
            reply_markup=keyboard,
        )


@dp.message_handler(text="Центр")
async def centr(message: types.Message):
    try:
        url = f"https://roseman.airalab.org/api/sensor/c9a3d4bfeac495243aacc7278105501a31fc5f43f7ad6230db89f851a49eeb17/{dt()}/{dt1()}"
        r = requests.get(url).json()
        main = r.get("result")
        for data in main:
            pm10 = data.get("data").get("pm10")
            temp = data.get("data").get("temperature")
            time = datetime.fromtimestamp(data.get("timestamp"))
            humidity = data.get("data").get("humidity")
        if float(pm10) > 50:
            await bot.send_message(
                message.chat.id,
                f"<code>Дата: {time}\nРайон: Центр\nИКВ: {pm10} 🙊\nТемпература: {temp}°С\nВлажность: {humidity}%</code>",
                reply_markup=keyboard,
            )
        else:
            await bot.send_message(
                message.chat.id,
                f"<code>Дата: {time}\nРайон: Центр\nИКВ: {pm10} ☘\nТемпература: {temp}°С\nВлажность: {humidity}%</code>",
                reply_markup=keyboard,
            )
    except:
        await bot.send_message(
            message.chat.id,
            f"<code>Не могу обнаружить датчик 😬</code>",
            reply_markup=keyboard,
        )


@dp.message_handler(text="Чурилово")
async def churilovo(message: types.Message):
    try:
        url = f"https://roseman.airalab.org/api/sensor/eca00d1f1caecfe51e5feacd76a12dfa07ebd61c91c718a69777eb973105e1f9/{dt()}/{dt1()}"
        r = requests.get(url).json()
        main = r.get("result")
        for data in main:
            pm10 = data.get("data").get("pm10")
            temp = data.get("data").get("temperature")
            time = datetime.fromtimestamp(data.get("timestamp"))
            humidity = data.get("data").get("humidity")
        if float(pm10) > 50:
            await bot.send_message(
                message.chat.id,
                f"<code>Дата: {time}\nРайон: Чурилово\nИКВ: {pm10} 🙊\nТемпература: {temp}°С\nВлажность: {humidity}%</code>",
                reply_markup=keyboard,
            )
        else:
            await bot.send_message(
                message.chat.id,
                f"<code>Дата: {time}\nРайон: Чурилово\nИКВ: {pm10} ☘\nТемпература: {temp}°С\nВлажность: {humidity}%</code>",
                reply_markup=keyboard,
            )
    except:
        await bot.send_message(
            message.chat.id,
            f"<code>Не могу обнаружить датчик 😬</code>",
            reply_markup=keyboard,
        )


@dp.message_handler(text="Все районы")
async def send_welcome(message: types.Message):
    await bot.send_message(
        message.chat.id,
        "<code>В разработке 👨‍💻</code>",
        reply_markup=keyboard,
    )


@dp.message_handler()
async def send_welcome(message: types.Message):
    await bot.send_message(
        message.chat.id,
        "<code>Не могу распознать запрос, выберите cвой район 🧐</code>",
        reply_markup=keyboard,
    )


if __name__ == "__main__":
    executor.start_polling(dp)

# def dt():
#     now = str(datetime.now())[:10]
#     timeStamp = datetime.strptime(now, "%Y-%m-%d").timestamp()
#     return int(timeStamp)

# def dt1():
#     now = str(datetime.now())[:11] + "23:59:59"
#     timeStamp = datetime.strptime(now, "%Y-%m-%d %H:%M:%S").timestamp()
#     return int(timeStamp)

# def SZ():
#     url = f'https://roseman.airalab.org/api/sensor/135fbacd20ff3ad0c8ebda98ca83fef6f1daa136448b1fffc1af3e2629b1a390/{dt()}/{dt1()}'
#     r = requests.get(url).json()
#     main = r.get('result')
#     for data in main:
#         pm10 = data.get('data').get('pm10')
#         temp = data.get('data').get('temperature')
#         time = datetime.fromtimestamp(data.get('timestamp'))
#         humidity = data.get('data').get('humidity')
#     if (float(pm10)>50):
#         print(f'{time} | Северо-Запад | ИКВ: {pm10} ☠ | Температура: {temp}°С | Влажность: {humidity}%')
#     else:
#         print(f'{time} | Северо-Запад | ИКВ: {pm10} ✔ | Температура: {temp}°С | Влажность: {humidity}%')

# def CHMZ():
#     url = f'https://roseman.airalab.org/api/sensor/81c9bfbbe8c7bd0ac0670e435853a90008d84222b79c97e09d28214ae26eec03/{dt()}/{dt1()}'
#     r = requests.get(url).json()
#     main = r.get('result')
#     for data in main:
#         pm10 = data.get('data').get('pm10')
#         temp = data.get('data').get('temperature')
#         time = datetime.fromtimestamp(data.get('timestamp'))
#         humidity = data.get('data').get('humidity')
#     if (float(pm10)>50):
#         print(f'{time} | ЧМЗ | ИКВ: {pm10} ☠ | температура: {temp}°С | Влажность: {humidity}%')
#     else:
#         print(f'{time} | ЧМЗ | ИКВ: {pm10} ✔ | температура: {temp}°С | Влажность: {humidity}%')

# def centr():
#     url = f'https://roseman.airalab.org/api/sensor/c9a3d4bfeac495243aacc7278105501a31fc5f43f7ad6230db89f851a49eeb17/{dt()}/{dt1()}'
#     r = requests.get(url).json()
#     main = r.get('result')
#     for data in main:
#         pm10 = data.get('data').get('pm10')
#         temp = data.get('data').get('temperature')
#         time = datetime.fromtimestamp(data.get('timestamp'))
#         humidity = data.get('data').get('humidity')
#     if (float(pm10)>50):
#         print(f'{time} | Центр | ИКВ: {pm10} ☠ | температура: {temp}°С | Влажность: {humidity}%')
#     else:
#         print(f'{time} | Центр | ИКВ: {pm10} ✔ | температура: {temp}°С | Влажность: {humidity}%')

# def churilovo():
#     url = f'https://roseman.airalab.org/api/sensor/eca00d1f1caecfe51e5feacd76a12dfa07ebd61c91c718a69777eb973105e1f9/{dt()}/{dt1()}'
#     r = requests.get(url).json()
#     main = r.get('result')
#     for data in main:
#         pm10 = data.get('data').get('pm10')
#         temp = data.get('data').get('temperature')
#         time = datetime.fromtimestamp(data.get('timestamp'))
#         humidity = data.get('data').get('humidity')
#     if (float(pm10)>50):
#         print(f'{time} | Чурилово | ИКВ: {pm10} ☠ | температура: {temp}°С | Влажность: {humidity}%')
#     else:
#         print(f'{time} | Чурилово | ИКВ: {pm10} ✔ | температура: {temp}°С | Влажность: {humidity}%')

# while True:
#     SZ()
#     CHMZ()
#     centr()
#     churilovo()
#     sleep(3600)
