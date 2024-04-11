
def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = face * couponRate
    for t in range(1,m+1):
        pv = (1+y)**(-t)
        pvcf = cf * pv
        pvcfsum += pvcf
    bondPrice = pvcfsum + face * pv
    return(bondPrice)
