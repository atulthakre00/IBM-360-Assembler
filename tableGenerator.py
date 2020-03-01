def symbolTable(relLocn , pseudoType , rrType , rxType):
    symTab = []
    for x in relLocn:
        if(x[1][0] != ''):
            length = 0
            relocation = 'R'
            value = x[0]
            if x[1][1] in pseudoType:
                length = 1
            elif x[1][1] in rrType:
                length = 2
            elif x[1][1] in rxType:
                length = 4
            if x[1][1] == 'EQU':
                relocation = 'A'
                if x[1][2] != '*':
                    value = x[1][2]
            symTab.append([x[1][0] , int(value) , length , relocation])
    return(symTab)

# format baseReg , Content
def baseTable(relLocn,symTab):
    bTab = []
    for x in relLocn:
        if x[1][1] == 'USING':
            temp = x[1][2].split(',')
            if temp[0] == '*':
                temp[0] = x[0]
            elif not(temp[0].isnumeric()):
                temp[0] = valFromSymbol(temp[0],symTab)
            if not(temp[1].isnumeric()):
                temp[1] = valFromSymbol(temp[1],symTab)
            bTab.append([ int(temp[1]) , int(temp[0]) ])
    return bTab