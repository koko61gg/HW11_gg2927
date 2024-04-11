
def getBondPrice_Z(face, couponRate, times, yc):
    pvcfsum = 0
    for t, y in zip(times, yc):
        cf = face * couponRate
        pv = (1+y) ** (-t)
        pvcf = cf * pv
        pvcfsum += pvcf
    bondPrice = pvcfsum + face * pv
    return(bondPrice)
