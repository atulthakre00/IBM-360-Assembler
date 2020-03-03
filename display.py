
def disp(relLocn,symTab,litTab,bTab,machTab):
    print("Assembly Instructions\n")
    print("Relative Location     " + "Assembly Instruction\n")
    for x in relLocn:
        if len(x[1][2]) < 20:
            print("%17d     %15s %10s   %s"%(x[0],x[1][0],x[1][1],x[1][2]))
        else:
            print("%17d     %15s %10s   %s"%(x[0],x[1][0],x[1][1],(x[1][2][:20]) + "...."))            
    print("\n--------------------------------------------------------".center(80))
    
    print("\n\nSymbol Table\n")
    print("Symbol %14s Value %6s Length %4s Relocation\n"%(" " , " " , " "))
    for x in symTab:
        print("%15s %4s %6d %6s %4d %10s %s"%(x[0]," ",x[1]," ",x[2]," ",x[3]))
    print("\n--------------------------------------------------------".center(80))
    
    print("\n\nLiteral Table\n")
    print("Literal %14s Value %6s Length %4s Relocation\n"%(" " , " " , " "))
    for x in litTab:
        print("%15s %4s %6d %6s %4d %11s %s"%(x[0]," ",x[1]," ",x[2]," ",x[3]))
    print("\n--------------------------------------------------------".center(80))
    
    print("\n\nBase Table\n")
    print("Base Register %5s Content %6s\n"%(" " , " " ))
    for x in bTab:
        print("%5d %12s %5d"%(x[0]," ",x[1]))
    print("\n--------------------------------------------------------".center(80))
    
    print("\n\nMachine Instructions\n")
    print("Relative Location     " + "Machine Instruction\n")
    for x in machTab:
        if len(x[1][1]) < 20:
            print("%17d     %15s    %s"%(x[0],x[1][0],x[1][1]))
        else:
            print("%17d     %15s    %s"%(x[0],x[1][0],(x[1][1][:20]) + "...."))            
    print("\n--------------------------------------------------------".center(80))



