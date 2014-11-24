cast = ['Cleese', 'Palin', 'Jones', 'Idle']

# ['Cleese', 'Palin', 'Jones', 'Idle']
print(cast)

# 4
print(len(cast))

# Palin
print(cast[1])

# ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.append("Gilliam")
print(cast)

# 'Gilliam'
cast.pop()
# ['Cleese', 'Palin', 'Jones', 'Idle']
print(cast)

# ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']
cast.extend(['Gilliam','Chapman'])
print(cast)

# ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.remove('Chapman')
print(cast)

# ['Chapman', Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.insert(0, 'Chapman')
print(cast)