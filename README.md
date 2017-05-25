## Overview

This bot posts synopses of twitter feeds to reddit.

ReddTwit is free software, so you are free to use, copy, modify, and distribute this code as you desire.  Though, I would certainly appreciate if you credited the original project.

## Setup

First, you must get your api credentials from reddit and twitter.

Make sure you have an account on both, then follow the instructions [here](http://progur.com/2016/09/how-to-create-reddit-bot-using-praw4.html) under **Registering the Bot** for reddit.  You need to do a similar process [on Twitter](https://apps.twitter.com/), just make sure you also get an Access Token and Token Secret.

Through this process, you will get a Client ID and Secret from Reddit, and your Twitter Key, Secret, Token, and Token Secret.

Set RedditClientID, RedditSecret, RedditUsername, RedditPassword, TwitterKey, TwitterSecret, TwitterToken, and TwitterTokenSecret appropriately in your environment variables.  Lastly, set RedditAgent in your environment variables.  It doesn't seem to have exact specifications, but it's best to include your username, and a little bit about your bot.  Something like this works fine:

`/u/myusername bot to summarize twitter feeds`

It's easiest to export these in your .bashrc.

## How to use

In order to make a single post (not scheduled), just run:

`./update.py subredditname twitterhandle`

The script automatically posts only tweets you have not yet posted to that subreddit, for that particular user.

*Note: this is not done in a particularly robust way.  The id of the most recent tweet fetched is simply saved to a file in the current directory identifying the user and subreddit, and only tweets newer than that id are fetched.  This could fail if you try and post too often to reddit, since an id would be saved that did not post.  This could also fail if the user specified has tweeted more than 200 times since the script was last run.  This may be improved later.*

To make regular posts, simply set a cronjob to run at the interval you specify.

# Future improvements

The project could benefit from some pep8.  In addition, I may automate some tools for making regular posts.
