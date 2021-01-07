reg =   [[0,0,"$zero"],
        [1,0,"$at"],
        [2,0,"$v0"],
        [3,0,"$v1"],
        [4,0,"$a0"],
        [5,0,"$a1"],
        [6,0,"$a2"],
        [7,0,"$a3"],
        [8,0,"$t0"],
        [9,0,"$t1"],
        [10,0,"$t2"],
        [11,0,"$t3"],
        [12,0,"$t4"],
        [13,0,"$t5"],
        [14,0,"$t6"],
        [15,0,"$t7"],
        [16,0,"$s0"],
        [17,0,"$s1"],
        [18,0,"$s2"],
        [19,0,"$s3"],
        [20,0,"$s4"],
        [21,0,"$s5"],
        [22,0,"$s6",],
        [23,0,"$s7"],
        [24,0,"$t8"],
        [25,0,"$t9"],
        [26,0,"$k0"],
        [27,0,"$k1"],
        [28,0,"$gp"],
        [29,0,"$sp"],
        [30,0,"$fp"],
        [31,0,"$ra"] ]
LO = 0
HI = 0

pc = -4

instruction_count = 0

data_array = []
for x in range(0, 3001):
	data_array.append(0)

def PC_plus4():
  global pc
  pc += 4

def twoscomp(s):
  for j in reversed(range(len(s))):
    if s[j] == '1':
      break

  t = ''
  for i in range(0, j, 1):
    t += str(1 - int(s[i]))
  for i in range(j, len(s), 1):
    t += s[i]

  return (t)


def bin_to_dec(b):
    if (b[0] == "0"):
        return int(b, base=2)
    else:
        for j in reversed(range(len(b))):
            if b[j] == '1':
                break
        pos_num = ''
        for i in range(0, j, 1):
            pos_num += str(1 - int(b[i]))
        for i in range(j, len(b), 1):
            pos_num += b[i]

        neg_num = '-' + pos_num
        #decimal = int(pos_num, base = 10)
        #decimal =
        #y = dec(int(t))
        #print(str(dec))
        return int(neg_num, base=2)


def hex_to_bin(line):
    h = line.replace("\n", "")
    i = int(h, base=16)
    b = bin(i)
    b = b[2:].zfill(32)
    print(f'Instruction {h} in binary is {b}')
    return (b)

#def bin_to_hex(j_addr):
    #j = int(j_addr, base=2)
    #a = hex(j)
    #a = 
global bne
global beq
bne = 0
beq = 0


def func_addi(rs, rt, imm):
  reg[rt][1] = int(reg[rs][1]) + int(imm)
  updatedReg = reg[rt][1]
  return updatedReg

def func_andi(rs, rt, imm):

  rs_val = bin(reg[rs][1])
  rs_val = rs_val[2:].zfill(16)
  imm_val = bin(imm)
  imm_val = imm_val[2:].zfill(16)

  new = ''

  for i in range(16):
    if imm_val[i] == '1':
      if rs_val[i] == '1':
        # newlist[i] = '1'
        new = new + '1'
        # print(f'{i}')
    else:
      new = new + '0'

  # new = new.zfill(16)

  # print(f'rs = {rs_val} | imm = {imm_val}')
  # print(f'new value = {new}')

  newVal = bin_to_dec(new)
  reg[rt][1] = newVal

  return newVal

def func_ori(rs, rt, imm):
  rs_val = bin(reg[rs][1])
  rs_val = rs_val[2:].zfill(16)
  imm_val = bin(imm)
  imm_val = imm_val[2:].zfill(16)

  new = ''

  for i in range(16):
    if imm_val[i] == '0' and rs_val[i] == '0':
        new = new + '0'
        # print(f'{i}')
    else:
      new = new + '1'

  # print(f'rs = {rs_val} | imm = {imm_val}')
  # print(f'new value = {new}')
  
  newVal = bin_to_dec(new)
  reg[rt][1] = newVal

  return newVal

