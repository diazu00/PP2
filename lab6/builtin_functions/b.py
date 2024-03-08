def count_letters(s):
    cnt_u, cnt_l = 0, 0
    for i in s:
        if i.isupper():
            cnt_u += 1
        elif i.islower():
            cnt_l += 1
    return(cnt_u, cnt_l)
s = "This IS a SeCond TaSk"
cnt_u, cnt_l = count_letters(s)
print("Uppercase letters: ", cnt_u)
print("Lowercase_letters: ", cnt_l)