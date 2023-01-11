x = input()
q = '"'
vowel_list = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
for i in x:
    if i not in vowel_list:
        q += i
print(q+'"')
