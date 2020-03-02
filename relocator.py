def relLocationCalc(codeModified , pseudoType , rrType , rxType, litTab):    
    relLocn = []
    litCount = 0
    relLocn.append([0,codeModified[0]])
    (i,n) = (0,len(codeModified))
    count = 0
    tempLit = []
    while i<n-1:
        x = (codeModified[i][2]).split(',')
        for t in x:
            if len(t)!=0 and t[0] == '=':
                litCount += 1
                tempLit.append(t)
        if codeModified[i][1] == 'DC':
            count = count + 4*len(x)            
        elif codeModified[i][1] == 'DS':
            count = count + 4*(int(x[0][:x[0].index('F')]))            
        elif codeModified[i][1] in pseudoType:
            count = count + 0
        elif codeModified[i][1] in rrType:
            count = count + 2            
        elif codeModified[i][1] in rxType:
            count = count + 4
        else:
            if codeModified[i][1] == 'LTORG':
                while count%8 != 0:
                    count += 1
                for j in tempLit:
                    litTab.append([j,count,4,'R'])
                    count += 4
                tempLit = []
                litCount = 0                
        relLocn.append([count,codeModified[i+1]])
        i = i + 1
    if litCount != 0:
        while count%8 != 0:
            count += 1
        for j in tempLit:
            litTab.append([j,count,4,'R'])
            count += 4
        litCount = 0
    return relLocn