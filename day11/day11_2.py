monkeys = []
monkey_lines = []
with open('day11.txt', 'r', encoding='utf-8') as rf:
  lines = rf.readlines()
  for line in lines:
    if line != "\n":
      line = line.rstrip()
      line = line.strip()
      monkey_lines.append(line)
    else:
      monkeys.append(list(monkey_lines))
      monkey_lines.clear()
  monkeys.append(list(monkey_lines))
  monkey_lines.clear()

m = []
for monkey in monkeys:  
  m_parsed = []
  for command in monkey:
    if command.startswith("Monkey"):
      monkey_number = command.split(" ")[1]
      monkey_number = monkey_number.replace(':', '')
      m_parsed.append(monkey_number)
    elif command.startswith("Starting items:"):
      monkey_items = command.split(" ")
      only_ints = []
      for item in monkey_items:
        item = item.replace(',', '')
        if item.isdigit():
          item = int(item)
          only_ints.append(item)
      m_parsed.append(only_ints)
    elif command.startswith("Operation:"):
      monkey_operations = command.split(" ")
      m_parsed.append(monkey_operations[-2:len(monkey_operations)])
    elif command.startswith("Test:"):
      monkey_test = command.split(" ")[-1]
      m_parsed.append(monkey_test)
    elif command.startswith("If true:"):
      monkey_if_true = command.split(" ")[-1]
      m_parsed.append(monkey_if_true)
    elif command.startswith("If false:"):
      monkey_if_false = command.split(" ")[-1]
      m_parsed.append(monkey_if_false)
    else:
      continue
  m.append(m_parsed)


monkeys_dict = {}
monkeys_inspections = {}
for i in range(len(m)):
  monkeys_dict[i] = list(m[i][1])
  monkeys_inspections[i] = 0
for i in range(len(m)):
  monkeys_dict[i] = [[it % int(monkey[3]) for monkey in m] for it in monkeys_dict[i]]
  
for j in range(10000):
  for i in m:
    for starting_item in list(monkeys_dict[int(i[0])]):
      stress = 0
      operation = i[2][0]
      
      new_st = []
      for k in range(len(starting_item)):
        stress = 0
        value = i[2][1]
        if value.isdigit():
          value = int(i[2][1])
        else:
          value = starting_item[k]
        if operation == "+":
          new_st.append((starting_item[k] + value) % int(m[k][3]))
        elif operation == "*":
          new_st.append((starting_item[k] * value) % int(m[k][3]))
        else:
          continue
      test = int(i[3])
      monkeys_inspections[int(i[0])] += 1
      if new_st[int(i[0])] == 0:
        monkeys_dict[int(i[4])].append(new_st)
        monkeys_dict[int(i[0])].remove(starting_item)
      else:
        monkeys_dict[int(i[5])].append(new_st)
        monkeys_dict[int(i[0])].remove(starting_item)

monkeys_inspections = sorted(monkeys_inspections.values())
retval = monkeys_inspections[-1] * monkeys_inspections[-2]
print(retval)

