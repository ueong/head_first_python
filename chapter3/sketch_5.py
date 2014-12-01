import os

try:
	data = open('sketch.txt')

	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':',1)
			print(role, end='')
			print(' said: ', end='')
			print(line_spoken, end='')
		except ValueError: # this
			pass
	data.close()
except IOError: # and this
	print('The datafile is missing!')
