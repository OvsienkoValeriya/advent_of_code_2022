cursor_lst = [1]
signal_strength = [1]
with open('day10.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  ind = 1
  for line in lines:
    line = line.rstrip().split(" ")    
    if line[0] == "noop":
      cursor_lst.append(cursor_lst[-1])
      signal_strength.append(cursor_lst[-1]*ind)
      ind+=1
    else:
      value = int(line[1])
      signal_strength.append(cursor_lst[-1]*ind)
      cursor_lst.append(cursor_lst[-1])
      ind+=1
      final_value = cursor_lst[-1]+value
      signal_strength.append(cursor_lst[-1] * ind)
      cursor_lst.append(final_value)
      ind+=1


print(signal_strength[20] + signal_strength[60] + signal_strength[100] + signal_strength[140] + signal_strength[180] + signal_strength[220])
