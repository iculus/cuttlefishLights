from numpy import interp, zeros, chararray, reshape, append, array, roll, where, fliplr

def heart(color):
	x = color
	return array([	[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,x,x,0,0,0,x,x,0,0],
			[0,x,0,0,x,0,x,0,0,x,0],
			[x,0,0,0,0,x,0,0,0,0,x],
			[x,0,0,0,0,0,0,0,0,0,x],
			[0,x,0,0,0,0,0,0,0,x,0],
			[0,0,x,0,0,0,0,0,x,0,0],
			[0,0,0,x,0,0,0,x,0,0,0],
			[0,0,0,0,x,0,x,0,0,0,0],
			[0,0,0,0,0,x,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],	
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0]	])

def dot(xPos, yPos, Color):
	setArray = array([	[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],	
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0]	])
	setArray[xPos][yPos] = Color
	return setArray

def diagonalLine():
	return array([	[4,0,0,0,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,0,0,0,0],
			[0,0,2,0,0,0,0,0,0,0,0],
			[0,0,0,3,0,0,0,0,0,0,0],
			[0,0,0,0,4,0,0,0,0,0,0],
			[0,0,0,0,0,5,0,0,0,0,0],
			[0,0,0,0,0,0,6,0,0,0,0],
			[0,0,0,0,0,0,0,7,0,0,0],
			[0,0,0,0,0,0,0,0,8,0,0],
			[0,0,0,0,0,0,0,0,0,9,0],
			[0,0,0,0,0,0,0,0,0,0,10],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],	
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0]	])

def chevronLine(fill=True):
	if fill: P = 0
	if not fill: P = 7

	return array([	[4,0,0,0,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,0,0,0,0],
			[0,0,2,0,0,0,0,0,0,0,0],
			[0,0,0,3,0,0,0,0,0,0,0],
			[0,0,0,0,4,0,0,0,0,0,0],
			[0,0,0,0,0,5,0,0,0,0,0],
			[0,0,0,0,0,0,6,0,0,0,0],
			[0,0,0,0,0,0,0,7,0,0,0],
			[0,0,0,0,0,0,0,0,8,0,0],
			[0,0,0,0,0,0,0,0,0,9,0],
			[0,0,0,0,0,0,0,0,0,0,10],
			[0,0,0,0,0,0,0,0,0,9,0],
			[0,0,0,0,0,0,0,0,8,0,0],
			[0,0,0,0,0,0,0,7,0,0,0],
			[0,0,0,0,0,0,6,0,0,0,0],
			[0,0,0,0,0,5,0,0,0,0,0],	
			[0,0,0,0,4,0,0,0,0,0,0],
			[0,0,0,3,0,0,0,0,0,0,0],
			[0,0,2,0,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,0,0,0,0],
			[9,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,P]	])

def patternOne (simulator2,c1,c2):
	#flips and copies
	simulator1=fliplr(simulator2)
	#sets color
	simulator2=where(simulator2 == 0, simulator2,c1)
	simulator1=where(simulator1 == 0, simulator2,c2)
	#moves
	simulator2=roll(simulator2, 1,1)
	#merges
	newSim=where(simulator2 != 0, simulator2,simulator1)
	simulator1=roll(simulator1, 1,1)
	return newSim, simulator2

