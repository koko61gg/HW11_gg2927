
def getBondDuration(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    w_pvcf = 0
    cf = face * couponRate
    for t in range(1,m+1):
        pv = (1+y)**(-t)
        pvcf = cf * pv
        pvcfsum += pvcf
        w_pvcf = w_pvcf + pvcf*t
    bondPrice = pvcfsum + face * pv
    pvcf_t = w_pvcf + face * pv *t
    bondDuration = pvcf_t/bondPrice
    return(bondDuration)
