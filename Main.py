import os
import openai

openai.api_key_path = 'D:\KEYS\TextAdvKey.txt'
model_engine = "text-davinci-003"

userSituations = ["Hands bound behind back."]

userGoodActions = ["Find sharp object."]

userBadActions = ["Struggle."]

userCurrentState = 0

def promptGPT(userAction):
    indoctronation = "You are a bot and your only role is to determine if a sentence is similar to one of two statments. If the sentence is similar to the first statement, only respond with the word 'ONE', if the sentence is similar to the second statment, only respond with the word 'TWO'. If neither of the statements are similar, respond with 'NEITHER'."
    indoctronation += "\nThe sentence is as follows: " + userAction
    indoctronation += "\nThe first statement is as follows: " + userGoodActions[userCurrentState]
    indoctronation += "\nThe second statement is as follows: " + userBadActions[userCurrentState]
    print(indoctronation)
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = indoctronation,
        max_tokens = 3,
        n = 1,
        stop = None,
        temperature = 0.1,
    )
    return completion.choices[0].text

with open ('intro.txt', 'r') as file:
    print(file.read())

playing = True
while (playing):
    action = input("What do you do?\n> ")
    print(promptGPT(action))