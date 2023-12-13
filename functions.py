instructionCounter = 0

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
    instructionList.append(fullInstruction)

#This function will take the list of instructions and separate the bits
#into it's designated bit sizes. The control will determine what type of
#instruction the current instruction is
def instructionMemory(instructionCounter):
    instruction = instructionList[instructionCounter]
    return instruction

def binary_to_decimal(binary_string):
  decimal_value = 0
  power = 0

  for digit in reversed(binary_string):
    decimal_value += int(digit) * 2**power
    power += 1

  return decimal_value

def decimal_to_binary(decimal_number):

  binary_string = ""

  while decimal_number > 0:
    remainder = decimal_number % 2
    binary_string = str(remainder) + binary_string
    decimal_number //= 2

  binary_string = binary_string.zfill(32)
  return binary_string

def populateRegisters():
    registers = []
    zero = "00000000000000000000000000000000"
    for i in range(32):
        registers.append(zero)
    return registers


#increments the program counter by 1
def incrementCounter(counter):
    counter += 1
    return counter
    
#control unit will take the first 6 bits of the instruction as an input
#and determine what instruction should be ran
def controlUnit(instruction, counter):
    opcode = instruction[0:6]
    if(opcode == "000000"):
        aluControl(instruction)
    elif(opcode == "001001"):
        addiu(instruction)
    elif(opcode == "000100"):
        beq(instruction)
    elif(opcode == "000010"):
        jump(instruction)
    elif(opcode == "100011"):
        loadWord(instruction)
    elif(opcode == "101011"):
        storeWord(instruction)
    else:
        return "halt"
    
#this function will only be ran if it is an R type instruction
#It will get the func code of the instruction as the input and output
#the operation the ALU has to do
def aluControl(instruction):
    funcCode = instruction[26:]
    if(funcCode == "100001"):
        addu(instruction)
    elif(funcCode == "100011"):
        subu(instruction)
    elif(funcCode == "100100"):
        bitwiseAnd(instruction)
    elif(funcCode == "100101"):
        bitwiseOr(instruction)
    elif(funcCode == "100111"):
        bitwiseNor(instruction)

def binaryAdder(num1, num2):
    #Converting to base 2 format
    intNum1 = int(num1, 2)
    intNum2 = int(num2, 2)
    
    sum = intNum1 + intNum2
    
    #Converting back to binary
    finalString = bin(sum)[2:]
    return finalString

#Below are the R type instructions

def addu(instruction):
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    destinationReg = binary_to_decimal(instruction[16:21])
    
    num1 = binary_to_decimal(REGISTERS[targetReg])
    num2 = binary_to_decimal(REGISTERS[sourceReg])
    sum = num1 + num2
    REGISTERS[destinationReg] = decimal_to_binary(sum)
    
def subu(instruction):
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    destinationReg = binary_to_decimal(instruction[16:21])
    
    num1 = binary_to_decimal(REGISTERS[targetReg])
    num2 = binary_to_decimal(REGISTERS[sourceReg])
    difference = num1 - num2
    REGISTERS[destinationReg] = decimal_to_binary(difference)
    

def bitwiseOr(instruction):
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    destinationReg = binary_to_decimal(instruction[16:21])
    bitwiseOr = ""
    
    length = len(REGISTERS[targetReg])
    
    for i in range(length):
        if(REGISTERS[sourceReg][i] == "1" or REGISTERS[targetReg][i] == "1"):
            bitwiseOr = bitwiseOr = bitwiseOr + "1"
        else:
            bitwiseOr = bitwiseOr = bitwiseOr + "0"
    
    REGISTERS[destinationReg] = bitwiseOr

def bitwiseNor(instruction):
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    destinationReg = binary_to_decimal(instruction[16:21])
    bitwiseNor = ""
    
    length = len(REGISTERS[targetReg])
    
    for i in range(length):
        if(REGISTERS[sourceReg][i] == "1" or REGISTERS[targetReg][i] == "1"):
            bitwiseNor = bitwiseNor + "0"
        else:
            bitwiseNor = bitwiseNor + "1"
    
    REGISTERS[destinationReg] = bitwiseNor


def bitwiseAnd(instruction):
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    destinationReg = binary_to_decimal(instruction[16:21])
    bitwiseAnd = ""
    
    length = len(REGISTERS[targetReg])
    
    for i in range(length):
        if(REGISTERS[sourceReg][i] == "1" and REGISTERS[targetReg][i] == "1"):
            bitwiseAnd = bitwiseAnd + "1"
        else:
            bitwiseAnd = bitwiseAnd + "0"
    
    REGISTERS[destinationReg] = bitwiseAnd

#Below are the I type instructions

def addiu(instruction):
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    immediate = binary_to_decimal(instruction[16:32])

    #num1 = binary_to_decimal(REGISTERS[immediate])
    num2 = binary_to_decimal(REGISTERS[sourceReg])
    sum = immediate + num2

    REGISTERS[targetReg] = decimal_to_binary(sum)

def loadWord(instruction):
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    immediate = binary_to_decimal(instruction[16:32])

    num1 = binary_to_decimal(iMemoryList[immediate])
    num2 = binary_to_decimal(REGISTERS[sourceReg])
    toLoad = num1 + num2
    REGISTERS[targetReg] = decimal_to_binary(toLoad)

def storeWord(instruction):
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    immediate = binary_to_decimal(instruction[16:32])

    num1 = binary_to_decimal(REGISTERS[sourceReg])
    #num2 = binary_to_decimal(iMemoryList[immediate])
    storeAddress = num1 + immediate
    iMemoryList[storeAddress] = REGISTERS[targetReg] 


def beq(instruction):
    global instructionCounter   
    targetReg = binary_to_decimal(instruction[11:16])
    sourceReg = binary_to_decimal(instruction[6:11])
    immediate = binary_to_decimal(instruction[16:32])

    if(REGISTERS[sourceReg] == REGISTERS[targetReg]):
        #counter = counter + immediate
        for i in range(immediate):
            instructionCounter = incrementCounter(instructionCounter)
    
    
        
#Below will be the J type instructions

def jump(instruction):
    global instructionCounter
    address = binary_to_decimal(instruction[6:32])
    instructionCounter = (address - 1)

def writeToFile(list, filename):
    with open(filename, 'w') as memoryFile:
        for i in range(32):
            memoryFile.write(list[i] + "\n")
        memoryFile.close()
    
    
iMemoryList = []
instructionList = []
currentInstruction = ""
REGISTERS = populateRegisters()
instructionCounter = 0
    