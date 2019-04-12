import json
import config
import meatballs
import today
from twython import Twython, TwythonError

def tweet(event, context):
    twitter = Twython(config.APP_KEY, config.APP_SECRET,
                      config.OAUTH_TOKEN, config.OAUTH_TOKEN_SECRET)
    message = ""
    isTodayMeatballsDay = meatballs.isIt()

    try:
        twitter.update_status(status=isTodayMeatballsDay)
        message = "Function passed, status: " + isTodayMeatballsDay
    except TwythonError as err:
        message = "Function failed, status: " + isTodayMeatballsDay + "\nError: " + err
        pass

    body = {
        "message": message,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print(response)
    return response