total_score = 0
rock_score = 1
paper_score = 2
scissors_score = 3
win_score = 6
draw_score = 3

with open('day2.txt','r', encoding='utf-8') as rf:
  lines = rf.readlines()
  for line in lines:
    sp = line.split()
    if(sp[0] == "A"): #rock
      if(sp[1] == "X"): #rock
        total_score+=draw_score
        total_score+=rock_score
      elif(sp[1] == "Y"): #paper
        total_score += win_score 
        total_score += paper_score
      else: #scissors
        total_score+=scissors_score     
    elif(sp[0] == "B"): #paper
      if(sp[1] == "X"): #rock
        total_score+=rock_score
      elif(sp[1] == "Y"): #paper
        total_score+=draw_score
        total_score+=paper_score
      else: #scissors
        total_score+=win_score
        total_score+=scissors_score
    else: #scissors
      if(sp[1] == "X"): #rock
        total_score+=win_score
        total_score+=rock_score
      elif(sp[1] == "Y"): #paper
        total_score+=paper_score
      else: #scissors
        total_score+=draw_score
        total_score+=scissors_score

print(total_score)