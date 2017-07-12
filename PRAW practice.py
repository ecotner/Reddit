# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:31:38 2015

@author: 27182_000
"""

import praw

user_agent = ("Karma breakdown 1.0 by /u/_Daimon_ "
              "github.com/Damgaard/Reddit-Bots/")
r = praw.Reddit(user_agent=user_agent)
thing_limit = 10
user_name = "Physicswizard"
user = r.get_redditor(user_name)
gen = user.get_submitted(limit=thing_limit)
karma_by_subreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0)
                                     + thing.score)
import pprint
pprint.pprint(karma_by_subreddit)