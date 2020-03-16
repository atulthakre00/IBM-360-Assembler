# IBM 360 Assembler
This is a miniature version of IBM 360 Assembler that converts a assembly instructions containing txt file to machine code

########################################################

Modules  |  Functions


display.py  |  Functions: To display base, literal, symbol and machine table

machineInstructions.py  |  Converts assembly instructions into machine mnemonic code 

relocator.py  |  Assign relative location to assebly code and make literal table

tableGenerator.py  |  Generates base table and symbol table 

valueCalculator.py  |  Base Table ,Literal Table, Index ,Address Calculation

IBM 360 assembler | Main file that calls all other functions


########################################################

AssemblyCode.txt and AssemblyCode2.txt are assembly code sample inputs for testing the IBM 360 assembler

Format of Assembler Instructions

Relative Location         Assembly Instruction

########################################################

Format of Symbol Table

Symbol          Value         Length          Relocation

########################################################

Format of Literal Table

Literal         Value         Length          Relocation

########################################################

Format of Base Table

Base Register         Content

########################################################

Format Of Machine Instructions

Relative Location         Machine Instruction

########################################################