def func_lui(rt, imm):
  if (imm < 0):
    imm = imm*-1
    imm_val = bin(imm)
    imm_val = imm_val[2:].zfill(16)

    imm_val = twoscomp(imm_val)
  
  else:
    imm_val = bin(imm)
    imm_val = imm_val[2:].zfill(16)


  new = str(imm_val)

  for i in range(16):
      new = new + '0'

  print(f'imm = {imm_val} | shift left = 16')
  print(f'new value = {new}')

  newVal = bin_to_dec(new)
  reg[rt][1] = newVal

  return newVal

def func_beq(rs, rt, imm):
  global pc
  global beq
  if (int(reg[rs][1]) == int(reg[rt][1])):
    beq = 1
    pc = pc + imm*4
    # print(f'implementing beq...')
  else:
    beq = 0
    pc = pc + 4
    # print(f'no beq found')
  
  return beq

def func_bne(rs, rt, imm):
  global pc
  if (int(reg[rs][1]) != int(reg[rt][1])):
    bne = 1
    pc = pc + imm*4
  else:
    bne = 0
    pc = pc + 4
  return bne

def func_add(rs, rt, rd):
  reg[rd][1] = int(reg[rs][1] + int(reg[rt][1]))
  updatedReg = reg[rd][1]
  return updatedReg

def func_sub(rs, rt, rd):
  reg[rd][1] = int(reg[rs][1] - int(reg[rt][1]))
  updatedReg = reg[rd][1]
  return updatedReg

def func_slt(rs, rt, rd):
  if(reg[rs][1] < reg[rt][1]):
          reg[rd][1] = 1
  else:
          reg[rd][1] = 0
  updatedReg = reg[rd][1]
  return updatedReg

def func_mul(rs, rt, rd):
  reg[rd][1] = int(reg[rs][1]) * int(reg[rt][1])
  updatedReg = reg[rd][1]

  global LO
  LO += updatedReg
  return updatedReg

def func_xor(rs, rt, rd):
  rs_val = bin(reg[rs][1])
  rs_val = rs_val[2:].zfill(16)
  rt_val = bin(reg[rt][1])
  rt_val = rt_val[2:].zfill(16)

  new = ''

  for i in range(16):
    if(rs_val[i] == rt_val[i]):
      new = new + '0'
    else:
      new = new + '1'


  newVal = bin_to_dec(new)
  reg[rd][1] = newVal

  return newVal


def func_sll(rt, rd, sh):
  rt_val = bin(reg[rt][1])
  rt_val = rt_val[2:].zfill(16)

  new = str(rt_val)

  for i in range(sh):
      new = new + '0'

  print(f'rt = {rt_val} | shift left = {sh}')
  print(f'new value = {new}')

  newVal = bin_to_dec(new)
  reg[rd][1] = newVal

  return newVal


def func_srl(rt, rd, sh):
  rt_val = bin(reg[rt][1])
  rt_val = rt_val[2:].zfill(16)
  
  new = ''
  sh_val = 16 - sh

  rt_val = rt_val[:sh_val].zfill(16)
  new = new + str(rt_val)
  
  # print(f'rt = {rt_val} | shift right = {sh}')
  # print(f'new value = {new}')

  newVal = bin_to_dec(new)
  reg[rd][1] = newVal

  return newVal



