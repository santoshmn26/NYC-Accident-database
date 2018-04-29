# -*- coding: utf-8 -*-
#!/usr/bin/env python
#importing system modules
import sys
import folium
x1=[] # a list to store all the locations of the accidents 
mapit = folium.Map( location=[40.6960346,-73.9845292], zoom_start=6 )
for row in sys.stdin:	# iterating each row from the csv file
	try:		
		row=row.strip()	# striping the each rows from the database
		words=row.split()	# string each attributes in the row to get the location attribute
		x=words[0]
		x=x.split(',')		# x[2] contains the location from the string for the location of the accident
		if(x[4]!="")&(x[5]!=""):
			y=x[4]+','+x[5]
		print(y)
		if(y!=""):		# to ignore null values
			if(y not in x1):
				x1.append(y)		# make a list of all values
			print '%s\t%s' % (y,1)	# printing location and the occurance times
			folium.Marker( location=[ float(x[4]), float(x[5]) ]).add_to( mapit )
		continue
	except:
		continue
	mapit.save( 'map_output.html')
