import numpy as np
def candidateGen (Fkprev):
    npFkprev = np.asarray(Fkprev)
    C = []
    for i in range(len(npFkprev) - 1):
        for j in range(i+1, len(npFkprev)):
            f1 = npFkprev[i]
            f2 = npFkprev[j]
            if np.array_equal(f1[:-1],f2[:-1]):
                if (f1[-1] < f2[-1]):
                    c = np.append(f1,[f2[-1]])
                else:
                    c = np.append(f2,[f1[-1]])
                
                p = np.ma.array(c, mask=False)
                include = True
                for k in range(len(c)):
                    p.mask[k] = True
                    pc = p.compressed()
                    p.mask[k] = False
                    #print pc
                    if any(np.equal(npFkprev,pc).all(1)) == False:
                        include = False
                if include == True:
                    C.append(c.tolist())
    return C