def process(b):
    b_op = b[0:6]
    b_rs = b[6:11]
    b_rt = b[11:16]
    b_imm = b[16:]
    b_rd = b[16:21]
    b_sh = b[21:26]
    b_func = b[26:]
    b_addr = b[6:]

    #print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')

    asm = ""

    if (b_op == '001000'):  # ADDI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        updateReg1 = func_addi(rs_1, rt_1, imm)
        reg1 = reg[rt_1][2]

        PC_plus4()
        asm = "addi " + rt + ", " + rs + ", " + imm
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')

        #print(reg_array)

    elif (b_op == '000000') and (b_func == '100000'):  # ADD
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        rd_1 = int(b_rd, base=2)

        updateReg1 = func_add(rs_1, rt_1, rd_1)
        reg1 = reg[rd_1][2]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        PC_plus4()
        asm = "add " + rd + ", " + rs + ", " + rt
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')

        # reg_array[rd_1] = reg_array[rs_1] + reg_array[rt_1]
        #print(reg_array)

    elif (b_op == '000000') and (b_func == '100010'):  # SUB
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        rd_1 = int(b_rd, base=2)

        updateReg1 = func_sub(rs_1, rt_1, rd_1)
        reg1 = reg[rd_1][2]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        PC_plus4()
        asm = "sub " + rd + ", " + rs + ", " + rt
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')

        # reg_array[rd_1] = reg_array[rs_1] - reg_array[rt_1]

    elif (b_op == '001100'):  # ANDI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        imm_1 = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        updateReg1 = func_andi(rs_1, rt_1, imm_1)
        reg1 = reg[rt_1][2]

        PC_plus4()
        asm = "andi " + rt + ", " + rs + ", " + imm
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')

        #reg_array[rt_1] = 

    elif (b_op == '000000') and (b_func == '101010'):  # SLT
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        rd_1 = int(b_rd, base=2)

        updateReg1 = func_slt(rs_1, rt_1, rd_1)
        reg1 = reg[rd_1][2]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        PC_plus4()
        asm = "slt " + rd + ", " + rs + ", " + rt
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')


    elif (b_op == '100011'):  # LW
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)
        
        # current_word = '{:04X}'.format(rs+imm+8192) 
        # loaded_word = data_array[imm+rs]

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "lw " + rt + ", " + imm + '(' + rs + ')'
        PC_plus4()
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'pc = {pc}')
        # print(f'Current word 0x{current_word} loaded {loaded_word}')

    elif (b_op == '101011'):  # SW
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        # current_word = '{:04X}'.format(rs+imm+8192)
        # data_array[imm+rs] = rt

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "sw " + rt + ", " + imm + '(' + rs + ')'
        PC_plus4()
        
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'pc = {pc}')
        # print(f'Stored word {rt} at 0x{current_word}')

    elif (b_op == '000000') and (b_func == '000000'): #SLL
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)
        sh = int(b_sh, base=2)

        rt = "$" + str(rt)
        rd = "$" + str(rd)
        sh = str(sh)

        rt_1 = int(b_rt, base=2)
        rd_1 = int(b_rd, base=2)
        sh_1 = int(b_sh, base=2)

        reg1Update = func_sll(rt_1, rd_1, sh_1)
        reg1 = reg[rd_1][2]

        PC_plus4()
        asm = "sll " + rd + ", " + rt + ", " + sh
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {reg1Update}')
        print(f'pc = {pc}')

    elif(b_op == '000000') and (b_func == '100110'): #XOR
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)

        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        rd_1 = int(b_rd, base=2)

        reg1Update = func_xor(rs_1, rt_1, rd_1)
        reg1 = reg[rd_1][2]

        PC_plus4()
        asm = "xor " + rd + ", " + rs + ", " + rt
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {reg1Update}')
        print(f'pc = {pc}')
    
    elif(b_op == '000100'): #BEQ
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)
        imm_1 = bin_to_dec(b_imm)
        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        global beq
        beq = func_beq(rs_1, rt_1, imm_1)
        
        asm = "beq " + rt + ", " + rs + ", " + imm
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: none')
        print(f'pc = {pc}')

    elif(b_op == '000101'): #BNE
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)
        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        imm_1 = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        global bne
        bne = func_bne(rs_1, rt_1, imm_1)

        asm = "bne " + rt + ", " + rs + ", " + imm
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: none')
        print(f'pc = {pc}')
    
    elif (b_op == '000010'): #J
        addr = bin_to_dec(b_addr)

        addr = str(addr)

        asm = "j " + addr
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: none')
        print(f'pc = {pc}')
    
    elif (b_op == '001111'): #LUI

        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)


        rt = "$" + str(rt)
        imm = str(imm)

        rt_1 = int(b_rt, base=2)
        imm_1 = bin_to_dec(b_imm)

        reg1Update = func_lui(rt_1, imm_1)
        reg1 = reg[rt_1][2]


        PC_plus4()
        asm = "lui " + rt + ", " + imm
        print(f'-> {b_op} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {reg1Update}')
        print(f'pc = {pc}')
    
    elif (b_op == '001101'): #ORI
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        imm = bin_to_dec(b_imm)

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        imm_1 = bin_to_dec(b_imm)

        updateReg1 = func_ori(rs_1, rt_1, imm_1)
        reg1 = reg[rt_1][2]

        PC_plus4()
        asm = "ori " + rt + ", " + rs + ", " + imm
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')

    elif (b_op == '011100') and (b_func == '000010'): #MUL
        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)
        rs_1 = int(b_rs, base=2)
        rt_1 = int(b_rt, base=2)
        rd_1 = int(b_rd, base=2)

        updateReg1 = func_mul(rs_1, rt_1, rd_1)
        reg1 = reg[rd_1][2]


        rs = "$" + str(rs)
        rt = "$" + str(rt)
        rd = "$" + str(rd)
        PC_plus4()
        asm = "mul " + rd + ", " + rs + ", " + rt
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {updateReg1}')
        print(f'pc = {pc}')


    elif (b_op == '000000') and (b_func == '000010'): #SRL
        rt = int(b_rt, base=2)
        rd = int(b_rd, base=2)
        sh = int(b_sh, base=2)

        rt = "$" + str(rt)
        rd = "$" + str(rd)
        sh = str(sh)

        rt_1 = int(b_rt, base=2)
        rd_1 = int(b_rd, base=2)
        sh_1 = int(b_sh, base=2)

        reg1Update = func_srl(rt_1, rd_1, sh_1)
        reg1 = reg[rd_1][2]

        PC_plus4()
        asm = "srl " + rd + ", " + rt + ", " + sh
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_rd} | {b_sh} | {b_func}')
        print(f'in asm: {asm}')
        print(f'Updated registers: {reg1} = {reg1Update}')

    elif (b_op == '101111'):  # WIDTH
        #width rt, imm(rs)

        rs = int(b_rs, base=2)
        rt = int(b_rt, base=2)
        
        imm = bin_to_dec(b_imm)
        
        width_binary = "{0:b}".format(imm+rs)
        width = (len(width_binary) - width_binary[::-1].index("1") - 1) - width_binary.index("1") + 1

        rs = "$" + str(rs)
        rt = "$" + str(rt)
        imm = str(imm)

        asm = "width " + rt + ", " + imm + '(' + rs + ')'
        PC_plus4()
        
        print(f'-> {b_op} | {b_rs} | {b_rt} | {b_imm}')
        print(f'in asm: {asm}')
        print(f'pc = {pc}')
        print(f'Width is {width}')

    return (asm)

