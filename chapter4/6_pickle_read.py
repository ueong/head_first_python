import pickle
import print_lol

try:
	with open('man_data.pickle', 'rb') as man_file, open('other_data.pickle', 'rb') as other_file:
		man = pickle.load(man_file)
		other = pickle.load(other_file)
except IOError as err:
	print('File Error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickling error: ' + str(err))

print_lol.print_lol(man)
print('')
print_lol.print_lol(other)
