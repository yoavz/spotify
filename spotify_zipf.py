a = raw_input('Enter a filename: ')
f = open(a)
lines = f.readlines()
f.close()

n = int(lines[0].split(" ")[0])
m = int(lines[0].split(" ")[1])

class Song:
	def __init__(self, i, f, name):
		self.i = i
		self.f = f
		self.name = name
		self.z = 1.0 / self.i
		self.q = f / self.z
		

songs = []

for i in range(1, n+1):
	f = float(lines[i].split(" ")[0])
	name = lines[i].split(" ")[1].rstrip("\n")
	songs.append(Song(float(i), f,  name))



for i in range(m):
	next = max(songs, key= lambda x: x.q)
	songs.remove(next)
	print next.name