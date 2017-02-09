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
supp_vals_dict={}
for sv in support_values:
    supp_vals_dict[sv[0]] = sv[1]
print "support_vals",supp_vals_dict[70]
print "--------------------------------------------------------------"
Ctemp_=[]
dict_c = {}
Ctemp_ = input_data.get("C_1")
for c in Ctemp_:
    dict_c[c[0]]=c[1]
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
print "dict first set ",dict_c
print "*************************************************************"

# Main implementation of for loop
Fkprev = [[x] for x in L if sup[x] >= MIS[x]]
F1=Fkprev
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

# F has an empty list in the end trimming that list
F.pop()
print "F after popping", F
def write_to_file(F,C,TC,supp_vals_dict,dict_c):

    pen = open("output.txt","w")
    #print frequent 1-itemsets
    pen.write("Frequent 1-item sets:")
    pen.write("\n\n\t")
    # Writing frequent 1 item sets to file 
    for f1 in F1:
        pen.write(str(supp_vals_dict.get(f1[0]))+" : "+"{"+str(f1[0])+"}")
        
        pen.write("\n")
        pen.write("\t")
    pen.write("\n\tTotal number of frequent 1-itemsets = "+str(len(F1))+"\n")
    # Writing > 1 frequent item sets
    dc_count= 0 # this is to retrieve dicts
    k=2
    for f2 in F:
        pen.write("\nFrequent "+str(k)+"-item sets:")
        pen.write("\n\n\t")
        my_d = TC[dc_count]
        for f in f2:
            if (my_d.get(tuple(f)) != None):
                pen.write(str(my_d.get(tuple(f)))+" : "+"{"+str(f).strip('[]')+"}")
                #find the tail count here
                tail=""
                if k==2:
                    tail = str(dict_c.get(f[1]))
                else:
                    tail = str(my_d.get(tuple(f[1:])))
                pen.write("\nTail count = "+tail)        
                pen.write("\n")
                pen.write("\t")
                

                #print str(my_d.get(tuple(f))) +str(tuple(f))+"tuple count" 
        pen.write("\n\tTotal number of frequent "+str(k)+"-itemsets = "+str(len(f2))+"\n")
        dc_count = dc_count+1
        k = k+1
    print F
            



write_to_file(F,C,TC,supp_vals_dict,dict_c)