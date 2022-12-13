edges = []
graph = {}
e_ind = ""
start = ""  
l_lines = []
labels = {}
with open('day12.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  for line in lines:
    if line != "\n":
      l_lines.append(line.rstrip())
  for i in range(len(l_lines)):
    for j in range(len(l_lines[i])):
      if l_lines[i][j] == "S":
        start = f'{i}-{j}'
        l_lines[i] = l_lines[i].replace("S", "a")
      if l_lines[i][j] == "E":
        e_ind = f'{i}-{j}'
        l_lines[i] = l_lines[i].replace("E", "z")
  
  for i, a in enumerate(l_lines):  
    for j, b in enumerate(a):
      current = l_lines[i][j]
      labels[f'{i}-{j}'] = current
      next = l_lines[i][j+1] if j+1 < len(l_lines[i]) else None
      prev = l_lines[i][j-1] if j-1 >= 0 else None
      up = l_lines[i-1][j] if i-1 >= 0 else None
      down = l_lines[i+1][j] if i+1 <= len(l_lines) - 1 else None
      if next != None and ord(next) - ord(current) <=1:
        edges.append(tuple((f'{i}-{j}', f'{i}-{j+1}'))) 
      if prev != None and ord(prev) - ord(current) <=1:
        edges.append(tuple((f'{i}-{j}', f'{i}-{j-1}')))
      if up != None and ord(up) - ord(current) <=1:
        edges.append(tuple((f'{i}-{j}', f'{i-1}-{j}')))
      if down != None and ord(down) - ord(current) <=1:
        edges.append(tuple((f'{i}-{j}', f'{i+1}-{j}')))

  for edge in edges:
    if edge[1] not in graph:
      graph[edge[1]] = [edge[0]]
    else:
      graph[edge[1]].append(edge[0])

shortest_paths = {e_ind: (None, 0)}
def dijsktra(graph, initial):
  current_node = initial
  visited = set()
  while True:
    visited.add(current_node)
    destinations = graph[current_node] if current_node in graph else []
    weight_to_current_node = shortest_paths[current_node][1]
    for next_node in destinations:
        weight = 1 + weight_to_current_node
        if next_node not in shortest_paths:
            shortest_paths[next_node] = (current_node, weight)
        else:
            current_shortest_weight = shortest_paths[next_node][1]
            if current_shortest_weight > weight:
                shortest_paths[next_node] = (current_node, weight)
    next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
    if not next_destinations:
        break
    current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

  paths = []
  for i in [x[0] for x in labels.items() if x[1] == "b"]:
    current_node = i
    path = []
    while current_node is not None:
      path.append(current_node)
      next_node = shortest_paths[current_node][0]
      current_node = next_node
    paths.append(path)
  return paths
paths = dijsktra(graph, e_ind)
print(min(map(len,paths)))
