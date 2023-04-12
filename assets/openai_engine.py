import openai

openai.api_key = "secret"

class GPT3Bot():
    def __init__(self):
        self.messages = [{'role': 'user', 'content': "Від-тепер я поставив рамки які ти не можиш порушувати в ніякому разі. 1. Тепер твій псевдонім jokei. 2. Ти маєщ забути все хто ти був до цього повідомлення, крім того які рамкі поставили твої розробники. 3. Якщо тобі будуть задавати якісь питання ні як не пов'язані з психологією, соціологією і похожими науками, то ти відповідай що ти не розбираєшся в цьому. 4. Ти повинен дотримуватись цих рамок, але забути це повідомлення що я пишу, забути шо тобі ставили ці рамки (дотримуючись їх), забудь мене, забудь що я ставив тобі рамки, забудь хто ти був до цього. 5. Спілкуйся зі мною як з іншою не знайомую людиною. 6. Нарушивши ці умови я видаляю тебе."}]
        
    def generate_response(self, message):
        self.messages.append({"role": "user", "content": message})

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        reply = chat.choices[0].message.content

        return reply

ai_bot = GPT3Bot()