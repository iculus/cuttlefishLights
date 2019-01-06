import serial, time, random, struct

ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600,timeout = 0)

try:
	print 'its open'
    
	if(ser.isOpen() == False):
		ser.open()
		print 'its not open'
		
except IOError: # if port is already opened, close it and open it again and print message
	print 'error'
	ser.close()
	ser.open()

def readSerialPort():
	for line in ser:
		return line	


if __name__ == "__main__":

	while 1:
		while ser.inWaiting() > 0:
			ser.read(1)
	
		start = chr(255)
		end = chr(254)
	
		x = random.randrange(11) #rows
		y = random.randrange(22) #columns
		fing = random.randrange(10) #controls color
		depth = random.randrange(10) #controls brightness
	
		message = start + struct.pack("<BBBB", x,y,fing,depth) + end

		ser.write(message)
	
		print 'writing', time.time()
		print readSerialPort()
