len_N = input().split()

S = []

for target_list in range(len(len_N)):
    x = len_N[target_list]
    if len_N[target_list] == '+':
        a = S.pop()
        b = S.pop()
        S.append(a+b)
    elif len_N[target_list] == '-':
        a = S.pop()
        b = S.pop()
        S.append(b-a)
    elif len_N[target_list] == '*':
        a = S.pop()
        b = S.pop()
        S.append(b*a)
    elif len_N[target_list] == '/':
        a = S.pop()
        b = S.pop()
        S.append(b/a)
    else:
        # push
        x = int(x)
        S.append(x)
print(str(S[0]))
