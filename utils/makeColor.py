#GRB

mx = 255 #max value
num = 10 # number of brightnesses

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


R = "RED = (0,255,0)"
O = "ORANGE = (100,255,0)"
Y = "YELLOW = (255,255,0)"
T = "TEAL = (255,0,255)"
G = "GREEN = (255,0,0)"
B = "BLUE = (0,0,255)"
F = "FUCHA = (0,255,100)"
P = "PURPLE = (0,170,255)"
W = "WHITE = (255,255,255)"


colors = [R,O,Y,T,G,B,F,P,W]

for color in colors:
	color = color.replace('(','').replace(')','').replace(' ','')
	name,color=color.split('=')
	a,b,c=color.split(',')

	for i,val in enumerate(range(num)):
		st = 'uint32_t ' + name +'_'+ str(i) + ' = strip.Color('+str(int(a)/(num-1)*val)+\
			','+str(int(b)/(num-1)*val)+','+str(int(c)/(num-1)*val)+');'
		print st

	print '\n'
