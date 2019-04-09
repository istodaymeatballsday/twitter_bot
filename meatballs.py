import requests
import config
from bs4 import BeautifulSoup as soup


def isIt ():
    response = requests.get(config.MEATBALL_LAMDA)
    html = soup(response.text, "html.parser")
    isIt = html.find("div", id="answer").findNext("h1").text
    return isIt
