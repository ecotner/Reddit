# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:31:38 2015

@author: 27182_000
"""

import praw
import time
import random
import sys

#define function to reply to comments/submissions
def reply(string, parent):
    if string == "alot":
        response_list = ["    a lot\nFTFY",
                         "Hey, so I don't want to sound like a douche here, but 'alot' is actually two words: 'a lot'. Just FYI.\n\nIdiot.",
                         "Yo, I think you're confusing the alot, [a large fictitious creature](http://4.bp.blogspot.com/_D_Z-D2tzi14/S8TRIo4br3I/AAAAAAAACv4/Zh7_GcMlRKo/s400/ALOT.png) popularized by the blog [Hyperbole and a Half](http://hyperboleandahalf.blogspot.com/2010/04/alot-is-better-than-you-at-everything.html), with the the phrase 'a lot', which means 'many' or 'often' depending on context. Just wanted you to know so you don't look like an idiot in the future. Not that you look like an idiot now! You look great! Very sexy.\n\nWhat I'm trying to say is that your looks are probably your best quality... but you should probably read more books.",
                         "UNAUTHORIZED USAGE OF 'ALOT' DETECTED\n\nDEPLOYING COUNTERMEASURES:\n\n...\n\nINITIATE RESPONSE:\n\nWOW ARE YOU RETARDED?! IT'S SPELLED 'A LOT'. AS IN TWO SEPARATE WORDS. JESUS, GO READ A BOOK OR SOMETHING.\n\nTERMINATE RESPONSE\n\n...\n\nSUBROUTINE COMPLETED, RESUMING STANDBY MODE"]
    elif string == "proved":
        pass
    elif string == "payed":
        pass
    elif string == "irregardless":
        pass
    response_signature = "\n*****\nHi! I'm a bot. Sorry if I was a little rude to you^^^not ^^^really ^^^though. Please direct all suggestions, comments or criticisms [here!](http://www.chicagomanualofstyle.org/15/ch05/ch05_toc.html)"
    response = random.choice(response_list) + response_signature
    if str(type(parent)) == "<class 'praw.objects.Comment'>":
        parent.reply(response)
#        print response + response_signature
    elif str(type(parent)) == "<class 'praw.objects.Submission'>":
        parent.add_comment(response)
#        print response + response_signature
    else:
        pass
    time.sleep(600)

submission_ignore_list = []
comment_ignore_list = []

def check_for_string(string, parent):
    check = False
    #determines whether it's a comment/submission and reads in the text
    if str(type(parent)) == "<class 'praw.objects.Comment'>":
        text_body = parent.body.encode("cp437", errors='ignore').lower()
    elif str(type(parent)) == "<class 'praw.objects.Submission'>":
        text_body = parent.selftext.encode("cp437", errors='ignore').lower()
    else:
        text_body = ""
    #determines whether the string is present in the text, tries reduce misidentifications
    if any(string in text_body):
        if (parent.id in comment_ignore_list) or (parent.id in submission_ignore_list):
            print "Possible repeat %s found." % string
        elif (parent.id not in comment_ignore_list) \
            and (parent.id not in submission_ignore_list) and (parent.author.name != "Y_CANT_U_GRAMMAR_BOT"):
            if any(" " + string + " " in text_body):
                check = True
            elif text_body == string:
                check = True
            elif (text_body[0:len(string)+1] == string + " ") or (text_body[-(len(string)+1):-1] + text_body[-1] == " " + string):
                check = True
            elif any(" " + string + "." in text_body):
                check = True
            elif any(" " + string + "!" in text_body):
                check = True
            elif any(" " + string + "?" in text_body):
                check = True
            else:
                check = False
    return check

#start timing for benchmarking purposes
start_time = time.time()

user_agent = ("Obnoxious grammar-correcting script by /u/Physicswizard. Corrects people who use 'alot'.")
r = praw.Reddit(user_agent=user_agent)
r.login('Y_CANT_U_GRAMMAR_BOT', 'Fusion1!')


#main function

#while True:
#gets top submissions from selected subreddits; banned from: movies, funny
subreddit = r.get_subreddit('pics+gaming+videos+gifs+mildlyinteresting+todayilearned+circlejerk+grammar+grammarnazi')
#subreddit = r.get_subreddit('test')
submission_list = subreddit.get_hot(limit=100)

#begin parsing submissions
for submission in submission_list:
#    submission.replace_more_comments(limit=None, threshold=0)
    if check_for_string("alot", submission):
        submission_ignore_list.append(submission.id)
        print "Identified 'alot' in submission; url: %s" % (submission.permalink.encode("cp437", errors='ignore'))
        reply("alot", submission)
        
    #begin parsing comments in submission
    flat_comments = praw.helpers.flatten_tree(submission.comments)
    for comment in flat_comments:
        try:
            if check_for_string("alot", comment):
                comment_ignore_list.append(comment.id)
                print "Identified 'alot' in comment; url: %s%s" % (submission.permalink.encode("cp437", errors='ignore'), comment.id)
                reply("alot", comment)
        except AttributeError:
            pass

#print "submission ignore ID's: %s" % submission_ignore_list
#print "comment ignore ID's: %s" % comment_ignore_list

print "run time: %s seconds" % (time.time() - start_time)