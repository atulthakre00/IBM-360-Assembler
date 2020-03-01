def valFromSymbol(symbol,symTab):
    for x in symTab:
        if x[0] == symbol:
            return x[1]
    return -1

def valFromLiteral(val,litTab):
    for x in litTab:
        if x[0] == val:
            return x[1]
    return -1

def indexExtractor(a,bTab,symTab):
    i = a.index('(')+1
    j = a.index(')')
    return valFromSymbol(a[i:j],symTab)

def calcAddress(relAddress,index,basePointer,bTab):
    offset = -1
    baseReg = 0
    while offset < 0 and basePointer >= 0:
        baseContent = bTab[basePointer][1]
        baseReg = bTab[basePointer][0]
        offset = relAddress - baseContent
        basePointer -= 1        
    return ( str(offset) + "(" + str(index) + "," + str(baseReg) + ")" )