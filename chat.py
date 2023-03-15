import openai

openai.api_key = ''

class Chat():

    def __init__(self, starters = [], model="gpt-3.5-turbo"):
        self.starters = starters
        self.dialogue = []
        self.model = model

        for s in self.starters:
            self.ask(s)

        self.user_prompt()

    def ask(self, prompt):
        self.dialogue.append({"role": "user", "content": prompt})

        self.request()

    def request(self):
        result = openai.ChatCompletion.create(model=self.model, messages=self.dialogue)

        output = result['choices'][0]['message']['content']
        print(output)

        self.dialogue.append({"role": "assistant", "content": output})

    def user_prompt(self):
        prompt = input('>>> ')

        self.ask(prompt)
        self.user_prompt()

Chat()