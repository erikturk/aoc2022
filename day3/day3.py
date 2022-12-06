import string

priority = {}
sum_priority =0
for letter in (string.ascii_lowercase + string.ascii_uppercase):
	priority[letter]=(string.ascii_lowercase+string.ascii_uppercase).index(letter)+1

f = open('day3.txt','r')
common = ''
group = ["","",""]
for line in f:
  
	
  if any([x == "" for x in group]):
    group.pop(0)
    group.append(line.strip())
  
  if all([x != "" for x in group]):
    print(group)    
    common = list(set(set(list(group[0])) & set(list(group[1])) & set(list(group[2]))))[0]
    print(common)
    print(priority[common])
  	
    
    group = ["","",""]
	
    sum_priority = sum_priority + priority.get(common,0)
	
print(sum_priority)
	
