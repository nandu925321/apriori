'''
Created on Feb 6, 2017

@author: sourabh
'''
from read_file_for_MSApriori import read_files
from candidateGen import *
#from candidateGen import candidateGen
import sys

inputFile = sys.argv[1]
parameterFile = sys.argv[2]

input_data = read_files(inputFile, parameterFile)
#print "________________________________________________________"
#print input_data
#print "________________________________________________________"

N = input_data["N"]
T = input_data["T"]
I = input_data["I"]
MIS = input_data["MIS"]
sup = input_data["sup"]


def keyGen(cmpValue):
    return MIS[cmpValue]

def is_subset(a, b):
  c = np.intersect1d(a,b)
  return c.size == b.size

I.sort(key=keyGen)

print "--------------------------------------------------------------"
print I
print MIS
print "--------------------------------------------------------------"


mis_values_sorted = input_data["MIS"]
support_values = input_data["C_1"]
C=[]
C.insert(0, input_data.get("C_1"))
dict_c = {}
L = []

# sort and fill L
savedI = 0.0
for i in I:
    if (sup[i] >= MIS[i]) and savedI == 0.0:
        savedI = MIS[i]
        L.append(i)
    elif (sup[i] >= savedI) and savedI > 0.0 :
        L.append(i)
            
print "*************************************************************"
print L
print "*************************************************************"

# Main implementation of for loop
Fkprev = [[x] for x in L if sup[x] >= MIS[x]]
print "Fkprev: ", Fkprev
F= []
C = []
TC = []
k=1
npT = np.asarray(T)
scd = input_data["SDC"]
while True:
    if(len(Fkprev)>0):
        
        my_dict = {}
        if k==1:
            Ck = level2CandidateGen(L, MIS, sup, scd)
        else:
            Ck = candidateGen(Fkprev, MIS, sup, scd)
        print "Ck: ", Ck
        for c in Ck:
            
            # print c
            my_dict[tuple(c)] = 0    

        for t in npT:
            for c in Ck:
                npt = np.asarray(t)
                npc = np.asarray(c)
                if is_subset(npt, npc) :
            
                    count = my_dict.get(tuple(c))
                    count = count + 1
                    my_dict[tuple(c)] = count
            
                    cic_without_first_item = c[1:]
                    if( cic_without_first_item in t):
                        c_minus_one_count = my_dict.get(tuple(cic_without_first_item))
                        c_minus_one_count = c_minus_one_count + 1
                        my_dict[tuple(cic_without_first_item)] = c_minus_one_count
                
             
        Fk = [c for c in Ck if float(my_dict.get(tuple(c))) / input_data.get('N') > MIS[c[0]]]
        print "000000000000000000000000000000000000000000000000000000000000000"
        print "my_dict : ", my_dict
        print Fk
        print "000000000000000000000000000000000000000000000000000000000000000"
        F.append(Fk)
        C.append(Ck)
        TC.append(my_dict)
        Fkprev = Fk

        k = k + 1
                                    
    else:
             
        break
print F