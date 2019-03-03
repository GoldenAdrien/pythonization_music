import math
#x = math.sin(math.pi)
#print(str(round(x,2)))
#"{0:2g}".format(math.pi)

m = 32767 / 2
#print(m*math.sin(t))

newFile = open("byte.dat", "wb")

imax = 44100
f=440
for i in range(0, imax):
	t=i/44100
	s=int(m*math.sin(f*2*math.pi*t))
	ba=s.to_bytes(2, byteorder='little', signed='true')
	newFile.write(ba)

print("correct syntax")
