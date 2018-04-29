# -*- coding: utf-8 -*-
#!/usr/bin/env python
#importing system modules
import sys
x1=[] # a list to store all the locations of the accidents 
for row in sys.stdin:	# iterating each row from the csv file
	try:		
		row=row.strip()	# striping the each rows from the database
		words=row.split()	# string each attributes in the row to get the location attribute
		x=words[0]
		x=x.split(',')		# x[2] contains the location from the string for the location of the accident
		if(x[2]!=""):		# to ignore null values
			if(x[2] not in x1):
				x1.append(x[2])		# make a list of all values
			print '%s\t%s' % (x[2],1)	# printing location and the occurance times
		continue
	except:
		continue
for row in sys.stdin:	# iterating each row from the csv file
	try:		
		row=row.strip()	# striping the each rows from the database
		words=row.split(",")	# string each attributes in the row to get the location attribute
		x=words[19]
		print(x)
		#x=x.split(',')		# x[2] contains the location from the string for the location of the accident
		if(x!=""):		# to ignore null values
			if(x not in x1):
				x1.append(x)		# make a list of all values
			print '%s\t%s' % (x,1)	# printing location and the occurance times
		continue
	except:
		continue


