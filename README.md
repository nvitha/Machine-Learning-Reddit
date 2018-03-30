# Machine Learning Final Project
By Taylor Jones and Nicholas Vitha

To run the reddit scripts, you will need an install of PostgreSQL as well as these packages from pip:
praw,psycopg2,ConfigParser

You will need a reddit account to request access to the API (https://www.reddit.com/prefs/apps/). From there, you will need to add the client_id,client_secret, and a user_agent to the config.ini in both postlogging/config.ini and commentlogging/config.ini

Postgres command to export to CSV and trim data:
\COPY (select subreddit, body from comments) TO '/path/to/file.csv' DELIMITER ',' CSV HEADER;
