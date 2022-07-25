'''
Utsav Garg - 2021108
Ashutosh Gera - 2021026
Aman Sharma - 2021010
Group - A40
'''

#Clarification 3: In case of overflow, set overflow flag and take the register value as regval= regval mod 2^16.
#In case of underflow, set the overflow flag and regval = 0

#Building a simulator for the given ISA
#Code is executed until hlt instruction is reached

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

reg_rev = {'000' : 'R0', '001' : 'R1', '010' : 'R2', '011': 'R3', '100': 'R4', '101':'R5', '110':'R6', '111':'FLAGS'}

reg_values={
    'R0' : 0,
    'R1' : 0,
    'R2' : 0,
    'R3' : 0,
    'R4' : 0,
    'R5' : 0,
    'R6' : 0,
    'FLAGS' : 0
}
#INITIALIZE ALL REGISTER VALUES TO ZERO

def dec2bin(str_number):
    st = ''
    while int(str_number) > 0:
        remainder = str_number % 2
        st += str(remainder)
        str_number = int(str_number)//2
    return st[::-1] 

def bin2dec(str_bin):
    str_bin = str_bin[::-1]
    dec = 0
    for i in range(len(str_bin)):
        dec += int(str_bin[i]) * (2**i)
    return dec

def main():
    instruction_count = 0
    instruction = {} #dict to store input binary file
    global prog_counter
    prog_counter = 0
    
    while True:
        try:
            l = input().strip()
            if l != '':
                instruction[instruction_count] = l
                instruction_count += 1
        
        except EOFError:
            break        
    
            
