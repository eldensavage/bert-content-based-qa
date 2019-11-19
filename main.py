from bert import ODQA


model = ODQA('model')

with open("content.txt", "r") as data:
    content = data.read()

question = input("Enter Your Question: ")

answer = model.predict(content,question)

print(answer['answer'])
