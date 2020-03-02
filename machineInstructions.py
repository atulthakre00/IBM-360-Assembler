def machInstn(relLocn , symTab , bTab , litTab , pseudoType , rrType , rxType):
    (n,i) = (len(relLocn),0)
    basePointer = -1
    machTab = []
    while i<n:
        cmd = relLocn[i][1][1]
        if relLocn[i][1][1] in pseudoType:
            if relLocn[i][1][1] == 'USING':
                basePointer += 1
        elif relLocn[i][1][1] in rrType:
            temp = relLocn[i][1][2].split(',')
            if len(temp) == 2:
                if not(temp[0].isnumeric()):
                    t = valFromSymbol(temp[0],symTab)
                    if t == -1:
                        t = valFromLiteral(temp[0],litTab)
                    temp[0] = t
                if not(temp[1].isnumeric()):
                    t = valFromSymbol(temp[1],symTab)
                    if t == -1:
                        t = valFromLiteral(temp[1],litTab)
                    temp[1] = t
            else:
                if not(temp[0].isnumeric()):
                    temp[0] = valFromSymbol(temp[0],symTab)
                if relLocn[i][1][1] == "BR":
                    temp.insert(0,15)
                    cmd = "BCR"                
            arg = str(temp[0]) + "," + str(temp[1])                
            machTab.append([relLocn[i][0],[cmd , arg]])
        elif relLocn[i][1][1] == 'CLI':
            pass
        elif relLocn[i][1][1] in rxType:
            temp = relLocn[i][1][2].split(',')
            if relLocn[i][1][1] == 'BNE':
                temp.insert(0,'7')
                cmd = 'BC'
            if len(temp) == 2:
                index = 0
                if not(temp[0].isnumeric()):
                    temp[0] = valFromSymbol(temp[0],symTab)
                if temp[1].find(')') != -1 and temp[1][0] != '=':
                    index = indexExtractor(temp[1],bTab,symTab)
                    if temp[1][0] != '=':
                        temp[1] = temp[1][:temp[1].find('(')]
                if not(temp[1].isnumeric()):
                    t = valFromSymbol(temp[1],symTab)
                    if t == -1:
                        t = valFromLiteral(temp[1],litTab)  
                    temp[1] = t
                
                temp[1] = calcAddress(temp[1],index,basePointer,bTab)
                arg = str(temp[0]) + "," + str(temp[1])                
                machTab.append([relLocn[i][0],[cmd , arg]])  
        elif relLocn[i][1][1] == 'LTORG' or relLocn[i][1][1] == 'DS' or relLocn[i][1][1] == 'DC':
            pass
        i += 1
    return(machTab)