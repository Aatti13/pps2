x = input()
valid = 1
for i in x:
    if len(x) == 10 and x[-1].isalpha() and x[:5:].isalpha() and x[6:9].isdigit() and x.isalnum() \
            and x.isupper():
        valid = 1
    else:
        valid = 0
if valid == 1:
    print("valid")
else:
    print("invalid")
