"""
This program will be doing the CMSC 411 project of
creating a single cycle processor using MIPS architecture
"""

INSTRUCTION_FILENAME = "Instructions1.txt"
MEMORY_FILENAME = "Memory1.txt"
INITIAL_MEMORY = "IMemory.txt"

iMemoryList = []
instructionList = []
instructionCounter = 0
currentInstruction = ""

#get memory will populate the IMemory.txt into iMemoryList
def getMemory(filename):
    memoryFile = open(filename, "r")
    for line in memoryFile:
        iMemoryList.append(line.strip())
    memoryFile.close()

#fetch instruction will get all the instructions
#and put them in a list.
def fetchInstruction(filename):
    instructionFile = open(filename, "r")
    
    #instruction byte will be a list containing
    #each byte of instructions. 1 byte of instruction
    #is one line of the text file
    instructionByte = []
    for line in instructionFile:
        instructionByte.append(line.strip())
    instructionFile.close()

    
    combineBytes(instructionByte)

#This function will combine 4 bytes together to make
#a full 32 bit instruction
def combineBytes(list):
    fullInstruction = ""
    counter = 0
    for byte in list:
        if (counter % 4 == 0) and (counter != 0):
            instructionList.append(fullInstruction)
            fullInstruction = byte
        else:
            fullInstruction = fullInstruction + byte
        counter += 1

#increments the program counter by 1
def programCounter(counter):
    counter += 1

#This function will take the list of instructions and separate the bits
#into it's designated bit sizes. The control will determine what type of
#instruction the current instruction is
def instructionMemory(instructionList):
    instruction = instructionList[instructionCounter]
    currentInstruction = instruction
    
#control unit will take the first 6 bits of the instruction as an input
#and determine what instruction should be ran
def controlUnit(opcode):
    if(opcode == "000000"):
        return aluControl()
    elif(opcode == "001001"):
        return "addiu"
    elif(opcode == "000100"):
        return "beq"
    elif(opcode == "000010"):
        return "j"
    elif(opcode == "100011"):
        return "lw"
    elif(opcode == "101011"):
        return "sw"
    else:
        return "halt"
    
#this function will only be ran if it is an R type instruction
#It will get the func code of the instruction as the input and output
#the operation the ALU has to do
def aluControl(funcCode):
    if(funcCode == "100001"):
        return "addu"
    elif(funcCode == "100011"):
        return "subu"
    elif(funcCode == "100100"):
        return "and"
    elif(funcCode == "100101"):
        return "or"


def addu(instruction):
    pass

if __name__ == "__main__":
    fetchInstruction(INSTRUCTION_FILENAME)
    print(instructionMemory(instructionList))
    