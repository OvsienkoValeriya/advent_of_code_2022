lst_of_items = []
lst = []
values_lst = []

with open('day1.txt','r', encoding='utf-8') as rf:
  lines = rf.readlines()
  for line in lines:
    if line != "\n":
      lst.append(int(line))
    else:
      lst_of_items.append(list(lst))
      lst.clear()
      
for list in lst_of_items:
  value = 0
  for l in list:
    value+=l
  values_lst.append(value)

values_lst.sort(reverse=True)

print(values_lst[0])
print(values_lst[0]+values_lst[1]+values_lst[2])