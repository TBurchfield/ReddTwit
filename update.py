#!/usr/bin/env python2.7

#Will scrape a list of twitter users, and make reddit posts about their tweets

import os
import json
import praw


try:
	client_id = os.environ["RedditClientID"]
	client_secret = os.environ["RedditSecret"]
	username = os.environ["RedditUsername"]
	client_id = os.environ["RedditPassword"]
except KeyError:
	print ""
	print "Error:"
	print ""
	print "Please set RedditClientID, RedditSecret,"
	print "RedditPassword, and RedditUsername in your environment variables."
	print ""
