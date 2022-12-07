dir_and_files_dict = {}
with open('day7.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  dir_path = [","]
  current_dir = ""
  for line in lines:
    if line.startswith("$ cd"):
      dir_name = line.rstrip().split(" ")[-1]
      dir_name = dir_name.rstrip()
      if dir_name == "..":
        dir_path = dir_path[:-1]
      else:
        dir_path.append(dir_name)
      current_dir = dir_path[-2]  + dir_path[len(dir_path)-1]
    elif line.startswith("dir"):
      dir_name = line.rstrip().split(" ")[-1]
      dir_name = dir_name.rstrip()
      if current_dir not in dir_and_files_dict:
        dir_and_files_dict[current_dir] = []
      dir_and_files_dict[current_dir].append( dir_path[len(dir_path)-1] + dir_name)
    elif line == "$ ls\n":
      continue
    else:
      if current_dir not in dir_and_files_dict:
        dir_and_files_dict[current_dir] = []
      dir_and_files_dict[current_dir].append(int(line.split(" ")[0]))

while not all(isinstance(item, int) for item in dir_and_files_dict.values()):
  for k,v in dir_and_files_dict.items():
    if not isinstance(v, int) and all(isinstance(item, int) or isinstance(dir_and_files_dict[item], int) for item in v):
      dir_and_files_dict[k] = sum(item for item in v if isinstance(item, int)) + sum(dir_and_files_dict[item] for item in v if not isinstance(item, int))

retval = 0
for i in dir_and_files_dict.values():
  if i <= 100000:
    retval+=i
print(retval)

total_disk_space = 70000000
occupied = sorted(dir_and_files_dict.values())[-1]
free = total_disk_space - occupied
for_update = 30000000
need = for_update - free


for i in sorted(dir_and_files_dict.values()):
  if i >= need:
    print(i)
    break
   