from functools import cmp_to_key

def compare_lists(list1, list2):
  result = 0
  for c,d in zip(list1,list2):
    if isinstance(c, int) and isinstance(d, int):
      if c == d:
        continue
      elif c < d:
        result = -1
        break
      else:
        result = 1
        break
    elif isinstance(c, list) and isinstance(d, list):
      result = compare_lists(c, d)
      if result != 0:
        break
    elif isinstance(c, int):
      result = compare_lists([c], d)
      if result !=0:
        break        
    elif isinstance(d, int):
      result = compare_lists(c, [d])
      if result !=0:
        break
    
  if result != 0:
    return result
  else:
    return len(list1) - len(list2)

with open('day13.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  lst_of_items = []
  lst = []
  for line in lines:
    if line != "\n":
      lst_of_items.append(eval(line.rstrip()))
  lst_of_items.append(eval(line.rstrip()))
  lst_of_items.append([[2]])
  lst_of_items.append([[6]]) 

  lst_of_items = sorted(lst_of_items, key=cmp_to_key(compare_lists))

  retval = 1
  for i, elem in enumerate(lst_of_items):
    if elem == [[2]]:
      retval *= i
    elif elem == [[6]]:
      retval *= i
    else:
      continue
      
  print(retval)
