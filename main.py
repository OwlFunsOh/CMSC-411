"""
This program will be doing the CMSC 411 project of
creating a single cycle processor using MIPS architecture
"""
import functions

INSTRUCTION_FILENAME = "Instructions1.txt"
MEMORY_FILENAME = "Memory1.txt"
INITIAL_MEMORY = "IMemory.txt"
"""
iMemoryList = []
instructionList = []
instructionCounter = 0
currentInstruction = ""
REGISTERS = functions.populateRegisters()

"""

if __name__ == "__main__":
    functions.fetchInstruction(INSTRUCTION_FILENAME)
    functions.getMemory(INITIAL_MEMORY)
    functions.REGISTERS[0] = "00000000000000000000000000001100"
    functions.REGISTERS[1] = "00000000000000000000000000001100"
    functions.subu("00000000000000010000100000000000")
    print(functions.REGISTERS)

    
    
    