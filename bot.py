#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pickle
from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import os
import pytz
import datetime
from datetime import datetime
tz_NY = pytz.timezone('Europe/Moscow')
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M"))

app = Client('cmd', api_id=15897262, api_hash='90476d9c65a86b03837e1e249314cd75')

app.start()

app.stop()


if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
            
@app.on_message(filters.command('start_time', prefixes='.') & filters.me)
def time_bot(_, msg):
    tz_NY = pytz.timezone('Europe/Moscow')
    datetime_NY = datetime.now(tz_NY)
    msg.edit('<b>Запущен Auto-name-time бот, ожидайте</b>')
    sleep(2)
    while True:
        sleep(0.1)
        msg.edit('<b>Запущен!</b>')
        while True:
            sleep(60)
            count = app.get_chat_members_count(chat_id=-1001786706929)
            tz_NY = pytz.timezone('Europe/Moscow')
            datetime_NY = datetime.now(tz_NY)
            app.update_profile(first_name=f"ᅠTime ᅠ : {datetime_NY.strftime('%H:%M')} ",
                               bio=f"Autobio by @fazzers_skrypt [{count}]")

app.run()
