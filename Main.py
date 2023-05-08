import os
import openai

openai.api_key_path = 'D:\KEYS\TextAdvKey.txt'
model_engine = "text-davinci-003"

userSituations = ["Hands bound behind back."]

userGoodActions = ["Find sharp object."]

userBadActions = ["Struggle."]

userCurrentState = 0

def promptGPT(userAction):
    indoctronation = "You are a bot and your only role is to determine if a SENTENCE is similar to one of two STATEMENTS. If the SENTENCE is similar to STATEMENT ONE, only respond with the word 'ONE', if the SENTENCE is similar to STATEMENT TWO, only respond with the word 'TWO'. If neither of the STATEMENTS are similar with the SENTENCE, respond with 'NONE'."
    indoctronation += "\nSENTENCE: " + userAction + "."
    indoctronation += "\nSTATEMENT ONE: " + userGoodActions[userCurrentState]
    indoctronation += "\nSTATEMENT TWO: " + userBadActions[userCurrentState]
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