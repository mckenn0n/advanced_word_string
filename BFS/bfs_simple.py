import string
import sys
from queue import Queue

def word_chain():
	track = {}
	alpha = [x for x in string.ascii_lowercase[:26]]
	dict_four = set([x[:-1] for x in open('../four_alpha.txt','r')])
	fringe = Queue(len(dict_four))
	visited = set()
	found = False


	if len(sys.argv) != 3:
		print("Enter the a 'Start' word and 'End' word as command line arguments.")
		sys.exit()

	start = sys.argv[1]
	end = sys.argv[2]

	if start == end:
		print('The word chain length form ' + start +' to ' + end +  ' is 0.')
		sys.exit()

	if len(start) != 4 or len(end) != 4:
		print('Both words most be four letters long.')
		sys.exit()

	if start not in dict_four:
		print("'Start' was not in the dictionary.'")
		sys.exit()

	if end not in dict_four:
		print("'End' was not in the dictionary.'")
		sys.exit()

	track[start] = None
	visited.add(start)
	fringe.put(start)

	while not found:
		word = fringe.get()
		for i in range(len(word)):
			new_word = list(word)
			for new_letter in alpha:
				new_word[i] = new_letter
				tword = ''.join(new_word)
				if tword in dict_four and tword not in visited:
					fringe.put(tword)
					visited.add(tword)
					track[tword] = word
					if tword == end:
						found = True
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
	word_chain()