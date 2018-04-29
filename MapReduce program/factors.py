# -*- coding: utf-8 -*-
#!/usr/bin/env python
#importing system modules
import sys
x1=[] # a list to store all the locations of the accidents 
for row in sys.stdin:	# iterating each row from the csv file
	try:		
		row=row.strip()	# striping the each rows from the database
		words=row.split(",")	# string each attributes in the row to get the location attribute
		x=words[19]
		y=words[20]
		z=words[21]
		print(x)
		#x=x.split(',')		# x[2] contains the location from the string for the location of the accident
		if(x!=""):		# to ignore null values
			if(x not in x1):
				x1.append(x)		# make a list of all values
			print '%s\t%s' % (x,1)	# printing location and the occurance times
		if(y!=""):		# to ignore null values
			if(y not in x1):
				x1.append(y)		# make a list of all values
			print '%s\t%s' % (y,1)	# printing location and the occurance times
		if(z!=""):		# to ignore null values
			if(z not in x1):
				x1.append(z)		# make a list of all values
			print '%s\t%s' % (z,1)	# printing location and the occurance times
		continue
	except:
		continue


