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
        [types.KeyboardButton(text="Revised Edition")],
        [types.KeyboardButton(text="20th Edition")],
        [types.KeyboardButton(text="Search")],
        [types.KeyboardButton(text="Support me")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.reply(r"Hello. I am DiceBotWoD. Print '/roll' or '/r' and dice parameters separated by space, and I will throw dices for you. For example: '/r 7 10 6'", reply_markup=keyboard)


@db.message_handler(commands=['dice', 'Dice'])
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


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
                await message.answer("I didn't find anything based on your request")
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
        await message.answer('Result: {}. Successes: {}'.format(result[0], result[1]))
    except ValueError:
        await message.answer("Please, specify the parameters [number of dices, the edge and the difficulty] after the /roll command separated by a space")


@db.message_handler(commands=['Roll3r', 'roll3r', 'r3r'])
async def roll_diceV3(message: types.Message):
    """Fuction for rolling dices according to the rules of the Revised Edition"""
    try:
        await message.answer_dice(emoji="🎲")
        result = rollV3(message.text.split(' '))
        await message.answer('Result: {}. Successes: {}'.format(result[0], result[1]))
    except ValueError:
        await message.answer("Please, specify the parameters [number of dices, the edge and the difficulty] after the /roll3r command separated by a space")


@db.message_handler(commands=['Roll4r', 'roll4r', 'r4r'])
async def roll_diceV4(message: types.Message):
    """Fuction for rolling dices according to the rules of the 20th Edition"""
    try:
        await message.answer_dice(emoji="🎲")
        result = rollV4(message.text.split(' '))
        await message.answer('Result: {}. Successes: {}'.format(result[0], result[1]))
    except ValueError:
        await message.answer("Please, specify the parameters [number of dices, the edge and the difficulty] after the /roll4r command separated by a space")


@db.message_handler()
async def version(message: types.Message):
    if message.text == 'Revised Edition':
        await message.answer("To roll dices according to the Revised Edition use the command '/roll3r' or '/r3r' with parameters")
    elif message.text == '20th Edition':
        await message.answer("To roll dices according to the 20th Edition use the command '/roll4r' or '/r4r' with parameters")
    elif message.text == 'Search':
        await message.answer("To search for information use the command '/search' with the word or phrase for which you want to find information")
    elif message.text == 'Support me':
        await message.answer("If you want to support me, you can send a donation to one of these cards:\nyour_card_number_1\nyour_card_number_2\nThank you!")


if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
