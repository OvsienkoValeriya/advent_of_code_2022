priorities_sum = 0
with open('day3.txt','r', encoding='utf-8') as rf:
  lines = rf.readlines()
  groups =  [lines[i:i + 3] for i in range(0, len(lines), 3)]
  for group in groups:
    common_char = list(set(group[0].rstrip()) & set(group[1].rstrip()) & set(group[2].rstrip()))[0]
    if common_char.islower():
      ordinal = ord(common_char) - ord('a')
      priority = ordinal+1
      priorities_sum += priority
    else: 
      ordinal = ord(common_char) - ord('A')
      priority = ordinal + 27
      priorities_sum += priority

print(priorities_sum)