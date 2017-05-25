#!/usr/bin/env python2.7
#Will scrape a list of twitter users, and make reddit posts about their tweets
import os
import sys
import praw
import twitter

try:
    Rcli_id  = os.environ["RedditClientID"]
    Rcli_sec = os.environ["RedditSecret"]
    Ruser    = os.environ["RedditUsername"]
    Rpasswd  = os.environ["RedditPassword"]
    Ragent   = os.environ["RedditAgent"]
    TKey     = os.environ["TwitterKey"]
    TSecret  = os.environ["TwitterSecret"]
    TTok     = os.environ["TwitterToken"]
    TTokSec  = os.environ["TwitterTokenSecret"]

except KeyError:
    print ""
    print "Please set ALL of:"
    print "----------------------------------"
    print "RedditClientID        RedditSecret"
    print "RedditAgent         RedditPassword"
    print "RedditUsername          TwitterKey"
    print "TwitterSecret         TwitterToken"
    print "TwitterTokenSecret"
    print "----------------------------------"
    print "in your environment variables."
    print ""
    sys.exit(1);

def get_statuses(name, since, usesince, twitterapi):
    # fetches statuses, returns list of status instances
    if usesince: #we have a most recent
        statuses = twitterapi.GetUserTimeline(
                   screen_name=name, include_rts=False, \
                   exclude_replies=True, since_id=since, count=200)
    else:
        statuses = twitterapi.GetUserTimeline(
                   screen_name=name, include_rts=False, \
                   exclude_replies=True, count=200)
    return statuses

def header(name):
    ret = "{}'s tweets\n\n".format(name)
    ret += "----\n\n"
    return ret

def footer():
    ret = "----\n\n"
    ret += "Boop.  I am a bot made with ReddTwit, the source code for which can be found [here](https://github.com/TBurchfield/ReddTwit)."
    return ret

def status_to_str(name, status):
    # Called by statuses_to_str, just returns a nicely formatted string
    # representing reddit markdown for a tweet.
    ret = u">{}\n\n".format(status.text)
    ret += "[link](https://twitter.com/{}/status/{})\n\n".format(name, status.id)
    ret += "&nbsp;\n\n"
    return ret

def statuses_to_str(name, statuses):
    # takes list of status instances, and converts to string by calling status_to_str
    post_string = header(name)
    for status in statuses:
        post_string += status_to_str(name, status)
    return post_string

def config(name, subreddit):
    #fetch config, if it exists
    usesince = False
    since = 0
    filename = ".{}-{}".format(name,subreddit)
    if os.path.isfile(filename):
        usesince = True;
        with open(filename, "r") as f:
            since = f.readline().strip()
    return [since, usesince]

def update_config(name, subreddit, since):
    filename = ".{}-{}".format(name,subreddit)
    with open(filename,"w") as f:
        f.write(since+"\n")

if __name__ == "__main__": # just in case anyone imports this
    subreddit = sys.argv[1]  # which subreddit to post to
    handle = sys.argv[2]     # which user to scrape
    redditapi = praw.Reddit(client_id=Rcli_id,
                         client_secret=Rcli_sec,
                         username=Ruser,
                         password=Rpasswd,
                         user_agent=Ragent)
  
    twitterapi = twitter.Api(consumer_key=TKey,
                         consumer_secret=TSecret,
                         access_token_key=TTok,
                         access_token_secret=TTokSec)
  
    [since, usesince] = config(handle, subreddit)
    statuses = get_statuses(handle,since,usesince,twitterapi)
    if len(statuses) > 0:
        update_config(handle, subreddit, statuses[0].id_str) #just in case id overflows
        mypost =  statuses_to_str(handle,statuses)
        redditapi.subreddit(subreddit).submit(title="Tweets of {}".format(handle),selftext=mypost)
    else:
        print "No new posts from {}.".format(handle)
