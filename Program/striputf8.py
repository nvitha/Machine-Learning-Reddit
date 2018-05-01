infile = open("comments.csv")
outfile = open("cleaned_comments.csv",'w')
lines = infile.read().splitlines()

for line in lines:
	tmp_line = line.decode("utf-8")
	ascii_line = tmp_line.encode("ascii","ignore")
	outfile.write(ascii_line + '\n')
outfile.close()
