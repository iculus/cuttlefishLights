from numpy import interp, zeros, chararray, reshape, append, array, roll

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

def chevronLine():
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
			[0,0,0,0,0,0,0,0,0,0,0]	])