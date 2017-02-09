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
must = input_data["must"]
cannot_be_together = input_data["cannot"]

def keyGen(cmpValue):
    return MIS[cmpValue]

def is_subset(a, b):
    npa = np.asarray(a)
    npb = np.asarray(b)
    npc = np.intersect1d(npa, npb)
    return npc.size == npb.size

def contains_atleast_one_of(a, b):
    c = np.asarray(a)
    d = np.asarray(b)
    return (np.intersect1d(c,d)).size > 0

I.sort(key=keyGen)

mis_values_sorted = input_data["MIS"]
support_values = input_data["C_1"]
supp_vals_dict={}
for sv in support_values:
    supp_vals_dict[sv[0]] = sv[1]

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


# Main implementation of for loop
Fkprev = [[x] for x in L if sup[x] >= MIS[x]]
F1=Fkprev

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

        for c in Ck:
            
            # print c
            my_dict[tuple(c)] = 0    

        for t in npT:
            for c in Ck:
                if is_subset(t, c) :
            
                    count = my_dict.get(tuple(c))
                    count = count + 1
                    my_dict[tuple(c)] = count
            
                    cic_without_first_item = c[1:]
                    if( cic_without_first_item in t):
                        c_minus_one_count = my_dict.get(tuple(cic_without_first_item))
                        c_minus_one_count = c_minus_one_count + 1
                        my_dict[tuple(cic_without_first_item)] = c_minus_one_count
                
             
        Fk = [c for c in Ck if float(my_dict.get(tuple(c))) / input_data.get('N') > MIS[c[0]]]
        F.append(Fk)
        C.append(Ck)
        TC.append(my_dict)
        Fkprev = Fk

        k = k + 1
                                    
    else:
             
        break

# F has an empty list in the end trimming that list
F.pop()


def write_to_file(F1, F, C, TC, supp_vals_dict, dict_c, must, cannot):

    pen = open("output.txt","w")
    #print frequent 1-itemsets
    pen.write("Frequent 1-item sets:")
    pen.write("\n\n\t")
    # Writing frequent 1 item sets to file 
    F1_with_must_have = 0
    for f1 in F1:
        if (f1[0] in must):
            pen.write(str(supp_vals_dict.get(f1[0]))+" : "+"{"+str(f1[0])+"}")
        
            pen.write("\n")
            pen.write("\t")
            F1_with_must_have = F1_with_must_have + 1
    pen.write("\n\tTotal number of frequent 1-itemsets = "+ str(F1_with_must_have) +"\n")
    # Writing > 1 frequent item sets

    dc_count= 0 # this is to retrieve dicts
    k=2
    for f2 in F:
        F_with_must_have = 0
        pen.write("\nFrequent "+str(k)+"-item sets:")
        pen.write("\n\n\t")
        my_d = TC[dc_count]
        for f in f2:
            cbtFlag = False
            for cbt in cannot_be_together:
                if is_subset(f, cbt):
                    cbtFlag = True
            if (my_d.get(tuple(f)) != None and contains_atleast_one_of(f, must) and cbtFlag == False):
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
                F_with_must_have = F_with_must_have + 1

                #print str(my_d.get(tuple(f))) +str(tuple(f))+"tuple count" 
        pen.write("\n\tTotal number of frequent "+str(k)+"-itemsets = "+str(F_with_must_have)+"\n")
        dc_count = dc_count+1
        k = k+1     


print "I :", I , "\n"

print "sup : ", sup , "\n"

print "F :", F1, F, "\n"

print "TC :", TC, "\n"

write_to_file(F1, F, C, TC, supp_vals_dict, dict_c, must, cannot_be_together)
