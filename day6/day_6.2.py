with open('day6.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  datastream_buffer = lines[0]

  j = 0
  for i in datastream_buffer:
    if len(set(datastream_buffer[j: j+ 14])) == 14:
      print(j+14)
      break
    else:
      j+=1
      continue
      