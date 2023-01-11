from string import ascii_lowercase

x = input()
y = x.lower()
r1 = y.split(" ")
ll = {}
banned = 0
value_ll = []
for i in r1:
    if i == i[::-1]:
        ll[i] = len(i)
        banned = 1
    elif i != i[::-1]:
        for j in i:
            if j in ascii_lowercase:
                banned = 2
            else:
                banned = 3
if banned == 1:
    for key, value in ll.items():
        value_ll.append(value)
    print(max(value_ll))
elif banned == 2:
    print(1)
else:
    print("Invalid Input")
