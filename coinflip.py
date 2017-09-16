H=0
COINFLIPS = 1000
import random
for x in range(COINFLIPS):
	r=random.random()
	print r
	if r > 0.5:
		H=H+1
		print "heads"
	else:
		print "tails"
	print "Number of Heads", H
	PROB = (H *1.0 / COINFLIPS)
	print "PROBABILITY", PROB	
