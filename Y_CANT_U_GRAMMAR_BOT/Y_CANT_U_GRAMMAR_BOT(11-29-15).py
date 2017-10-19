# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:31:38 2015

@author: 27182_000
"""

import praw
import time
import random

#define function to reply to comments/submissions
def reply(parent_type):
    response_list = ["    a lot\nFTFY",
                     "Hey, so I don't want to sound like a douche here, but 'alot' is actually two words: 'a lot'. Just FYI.\n\nIdiot.",
                     "Yo, I think you're confusing the alot, [a large fictitious creature](http://4.bp.blogspot.com/_D_Z-D2tzi14/S8TRIo4br3I/AAAAAAAACv4/Zh7_GcMlRKo/s400/ALOT.png) popularized by the blog [Hyperbole and a Half](http://hyperboleandahalf.blogspot.com/2010/04/alot-is-better-than-you-at-everything.html), with the the phrase 'a lot', which means 'many' or 'often' depending on context. Just wanted you to know so you don't look like an idiot in the future. Not that you look like an idiot now! You look great! Very sexy.\n\nWhat I'm trying to say is that your looks are probably your best quality... but you should probably read more books.",
                     "UNAUTHORIZED USAGE OF 'ALOT' DETECTED\n\nDEPLOYING COUNTERMEASURES:\n\n...\n\nINITIATE RESPONSE:\n\nWOW ARE YOU RETARDED?! IT'S SPELLED 'A LOT'. AS IN TWO SEPARATE WORDS. JESUS, GO READ A BOOK OR SOMETHING.\n\nTERMINATE RESPONSE\n\n...\n\nSUBROUTINE COMPLETED, RESUMING STANDBY MODE"]
    response_signature = "\n*****\nHi! I'm a bot. Sorry if I was a little rude to you^^^^^(not really though). Please direct all suggestions, comments or criticisms [here!](http://www.chicagomanualofstyle.org/15/ch05/ch05_toc.html)"
    response = random.choice(response_list)
    if parent_type == "submission":
        submission.add_comment(response + response_signature)
#        print response + response_signature
    if parent_type == "comment":
        comment.reply(response + response_signature)
#        print response + response_signature

#def check_for_alot(parent_type):
#    check = False
#    if parent_type == "submission":
#        check = any("alot" in submission.selftext.encode("cp437", "ignore").lower())

#start timing for benchmarking purposes
start_time = time.time()

user_agent = ("Obnoxious grammar-correcting script by /u/Physicswizard")
r = praw.Reddit(user_agent=user_agent)
r.login('Y_CANT_U_GRAMMAR_BOT', 'Fusion1!')

submission_ignore_list = []
comment_ignore_list = []

#main function
#while True:
#gets top submissions from selected subreddits
subreddit = r.get_subreddit('pics+gaming+funny+videos+movies+gifs+mildlyinteresting+circlejerk+grammar+grammarnazi')
#subreddit = r.get_subreddit('test')
submission_list = subreddit.get_hot(limit=500)

#begin parsing submissions
for submission in submission_list:
#    submission.replace_more_comments(limit=None, threshold=0)
    if (any(" alot" in submission.selftext.encode("cp437", "ignore").lower()) \
            or any("alot " in submission.selftext.encode("cp437", "ignore").lower()) \
            or any(" alot" in submission.title.encode("cp437", "ignore").lower()) \
            or any("alot " in submission.title.encode("cp437", "ignore").lower())) \
            and (submission.id in submission_ignore_list) \
            and (submission.author.name != "Y_CANT_U_GRAMMAR_BOT"):
        print "Repeat 'alot' detected!"
    if (any(" alot" in submission.selftext.encode("cp437", "ignore").lower()) \
            or any("alot " in submission.selftext.encode("cp437", "ignore").lower()) \
            or any(" alot" in submission.title.encode("cp437", "ignore").lower()) \
            or any("alot " in submission.title.encode("cp437", "ignore").lower())) \
            and (submission.id not in submission_ignore_list) \
            and (submission.author.name != "Y_CANT_U_GRAMMAR_BOT"):
        submission_ignore_list.append(submission.id)
        parent_type = "submission"
        print "Identified 'alot' in submission; url: %s" % (submission.permalink)
        reply("submission")
        time.sleep(600)
        
    
    #begin parsing comments in submission
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    for comment in flat_comments:
        try:
            if (any(" alot" in comment.body.encode("cp437", "ignore").lower()) \
                    or any("alot " in comment.body.encode("cp437", "ignore").lower())) \
                    and (comment.id in comment_ignore_list) \
                    and (comment.author.name != "Y_CANT_U_GRAMMAR_BOT"):
                print "Repeat 'alot' detected!"
            if (any(" alot" in comment.body.encode("cp437", "ignore").lower()) \
                    or any("alot " in comment.body.encode("cp437", "ignore").lower())) \
                    and (comment.id not in comment_ignore_list) \
                    and (comment.author.name != "Y_CANT_U_GRAMMAR_BOT"):
                comment_ignore_list.append(comment.id)
                parent_type = "comment"
                print "Identified 'alot' in comment; url: %s%s" % (submission.permalink, comment.id)
                reply("comment")
                time.sleep(600)
        except AttributeError:
            pass

#print "submission ignore ID's: %s" % submission_ignore_list
#print "comment ignore ID's: %s" % comment_ignore_list

print "run time: %s seconds" % (time.time() - start_time)