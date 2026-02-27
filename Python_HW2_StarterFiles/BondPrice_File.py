
import numpy as np

def getBondPrice(y, face, couponRate, m, ppv=1):
    
    n = m * ppv
    C = face * couponRate / ppv
    
    t = np.arange(1, n+1)
    discount = 1 / (1 + y/ppv)**t
    
    couponPV = np.sum(C * discount)
    facePV = face / (1 + y/ppv)**n
    
    return couponPV + facePV
