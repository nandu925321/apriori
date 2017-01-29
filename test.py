from candidateGen import *

#Values taken from text book, page number 22, example 3.
a = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [1, 3, 5], [2, 3, 4]]
b = [['apple', 'ball', 'cat'], ['apple', 'ball', 'dog'], ['apple', 'cat', 'dog'], ['apple', 'cat', 'egg'], ['ball', 'cat', 'dog']]
res = candidateGen(a)
print res
res = candidateGen(b)
print res
