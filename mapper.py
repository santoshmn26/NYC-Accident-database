# -*- coding: utf-8 -*-
#!/usr/bin/env python
#importing system modules
import sys
x1=[] # a list to store all the locations of the accidents 
for i in range(100000):
	for row in sys.stdin:	# iterating each row from the csv file
		row=row.strip()	# striping the each rows from the database
		words=row.split()	# string each attributes in the row to get the location attribute
		x=words[0]
		x=x.split(',')		# x[2] contains the location from the string for the location of the accident
		try:		
			if(x[2]!=""):		# to ignore null values
				if(x[2] not in x1):
					x1.append(x[2])		# make a list of all values
				print '%s\t%s' % (x[2],1)	# printing location and the occurance times
			break
		except:
			break
#mapping cotributing factor 1 for the accident
for i in range(100000):
	for row in sys.stdin:	# iterating each row from the csv file
		x=row.split(",")	# striping the each rows from the database
		try:		
			if(x[19]!=""):		# to ignore null values
				if(x[19] not in x1):	# x[19] contains the attribute for contributing factors of the accident
					x1.append(x[19])	# make a list of all values
				print '%s\t%s' % (x[19],1)	# printing location and the occurance times
			break
		except:
			break
#mapping cotributing factor 2 for the accident
for i in range(100000):
	for row in sys.stdin:	# iterating each row from the csv file
		x=row.split(",")	# striping the each rows from the database
		try:		
			if(x[20]!=""):		# to ignore null values
				if(x[20] not in x1):	# x[19] contains the attribute for contributing factors of the accident
					x1.append(x[20])	# make a list of all values
				print '%s\t%s' % (x[20],1)	# printing location and the occurance times
			break
		except:
			break
