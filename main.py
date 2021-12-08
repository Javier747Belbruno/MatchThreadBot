
import re,requests,requests.auth,sys,json,unicodedata
from keep_alive import keep_alive
from time import sleep
from timestamp import getTimestamp
from prawAuth import setupPraw
from logger import setupLog

#Setup
logger = setupLog()

logger.warning("[STARTUP]")
print(getTimestamp() + "[STARTUP]")


#Auth
reddit = setupPraw(logger)

def postIt():
    title = "Test"
    url = "https://praw.readthedocs.io"
    reddit.subreddit("promiedos").submit(title, url=url)


#Serving
keep_alive()


# Every minute, check mail, create new threads, update all current threads
running = True
retries = 0
while running:
    try:
        #postIt()
        retries = 0
        sleep(60)
    except KeyboardInterrupt:
        logger.warning("[MANUAL SHUTDOWN]")
        print(getTimestamp() + "[MANUAL SHUTDOWN]\n")
        running = False
    except UnicodeDecodeError:
        retries += 1
        print(getTimestamp() + "UnicodeDecodeError, check log file [retries = " + str(retries) + "]")
        logger.exception("[UNICODE ERROR:]")
        #flushMsgs()
    except UnicodeEncodeError:
        retries += 1
        print(getTimestamp() + "UnicodeEncodeError, check log file [retries = " + str(retries) + "]")
        logger.exception("[UNICODE ERROR:]")
        #flushMsgs()
    except Exception:
        retries += 1
        print(getTimestamp() + "Unknown error, check log file [retries = " + str(retries) + "]")
        logger.exception("[UNKNOWN ERROR:]")
        sleep(60) 
