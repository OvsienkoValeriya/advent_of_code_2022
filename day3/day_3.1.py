priorities_sum = 0
with open('day3.txt','r', encoding='utf-8') as rf:
  lines = rf.readlines()
  for line in lines:
    ind = (len(line)-1)//2 
    first_compartment = line[0:ind]
    second_compartment = line[ind:len(line)]
    common_char = list(set(first_compartment) & set(second_compartment))[0]
    if common_char.islower():
      ordinal = ord(common_char) - ord('a')
      priority = ordinal + 1
      priorities_sum += priority
    else: 
      ordinal = ord(common_char) - ord('A')
      priority = ordinal + 27
      priorities_sum += priority

print(priorities_sum)