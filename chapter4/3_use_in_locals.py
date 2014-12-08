import os

man = []
other = []
try:
	## data = open('missing.txt')
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':',1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()

except IOError as err:
	print('File error : ' + str(err))

finally:
	if 'data' in locals():
		data.close()

try:
	manfile = open('man_data.txt','w')
	otherfile = open('other_data.txt','w')
	print(man, file=manfile)
	print(other, file=otherfile)

except IOError as err:
	print('Write file error : ' + str(err))

finally:
	manfile.close()
	otherfile.close()
