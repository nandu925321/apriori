from candidateGen import *

#Values taken from text book, page number 22, example 3.
a = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [1, 3, 5], [2, 3, 4]]
#b = [['apple', 'ball', 'cat'], ['apple', 'ball', 'dog'], ['apple', 'cat', 'dog'], ['apple', 'cat', 'egg'], ['ball', 'cat', 'dog']]
MIS = {1:0.1, 2:0.2, 3:0.05, 4:0.06, 5:0.001}
sup = {1:0.8, 2:0.6, 3:0.8, 4:0.6, 5:0.2}
MSD = 0.4
res = candidateGen(a, MIS, sup, MSD)
print res
#res = candidateGen(b, MIS, sup, MSD)
#print res
L = [ 100, 140, 90, 60, 50 ]
counts = {100: 1, 140: 1, 80:5, 90:2, 60:0, 50:2}
MIS = {100: 0.10, 140: 0.15, 80: 0.20, 90: 0.20, 60: 0.30, 50: 0.40}
sup = {100: 1/6.0, 140: 1/6.0, 80: 5/6.0, 90: 2/6.0, 60: 0, 50: 2/6.0}
print sup
res2 = level2CandidateGen (L, MIS, sup, MSD)
res = candidateGen(res2, MIS, sup, MSD)
print res2
print res
