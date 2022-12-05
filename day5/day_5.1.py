line_stacks = []
instructions = []
stacks = [[],[],[],[],[],[],[],[],[]]

with open('day5.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  for line in lines:
    if line.startswith("move"):
      instructions.append(line)
    else:
      line_stacks.append(line)
  for stack in line_stacks:
    stacks[0].append(stack[0:3])    
    stacks[1].append(stack[4:7])
    stacks[2].append(stack[8:11])
    stacks[3].append(stack[12:15])
    stacks[4].append(stack[16:19])
    stacks[5].append(stack[20:23])
    stacks[6].append(stack[24:27])
    stacks[7].append(stack[28:31])
    stacks[8].append(stack[32:35])
  for i in range(len(stacks)):
    del(stacks[i][len(stacks[i])-2:len(stacks[i])-1])
    stacks[i] = list(filter(lambda a: a != "   ", stacks[i]))
  for instruction in instructions:
    instruction = list(instruction.split())
    how_much = int(instruction[1])
    stack_from = int(instruction[3])-1
    stack_to = int(instruction[5]) - 1
    for i in range(int(how_much)):
      element = stacks[stack_from].pop(0)
      stacks[stack_to].insert(0, element)
    
output = "".join([str(stack[0]) for stack in stacks])
output = output.replace("[", "")
output = output.replace("]", "")
print(output)