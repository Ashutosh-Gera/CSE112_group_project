'''
Ashutosh Gera - 2021026
Utsav Garg - 2021108
Aman Sharma - 2021010
Group - A40
'''

#Creating a simple assembler capable of executing the instructions of given ISA and converts them into binary code!!

var_temp_list = [0]
register_dict = {'R0' : '000', 'R1' : '001', 'R2' : '010', 'R3' : '011', 'R4' : '100', 'R5' : '101', 'R6' : '110', 'FLAGS' : '111'}
variable_dict = {}
global label_dict #list containing all the labels
label_dict = {}

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

typeB_list = ["rs","ls"]

typeC_list = ["cmp","not","div"]

typeABC_list = typeA_list + typeB_list + typeC_list

typeD_list = ["ld","st"]

typeE_list = ["jmp","jlt","jgt","je"]

typeF_list = ["hlt"]

type_total = typeA_list + typeB_list + typeC_list + typeD_list + typeE_list + typeF_list + ["mov", "var"]


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
    if (r1.upper() in register_dict) and (r2.upper() in register_dict) and (r3.upper() in register_dict):
        pass
    else:
        print("The register used is not of the declared type")
        exit()
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
    print (op + c1  + format_zero_adder(bin_imm_val,8))


def typeC(instruction,r1,r2):
    #2 register type
    if (r1.upper() in register_dict) and (r2.upper() in register_dict):
        pass
    else:
        print("The register used is not of the declared type")
 
    op = op_dict[instruction]
    c1 = register_dict[r1.upper()]
    c2 = register_dict[r2.upper()]

    print (op  + '0' * 5 + c1  + c2)


def typeD(instruction, r1, variable_name):
    #register and memory address type

    op = op_dict[instruction]
    c1 = register_dict[r1.upper()]
    mem_addr = variable_dict[variable_name]
    
    print (op + c1  + mem_addr)
 
    
def typeE(instruction, mem_addr):
    #memory address type
    label_instruction_num = label_dict[mem_addr]
    print (op_dict[instruction] + '0'*3  + format_zero_adder(dec2bin(label_instruction_num),8))
    # for i in inp:
    #     if (i<label_instruction_num):
    #         pass
    #     else:
    #         identify_input(inp[i])

def typeF(instruction):
    #halt
    print (op_dict[instruction] + '0'*11)


def instruction_initialize(input):
    
    if (input[0] in typeA_list):
        typeA(input[0],input[1],input[2],input[3])

    elif (input[0] in typeB_list):
        typeB(input[0],input[1],input[2])

    elif (input[0] in typeC_list):
        typeC(input[0],input[1],input[2])

    elif (input[0] in typeD_list):
        typeD(input[0],input[1],input[2])

    elif (input[0] in typeE_list):
        typeE(input[0],input[1])

    elif (input[0] in typeF_list):
        typeF(input[0])

    elif (input[0] == "mov"):
        if (input[2][0]=="$"):
            typeB("mov1",input[1],input[2])
        else:
            typeC("mov2",input[1],input[2])

    else:
        #for error handling
        pass

def var_define(input, var_counter):
    variable_dict[input[1]] = format_zero_adder(dec2bin(var_counter),8)
    return

def identify_input(input):
    if (input == []):
        return
    elif (input[0] == "var"):
        global var_counter
        var_counter = var_temp_list[0] #For 0 based indexing
        var_define(input, var_counter+input_count-var_count_final)
        var_temp_list[0] += 1
        return
    elif (input[0][-1] == ":"): #Prints instruction ahead of label
        label_rest_input = input[1:]
        instruction_initialize(label_rest_input)
        return
    else:
        instruction_initialize(input)
        return

def line_check(line_input_count):
    if (line_input_count > 256):
        print("Total instruction lines exceeded count of 255")
        exit()

def var_error(inp,var_count):
        var_initial_count = 0
        i = 0
        while (inp[i][0] == 'var'):
            var_initial_count+=1
            i+=1
        if (var_initial_count != var_count):
            while (inp[i][0] != 'var'):
                i+=1
            print(f"var defined at {i} instruction, not at beginning of the file")
            exit()

def halt_error(inp):
    hlt_count = 0
    for i in inp:
        # -1 replaced by 0 to ensure counts label: hlt as well.
        if (inp[i][-1] == 'hlt'):
            hlt_count += 1
    if (hlt_count == 0):
        print("hlt instruction missing")
        exit()
    if (hlt_count==1 and inp[len(inp)-1][-1] != 'hlt'):
        print("hlt not being used as the last instruction")
        exit()
    if (hlt_count>1):
        print("More than one hlt")
        exit()

def lbl_error(label_list):
    #function to check if there are any errors in labels
    a = set(label_list)
    
    if len(a) != len(label_list):
        print ("Error: Defining label with same name multiple times!")
        exit()
    
