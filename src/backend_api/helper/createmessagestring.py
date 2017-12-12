import json

def createmessagestring(in_message):
    return json.dumps({'message': in_message})
