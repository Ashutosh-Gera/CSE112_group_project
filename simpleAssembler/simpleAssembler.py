'''
Ashutosh Gera - 2021026
Utsav Garg - 2021108
Aman Sharma - 2021010
Group - A40
'''

#Creating a simple assembler capable of executing the instructions of given ISA and converts them into binary code!!

register_dict = {'R0' : '000', 'R1' : '001', 'R2' : '010', 'R3' : '011', 'R4' : '100', 'R5' : '101', 'R6' : '110', 'FLAGS' : '111'}

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

typeA_list = ["add","sub","mul","xor","or","and"]
typeB_list = ["ls"]
typeC_list = ["cmp","not","div"]
typeD_list = ["ld","st"]
typeE_list = ["jmp","jlt","jgt","je"]
typeF_list = ["hlt"]
type_total=typeA_list + typeB_list + typeC_list + typeD_list + typeE_list + typeF_list + ["mov" + "var"]
def dec2bin(str_number):
    st = ''
    while int(str_number) > 0:
        remainder = str_number % 2
        st += str(remainder)
        str_number = int(str_number)//2
    return st[::-1]    

def format_zero_adder(str1,size_req):
	return (size_req-len(str1))*"0"+str1

#defining functions for binary encoding
def typeA(instruction,r1,r2,r3):
    #3 register type

    c1 = register_dict[r1.upper()]
    c2 = register_dict[r2.upper()]
    c3 = register_dict[r3.upper()]

    op = op_dict[instruction]
    print (op + '_' + '0'*2 + '_' + c1 + '_' + c2 + '_' + c3)


def typeB(instruction, reg, imm_val):
    #register & immedicate vale type

    op = op_dict[instruction]
    c1 = register_dict[reg.upper()]
    imm_val = (imm_val.replace('$', '')).strip()
    int_imm_val = int(imm_val)

    #if (int_imm_val > 255):
    #raise ValueError ("Immediate value exceeding the 8-bit limit")

    bin_imm_val = dec2bin(int_imm_val)
    print (op + '_' + c1 + '_' + format_zero_adder(bin_imm_val,8))


def typeC(instruction,r1,r2):
    #2 register type

    op = op_dict[instruction]
    c1 = register_dict[r1.upper()]
    c2 = register_dict[r2.upper()]

    print (op + '_' + '0' * 5 + '_' + c1 + '_' + c2)


def typeD(instruction, r1, mem_addr):
    #register and memory address type

    op = op_dict[instruction]
    c1 = register_dict[r1.upper()]
    
    print (op + '_' + c1 + '_' + mem_addr)
    
def typeE(instruction, mem_addr):
    #memory address type

    print (op_dict[instruction] + '_' + '0'*3 + '_' + mem_addr)


def typeF(instruction):
    #halt

    print (op_dict[instruction] + '_' + '0'*11)

def instruction_initialize(str_input):
    if (str_input[0] in typeA_list):
        typeA(str_input[0],str_input[1],str_input[2],str_input[3])

    elif (str_input[0] in typeB_list):
        typeB(str_input[0],str_input[1],str_input[2])

    elif (str_input[0] in typeC_list):
        typeC(str_input[0],str_input[1],str_input[2])

    elif (str_input[0] in typeD_list):
        typeD(str_input[0],str_input[1],str_input[2])

    elif (str_input[0] in typeE_list):
        typeE(str_input[0],str_input[1])

    elif (str_input[0] in typeF_list):
        typeF(str_input[0])

    elif (str_input[0] == "mov"):
        if (str_input[2][0]=="$"):
            typeB("mov1",str_input[1],str_input[2])
        else:
            typeC("mov2",str_input[1],str_input[2])

    else:
        #for error handling
        pass

def identify_input(str_input):
    if (str_input == []):
        return
    elif (str_input[0] == "var"):
        #var_define(str_input)
        return
    elif (str_input[0][-1] == ":"):
        #label_initialize(str_input)
        return
    else:
        instruction_initialize(str_input)
        return
var_list=[]
var_label=[]
def store_variables(str_input):
    # to store values of new variables
    if (str_input[0]=="var") :
        var_list.append(str_input[1])
    if (str_input[0] not in type_total and str_input[0][-1]==":" ):
        var_label.append(str_input[0][:-1])

def error_handling(str_input):
    # error handling
    # a. Typos in instruction name or register name
    if (str_input[0] not in type_total):
        print("Syntax Error")
        quit()
    if (str_input[0] not in type_total and str_input[0][-1]!=":"):
        print("Syntax Error")
        quit()
    if (str_input[0]=="mov" and str_input[1][0]!="$"):
        print("Syntax Error")
        quit()
    # b. Use of undefined variables
    # g. Variables not declared at the beginning

    if ((str_input[0]=="ls" or str_input[0]=="st") and str_input[1] not in var_list):
        print("Use of undefined variable or Variable not declared at the beginning")
        quit()
    # e. Illegal Immediate values (more than 8 bits)
    if (str_input[0]=="mov" and str_input[1][0]=="$"):
        if (int(str(str_input[1][1:]))>255 or int(str(str_input[1][1:]))<0 ):
            print("Illegal Immediate values Error(more than 8 bits)")
            quit()
    # f. Misuse of labels as variables or vice-versa
    if (str_input[0] not in type_total and str_input[0][-1]==":" and str(str_input[0][:-1]) in var_list):
        print("Misuse of variable as label")
        quit()
    if (str_input[0]=="var" and str_input[1] in var_label):
        print("Misuse of labels as variables")
        quit()


    

def main():
    n = int(input("Number Of Operations: "))
    # hlt error check
    hlt_check=0
    

    while(n):
        string_input = input().split()
        # flag for hlt
        if (string_input[0]=="hlt" and hlt_check==0):
            hlt_check=1
        # to check whether multiple hlts are used or not
        elif (string_input[0]=="hlt" and hlt_check!=0):
            print("Use of multiple hlt")
            quit()
        # to check if hlt is not used as last instruction
        elif (string_input[0]!="hlt" and hlt_check!=0):
            print("hlt not being used as the last instruction")
            quit()
        # to check if hlt is missing
        elif (n==1 and string_input[0]!="hlt" ):
            print("Missing hlt instruction")
            quit()

        identify_input(string_input)
        n-=1




if __name__ =="__main__":
    main()
