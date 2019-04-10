import requests
import config
import json
import today

def getPunctuation(number):
    if (int(number) % 2) == 1:
        return "."
    else:
        return ""

def parseCode(code):
    if code == 1:
        return "Yep" + getPunctuation(today.getNumber())
    elif code == 2:
        return "Nope. But it is mashed potatos" + getPunctuation(today.getNumber())
    else:
        return "Nope" + getPunctuation(today.getNumber())

def isIt ():
    response = requests.get(config.MEATBALL_LAMDA)
    jsonResponse = json.loads(response.text)
    code = jsonResponse['code']
    return parseCode(code)