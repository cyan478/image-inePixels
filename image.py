def create():
	str = ""

	str += "P3 500 500 255\n"

	for i in range(500):
		for j in range(500):
			if (i == 0) or (j == 0):
				R = 100
				G = 0
				B = 0
			elif (i == 50) or (j == 50) or (i == 450) or (j == 450):
				R = 1
				G = 1
				B = 1
			else:
				R = (i+j) % 256
				G = (i/j) % 256
				B = (i-j) % 256

			str += "%s %s %s\n"%(R,G,B)

	return str

def write():
	f = open( "img.ppm", "w")
	s = create()
	f.write(s)

write()

