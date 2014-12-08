import os

man = []
other = []
try:
	# with open('missing.txt') as data:
	with open('sketch.txt') as data:
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
except IOError as err:
	print('File error : ' + str(err))

try:
	with open('man_data.txt','w') as manfile, open('other_data.txt','w') as otherfile:
		print(man, file=manfile)
		print(other, file=otherfile)
except IOError as err:
	print('Write file error : ' + str(err))

with open('man_data.txt') as mdf:
	print(mdf.readline())

with open('other_data.txt') as odf:
	print(odf.readline())

