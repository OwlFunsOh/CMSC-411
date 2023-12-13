"""
This program will be doing the CMSC 411 project of
creating a single cycle processor using MIPS architecture
"""
import functions

INSTRUCTION_FILENAME = "Instructions1.txt"
MEMORY_FILENAME = "Memory1.txt"
INITIAL_MEMORY = "IMemory.txt"
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
        functions.controlUnit(functions.currentInstruction)
        
        print(functions.instructionCounter)
        #increment counter
        functions.instructionCounter = functions.incrementCounter(functions.instructionCounter)
        functions.currentInstruction = functions.instructionMemory(functions.instructionCounter)

    
    print("Program terminated")


        
        
    

    
    
    