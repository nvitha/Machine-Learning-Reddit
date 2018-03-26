drop table if exists posts;
drop table if exists comments;

create table posts (id serial, username text, permalink text, subreddit text, title text, datetime timestamp);
create table comments (id serial, username text, permalink text, subreddit text, body text, datetime timestamp);
