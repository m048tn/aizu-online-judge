# Selection Sort
# 選択ソート

N = int(input())

len_N = list(map(int, input().split()))


def selectionSort(N, len_N):
    count = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if len_N[j] < len_N[minj]:
                minj = j

        tmp = len_N[i]
        len_N[i] = len_N[minj]
        len_N[minj] = tmp
        if i != minj:
            count += 1

    return len_N, count


ans_N, count = selectionSort(N, len_N)

for i in range(N):
    print(str(len_N[i]), end='')
    if i == N-1:
        print('\n' + str(count))
        break
    else:
        print(' ', end='')
