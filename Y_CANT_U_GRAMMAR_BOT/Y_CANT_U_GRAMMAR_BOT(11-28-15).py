# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:31:38 2015

@author: 27182_000
"""

import praw
import time

start_time = time.time()

user_agent = ("Obnoxious grammar-correcting script by /u/Physicswizard")
r = praw.Reddit(user_agent=user_agent)
#r.login('Y_CANT_U_GRAMMAR_BOT', 'Fusion1!')

submission_ignore_list = []
comment_ignore_list = []

while True:
    subreddit = r.get_subreddit('pics+funny+todayilearned+aww+gaming')
    submission_list = subreddit.get_hot(limit=500)

    for submission in submission_list:    
        if (any("alot" in submission.selftext.encode("cp437", "ignore").lower()) or any("alot" in submission.title.encode("cp437", "ignore").lower())) and (submission.id in submission_ignore_list):
            print "Repeat 'alot' detected!"
        if (any("alot" in submission.selftext.encode("cp437", "ignore").lower()) or any("alot" in submission.title.encode("cp437", "ignore").lower())) and (submission.id not in submission_ignore_list):
            submission_ignore_list.append(submission.id)
            print "Identified 'alot' in submission; url: %s" % (submission.permalink)
    #        submission.add_comment("    a lot\nFTFY")
        flat_comments = praw.helpers.flatten_tree(submission.comments)
        for comment in flat_comments:
            try:
                if any("alot" in comment.body.encode("cp437", "ignore").lower()) and (comment.id in comment_ignore_list):
                    print "Repeat 'alot' detected!"
                if any("alot" in comment.body.encode("cp437", "ignore").lower()) and (comment.id not in comment_ignore_list):
                    comment_ignore_list.append(comment.id)
                    print "Identified 'alot' in comment; url: %s%s" % (submission.permalink, comment.id)
    #                comment.reply("    a lot\nFTFY")
            except AttributeError:
                pass

#print "submission ignore ID's: %s" % submission_ignore_list
#print "comment ignore ID's: %s" % comment_ignore_list

print "run time: %s seconds" % (time.time() - start_time)