
def getBondPrice_E(face, couponRate, m, yc):
    bondPrice = 0
    for t, y in enumerate(yc, 1):
        cf = face * couponRate
        pv = (1 + y) ** (-t)
        pvcf = cf * pv
        if t < m:
            bondPrice += pvcf
        else:
            bondPrice += pvcf + face * pv
    return(bondPrice)
