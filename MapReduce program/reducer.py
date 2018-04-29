from operator import itemgetter
import sys
current_word= None	# declare current word 
current_count=0		# initilize the count to zero
word=None


for line in sys.stdin:			# get input from standard input
	line=line.strip()
	try:
		word, count=line.split('\t',1)	# strip the line to get the word and the count
		count=int(count)		# convert string 1 to int 1
	except ValueError:
		continue

	if current_word==word:
		current_count+= count	# increment the count of the current word
	else:
		if current_word:
			print '%s\t%s' % (current_word, current_count)
		current_count=count
		current_word=word

if current_word==word:
	print '%s\t%s' % (current_word, current_count)
	

