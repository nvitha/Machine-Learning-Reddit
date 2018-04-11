import praw
import psycopg2
import re

conn = psycopg2.connect("dbname=nick user=nick")
cur = conn.cursor()
conn.set_client_encoding('UTF8')

file = open("comments.csv","w+")

cur.execute('SELECT subreddit, body FROM comments')
r = re.compile(r"\s+")

num = 0
delimeter = " ////////######## "


while(num < 300,000):
	num += 1
	line = cur.fetchone()
	subreddit = line[0]
	comment = line[1]
	comment = r.sub(" ", comment)
	file.write(str(num) + delimeter + subreddit + delimeter + comment + "\n")

file.close()
cur.close()
conn.close()
