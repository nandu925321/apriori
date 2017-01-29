'''
Created on Jan 27, 2017

@author: sourabh
'''
# MS Algol

import  re
import numpy as np


def candidateGen (Fkprev):
    npFkprev = np.asarray(Fkprev)
    C = []
    for i in range(len(npFkprev) - 1):
        for j in range(i + 1, len(npFkprev)):
            f1 = npFkprev[i]
            f2 = npFkprev[j]
            if np.array_equal(f1[:-1], f2[:-1]):
                if (f1[-1] < f2[-1]):
                    c = np.append(f1, [f2[-1]])
                else:
                    c = np.append(f2, [f1[-1]])
                
                p = np.ma.array(c, mask=False)
                include = True
                for k in range(len(c)):
                    p.mask[k] = True
                    pc = p.compressed()
                    p.mask[k] = False
                    # print pc
                    if (npFkprev[...]==pc).all(1).any() == False:
                        include = False
                if include == True:
                    C.append(c.tolist())
    return C

def init_pass():
    # file_object = open("D:/Homeworks semester_one/Data Mining and Text Mining/One/Inputs/input-data.txt","r")
#     print "Name of the file: ", file_object.name -- remove this stuff only to check i/o 
#     print "Closed or not : ", file_object.closed
#     print "Opening mode : ", file_object.mode
#     print file_object.read()
    support_count = []
    linecounter = 0
    mis_values = []
    ret_dict = {}
    
    with open("D:/Homeworks semester_one/Data Mining and Text Mining/One/Inputs/input-data.txt", "r") as f:
        data = f.readlines()
        for line in data:
            linecounter = linecounter + 1
            support_count.append([int(s) for s in re.findall(r'\b\d+\b', line)])
    
    ret_dict ['T'] = support_count
    # print ret_dict ['T']
    support_count = sum(support_count, [])
    # consider using other alternatives if the array size is large
    # http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
    # print support_count
    support_count = [[x, support_count.count(x)] for x in set(support_count)]
    # use other methods if this crashes http://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item-in-python
    # print support_count
    support_count.sort(cmp=None, key=None, reverse=False)
    # print support_count
    # print linecounter
    ret_dict["C_1"] = support_count
    ret_dict['N'] = linecounter
    # print return_list
    
    with open ("D:/Homeworks semester_one/Data Mining and Text Mining/One/Inputs/parameter-file.txt", "r") as r:
        x = 0
        info = r.readlines()
        for line in info:
                     
            if(x > len(support_count) + 1):
                break
            else:
                x = x + 1         
                mis_values.append([int (i) for i in re.findall(r'\b\d+\b', line)])
               
    # print (mis_values)           
    mis_values = [[x[0], float(str(x[1]) + "." + str(x[2]))] for x in mis_values]
    
    mis_values = dict(mis_values)
    # print mis_values
    ret_dict["MIS"] = mis_values           
    # print mis_values
    # print ret_dict           
    return ret_dict



values = {}
values = init_pass()
minsup = 0.40
C = []
F = []
C.insert(0, values.get("C_1"))
# print C
F = [[[x[0]]  for x in C[0] if float(x[1]) / values.get('N') > minsup]]
# print F
k = 1
# print candidateGen(F[0])


 
while True:
     
    if(len(F[k - 1]) > 0):
        my_dict = {}
        # print k
        C.insert(k, candidateGen(F[k - 1]))
        for c in C[k]:
            # print c
            my_dict[tuple(c)] = 0
             
        for t in values.get('T'):
            # print t
            for c in C[k]:
                # print c
                for cic in c: 
                    if cic in t:
                                     
                        # print ("IN if")
                        count = my_dict.get(tuple(c))
                        count = count + 1
                        my_dict[tuple(c)] = count
         
     
        F.insert(k, [c for c in C[k] if float(my_dict.get(tuple(c))) / values.get('N') > minsup])                
       
        k = k + 1
     
                        
    else:
        break
         


print F
