s = tuple(map(str, input().split(",")))
master_spl = ["$", "@", "#"]
valid_password = []
for password in s:
    if 6 <= len(password) <= 12:
        ll, u, p, d, space = 0, 0, 0, 0, 0
        for i in password:
            if i.isupper():
                u += 1
            if i.islower():
                ll += 1
            if i.isdigit():
                d += 1
            if i in master_spl:
                p += 1
            if i == " ":
                space += 1
        if ll >= 1 and u >= 1 and p >= 1 and d >= 1 and space == 0:
            valid_password.append(password)

if len(valid_password) == 0:
    print("invalid")
else:
    for i in valid_password:
        print(i)