def print_reg():
  print(f'\n\nRegisters:\n')
  for i in range(32):
    print(f'{reg[i]}')
  print(f'\npc = {pc}')
  print(f'HI = {HI}')
  print(f'LO = {LO}')
  

# here begins main

input_file = open("defaultasm.txt", "r")
output_file = open("default.txt", "w")
line_count = 0


for line in input_file:
    line_count += 1
    print(f'\n Line {line_count}:', end='')
    bin_str = hex_to_bin(line)
    asmline = process(bin_str)
    if 'beq' in asmline:
      if(beq == 1):
        break
    if 'bne' in asmline:
      if(bne == 1):
        break

      
    output_file.write(asmline + '\n')
input_file.close()

input_file = open("defaultasm.txt", "r")
########## BEQ ##############
if(beq == 1):
  pcLine = pc - 2
  line_count = pcLine

  print(f'go to line: {pcLine}')

  for line in input_file.readlines()[pcLine:]:
    line_count += 1
    print(f'\n Line {line_count}:', end='')
    bin_str = hex_to_bin(line)
    asmline = process(bin_str)
    
    output_file.write(asmline + '\n')

########### BNE ############
if(bne == 1):
  pcLine = pc - 2
  line_count = pcLine

  print(f'line: {pcLine}')

  for line in input_file.readlines()[pcLine:]:
    line_count += 1
    print(f'\n Line {line_count}:', end='')
    bin_str = hex_to_bin(line)
    asmline = process(bin_str)
    
    output_file.write(asmline + '\n')


print_reg()

print(f'\n\nDATA MEMORY:')
print(f'\n{data_array}')

output_file.write(f'\n\nRegisters:\n')
for i in range(32):
  output_file.write(f'{reg[i]}\n')
output_file.write(f'\npc = {pc}\n')
output_file.write(f'HI = {HI}\n')
output_file.write(f'LO = {LO}\n')

instruction_count = f'\n\nTotal Instruction Count = {line_count}'
output_file.write(instruction_count)

output_file.close()