from question_model import Question
from data import question_data
question_bank = []
for question in question_data:
   # append qeustion object to a question bank list
   question_bank.append(Question(question["text"],question["answer"]))
print(question_bank[0].text)