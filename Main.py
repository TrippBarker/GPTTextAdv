import os
import openai

openai.api_key_path = 'D:\KEYS\TextAdvKey.txt'
model_engine = "text-davinci-003"

userSituations = ["Hands bound behind back."]

userGoodActions = ["Find sharp object."]

userBadActions = ["Struggle."]

userCurrentState = 0
hintCountdown = 3

def promptGPT(userAction):
    indoctronation = "You are a bot and your only role is to determine if a SENTENCE is similar to one of two STATEMENTS. If the SENTENCE is similar to STATEMENT ONE, only respond with the word 'ONE', if the SENTENCE is similar to STATEMENT TWO, only respond with the word 'TWO'. If neither of the STATEMENTS are similar with the SENTENCE, respond with 'NONE'."
    indoctronation += "\nSENTENCE: " + userAction + "."
    indoctronation += "\nSTATEMENT ONE: " + userGoodActions[userCurrentState]
    indoctronation += "\nSTATEMENT TWO: " + userBadActions[userCurrentState]
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
    print("Current Situation: " + userSituations[userCurrentState])
    action = input("What do you do?\n> ")
    gptResponse = promptGPT(action).upper().strip()
    if (userCurrentState == 0):
        if (gptResponse == "ONE"):
            hintCountdown = 3
            userCurrentState += 1
            print("You remember that you have a knife in your back pocket! Reaching carefully, you manipulate the blade open and saw away at the rope... You're free!!")
        elif (gptResponse == "TWO"):
            print("You squirm about, something sharp pokes at you from your back pocket...")
        else:
            if (hintCountdown == 0):
                hintCountdown = 3
                print("Nothing seems to be working... Maybe look for something sharp to cut the rope with...")
            else:
                print("No... That doesn't seem right...")
                hintCountdown -= 1
            
