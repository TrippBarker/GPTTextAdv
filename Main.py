import os
import openai

openai.api_key_path = 'D:\KEYS\TextAdvKey.txt'
model_engine = "text-davinci-003"

userSituations = ["Hands bound behind back.", 
                  "Standing in the Wizard's camp.",
                  "Running through forest.",
                  "Standing before the Wizard.",
                  "The Wizard is kneeling before you.",
                  "Beating the Wizard"]

userGoodActions = ["Find sharp object.", 
                   "Run away.",
                   "Look for exit.",
                   "Punch the Wizard.",
                   "Kick the Wizard."]

userBadActions = ["Struggle.", 
                  "Sit and wait.",
                  "Keep running.",
                  "Cower in fear.",
                  "Run away from the Wizard."]

goodActionResponse = ["You remember that you have a knife in your back pocket! Reaching carefully, you manipulate the blade open and saw away at the rope... You're free!!",
                      "With no real sense of direction, you spring to your feet and start running!",
                      "Squinting your eyes, you take in your surroundings... THERE!!! You see a beam of light glistening in the distance... You make your brake for it!\n''TEE-HEE-HEE'' *poof* Oh no! it's the Wizard, he has appeared right before you!!",
                      "You pull back your right fist and *POW* let him have it right in the kisser!! ''HEY NOW!!! THAT WAS NOT VERY NICE!!!'' The Wizard doubles over in pain.",
                      "*KA-PA_CHOW* You kick the Wizard square in the jaw, he's not gonna be eating any lone travelers for a while now!"]

badActionResponse = ["You squirm about, something sharp pokes at you from your back pocket...",
                     "You sit there... Twiddling your thumbs like a dumb-dumb",
                     "You run in circles, hopelessly lost in the forsest...",
                     "You cower in fear, like a wittle baby boi. Sow sad :(",
                     "You could run... But maybe this Wizard deserves to be taught more of a lesson..."]

hintResponse = ["Nothing seems to be working... Maybe look for something sharp to cut the rope with...",
                "Nothing seems to be working... Maybe... I dunno.... RUN??!!!??",
                "Nothing seems to be working... Maybe try looking for an exit.",
                "Nothing seems to be working... Maybe fight the Wizard.",
                "Nothing seems to be working... Maybe curb stomp that bitch."]


class GameState:
    userCurrentState = 0
    hintCountdown = 2

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
            if (gs.userCurrentState == 4):
                playing = False
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
    decisionMethod(gptResponse)
    if (gs.userCurrentState == 5):
        playing = False

print("And with that you leave the forest, the Wizard crying on a pile of leaves like the sorry wittle bitch he is, the end <3")