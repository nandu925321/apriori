'''
Created on Feb 6, 2017

@author: sourabh
'''
from read_file_for_MSApriori import read_files
from CandidateGen import level2CandidateGen
from CandidateGen import candidateGen

input_data = read_files()

N = input_data["N"]
T = input_data["T"]
mis_values_sorted = input_data["MIS"]
support_values = input_data["C_1"]
C=[]
C.insert(0, input_data.get("C_1"))
dict_c = {}
L = []

# create a dictionary with support counts
for x in support_values:
    dict_c[x[0]] = x[1]
# sort and fill L
for k in mis_values_sorted:
    mis = mis_values_sorted.get(k)
    if (dict_c.get(k) !=None and dict_c.get(k)>0):
        if (float(dict_c.get(k))/N >= mis):
            temp = [k,dict_c.get(k)]
            L.append(temp)
            temp=[]
            
print L

F= []

F = [[x[0],x[1]] for x in L if float(x[1])/N > mis_values_sorted.get(x[0])]

print mis_values_sorted
print F

# Main implementation of for loop
k=1
scd = input_data["SDC"]
while True:
    if(len(F[k-1])>0):
        
        my_dict = {}
        if k==1:
            C.insert(k,level2CandidateGen(L,scd))
        else:
            C.insert(k,candidateGen(F[k],scd))
     
            for c in C[k]:
                
                # print c
                my_dict[tuple(c)] = 0    
            
            for t in T:
                for c in C[k]:
                    for cic in t :
                
                        count = my_dict.get(tuple(c))
                        count = count + 1
                        my_dict[tuple(c)] = count
                
                        cic_without_first_item = cic[1:]
                        if( cic_without_first_item in t):
                            c_minus_one_count = my_dict.get(tuple(cic_without_first_item))
                            c_minus_one_count = c_minus_one_count + 1
                            my_dict[tuple(cic_without_first_item)] = c_minus_one_count
                    
                    
            F.insert(k, [c for c in C[k] if float(my_dict.get(tuple(c))) / input_data.get('N') > mis_values_sorted.get(c[0])])
                                    
    else:
             
        break
print F