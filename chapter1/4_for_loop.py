fav_movies = ["The Holy Grail", "The Life of Brian"]
print('# we don\'t want to work like this')
print(fav_movies[0])
print(fav_movies[1])


print('\n# use for loop')
for each_flick in fav_movies:
	print(each_flick)

print('\n# use while loop')
count = 0
while count < len(fav_movies):
	print(fav_movies[count])
	count = count + 1
