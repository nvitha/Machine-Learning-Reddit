# Machine Learning Final Project
By Taylor Jones and Nicholas Vitha

To run the reddit scripts, you will need an install of PostgreSQL as well as these packages from pip:
praw,psycopg2,ConfigParser

You will need a reddit account to request access to the API (https://www.reddit.com/prefs/apps/). From there, you will need to add the client_id,client_secret, and a user_agent to the config.ini in both postlogging/config.ini and commentlogging/config.ini

You can find our data in /Data/Scripts/comments.csv with a data structure of:

DatabaseID ////////######## Subreddit ////////######## comment
