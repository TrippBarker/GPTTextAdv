import os
import openai

openai.api_key_path = 'D:\KEYS\TextAdvKey.txt'
model_engine = "text-davinci-003"

userSituations = ["Hands bound behind back.", 
                  "Standing in the Wizard's camp"]

userGoodActions = ["Find sharp object.", 
                   "Run away."]

userBadActions = ["Struggle.", 
                  "Sit and wait."]

goodActionResponse = ["You remember that you have a knife in your back pocket! Reaching carefully, you manipulate the blade open and saw away at the rope... You're free!!",
                      "With no real sense of direction, you spring to your feet and start running!"]

badActionResponse = ["You squirm about, something sharp pokes at you from your back pocket...",
                     "You sit there... Twiddling your thumbs like a dumb-dumb"]

hintResponse = ["Nothing seems to be working... Maybe look for something sharp to cut the rope with...",
                "Nothing seems to be working... Maybe... I dunno.... RUN??!!!??"]


class GameState:
    userCurrentState = 0
    hintCountdown = 3

gs = GameState
def promptGPT(userAction):
    indoctronation = "You are a bot and your only role is to determine if a SENTENCE is similar to one of two STATEMENTS. If the SENTENCE is similar to STATEMENT ONE, only respond with the word 'ONE', if the SENTENCE is similar to STATEMENT TWO, only respond with the word 'TWO'. If neither of the STATEMENTS are similar with the SENTENCE, respond with 'NONE'."
    indoctronation += "\nSENTENCE: " + userAction + "."
    indoctronation += "\nSTATEMENT ONE: " + userGoodActions[gs.userCurrentState]
    indoctronation += "\nSTATEMENT TWO: " + userBadActions[gs.userCurrentState]
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = indoctronation,
        max_tokens = 3,
        n = 1,
        stop = None,
        temperature = 0.1,
    )
    return completion.choices[0].text

def decisionMethod(gptResponse):
        if (gptResponse == "ONE"):
            gs.hintCountdown = 3
            print(goodActionResponse[gs.userCurrentState])
            gs.userCurrentState += 1
        elif (gptResponse == "TWO"):
            print(badActionResponse[gs.userCurrentState])
        else:
            if (gs.hintCountdown == 0):
                gs.hintCountdown = 3
                print(hintResponse[gs.userCurrentState])
            else:
                print("No... That doesn't seem right...")
                gs.hintCountdown -= 1


with open ('intro.txt', 'r') as file:
    print(file.read())

playing = True
while (playing):
    print("Current Situation: " + userSituations[gs.userCurrentState])
    action = input("What do you do?\n> ")
    gptResponse = promptGPT(action).upper().strip()

    if (gs.userCurrentState == 0):
        decisionMethod(gptResponse)
    elif(gs.userCurrentState == 1):
        decisionMethod(gptResponse)      
