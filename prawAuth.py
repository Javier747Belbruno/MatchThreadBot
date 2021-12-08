import os
import praw
from time import sleep
from timestamp import getTimestamp


def setupPraw(logger):
	try:
            r = praw.Reddit(
                client_id = os.environ['client_id'],
                client_secret = os.environ['client_secret'],
                username = os.environ['username'],
                password  = os.environ['password'],
                user_agent = "<MatchThreadArgBot1.0>") 
            msg = "OAuth session opened as /u/" + r.user.me().name
            print(getTimestamp() + msg)
            logger.warning(msg)
            return r
	except Exception as e:
		print( getTimestamp() + "Setup Praw Error: Please ensure enviroment vars are correct\n" + e.args )
		logger.error("[SETUP ERROR:]")
		sleep(10)