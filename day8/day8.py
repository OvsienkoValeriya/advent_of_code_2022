with open('day8.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  rows = []
  for line in lines:
    rows.append(list(map(int,line.rstrip())))
visible = 0
for i in range(len(rows)):
  for j in range(len(rows[i])):
    tree = rows[i][j]
    trees_to_the_left = rows[i][j-1::-1] if j != 0 else []
    trees_to_the_right = rows[i][j+1:]
    trees_down = [rows[i+q][j] for q in range(1, len(rows)-i)]
    trees_up = [rows[i-q][j] for q in range(1, i+1)]
    if i == 0 or j == 0 or i == len(rows)-1 or j == len(rows[i])-1:
      visible+=1
    elif all(t < tree for t in trees_to_the_left) or all(t<tree for t in trees_to_the_right) or all(t < tree for t in trees_down) or all(t < tree for t in trees_up):
      visible+=1
    else:
      continue
print(visible)
                                                              
#part_2
scenic_scores = []
for i in range(len(rows)):
  for j in range(len(rows[i])):
    tree = rows[i][j]
    trees_to_the_left = rows[i][j-1::-1] if j != 0 else []
    trees_to_the_right = rows[i][j+1:]
    trees_down = [rows[i+q][j] for q in range(1, len(rows)-i)]
    trees_up = [rows[i-q][j] for q in range(1, i+1)]
    if i == 0 or j == 0 or i == len(rows)-1 or j == len(rows[i])-1:
      scenic_scores.append(0)
    else:
      total_score = 1
      left_score = 0
      right_score = 0
      up_score = 0
      down_score = 0
      for t in trees_to_the_left:
        if t < tree:
          left_score+=1
        else:
          left_score+=1
          break
      for t in trees_to_the_right:
        if t < tree:
          right_score+=1
        else:
          right_score+=1
          break
      for t in trees_up:
        if t < tree:
          up_score+=1
        else:
          up_score+=1
          break
      for t in trees_down:
        if t < tree:
          down_score+=1
        else:
          down_score+=1
          break

      total_score = left_score*right_score*up_score*down_score
      scenic_scores.append(total_score)
    
print(sorted(scenic_scores)[-1])