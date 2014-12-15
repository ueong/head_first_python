class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def top3(self):
		return (sorted(set([self.sanitize(t) for t in self.times]))[0:3])

	def add_time(self, time_value):
		self.times.append(time_value)

	def add_times(self, list_of_times):
		self.times.extend(list_of_times)

	def sanitize(self, time_string):
		if '-' in time_string:
			splitter = '-'
		elif ':' in time_string:
			splitter = ':'
		else:
			return(time_string)
			
		(mins, secs) = time_string.split(splitter)
		return (mins + '.' + secs)

vera = Athlete('Vera Vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22','1-21','2.22'])
print(vera.top3())
