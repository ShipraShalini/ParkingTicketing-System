import json

def createmessagestring(in_message):
    message = dict(message=in_message)
    return json.dumps(message)