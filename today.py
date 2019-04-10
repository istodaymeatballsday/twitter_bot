from datetime import datetime

def getDay():
    return datetime.now().strftime("%a")

def getNumber():
    return datetime.now().strftime("%w")
