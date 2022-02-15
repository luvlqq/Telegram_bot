import random
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='')
dp = Dispatcher(bot)

help_message = ('Данный бот был написан на коленке за n-ый промежуток времени. Он умеет много чего, если правильно с ним взаимодействовать и РАЗГОВАРИВАТЬ на дед внутри темы. Всем спасибо все свободны.')
th_min_sev = ('Эй, ты что тут считать собрался, клоун')
track = ('Гуль дед инсайд сборник русских хитов 2007 находится тут:'
         'https://www.youtube.com/watch?v=DAWphDKl948')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


@dp.message_handler(lambda message: message.text =='1000-7')
async def scheti(message: types.Message):
    await message.reply(th_min_sev)


@dp.message_handler(lambda message: message.text =='треки')
async def music(message: types.Message):
    await message.answer(track)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Что-то умное','Пикча']
    bat = ['Что ты умеешь ?']
    nBut = ['Хозяин']
    keyboard.insert(*nBut)
    keyboard.add(*buttons)
    keyboard.insert(*bat)
    await message.answer("Ну привет гуль ass ранга. Может хочешь посчитать? ", reply_markup=keyboard)


# @dp.message_handler(content_types=types.ContentType.ANY)
# async def echo(message: types.Message):
#     if message.text:
#         # Тут делайте всё, что нужно, если юзер отправил обычное сообщение
#         if message == '1000-7':
#             await message.answer("Вы отправили текст!")
#     else:
#         # Всё, что не попадает под текст
#         await message.answer("Что-то не на гулином")


@dp.message_handler(lambda message: message.text == "Что-то умное")
async def citata(message: types.Message):
    await message.answer(random.choice(list(open('citati.txt', encoding= 'UTF-8'))))


@dp.message_handler(lambda message: message.text == "Хозяин")
async def owner(message: types.Message):
    await message.answer('Самый главный тру дед инсайд канеки кен трипл S ранга обитает ''<a href="https://instagram.com/yvnglual">тут.</a>',parse_mode="HTML")


@dp.message_handler(lambda message: message.text == "Что ты умеешь ?")
async def info(message: types.Message):
    await message.answer('Я умею немного общаться. Ты можешь спросить у меня дед инсайд треки(треки), посчитать со мной 1000-7(1000-7) и позже будет еще. Но пока моему хозяину немного впадлу что-то добавлять еще.')


#
# @dp.message_handler(lambda message: message.text == "Пикча")
# async def pikcha(message: types.Message):
#     await message.answer(for filename in os.listdir('images'):
#         filename[filename.rfind(".") + 1:] in ['jpg', 'jpeg', 'png'])


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()




