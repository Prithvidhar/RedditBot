# Team fortress weapon stat Reddit Bot

## Description

A Reddit bot that responds to users when mentioned in the PythonforEngineer subreddit. Its functionality includes gathering the positive and negative attributes of Team Fortress 2 weapons and responding to a user on Reddit with these attributes. 

## Purpose

Currently, there are over 209 weapons in the class-based first-person shooter video game Team Fortress 2 (TF2). Oftentimes, when discussing the game it becomes necessary to obtain the statistics of a particular weapon in the to discuss its usefull in certain game scenario.

This tool can be used to help people on Reddit quickly gather this information in the form of a reply.

## Installation and usage

The code is stored in a single Python file that can be run on any machine assuming the Python interpreter is [installed](https://www.python.org/downloads/). Here is the command to run the program using your machine's terminal.

```
python3 weaponbot.py
```

Running the command will have the bot check its Reddit account for any mentions. If it finds any, it will look at the first word after its mention and scrape the details of the weapon from the TF2 Wiki

```
u/Tf2WeaponsBot Sandvich
(Yes, this is a real weapon in the game)
```

## Challenges and experiences

One of the major challenges was scrapping the right web content. I ended up using the `bs4` Python module to extract the text content from the wiki page's HTML. It was a fun experience coming up with the idea for this Reddit bot. After seeing u/The-Paranoid-Android providing links to users, it really made me think about how can provide such convenience to the users of the r/tf2 subreddit. It was also a good excuse to tinker with Reddit's API and get my hands dirty with web scraping.

## Future

Currently, the bot only replies when running the Python code manually. I plan to import this code in an AWS Lambda function and use the EventBridge service to periodically run the code to serve user requests.

Feel free to contact me on GitHub if you have any questions about the tool!
