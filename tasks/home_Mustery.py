import random

class Mystery:
    COMPLEXITY = 0

    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def quiz(self):
        print(self.question)
        self.choices.append(self.answer)

        if random.randint(0, 1):
            self.lst = self.answer.split(',')
            self.choices += self.lst[:random.randint(1, len(self.lst))]
        random.shuffle(self.choices)
        self.data = {k: v for k, v in enumerate(self.choices)}
        for k, v in self.data.items():
            print(f"{k}. {v}")
        self.res = input('Enter the answer number or skip the question "next":')

        if self.res == 'next':
            return 0
        elif self.data.get(int(self.res)) == self.answer:
            return 3
        else: return -3









q1 = Mystery(question="Первые четыре буквы алфавита.",
answer="А, Б, В, Г",
choices=[
"Ю, Щ, А, Я",
"Ж, Д, В, Н",
"П, Э, Н, У",
"Х, З, П, К"
])


print(q1.quiz())











