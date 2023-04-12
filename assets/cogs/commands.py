# -*- coding: utf-8 -*-

import sys
sys.path.append('E:/PROGRAMMING/jokei/assets')

import disnake
from disnake.ext import commands

from openai_engine import ai_bot

import json
with open("E:/PROGRAMMING/jokei/assets/mas/aizek_test_questions.json", "r", encoding='utf-8') as file:
    aizek_test_questions = json.load(file)

user_aizek_test_id_1 = {

}

user_aizek_test_id_2 = {

}


user_aizek_test_question_id = {

}

class JokeiCommands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # вивід списку команд
    @commands.slash_command(description="Написавши цю команду ви отримаєте інформацію про стандартні команди бота.")
    async def help(self, ctx):
        embed = disnake.Embed(
            title="Інформація про Jokei чат-бота.",
            description="Бот Python Discord створенний для психологічної підтримки. Він може проводити опитування, давати поради, робити соціальні експерименти.",
            color=disnake.Colour(0xffffff)
        )
        embed.add_field(
            name="Команди",
            value="```?temperament - Бот проводить коротку діагностику та надає користувачеві тип його темпераментру. Тест буде працювати для людей 12-18 років. ```\n"
                  "```?experiment - Бот пропонує соціальні експерименти для участі користувачів та надає інформацію про них.\" ```\n"
                  "```?advice - Бот надає користувачам поради щодо того, як впоратися зі стресом, тривогою та іншими емоціями.```\n"
                  "```?survey - Бот проводить опитування на певну тему, пов'язану з психологією та соціологією, та надає результати. ```\n"
                  "```?help - Бот надає короткий список команд, які можна використовувати для взаємодії з ним.```"
                  "```?about -  Бот надає короткий огляд психології, соціології та інших відповідних тем.```"
                  "```?sleep -  Бот надає користувачам поради та вправи для покращення якості їх сну та загального фізичного здоров'я.```"
                  "```?send - Ви надсилаєте будь яке павідомлення боту щоб він вам відповів.```"
                  "```?setup_chat - Бот створить особистий чат де ти зможеш з ним спілкуватись.```")
                  
        
        embed.set_image(url="https://media.tenor.com/LUWHCx7ilkkAAAAC/rei-ayanami.gif")
        await ctx.send(embed=embed)

    @commands.slash_command(description="Ця команди дозволяє вам спілкуватись з цим ботом.")
    async def send(self, ctx, message): 
        await ctx.response.defer()
        response = ai_bot.generate_response(message)
        await ctx.followup.send(response)

    # The slash command that responds with a message.
    @commands.slash_command(description="Тут ви отримаєете поради як правильно вести здоровий сон.")
    async def sleep(inter: disnake.ApplicationCommandInteraction):

        embed = disnake.Embed(
            title="Проблеми зі сном — типовий наслідок зустрічі з травматичною подією.",
            description="Щоб лягти спати, людині доводиться знижувати свою пильність. І це особливо важко тим, хто пережив стрес.\n\nТипові проблеми зі сном:\n\n```1. Важко заснути```\n```2. Нереривчастий сон```\n```3. Важко прокидатись```\n```4. Сонливість```\n```5. Нічні жахіття```",
        )
    
        await inter.response.send_message(
            embed=embed,
            components=[
                disnake.ui.Button(label="Продовжити", style=disnake.ButtonStyle.success, custom_id="s11"),
                disnake.ui.Button(label="Зупинитись", style=disnake.ButtonStyle.danger, custom_id="s12")
            ]
        )


    @commands.slash_command(description="")
    async def survey(self, ctx): 
        pass

    @commands.slash_command(description="Допомога впортись зі стресом.")
    async def advice(inter: disnake.ApplicationCommandInteraction): 
        
        advice_embed = disnake.Embed(title="Привіт! Ти як?",
                                    description="Мені дуже важливо знати, як ти зараз — чи відчуваєш напругу, неспокій, нервозність або тривогу?\nОціни свій рівень стресу в ці дні ⬇️"
                                    )
        
        await inter.response.send_message(
            embed=advice_embed,
            components=[
                disnake.ui.Button(label="В мене не має стресу!", style=disnake.ButtonStyle.secondary, custom_id="a11"),
                disnake.ui.Button(label="Є помірний стрес.", style=disnake.ButtonStyle.secondary, custom_id="a12"),
                disnake.ui.Button(label="Дуже сильний.", style=disnake.ButtonStyle.secondary, custom_id="a13")
            ]
        )

    @commands.slash_command(description="Визначити твій тип темпераметру.")
    async def temperament(inter: disnake.ApplicationCommandInteraction): 
        
        temperament_embed = disnake.Embed(title="Визначення темпераметру.", description="Цей тест на визначення тип темпераменту людини. Він базується на трьох основних типах темпераменту: сангвінік, холерик та флегматик. Тест складається з питань, які оцінюють реакцію людини на різні ситуації та її уподобання. Інформація, отримана під час тестування, допомагає визначити тип темпераменту людини та рекомендувати певні методи роботи та поведінки, що сприятимуть успішному функціонуванню та досягненню мети.")

        await inter.response.send_message(
            embed=temperament_embed,
            components=[
                disnake.ui.Button(label="Продовжити.    ", style=disnake.ButtonStyle.success, custom_id="t_yes"),
                disnake.ui.Button(label="Назад.", style=disnake.ButtonStyle.danger, custom_id="t_no"),
                disnake.ui.Button(label="Інформація.", style=disnake.ButtonStyle.url, url="https://chsresults.com/blog/test/eysencks-personality-inventory-epi-extroversionintroversion/"),
            ]
        )

    @commands.slash_command(description="")
    async def experiment(self, ctx): 
        pass


    @commands.Cog.listener()
    async def on_button_click(self, inter: disnake.MessageInteraction):
        
        # здоровий сон

        embed_sleep = disnake.Embed(
            title="Для поліпшення сну тобі необхідно дотримуватись 3 рекомедацій:",
            description="```1. Буденність```\n```2. Середовище```\n```3. Стиль життя```\n"
        )

        embed_s21 = disnake.Embed(
            title="Буденість."
        )

        embed_s21.add_field(name="Рекомендації для здорового сну",
                            value=f"```{inter.user.name}, для того, щоб забезпечити собі здоровий сон, важливо лягати і прокидатися приблизно в один і той самий час. Рекомендований час сну - від 7 до 9 годин на добу, але не забувай враховувати і свої власні потреби відпочинку.\n\n```"
                            "```Якщо в тебе з'явиться бажання вдень задрімати, то оптимальною тривалістю сну будуть 10-20 хвилин, що дозволить тобі легко і швидко прокинутися та отримати енергію на решту дня.\n\n```"
                            "```Також важливо більше часу проводити на вулиці, зокрема на сонячному світлі, але уникати яскравого світла за 2 години до сну.\n```"
                            "```Розумію, що не завжди можна дотримуватися цих рекомендацій, але стеж за своїм сном та намагайся перетворити його на щось регулярне та стале для твого здоров'я.```"
        )

        embed_s22 = disnake.Embed(
            title="Середовище.",
            description="```Важливим фактором сну є середовище, в якому ти засинаєш.Створи атмосферу, що заспокоює твій розум і розслабляє тіло перед сном.```"
        )

        embed_s22.add_field(name="Рекомендації для здорового сну",
                            value=f"```Якщо не маєш можливості контролювати своє оточення, є один корисний спосіб підготуватися до сну - уявити щось приємне перед засипанням. Просто закрий очі та уяви щось приємне, що дозволить тобі відчути позитивні емоції. Проте, якщо у тебе є можливість прийняти ванну з бульбашками, то щасливчик! Це, безсумнівно, чудовий спосіб розслабитися перед сном, тому я б обрав саме цей варіант.\n```", 
                            inline=False
        )

        embed_s22.add_field(name="Перед сном.",
                            value=f"```{inter.user.name}, намагайся уникати будь-яких подразників безпосередньо перед сном (наприклад, електронних пристроїв). Я розумію, що тобі, можливо, дуже хочеться почитати новини або переглянути свою стрічку в Instagram. Але, будь ласка, відклади це на завтра. Зараз тобі потрібно спати, а не думати про прочитане/побачене. \n\n```"
                            f"```{inter.user.name}, щоб максимально підготувати свій розум до сну, варто уникати будь-яких стимулів безпосередньо перед сном, таких як перегляд соціальних мереж чи читання новин. Я розумію, що можливо дуже звабливо відкрити свій телефон та почитати щось цікаве, але це може завадити твоєму сну. Тому, будь ласка, залиш це на завтра, коли ти будеш більш свіжим та відпочившим, а зараз сконцентруйся на тому, щоб максимально розслабитися та готуватися до сну.\n```", 
                            inline=False
        )

        embed_s22_2 = disnake.Embed(title="Про місце сну",description="```Давай перейдемо до місця, де ти будеш спати.\n Перш за все, переконайся, що твоє спальне місце є комфортним для тебе. Зверни увагу на матрац, температуру в кімнаті, рівень шуму та освітлення. Якщо це можливо, постарайся поліпшити ці умови, щоб забезпечити максимальний комфорт під час сну.\n\n```"
                            "```Обмеж свою спальню тільки функцією сну. Не використовуй її для їжі, читання, перегляду відео або будь-яких інших дій, крім відпочинку та сну. Якщо у тебе немає окремої спальні, спробуй знайти місце, де можна спати без розіграшів або будь-яких дій, що можуть перешкоджати відпочинку.```")
        
        embed_s23 = disnake.Embed(title="Важливим фактором сну є стиль твого життя. ", 
                                  description="```1. Додай фізичну активність з помірною інтенсивністю — не менше 30 хвилин 5 днів на тиждень.\n\nНе забувай, що в цьому контексті зараховується будь-яка фізична активність: швидко прогулятися до магазину, спуститися/піднятися сходами тощо.\nЗа 2 години до сну уникай інтенсивних вправ.\n\n```"
                                  "```2. Якщо ти багато працюєш, будь ласка, не роби цього безпосередньо перед сном.💡Відпочинок і сон — найкраща інвестиція у власну продуктивність.\n\n```"
                                  "```3. Дотримуйся здорового та збалансованого харчування.Спробуй ці рекомендації. Потім розкажеш мені про свій прогрес.\n\n```"
                                  "```4. Якщо маєш можливість, вибирай здорову їжу, що доступна тобі зараз. Будь ласка, не забувай про це.\n\n```"
                                  "```5. Увечері уникай стимуляторів (кофеїн і нікотин), алкоголю та важкої їжі.```")
        
        if inter.component.custom_id == "s11":
            await inter.response.send_message(
                embed=embed_sleep,
                components=[
                    disnake.ui.Button(label="1️⃣ Буденість", style=disnake.ButtonStyle.secondary, custom_id="s21"),
                    disnake.ui.Button(label="2️⃣ Середовище", style=disnake.ButtonStyle.secondary, custom_id="s22"),
                    disnake.ui.Button(label="3️⃣ Стиль Життя", style=disnake.ButtonStyle.secondary, custom_id="s23")
                ])
            
        elif inter.component.custom_id == "s12":
            await inter.response.send_message("```Команда була припинена.```")

        elif inter.component.custom_id == "s21":
            await inter.response.send_message(embed=embed_s21)

        elif inter.component.custom_id == "s22":
            await inter.response.send_message(embeds=[embed_s22, embed_s22_2])

        elif inter.component.custom_id == "s23":
            await inter.response.send_message(embed=embed_s23)

        # тест айзека

        

        if inter.component.custom_id == "t_yes":

            user_aizek_test_question_id[str(inter.user.id)] = 1
            user_aizek_test_id_1[str(inter.user.id)] = 1
            user_aizek_test_id_2[str(inter.user.id)] = 1

            embed_tn = disnake.Embed(title=f"Дайте відповідь на це питання {user_aizek_test_question_id[str(inter.user.id)]}/57",
                                    description=aizek_test_questions[str(user_aizek_test_question_id[str(inter.user.id)])])
            

            await inter.response.send_message(
                embed=embed_tn,
                components=[
                    disnake.ui.Button(label="Так.", style=disnake.ButtonStyle.success, custom_id=f"t{user_aizek_test_question_id[str(inter.user.id)]}1"),
                    disnake.ui.Button(label="Ні.", style=disnake.ButtonStyle.danger, custom_id=f"t{user_aizek_test_question_id[str(inter.user.id)]}2")
                ])

        elif inter.component.custom_id == "t_no":
            await inter.response.send_message("```Назад.```")

        elif list(inter.component.custom_id)[0] == "t" and user_aizek_test_question_id[str(inter.user.id)] != 58:  

            t_index = user_aizek_test_question_id[str(inter.user.id)]

            if list(inter.component.custom_id)[-1] == 1:
                
                if t_index in [1, 3, 8, 10, 13, 17, 22, 25, 27, 39, 44, 46, 49, 53, 56]:
                    user_aizek_test_id_1[str(inter.user.id)] += 1

                if t_index in [2, 4, 7, 9, 11, 14, 16, 19, 21, 23, 26, 28, 31, 33, 35, 38, 40, 43, 45, 47, 50, 52, 55, 57]:
                    user_aizek_test_id_2[str(inter.user.id)] += 1

            else:
                if t_index in [5, 15, 20, 29, 32, 34, 37, 41, 51]:
                    user_aizek_test_id_1[str(inter.user.id)] += 1

            user_aizek_test_question_id[str(inter.user.id)] += 1

            embed_tn = disnake.Embed(title=f"Дайте відповідь на це питання {user_aizek_test_question_id[str(inter.user.id)]}/57",
                                    description=aizek_test_questions[str(user_aizek_test_question_id[str(inter.user.id)])])

            await inter.response.send_message(
                embed=embed_tn,
                components=[
                    disnake.ui.Button(label="Так.", style=disnake.ButtonStyle.success, custom_id=f"t{user_aizek_test_question_id[str(inter.user.id)]}1"),
                    disnake.ui.Button(label="Ні.", style=disnake.ButtonStyle.danger, custom_id=f"t{user_aizek_test_question_id[str(inter.user.id)]}2")
                ]) 
            
        elif user_aizek_test_question_id[str(inter.user.id)] == 58:

            result_embed = disnake.Embed(title=f"Вітаю! Ви дали відповідь на всі питання 57/57",
                                description="Ось ваші результати:")
            


            if user_aizek_test_id_1[str(inter.user.id)] >= 0 and user_aizek_test_id_1[str(inter.user.id)] <= 10:
                result_embed.add_field(name="Екстраверсія", 
                                    value="```Ви інтроверт, зазвичай ви віддаєте перевагу проведенню часу сам на сам з собою, ніж бути в компанії багатьох людей. Ви можете бути більш складною в спілкуванні з незнайомими людьми, особливо на початку знайомства, але може стати дуже відкритою та дружелюбною, якщо ви почуваєтесь комфортно.\n\n Ви можете бути дуже творчою та глибоко думати про різні речі, ви можете проводити час, читаючи, створюючи щсоь або працюючи над проектами, які вас цікавлять. Ви можете відчувати, що ви найбільш продуктивні, коли вона знаходиться в самотності, де може зосередитися на своїх думках та ідеях.\n\nЗагалом, ви можете бути дуже цікавою та унікальною особистістю, яка насолоджується проведенням часу в самотності та може мати глибокі роздуми про світ навколо себе.```",
                                    inline=False)

            elif user_aizek_test_id_1[str(inter.user.id)] >= 15 and user_aizek_test_id_1[str(inter.user.id)] <= 24:
                result_embed.add_field(name="Екстраверсія", 
                                    value="```Ви екстравертна людина. Ти завжди знаходишся в центрі уваги, а твій оптимізм та енергія надихає тих, хто оточує тебе. Ти любиш проводити час з друзями та новими людьми, йти на вечірки та заходи, та завжди готова поспілкуватися з кимось новим. Твоя комунікабельність та відкритість дозволяє тобі легко знаходити спільну мову з людьми з різних культур і соціальних груп. ```",
                                    inline=False)
                 
            elif user_aizek_test_id_1[str(inter.user.id)] >= 11 and user_aizek_test_id_1[str(inter.user.id)] <= 14:
                result_embed.add_field(name="Екстраверсія", 
                                    value="```Ви є амбівертом, ви людина яка може проявляти як інтровертні, так і екстравертні риси характеру. Ти спілкуєшся з людьми та насолоджуєшся цим, але тільки коли тобі це потрібно. Іноді тобі буває потрібно знайти час для самотньої роботи, щоб сконцентруватися на своїх думках та завданнях. Також, ти можеш відчувати втому після тривалого спілкування та потребувати часу для відновлення енергії. Але взагалі ти можеш досить легко знаходити спільну мову з людьми та насолоджуватися інтерактивними соціальними ситуаціями, коли ти відчуваєш себе комфортно. ```",
                                    inline=False)



            if user_aizek_test_id_2[str(inter.user.id)] >= 0 and user_aizek_test_id_1[str(inter.user.id)] <= 10:
                result_embed.add_field(name="Невротизм", 
                                    value="```Ви емоційно стійка людина.```",
                                    inline=False)

            elif user_aizek_test_id_2[str(inter.user.id)] >= 11 and user_aizek_test_id_1[str(inter.user.id)] <= 16:
                result_embed.add_field(name="Невротизм", 
                                    value="```Ви емоційно вразлива людина.```",
                                    inline=False)
                 
            elif user_aizek_test_id_2[str(inter.user.id)] >= 17 and user_aizek_test_id_1[str(inter.user.id)] <= 22:
                result_embed.add_field(name="Невротизм", 
                                    value="```В вас з’являються окремі ознаки розхитаності нервової системи```",
                                    inline=False)

            elif user_aizek_test_id_2[str(inter.user.id)] >= 23 and user_aizek_test_id_1[str(inter.user.id)] <= 24:
                result_embed.add_field(name="Невротизм", 
                                    value="```Невротизм, що межує з патологією, можливий зрив, невроз.```",
                                    inline=False)

    @commands.slash_command(description="Цією командою ви створюєте особистий канал для себе, який бачите тільки ви")
    async def create_channel(self, ctx): 
        guild = ctx.guild
        category = disnake.utils.get(guild.categories, id=1095448300586532894)
        channel_name = f'📃┃{ctx.author.name}-channel'
        existing_channel = disnake.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            # створення нового текстового каналу
            await category.create_text_channel(channel_name)
            await ctx.send(f"Канал {ctx.author.name}-channel був успішно створений!")
            
        else:
            await ctx.send(f"Канал вже є створенний!")


def setup(bot: commands.Bot):
    bot.add_cog(JokeiCommands(bot))





