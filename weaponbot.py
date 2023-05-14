'''
A TF2 reddit bot that provides users on the stats of various TF2 weapons

Created by Prithvidhar Pudu

'''
import praw
import pdb
import re
import os
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")
#storing replied posts in list
if not os.path.isfile("posts_replied.txt"):
    post_replied = []
else:
    with open('posts_replied.txt','r') as f:
        post_replied = f.read()
        post_replied = post_replied.split('\n')
        post_replied = list(filter(None,post_replied))

for submission in subreddit.hot(limit=1):
    submission.comments.replace_more(limit=None)
    if submission.id not in post_replied:
        #Checking for comment
        for comment in submission.comments.list():
            print(comment.body)
# Writing replied post 
with open("posts_replied_to.txt", "w") as f:
    for post_id in post_replied:
        f.write(post_id + "\n")

