# -*- coding: utf-8 -*-

# імпорт модулів
from assets.bot import JokeiBot

import json
import server


# зчитування токену з файлу
with open("E:/PROGRAMMING/jokei/assets/mas/server_data.json", "r") as file:
    TOKEN = json.load(file)["token"]


# створення об'єкту JokeiBot та запуск бота
jokei_bot = JokeiBot()  
server.server()

jokei_bot.run(TOKEN)   
