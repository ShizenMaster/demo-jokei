# імпорт модулів
import disnake
from disnake.ext import commands

# створення класу для Jokei бота
class JokeiBot(commands.Bot):
    def __init__(self):
        # задання префікса команд
        super().__init__(command_prefix="?", intents=disnake.Intents.all())

        # додавання функції, яка виконується при запуску бота
        self.load_extension("assets.cogs.commands")

        self.add_listener(self.on_ready)

    async def on_ready(self):
        # виконується при запуску бота
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        await self.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="shiza?"))

