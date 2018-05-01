infile = open('cleaned_comments.csv','rw+')
keyfile = open('subreddits.csv')
outfile = open('replaced_subreddits.csv','w+')

dict = {}
for line in keyfile:
	(val,key) = line.split(',')
	key = key[:-1].lower()
	dict[key] = val.lower()

comments = infile.read().splitlines()
all_comments = []
for comment in comments:
	all_comments.append(comment.split(' ////////######## '))

new_list = []
for comment in all_comments:
	new_list.append([comment[0],dict[comment[1].lower()],comment[2]])

counter = 0
for comment in new_list:
	if comment[1] == '2':
		continue
	counter = 1
	for section in comment:
		if counter == 3:
			outfile.write(section + '\n')
			counter = 1
		else:
			counter +=1
			outfile.write(section + ' ////////######## '),
