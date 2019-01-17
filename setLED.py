#!/usr/bin/env python
import sys
import time as t

x = sys.argv[1]

print("LED %s" % x)

while x == 'on':
	print('on')
	t.sleep(0.001)
	print('off')
	t.sleep(0.001)
