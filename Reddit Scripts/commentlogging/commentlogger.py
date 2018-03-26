import praw
import psycopg2
from ConfigParser import SafeConfigParser

conn = psycopg2.connect("dbname=nick user=nick")
cur = conn.cursor()
conn.set_client_encoding('UTF8')


file = open("subreddits.csv","r")

parser = SafeConfigParser()
parser.read('config.ini')

reddit = praw.Reddit(client_id=parser.get('reddit_config', 'client_id'),
			client_secret=parser.get('reddit_config', 'client_secret'),
			user_agent=parser.get('reddit_config', 'user_agent'))
content = file.read()
subs = content.split(',')
subreddits_string = ''
for sub in subs:
	subreddits_string = subreddits_string + '+' + sub

for comment in reddit.subreddit(subreddits_string).stream.comments():
	cur.execute('INSERT INTO comments values (DEFAULT, %s, %s, %s, %s, now())', (comment.author.name, comment.permalink, comment.subreddit.display_name,comment.body))
	conn.commit()
