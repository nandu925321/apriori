'''
Created on Feb 7, 2017

@author: sourabh parime
'''
# Reads the input file for all the parameters


import re
import operator

def read_files(inputFile, parameterFile):
    # file_object = open("D:/Homeworks semester_one/Data Mining and Text Mining/One/Inputs/input-data.txt","r")
#     print "Name of the file: ", file_object.name -- remove this stuff only to check i/o 
#     print "Closed or not : ", file_object.closed
#     print "Opening mode : ", file_object.mode
#     print file_object.read()
    support_count = []
    linecounter = 0
    mis_values = []
    ret_dict = {}
    
    with open(inputFile, "r") as f:
        data = f.readlines()
        for line in data:
            linecounter = linecounter + 1
            support_count.append([int(s) for s in re.findall(r'\b\d+\b', line)])
    
    ret_dict ['T'] = support_count
    #print ret_dict ['T']
    support_count = sum(support_count, [])
    # consider using other alternatives if the array size is large
    # http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
    #print support_count
    ret_dict['I'] = [x for x in set(support_count)]
    support_count = [[x, support_count.count(x)] for x in set(support_count)]

    # use other methods if this crashes http://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item-in-python
    # print support_count
    support_count.sort(cmp=None, key=None, reverse=False)
    # print support_count
    # print linecounter
    ret_dict["C_1"] = support_count
    ret_dict['N'] = linecounter
    sup = {}
    for x in support_count:
        sup[x[0]]=float(x[1])/ret_dict['N']

    ret_dict['sup'] = sup
    print "I :"
    print ret_dict["I"]
    # print return_list
    spa = []
    
    with open (parameterFile, "r") as r:
        x = 0
        info = r.readlines()
        
        for line in info:
            
            if "MIS" in line:    
                mis_values.append([int (i) for i in re.findall(r'\b\d+\b', line)])
                
            if "SDC" in line:
                ret_dict["SDC"] = float(re.findall("\d+[\.]\d", line)[0])
                     
            if "cannot_" in line:
                
                #sp = re.findall(r"\{([^}]+)\}", line)
                
                sp = re.search(r"\{([^}]+)\}.*", line).group(0)
                temp = []
                num =''
                prev=''
                #print sp
                for i in sp:
                    
                   
                    
                    if i.isdigit():
                        num = num+i
                    
                    if i==',' and prev.isdigit():
                        temp.append(int(num))
                        num=''
                        
                    if i =='}' and prev.isdigit():
                        temp.append(int(num))
                        #print temp
                        spa.insert(0, temp)
                        num=''
                        #print temp
                        temp = []
                        #temp[:] = []
                                                          
                    prev = i    
        #print spa
                ret_dict["cannot"] = spa
            if "must" in line:
                    
                    mst = [int (i) for i in re.findall(r'\b\d+\b', line)]
                    ret_dict["must"] = mst
                    #print mst
#             if(x > len(support_count) + 1):
#                 break
#             else:
#                 x = x + 1         
#                 mis_values.append([int (i) for i in re.findall(r'\b\d+\b', line)])
#                
    # print (mis_values)           
    mis_values = [[x[0], float(str(x[1]) + "." + str(x[2]))] for x in mis_values]
    
    mis_values = dict(mis_values)
    # print mis_values
    ret_dict["MIS"] = mis_values           
    #print mis_values
    mis_sorted = sorted(ret_dict["MIS"].items(), key= operator.itemgetter(1))
    mis_d = {}
    for m in mis_sorted:
        mis_d[m[0]] = m[1]
    # use 0 to sort by keys
    ret_dict["MIS"]= mis_d
    #print(len(support_count)) 
    print ret_dict          
    return ret_dict
