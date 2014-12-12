def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
		
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return (None)

def print_top_coach_data(filename, rank):
	print(sorted(set([sanitize(each_t) for each_t in get_coach_data(filename)]))[0:rank])

for each_file in ['james.txt','julie.txt','mikey.txt','sarah.txt']:
	print_top_coach_data(each_file, 3)
