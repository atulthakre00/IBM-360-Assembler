

#format [symbol value length relocation]
      
  

def compConvert(fileLocn):
    fp = open(fileLocn,'r')
    # format Label@CMD@ARG1,ARG2,ARG3...................
    code = []
    fp.seek(0)
    for x in fp:
        code.append(x.strip())
    pseudoType = ['START','USING','EQU','END']
    rrType = ['BALR','BR','SR','AR','LR']
    rxType = ['L','A','ST','CLI','BNE','DS','DC','LA','C']
    codeModified = [x.split('@') for x in code]
    litTab = []
    relLocn = relLocationCalc(codeModified , pseudoType , rrType , rxType , litTab)
    symTab = symbolTable(relLocn , pseudoType , rrType , rxType)
    bTab = baseTable(relLocn,symTab)
    machTab = machInstn(relLocn , symTab , bTab , litTab , pseudoType , rrType , rxType)
    disp(relLocn,symTab,litTab,bTab,machTab)


compConvert("assemblyCode.txt")

compConvert("assemblyCode2.txt")

