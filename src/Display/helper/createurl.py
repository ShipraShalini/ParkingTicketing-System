from src.common.frontendconstants import *
from urlparse import urlparse

def createurl(endpoint):
    return "{0}{1}:{2}/{3}/".format(PROTOCOL, HOST, PORT, endpoint)