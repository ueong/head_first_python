import os

data = open('sketch.txt')

for each_line in data:
	# we used try-except
	try:
		(role, line_spoken) = each_line.split(':',1)
		print(role, end='')
		print(' said: ', end='')
		print(line_spoken, end='')
	except:
		# do nothing
		pass
data.close()
