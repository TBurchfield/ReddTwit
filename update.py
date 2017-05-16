#!/usr/bin/env python2.7

#Will scrape a list of twitter users, and make reddit posts about their tweets

import os
import sys
import json
import praw


try:
  cli_id = os.environ["RedditClientID"]
  cli_sec = os.environ["RedditSecret"]
  user = os.environ["RedditUsername"]
  passwd = os.environ["RedditPassword"]
  agent = os.environ["RedditAgent"]

except KeyError:
  print ""
  print "Error:"
  print ""
  print "Please set RedditClientID, RedditSecret,"
  print "RedditPassword, RedditAgent, and RedditUsername"
  print "in your environment variables."
  print ""
  sys.exit(1);

reddit = praw.Reddit(client_id=cli_id,
                     client_secret=cli_sec,
                     username=user,
                     password=passwd,
                     user_agent=agent)

print reddit.user.me()