def register_valid_check(instructions, var_list, label_list):
    
    for i in instructions.values():
        if i[0] in ['add', 'sub', 'mul', 'xor', 'or', 'and']:
            
            if len(i) != 4:
                print ("Error: Invalid instruction length")
                exit()
            
            if (i[1] not in register_dict.keys()) or (i[2] not in register_dict.keys()) or (i[3] not in register_dict.keys()):
                print ("Error: Wrong register input")
                exit()
                
            if (i[1] == 'FLAGS') or (i[2] == 'FLAGS') or (i[3] == 'FLAGS'):
                print ('Error: Invalid use of FLAGS register')
                exit()
                
        elif i[0] == 'mov':
            #type B mov
            if i[2][0] == '$':
                imm = int(i[2][1:])
                if (imm > 255) or (imm < 0):
                    print("Error: Invalid immediate value")
                    exit()
                if len(i) != 3:
                    print ("Error: Invalid instruction length")
                    exit()
                if i[1] not in register_dict.keys():
                    print ("Error: Invalid register")
                    exit()
                if i[1] == 'FLAGS':
                    print ("Error: Invalid use of FLAGS register")
                    exit()
            #type C mov
            else:
                if len(i) != 3:
                    print ("Error: Invalid instruction length")
                    exit()
                
                if i[1] not in register_dict.keys() or i[2] not in register_dict.keys():
                    print("Error: Invalid register")
                    exit()
                
                if i[1] == 'FLAGS':
                    print ("Error: Invalid use of FLAGS register")
                
        elif i[0] == 'ld' or i[0] == 'st':
            #a mem_addr in load and store must be a variable   
            if len(i) != 3:
                print("Error: Invalid instruction length")
                exit()
            
            if i[1] not in register_dict.keys():
                print ("Error: Invalid register used!!")
                exit()
            if i[1] == 'FLAGS':
                print ("Error: Invalid use of FLAGS register")                         
                exit()
            
            if i[2] not in var_list:
                print ("Error: A memory address in load and store must be a variable")
                exit()    
    
        elif i[0] in ['div', 'not','cmp']:
            if len(i) != 3:
                print ("Error: Invalid Instruction length")
                exit()
            
            if i[1] not in register_dict.keys() or i[2] not in register_dict.keys():
                print ("Error: Invalid register used")
                exit()
                
            if i[1] == 'FLAGS' or i[2] == 'FLAGS':
                print ("Invalid use of FLAGS register")
                exit()
            
        elif i[0] == 'rs' or i[0] == 'ls':
            if len(i) != 3:
                print ("Error: Invalid Instruction length")        
                exit()
            
            if i[1] not in register_dict.keys():
                print("Error: Invalid register used")
                exit()
            
            if i[1] == 'FLAGS':
                print("Error: Invalid use of FLAGS register")
                exit()
            
            if i[2][0] != '$':
                print ("Error: Invalid Syntax (no '$' used before immediate value!)")
                exit()
            
            if i[2][0] == '$':
                for j in i[2][1:]:
                    if j not in ['0','1']:
                        print("Error: Invalid syntax of imm val")
                        exit()
                        
                imm = int(i[2][1:])
                if (imm > 255) or (imm < 0):
                    print ("Error: Immediate value entered is greater than 8 bits!")
                    exit()
        
        elif i[0] in ['jmp', 'jlt', 'jgt', 'je']:
            
            if len(i) != 2:
                print ("Error: Invalid Instruction length")
                exit()
            
            if (i[1]+":") not in label_list:
                print ("Error: A mem address in jump instructions must be a label")
                exit()
         
        elif i[0] == 'hlt':
            
            if len(i) != 1:
                print ("Error: Invalid instruction length (giving commans to hlt)")        
                exit()
        
        else:
            print ("General Syntax error")
            exit()            
     
    return None                
                            
def main():
    
    global input_count
    global inp
    inp = {} #dictionary which stores input
    instructions = {} #dict to store input instructions
    vars = {} #dict to store input vars
    labels = {} #dict to store input labels
    input_count = 0 #to keep track of input 
    #print_count = 0 #keep track of print count
    lbl_count = 0 #keep track of number of labels
    inst_count = 0 #keeps track of number of non-var instructions
    var_list = [] #list containing all the input vars
    var_count = 0
    label_list=[] #list containing all the labels

    while True:
        try:
            l = input().split()
            inp[input_count] = l
            input_count += 1
            #if l[-1] == 'hlt':
                #break

        except EOFError:
            break    
   
    line_check(input_count)
    
    for i in inp:
        if inp[i][0] == 'var':
            vars[var_count] = inp[i]
            var_list.append(inp[i][1])
            var_count += 1

        elif inp[i][0] in type_total:
            instructions[inst_count] = inp[i]
            inst_count += 1
        
        elif inp[i][0][-1] == ':' and inp[i][0][-2] != ' ':
            labels[lbl_count] = inp[i]
            label_dict[inp[i][0][:-1]] = i - var_count
            lbl_count += 1
            label_list.append(inp[i][0])


        elif inp[i] == []:
            pass

        else:
            raise SyntaxError ("General Syntax Error")

    global var_count_final
    var_count_final = var_count

    register_valid_check(instructions, var_list, label_list)
    var_error(inp, var_count)
    halt_error(inp)
    lbl_error(label_list)

    for i in inp:
        identify_input(inp[i])
     

if __name__ =="__main__":
    main()