import numpy as np
def candidateGen (Fkprev, MIS, sup, MSD):
    npFkprev = np.asarray(Fkprev)
    C = []
    for i in range(len(npFkprev) - 1):
        for j in range(i+1, len(npFkprev)):
            f1 = npFkprev[i]
            f2 = npFkprev[j]
            if np.array_equal(f1[:-1],f2[:-1]) and abs(sup[f1[-1]] - sup[f2[-1]]) <= MSD:
                if (f1[-1] < f2[-1]):
                    c = np.append(f1,[f2[-1]])
                else:
                    c = np.append(f2,[f1[-1]])
                
                p = np.ma.array(c, mask=False)
                include = True
                for k in range(len(c)):
                    p.mask[k] = True
                    s = p.compressed()
                    p.mask[k] = False
                    if ((c[0] == s).any() == True) or (MIS[c[1]] == MIS[c[0]]):
                        if (npFkprev[...]==s).all(1).any() == False:
                            include = False
                if include == True:
                    C.append(c.tolist())
    return C


#where L is the output from InitPass function, countList is the list of counts of all items, MIS is the 
def level2CandidateGen (L, MIS, sup, MSD):
    C2 = []
    for i in range(len(L)):
        l = L[i]
        if sup[l] >= MIS[l]:
            for j in range(i+1, len(L)):
                h = L[j]
                if sup[h] >= MIS[l] and abs(sup[h] - sup[l]) <= MSD:
                    C2.append([l,h])
    return C2

