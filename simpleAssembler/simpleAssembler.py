'''
Ashutosh Gera - 2021026
Utsav Garg - 2021108
Aman Sharma - 2021010
Group - A40
'''

#Creating a simple assembler capable of executing the instructions of given ISA and converts them into binary code!!

#dictionary of registers with their corressponding address'
register_dict = {'R0' : '000', 'R1' : '001', 'R2' : '010', 'R3' : '011', 'R4' : '100', 'R5' : '101', 'R6' : '110', 'FLAGS' : '111'}

#dictionary of instructions with their corressponding opcodes
op_dict = {
    'add' : '10000',
    'sub' : '10001',
    'mov1' : '10010',
    'mov2' : '10011',
    'ld' : '10100',
    'st' : '10101',
    'mul' : '10110',
    'div' : '10111',
    'rs' : '11000',
    'ls' : '11001',
    'xor' : '11010',
    'or' : '11011',
    'and' : '11100',
    'not' : '11101',
    'cmp' : '11110',
    'jmp' : '11111',
    'jlt' : '01100',
    'jgt' : '01101',
    'je' : '01111',
    'hlt' : '01010'
}

#function to convert decimal numbers to binary
# for handling immediate values
def dec2bin(str_number):

    st = ''
    while int(str_number) > 0:
        remainder = str_number % 2
        st += str(remainder)
        str_number = int(str_number)//2
    return st[::-1]    


#defining functions for binary encoding
def typeA(instruction,r1,r2,r3):
    #3 register type

    c1 = register_dict[r1.upper()]
    c2 = register_dict[r2.upper()]
    c3 = register_dict[r3.upper()]

    op = op_dict[instruction]

    print (op + '0'*2 + c1 + c2 + c3)


def typeB(instruction, reg, imm_val):
    #register & immedicate vale type

    op = op_dict[instruction]
    c1 = register_dict[reg.upper()]
    imm_val = (imm_val.replace('$', '')).strip()
    int_imm_val = int(imm_val)

    #if (int_imm_val > 255):
    #raise ValueError ("Immediate value exceeding the 8-bit limit")

    bin_imm_val = dec2bin(int_imm_val)
    print (op + c1 + bin_imm_val)


def typeC(instruction,r1,r2):
    #2 register type

    op = op_dict[instruction]
    c1 = register_dict[r1.upper()]
    c2 = register_dict[r2.upper()]

    print (op + '0' * 5 + c1 + c2)


def typeD(instruction, r1, mem_addr):
    #register and memory address type

    op = op_dict[instruction]
    c1 = register_dict[r1.upper()]
    
    print (op + c1 + mem_addr)
    
def typeE(instruction, mem_addr):
    #memory address type

    print (op_dict[instruction] + '0'*3 + mem_addr)


def typeF(instruction):
    #halt

    print (op_dict[instruction] + '0'*11)


def binary_to_decimal(str_value):
	"Convert binary to decimal for immediate value instruction"
	len_str = len(str_value)
	decimal_value = 0
	for i in range(len_str):
		decimal_value += 2**(len_str-1-i)*int(str_value[i])
	return decimal_value

def format_zero_adder(str1,size_req):
	"Will Make 110 to 0000000000000110, required format"
	print((size_req-len(str1))*"0"+str1)
	return (size_req-len(str1))*"0"+str1

   
def Right_Shift(reg1,Imm):
    reg1=reg1>>Imm
    return reg1

def Left_Shift(reg1,Imm):
    ls=reg1<<Imm
    return ls

def Exclusive_OR(reg1, reg2, reg3):
    reg1=reg2^reg3
    return reg1

def Or(reg1,reg2,reg3):
    reg1=reg2|reg3
    return reg1

def And(reg1,reg2,reg3):
    reg1=reg2&reg3
    return reg1

def Invert(reg1,reg2):
    reg1=~reg2
    return reg1
Z=0
CY=0
def Compare(reg1,reg2):
	if(reg1<reg2):
		CY=1
		Z=0
	elif(reg1>reg2):
		Z=1
		CY=0
	else:
		Z=CY=0

#hello world
     



def main():
    #initially creating main working function so that we know which all helper function to make systematically and we'll be able to
    # make functions accordingly
    pass


    
     






if __name__ =="__main__":
    main()