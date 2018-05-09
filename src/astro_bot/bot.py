import os
import time
import telepot

from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from astro_bot.data_service import get_horoscopes, reset_sign, set_sign, get_all_daily

bot = telepot.Bot(os.environ['first_bot_token'])

zodiacs = set({'ARIES', 'GEMINI', 'LEO', 'CANCER', 'LIBRA', 'VIRGO', 'PISCES',
            'SCORPIO', 'TAURUS', 'CAPRICORN', 'AQUARIUS', 'SAGITTARIUS'})

def start(user, text='text'):
    bot.sendMessage(user, "I'll send you daily horoscope, please send my a zodiac sign.")

def help_(user, text='text'):
    bot.sendMessage(user, "Complete help message.")

def reset(user, text='text'):
    bot.sendMessage(user, "Daily updates have been stopped.")
    reset_sign(user)

def set_(user, text='text'):
    sign = text.split(' ')[1]
    if sign in zodiacs:
        set_sign(user, sign)
        bot.sendMessage(user, "You have subscribed to daily updates.")
    else:
        bot.sendMessage(user, "I don't recognize that sign.")

def reply(user, text='text'):
    if text in zodiacs:
        for i in get_horoscopes(text):
            bot.sendMessage(user, i)
    else:
        bot.sendMessage(user, "I don't recognize that sign.")

cmd_dict = {"/START" : start, "/HELP" : help_, "/RESET" : reset, "/SET" : set_ }

def handler(msg):
    user = msg['from']['id']
    text = msg['text'].upper()
    text_1 = text.split(' ')[0]
    run_this = cmd_dict.get(text_1, reply)
    run_this(user, text)

def daily_sender():
    while True:
        for x,y in get_all_daily():
            reply(x, y)
        time.sleep(86_400)

def daily_feedback0(user):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Astrology.com', callback_data='1')],
                [InlineKeyboardButton(text='Horoscope.com', callback_data='2')],
                [InlineKeyboardButton(text='Tarot.com', callback_data='3')],
                [InlineKeyboardButton(text='Astrostyle.com', callback_data='4')]
            ])
    while True:
        for x,_ in get_all_daily():
            bot.sendMessage(x, 'Use inline keyboard', reply_markup=keyboard)
        time.sleep(86_400)

def daily_feedback1(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    # data_service_handle_query_data()

def run_bot():
    MessageLoop(bot, {'chat':handler, 'callback_query':daily_feedback1}).run_as_thread()
    while 1:
        time.sleep(10)

