import subprocess

def startProcess():
	p = subprocess.Popen(['./findDevicePath.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="/home/admin/Desktop/cuttlefishLights/utils")
	out, err = p.communicate()
	return out

result = startProcess()

if "Arduino" in result: 
	dev,name = result.split('-')

try: dev = dev.strip(' ')
except: print "error"

