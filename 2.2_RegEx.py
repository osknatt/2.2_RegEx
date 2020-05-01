from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
print(f'Было: \n{contacts_list}')

new_list = []
new_list.append(contacts_list[0])
for c in contacts_list[1:]:
  new_list.append([])
  for i, element in enumerate(c):
    if 0 <= i and i <= 2:
      s = element.split()
      new_list[-1].extend(s)
    else:
      new_list[-1].append(element)

    if i == 2:
      if len(new_list[-1])  == 1:
        new_list[-1].extend(['',''])
      elif len(new_list[-1])  == 2:
        new_list[-1].extend([''])

my_dict = {}
for n in new_list[1:]:
  if n[0] not in my_dict:
    my_dict[n[0]] = n
  else:
    for i, element in enumerate(n):
      if element and my_dict[n[0]][i] == '':
        my_dict[n[0]][i] = element

result = []
result.append(contacts_list[0])
for i in my_dict:
  result.append(my_dict[i])

pattern = re.compile("(8|\+7)(\s*)(\(?)(\d{3})(\)?)(\s*-*)(\d{3})(\s*)(-*)(\d{2})(\s*)(-*)(\d+)(\s*)(\(*)(доб.)?(\s*)(\d*)(\)*)")
for lst in result:
  lst[5] = pattern.sub(r"+7(\4)\7-\10-\13\14\16\18", str(lst[5]))
print(f'Стало: \n{result}')

with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result)