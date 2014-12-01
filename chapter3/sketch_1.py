import os

data = open('sketch.txt')

for each_line in data:
	# we used find..
	if not each_line.find(':') == -1:
		(role, line_spoken) = each_line.split(':',1)
		print(role, end='')
		print(' said: ', end='')
		print(line_spoken, end='')
data.close()
