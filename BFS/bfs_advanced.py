import string
import sys
from multiprocessing import Process
from queue import Queue

track = {}
alpha = [x for x in string.ascii_lowercase[:26]]
dict_three = [x[:-1] for x in open('../three_alpha.txt','r')]
dict_four = [x[:-1] for x in open('../four_alpha.txt','r')]
dict_five = [x[:-1] for x in open('../five_alpha.txt','r')]
dict_full = set(dict_three + dict_four + dict_five)
fringe = Queue(len(dict_full))
visited = set()
start = sys.argv[1]
end = sys.argv[2]

def reduce(word):
	for i in range(len(word)):
			new_word = list(word)
			for rm in ['']:
				new_word[i] = rm
				tword = ''.join(new_word)
				if tword in dict_full and tword not in visited:
					fringe.put(tword)
					visited.add(tword)
					track[tword] = word
					if tword == end:
						return True
	return False

def grow(word):
	for i in range(len(word)):
			new_word = list(word)
			for new_letter in alpha:
				new_word.insert(i,new_letter)
				tword = ''.join(new_word)
				new_word = list(word)
				if tword in dict_full and tword not in visited:
					fringe.put(tword)
					visited.add(tword)
					track[tword] = word
					if tword == end:
						return True
	return False

def look(word):
	for i in range(len(word)):
				new_word = list(word)
				for new_letter in alpha:
					new_word[i] = new_letter
					tword = ''.join(new_word)
					if tword in dict_full and tword not in visited:
						fringe.put(tword)
						visited.add(tword)
						track[tword] = word
						if tword == end:
							return True
	return False

def word_chain():

	found = False

	if start == end:
		print('The word chain length form ' + start +' to ' + end +  ' is 0.')
		sys.exit()

	if len(start) != 4 or len(end) != 4:
		print('Both words most be four letters long.')
		sys.exit()

	if start not in dict_full:
		print("'Start' was not in the dictionary.'")
		sys.exit()

	if end not in dict_full:
		print("'End' was not in the dictionary.'")
		sys.exit()

	track[start] = None
	visited.add(start)
	fringe.put(start)

	while not found:
		word = fringe.get()
		if len(word) == 4:
			found = look(word)
			if found:
				break
			grow(word)
			reduce(word)
		elif len(word) == 3:

			look(word)
			found = grow(word)
			if found:
				break
		else:
			look(word)
			found = reduce(word)
			if found:
				break
			
	chain = []
	p = end
	while p != None:
		chain.append(track[p])
		p = track[p]
	chain = chain[:-1]
	chain = chain[::-1]
	chain.append(end)
	print(chain,'\nThe word chain length form ' + start +' to ' + end +  ' is ' + str(len(chain)-1) + '.')

if __name__ == '__main__':
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		print("Enter the a 'Start' word and 'End' word as command line arguments.")
		print("Optionally, you may enter a number of seconds you would like the program to try and find a complete word chain. (Default: 10)")
		sys.exit()	
	if len(sys.argv) == 4:
		time_out = int(sys.argv[3])
	else:
		time_out = 10
	p = Process(target=word_chain)
	p.start()
	p.join(time_out)
	if p.is_alive():
		print("Process took more than " + str(time_out) + " seconds. \nKilling process...")
		p.terminate()
		p.join()