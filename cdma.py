#-----------------------------------------
# CDMA-Sequence Generator for IM/DD Systems
# Adrian Krohn, ICT/NT, RealTime Lab 2022
#-----------------------------------------
import numpy as np

def cdma_short(data, chips): #Short Code
    ld = len(data)
    lc = len(chips)
    out = np.zeros(ld*lc)
    i = 0
    for d in data:
        for c in chips:
            out[i] = 1-(d+c)%2 #Unipolar Inverting
            i += 1
    return out

cdma_seq = cdma_short([1,0,0,1,1,0],[1,0,1,0])
print(cdma_seq)