import serial, struct
from numpy import interp, zeros, chararray, reshape, append, array, roll

start = chr(255)
end = chr(254)

def sendIt(sim, numFings, ser, bright):
	toSend = sim.T
	toSend = toSend.reshape(242)

	#add the numfings to the end of the message
	toSend = append(toSend,numFings) 

	#add the brightness to the end of the message
	toSend = append(toSend,bright)

	#build struct and send messa
	message = start+struct.pack("<244B", *toSend)+end
	ser.write(message)

def setupSerial():
	try: ser = serial.Serial(port = '/dev/ttyACM1', baudrate = 9600,timeout = 0)
	except: ser = serial.Serial(port = '/dev/ttyACM0', baudrate = 9600,timeout = 0)
	try:
		print 'Serial Port Open'
		if(ser.isOpen() == False):
			ser.open()
			print 'its not open'
	except IOError: # if port is already opened, close it and open it again and print message
		print 'error'
		ser.close()
		ser.open()
	return ser
