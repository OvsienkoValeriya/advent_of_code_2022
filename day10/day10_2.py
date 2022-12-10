cursor_lst = [1]

with open('day10.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  ind = 1
  for line in lines:
    line = line.rstrip().split(" ")    
    if line[0] == "noop":
      cursor_lst.append(cursor_lst[-1])
      ind+=1
    else:
      value = int(line[1])
      cursor_lst.append(cursor_lst[-1])
      ind+=1
      final_value = cursor_lst[-1]+value
      cursor_lst.append(final_value)
      ind+=1

sprite_positions = ""
cursor_lst.pop(-1)
chunks = [cursor_lst[x:x+40] for x in range(0, len(cursor_lst), 40)]
sp_ind = 0
for chunk in chunks:
  for ch in range(len(chunk)):
    signal = chunk[ch]
    if(ch == signal or ch == signal+1 or ch == signal-1):
      sprite_positions+="#"
    else:
      sprite_positions+="."

retval = [sprite_positions[i:i+(len(sprite_positions)//6)] for i in range(0, len(sprite_positions), len(sprite_positions)//6)]
for r in retval:
  print(r)
  
