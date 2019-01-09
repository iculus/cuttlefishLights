import sys

num = 242
print '\n\n\n'
count = 0

sys.stdout.write("int seq[] = {")
for i in range (num-1):
	sys.stdout.write("\tmsg1.bit"+str(i)+',')
	count += 1
	if count == 22:
		print '\r'
		count = 0
sys.stdout.write("msg1.bit"+str(num-1))
sys.stdout.write('};')

print '\n\n\n'
