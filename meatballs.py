import requests
import config
import json
from datetime import datetime

# Twitter dont allow same message everyday. 
# This will remove punctuation if day % 2 == 1
def fixString(word):
    number = datetime.now().strftime("%w")
    if (int(number) % 2) == 1:    
        word = word[:-1] if word.endswith('.') else word
    return word

def isIt ():
    response = requests.get(config.MEATBALL_LAMDA)
    jsonResponse = json.loads(response.text)
    word = jsonResponse['msg']
    return fixString(word)

print(isIt())