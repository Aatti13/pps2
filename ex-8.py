x = input("Person-1: ")
y = input("Person-2: ")
x1 = x.split("AGCT")
y1 = y.split("AGCT")
matcher_x1 = []
matcher_x2 = []
for i in range(0, len(x1)-1):
    if x1[i] == x1[i+1] == '':
        matcher_x1.append(x1[i])

for j in range(0, len(y1)-1):
    if y1[j] == y1[j+1] == '':
        matcher_x2.append(y1[j])

if len(matcher_x1) == len(matcher_x2):
    print("match")
else:
    print("mismatch")
