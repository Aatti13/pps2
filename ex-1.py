x = eval(input())
l_list = []
count = 0
for i in x:
    if type(i) == list:
        l_list.append(i)
        x.pop(x.index(i))
for p in l_list:
    for q in p:
        count += 1
if count == 0:
    print("cannot be unpacked...")
else:
    print(f"Total length: {count+len(x)}")
