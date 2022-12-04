contain = 0
with open('day4.txt','r', encoding='utf-8') as rf:
  lines = rf.readlines()
  for line in lines:
    line = line.rstrip().split(",")
    first_pair = [int(s) for s in line[0].replace("-", ",").split(',')]
    second_pair = [int(s) for s in line[1].replace("-", ",").split(',')]
    if first_pair[1] < second_pair[0] or first_pair[0] > second_pair[1]:
     continue
    else:
      contain+=1
  
print(contain)