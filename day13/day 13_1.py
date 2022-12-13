import ast
def compare_lists(list1, list2):
  result = None
  for c,d in zip(list1,list2):
    if isinstance(c, int) and isinstance(d, int):
      if c == d:
        continue
      elif c < d:
        result = True
        break
      else:
        result = False
        break
    elif isinstance(c, list) and isinstance(d, list):
      result = compare_lists(c, d)
      if result is not None:
        break
    elif isinstance(c, int):
      result = compare_lists([c], d)
      if result is not None:
        break        
    elif isinstance(d, int):
      result = compare_lists(c, [d])
      if result is not None:
        break
    
  if result is not None:
    return result
  elif len(list1) == len(list2):
    return None
  else:
    return len(list1) < len(list2)

o = 0
with open('day13.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  lst_of_items = []
  lst = []
  for line in lines:
    if line != "\n":
      lst.append(line.rstrip())
    else:
      lst_of_items.append(list(lst))
      lst.clear()
  lst_of_items.append(lst)
  
  for i, (a, b) in enumerate(lst_of_items):
      a = ast.literal_eval(a)        
      b = ast.literal_eval(b)
      score = compare_lists(a,b) 
      o+=i+1 if score else 0
      
print(o)
