#!/usr/bin/python
#GRB

mx = 255 #max value
num = 10 # number of brightnesses
numRows = 22

import sys
from numpy import reshape, vstack, zeros, hstack, array2string

'''
uint32_t RED = strip.Color(0,255,0);
uint32_t ORANGE = strip.Color(100,255,0);
uint32_t YELLOW = strip.Color(255,255,0);
uint32_t GREEN = strip.Color(255,0,0);
uint32_t TEAL = strip.Color(255,0,255);
uint32_t BLUE = strip.Color(0,0,255);
uint32_t FUCHA = strip.Color(0,255,100);
uint32_t PURPLE = strip.Color(0,170,255);
uint32_t NEW = strip.Color(170,120,66);
uint32_t WHITE = strip.Color(255,255,255);
uint32_t OFF = strip.Color(0,0,0);
'''

testing = False

if testing:
	printHeader = True
	printColor = True
	printConditional = True
	printArray = True
if not testing:
	printHeader = False
	printColor = False
	printConditional = False
	printArray = False

R = "RED = (0,255,0)"
O = "ORANGE = (100,255,0)"
Y = "YELLOW = (255,255,0)"
T = "TEAL = (255,0,255)"
G = "GREEN = (255,0,0)"
B = "BLUE = (0,0,255)"
PB = "PURPLEBLUE = (0,100,255)"
F = "FUCHA = (0,255,100)"
P = "PURPLE = (0,170,255)"
W = "WHITE = (255,255,255)"
W2 = "WHITE2 = (255,255,255)"


colors = [R,O,Y,G,T,B,PB,F,P,W,W2]

if not printHeader:
	print "#define leds 22"
	print "#define rows 11"
	print "#define PIN 6"
	print "\nuint32_t thisColor;"
	print "\nAdafruit_NeoPixel strip = Adafruit_NeoPixel(leds*rows, PIN, NEO_RGB + NEO_KHZ800);\n"


def split(color):
	color = color.replace('(','').replace(')','').replace(' ','')
	name,color=color.split('=')
	a,b,c=color.split(',')
	return a,b,c,name

#testNumber = 255
#testNum = 10
#exp = 2

#m0 = testNumber*1.0/(testNum-1)
#y = testNumber

'''
for X in range(testNum):
	Y0 = m0*X
	sys.stdout.write( str(int(Y0)) + ' ' )

print '\n'

for X in range(testNum):
	Y = m*(X**exp)
	sys.stdout.write( str(int(Y)) + ' ')
'''


def exponentY(X,exp,m):
	Y = m*(X**exp)
	return Y

def exponentX(Y,exp,m):
	X = (Y/m)**(0.5)
	return X

def binExponentY(localMax,exp,num):
	Ys = []
	m = localMax*1.0/((num-1)**exp)
	for X in range(num):
		Y = exponentY(X,exp,m)
		Ys.append(int(Y))
	return Ys

for color in colors:
	exp = 2
	a,b,c,name = split(color)
	A = binExponentY(int(a),2,num)
	B = binExponentY(int(b),2,num)
	C = binExponentY(int(c),2,num)
	#print a,b,c,name, A,B,C
	for index in range(num):
		st = 'uint32_t ' + name +'_'+ str(index) + ' = strip.Color('+str(A[index])+\
			','+str(B[index])+','+str(C[index])+');'
		if not printColor: print st
	if not printColor: print '\n'

'''
for color in colors:

	a,b,c,name = split(color)	

	for i,val in enumerate(range(num)): # change this to just val
		aCalc = int( int(a)*1.0/(num-1)*val )
		bCalc = int( int(b)*1.0/(num-1)*val )
		cCalc = int( int(c)*1.0/(num-1)*val )	
		st = 'uint32_t ' + name +'_'+ str(i) + ' = strip.Color('+str(aCalc)+\
			','+str(bCalc)+','+str(cCalc)+');'
		if not printColor: print st

	if not printColor: print '\n'
'''


if not printConditional: print "uint32_t picker(int value){"
if not printConditional: print '\tif (value < ' + '10' + ' ){thisColor = YELLOW_2;}'
maths = 0
for index, color in enumerate(colors):
	for i in range(num):
		a,b,c,name = split(color)
		maths = (index+1)*10+i
		if not printConditional: print "\tif (value == " + str(maths) +')', "{thisColor = " + name + \
			'_' + str(i)+ ';}'

if not printConditional: print '\tif (value > ' + str(maths) +') {thisColor = WHITE2_9;}'
if not printConditional: print '\treturn thisColor;}'

matrixSize = len(colors)*num	

count = 10
if not printArray: sys.stdout.write('\n')
if not printArray: sys.stdout.write('newSim = array([')
trip = False
for row in range(numRows):
	if not printArray: sys.stdout.write('[')
	for col in range(num):
		if not printArray: sys.stdout.write( str(count)+',')

		#if new size this eq might fail

		if count <= matrixSize-1+num and not trip: count = count +1
		if count > matrixSize-1+num: trip = True; count = 0
	if not printArray: 
		if row != numRows-1: sys.stdout.write('0],'); sys.stdout.write('\n')
		if row == numRows-1: sys.stdout.write('0]')
if not printArray: sys.stdout.write('])\n')
if not printArray: sys.stdout.write('\n')


'''

oneD = []
for i in range (matrixSize):
	oneD.append(i+10)

newRow = zeros(10)
newCol = zeros((numRows,1))

fullMatrix = reshape(oneD,[num,len(colors)])

print fullMatrix

for i in range(numRows-len(colors)):
	fullMatrix = vstack([fullMatrix,newRow])

fullMatrix = hstack([fullMatrix,newCol])
'''


