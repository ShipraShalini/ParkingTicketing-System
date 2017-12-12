
def removekey(data,key):
    try:
        del data[key]
    except KeyError:
        return data
    else:
        return data
