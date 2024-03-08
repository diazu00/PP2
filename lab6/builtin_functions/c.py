def palindrom(s):
    s = s.casefold() #casefold()мы делаем строку пригодным для бесрегистровых сравнений

    s_rev = reversed(s)

    if list(s) == list(s_rev):
        return "String is palindrom"
    else:
        return "Sring is not palindrom"

s = input()
print(palindrom(s))