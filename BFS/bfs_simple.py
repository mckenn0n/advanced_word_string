import string
from queue import Queue

track = {}
alpha = [x for x in string.ascii_lowercase[:26]]
dict_four = open('../four_alpha.txt','r')
dict_four = set([x[:-1] for x in dict_four])
fringe = Queue(len(dict_four))
visited = set()
path_len = 0

found = False

start = 'cats'
end = 'bear'

visited.add(start)
fringe.put(start)

# for i in range