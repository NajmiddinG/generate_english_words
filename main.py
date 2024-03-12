import logging
from flask import Flask, request
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from read_english_dictionary import get_words

API_TOKEN = '7003670909:AAHW9sf_aO3hSAIjDfEfqJ61Nu8UBCmLgIs'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
async def webhook():
    if request.method == 'POST':
        update = types.Update(**request.json)
        await dp.process_updates([update])
        return 'ok'

@dp.message_handler(commands=['start'])
async def handle_start_command(message: types.Message):
    try: await message.reply(f"👋 Hello  @{message.from_user.first_name}‍. ")
    except: await message.reply("👋 Hello.")

@dp.message_handler()
async def handle_all_messages(message: types.Message):
    letters = ''
    for i in message.text:
        if i.isalpha(): letters+=i
    if 0<len(letters)<8:
        await message.reply(get_words(letters))
    else:
        await message.reply("English harflari uzunligi 1-7 oralig'ida bo'lishi kerak!")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


# import logging
# from aiogram import Bot, Dispatcher, types, executor
# from aiogram.dispatcher import FSMContext
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from read_english_dictionary import get_words

# API_TOKEN = '7003670909:AAHW9sf_aO3hSAIjDfEfqJ61Nu8UBCmLgIs'
# bot = Bot(token=API_TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)


# @dp.message_handler(commands=['start'])
# async def handle_start_command(message: types.Message):
#     try: await message.reply(f"👋 Hello  @{message.from_user.first_name}‍. ")
#     except: await message.reply("👋 Hello.")

# @dp.message_handler()
# async def handle_all_messages(message: types.Message):
#     letters = ''
#     for i in message.text:
#         if i.isalpha(): letters+=i
#     if 0<len(letters)<8:
#         await message.reply(get_words(letters))
#     else:
#         await message.reply("English harflari uzunligi 1-7 oralig'ida bo'lishi kerak!")

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     executor.start_polling(dp, skip_updates=True)