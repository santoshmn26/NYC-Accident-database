from operator import itemgetter
import sys
current_word= None	# declare current word 
current_count=0		# initilize the count to zero
word=None

loc=['BOROUGH', 'BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS']  # different location in the database
loc_count=[]		# list of all the location with number of accidents 
c_factor=[]		# list of all the factors for accidents with number of occurances

for line in sys.stdin:			# get input from standard input
	line=line.strip()
	word, count=line.split('\t',1)	# strip the line to get the word and the count
	count=int(count)		# convert string 1 to int 1
#	print(line)

	if current_word==word:
		current_count+= count	# increment the count of the current word
	else:
		#x.append(word)
		if current_word:
			if(current_word in loc):
				tmp=current_word+','+str(current_count)
				loc_count.append(tmp)	# append the current word to the list of locations
			else:
				tmp=current_word+','+str(current_count)
				c_factor.append(tmp)	# append the current word to the list of factors for the accidents
			#print(current_word,current_count)
		current_count=count
		current_word=word

if current_word==word:
	#print (current_word, current_count)
	pass

print("--------------------------------------------------------------")	# display purpose
print("Location count:")
for i in loc_count:	# list of all the location with number of accidents
	print '%s' %(i)
print("--------------------------------------------------------------")	# display purpose
print("Factor count:")
for i in c_factor:	# list of all the factors for accidents with number of occurances
	print '%s' %(i)
print("--------------------------------------------------------------")	# display purpose

