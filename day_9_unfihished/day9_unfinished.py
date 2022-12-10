head_step_coord = [[0,0]]
x = 0
y = 0
tail_step_coord = [[0,0]]
with open('day9.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  for line in lines:
    line = line.rstrip().split(" ")
    for i in range(int(line[1])):
      if line[0] == 'R':
        x += 1
        head = [x,y]
        head_step_coord.append(head)
        prev_tail = tail_step_coord[-1]
        if ((head[0] == prev_tail[0]+1 or head[0] == prev_tail[0]-1) and head[1] == prev_tail[1]) or (head[0] == prev_tail[0] and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)) or (head[0] == prev_tail[0]+1 and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)) or (head[0] == prev_tail[0]-1 and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)):
          continue
        else:
          tail = [x-1, y]
          tail_step_coord.append(tail)        
      elif line[0] == 'L':
        x -= 1
        head = [x, y]
        head_step_coord.append(head)
        prev_tail = tail_step_coord[-1]
        if ((head[0] == prev_tail[0]+1 or head[0] == prev_tail[0]-1) and head[1] == prev_tail[1]) or (head[0] == prev_tail[0] and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)) or (head[0] == prev_tail[0]+1 and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)) or (head[0] == prev_tail[0]-1 and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)):
          continue
        else:
          tail = [x-1, y]
          tail_step_coord.append(tail)
      elif line[0] == 'U':
        y += 1
        head = [x,y]
        head_step_coord.append(head)
        prev_tail = tail_step_coord[-1]
        if ((head[0] == prev_tail[0]+1 or head[0] == prev_tail[0]-1) and head[1] == prev_tail[1]) or (head[0] == prev_tail[0] and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)) or (head[0] == prev_tail[0]+1 and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)) or (head[0] == prev_tail[0]-1 and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)):
          continue
        else:
          tail = [x, y-1]
          tail_step_coord.append(tail)        
      else:
        y -= 1
        head = [x,y]
        head_step_coord.append(head)
        prev_tail = tail_step_coord[-1]
        if ((head[0] == prev_tail[0]+1 or head[0] == prev_tail[0]-1) and head[1] == prev_tail[1]) or (head[0] == prev_tail[0] and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)) or (head[0] == prev_tail[0]+1 and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)) or (head[0] == prev_tail[0]-1 and (head[1] == prev_tail[1]+1 or head[1] == prev_tail[1]-1)):
          continue
        else:
          tail = [x, y-1]
          tail_step_coord.append(tail)
        


tail_step_coord = list(map(list,set(map(tuple,tail_step_coord))))
for step in tail_step_coord:
  if step[0] == 0 and step[1] == 0:
    tail_step_coord.remove(step)
  if step[0] < 0 or step[1] < 0:
    tail_step_coord.remove(step)

print(len(tail_step_coord))

 
#if (nh[0] == t[0]+1 or nh[0] == t[0]-1) and nh[1] == t[1]:#по горизонтали
#if nh[0] == t[0] and (nh[1] == t[1]+1 or nh[1] == t[1]-1): #по вертикали  
#if nh[0] == t[0]+1 and (nh[1] == t[1]+1 or nh[1] == t[1]-1): #по правой диагонали  
#if nh[0] == t[0]-1 and (nh[1] == t[1]+1 or nh[1] == t[1]-1): #по левой диалнали
  
  