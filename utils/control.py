#!/usr/bin/env python
from subprocess import Popen, PIPE

def do_it():
	sudo_password = 'admin'
	#command = 'leapd'.split()
	p = Popen(['gnome-terminal', '-x', 'ls'], stdin=PIPE, stderr=PIPE,universal_newlines=True, shell=True)
	sudo_prompt = p.communicate('\n')[1]
	#status = p.wait()

if __name__ == "__main__":
	do_it()
