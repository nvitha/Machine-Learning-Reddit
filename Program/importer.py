import pandas as pd

df = pd.read_csv('comments.csv',delimiter='////////########',engine='python', names = ["id","subreddit","comment"])



