"""
This program will be doing the CMSC 411 project of
creating a single cycle processor using MIPS architecture
"""
import functions

#Change the 3 variables below for different files

#Instruction filename is the name of the instruction file you want to use
INSTRUCTION_FILENAME = "Instructions1.txt"

#Initial Memory is the IMemory file you want to use
INITIAL_MEMORY = "IMemory.txt"

#Memory Filename is the memory file that will be outputted
MEMORY_FILENAME = "Memory1.txt"

#Register Filename is the register file that will be outputted
REGISTER_FILENAME = "Registers1.txt"


HALT = "11111111111111111111111111111111"
"""
iMemoryList = []
instructionList = []
instructionCounter = 0
currentInstruction = ""
REGISTERS = functions.populateRegisters()

"""

if __name__ == "__main__":
    #Set up the files
    functions.fetchInstruction(INSTRUCTION_FILENAME)
    functions.getMemory(INITIAL_MEMORY)

    functions.currentInstruction = functions.instructionMemory(functions.instructionCounter)
    
    #main loop
    while(functions.currentInstruction != HALT):
        #print(functions.currentInstruction)
        #perform instruction
        functions.controlUnit(functions.currentInstruction, functions.instructionCounter)

        #increment counter
        functions.instructionCounter = functions.incrementCounter(functions.instructionCounter)
        functions.currentInstruction = functions.instructionMemory(functions.instructionCounter)

    #Writing to file
    functions.writeToFile(functions.iMemoryList, MEMORY_FILENAME)
    functions.writeToFile(functions.REGISTERS, REGISTER_FILENAME)


    print("Program has completed")


        
        
    

    
    
    