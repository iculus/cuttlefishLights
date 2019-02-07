import serial, struct, sys
from numpy import interp, zeros, chararray, reshape, append, array, roll
sys.path.insert(1,'/usr/lib/python2.7')
import subprocess
from time import sleep

start = chr(255)
end = chr(254)

def startProcess():
	p = subprocess.Popen(['./findDevicePath.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="/home/admin/Desktop/cuttlefishLights/utils")
	out, err = p.communicate()
	return out

def sendIt(sim, numFings, ser, bright):
	ranger = volts = button = 0
	#print ser.read()
	toSend = sim.T
	toSend = toSend.reshape(242)

	#add the numfings to the end of the message
	toSend = append(toSend,numFings) 

	#add the brightness to the end of the message
	toSend = append(toSend,bright)

	#build struct and send messa
	message = start+struct.pack("<244B", *toSend)+end
	ser.write(message)

	#read incoming message
	inp = ser.readline()
    	vals = str(inp.decode("utf-8")).split(',')
	try:
		ranger = vals[0]
		volts = vals[1]
		button = vals[2]
	except: pass
    	sleep(1./120)
	return ranger, volts, button

def setupSerial():

	result = startProcess()
	if "Leonardo" in result:
		res = result.split('\n')
		for i in res:
			if "Leonardo" in i:
				dev,name = i.split('-')
			if "Feather" in i:
				dev2,name2 = i.split('-')
	print dev, name, dev2, name2
	
	ser = serial.Serial(port = str(dev.strip(' ')), baudrate = 115200,timeout = 0)

	try:
		if(ser.isOpen() != False):
			print 'Serial Port Open'
		if(ser.isOpen() == False):
			ser.open()
			print 'its not open'
	except IOError: # if port is already opened, close it and open it again and print message
		print 'error'
		ser.close()
		ser.open()
	return ser
