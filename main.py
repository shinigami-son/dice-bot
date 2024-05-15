import config
from func import roll, rollV3, rollV4
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TOKEN)
db = Dispatcher(bot)


@db.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    kb = [
        [types.KeyboardButton(text="/help")],
        [types.KeyboardButton(text="/donate")],
        [types.KeyboardButton(text="3-я редакция")],
        [types.KeyboardButton(text="4-я редакция")],
        [types.KeyboardButton(text="Поиск")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.reply(r"Привет. Я DiceBotWoD. Напишите '/roll' или '/r' и параметры кубов через пробел, а я кину кубы. Например: '/r 7 10 6'", reply_markup=keyboard)


@db.message_handler(commands=['dice', 'Dice'])
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@db.message_handler(commands=['donate'])
async def send_donate(message: types.Message):
    await message.answer("Если вы хотите поддержать меня, то можете отправить пожертвование на одну из этих двух карт:\nyour_card_number_1\nyour_card_number_2\nСпасибо!")


@db.message_handler(commands=['search'])
async def search_info(message: types.Message):
    """Function for searching different information about lore and rules"""
    searchQuery = message.text[8:].replace(' ', '+')
    url1 = f"https://wod.fandom.com/ru/wiki/{searchQuery}"
    url2 = f"https://wod.fandom.com/ru/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%9F%D0%BE%D0%B8%D1%81%D0%BA?query={searchQuery}&scope=internal&navigationSearch=true"
    url3 = f"https://www.google.com/search?q={searchQuery}+world+of+darkness"
    response_url1 = requests.get(url1)
    if not response_url1:
        response_url2 = requests.get(url2)
        if not response_url2:
            response_url3 = requests.get(url3)
            if not response_url3:
                await message.answer('Я ничего не нашёл по вашему запросу')
            else:
                await message.answer(url3)
        else:
            await message.answer(url2)
    else:
        await message.answer(url1)


@db.message_handler(commands=['Roll', 'roll', 'r'])
async def roll_dice(message: types.Message):
    """Function for base rolling"""
    try:
        await message.answer_dice(emoji="🎲")
        result = roll(message.text.split(' '))
        await message.answer('Результат броска: {}. Успехов: {}'.format(result[0], result[1]))
    except ValueError:
        await message.answer("Пожалуйста, укажите параметры [количество, тип, сложность] после команды /roll через пробел")


@db.message_handler(commands=['Roll3r', 'roll3r', 'r3r'])
async def roll_diceV3(message: types.Message):
    """Fuction for rolling dices according to the rules of Revised Edition"""
    try:
        await message.answer_dice(emoji="🎲")
        result = rollV3(message.text.split(' '))
        await message.answer('Результат броска: {}. Успехов: {}'.format(result[0], result[1]))
    except ValueError:
        await message.answer("Пожалуйста, укажите параметры [количество, тип, сложность] после команды /roll3r через пробел")


@db.message_handler(commands=['Roll4r', 'roll4r', 'r4r'])
async def roll_diceV4(message: types.Message):
    """Fuction for rolling dices according to the rules of 20th Edition"""
    try:
        await message.answer_dice(emoji="🎲")
        result = rollV4(message.text.split(' '))
        await message.answer('Результат броска: {}. Успехов: {}'.format(result[0], result[1]))
    except ValueError:
        await message.answer("Пожалуйста, укажите параметры [количество, тип, сложность] после команды /roll4r через пробел")


@db.message_handler()
async def version(message: types.Message):
    if message.text == '3-я редакция':
        await message.answer("Чтобы кинуть кубы по 3-й редакции (Revised), напишите команду '/roll3r' или '/r3r'")
    elif message.text == '4-я редакция':
        await message.answer("Чтобы кинуть кубы по 4-й редакции (20th), напишите команду '/roll4r' или '/r4r'")
    elif message.text == 'Поиск':
        await message.answer("Для поиска информации введите команду '/search' и то, что хотите найти")


if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)