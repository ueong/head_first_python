movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

# we want to make the list to ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]

# Method 1
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983) # or movies.append(1983)

print('Method 1')
print(movies)

# Method 2
movies = ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]

print('\nMethod 2')
print(movies)
