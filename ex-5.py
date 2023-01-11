n = input()
table = [
    {"A", "J", "S"},
    {"B", "K", "T"},
    {"C", "L", "U"},
    {"D", "M", "V"},
    {"E", "N", "W"},
    {"F", "O", "X"},
    {"G", "P", "Y"},
    {"H", "Q", "Z"},
    {"I", "R"},
]
destiny_no = 0
soul_no = 0
dream_no = 0
vowels = "AEIOU"
for i in n:
    for j in range(len(table)):
        if i in table[j]:
            destiny_no += j + 1
            if i in vowels:
                soul_no += j + 1
            else:
                dream_no += j + 1
            break


def sums(n):
    s = 0
    while n > 0 or s > 9:
        if n == 0:
            n = s
            s = 0
        s += n % 10
        n //= 10
    return s


print(sums(destiny_no))
print(sums(soul_no))
print(sums(dream_no))
#
