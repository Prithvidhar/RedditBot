'''
A TF2 reddit bot that provides users on the stats of various TF2 weapons

Created by Prithvidhar Pudu

'''
import praw
import pdb
import re
import os
import requests
from bs4 import BeautifulSoup

reddit = praw.Reddit('bot1')
output = ''
subreddit = reddit.subreddit("pythonforengineers")
# Writing replied post to mentioned
for mention in reddit.inbox.mentions(limit =10):
    # print(f'{mention.body} is the body of the mention')
    if not mention.new:
        continue
    weapon = mention.body.replace('u/Tf2WeaponStatsBot','')
    URL = 'https://wiki.teamfortress.com/wiki/{}'.format(weapon)
    output='{} Stats:\n\nPositive attributes:\n'.format(weapon)
    print(URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find(id='right-sidebar')
    # Finding positive attributes
    # print(results.prettify)
    tooltip = results.find('td', class_='loadout-tooltip-container')
    backpack = tooltip.find('div',class_ = 'tfwiki-backpack-item')
    positive_atts = backpack.find_all('span',class_= 'att_positive')
    negative_atts = backpack.find_all('span',class_= 'att_negative')
    for p in positive_atts:
        output+= '- '+ p.text + '\n'
    output+= '\n\nNegative attributes:\n'
    for n in negative_atts:
        output+='- '+n.text+'\n'
    print(output)
    mention.reply(output)
    mention.mark_read()
    



