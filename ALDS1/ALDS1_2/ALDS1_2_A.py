# Bubble Sort
# バブルソート

N = int(input())

len_N = list(map(int, input().split()))


def bubbleSort(N, len_N):
    flag = 1
    count = 0
    while flag:
        flag = 0
        for j in reversed(range(1, N)):
            if len_N[j] < len_N[j-1]:
                tmp = len_N[j]
                len_N[j] = len_N[j-1]
                len_N[j-1] = tmp

                flag = 1
                count += 1

    return len_N, count


ans_N, count = bubbleSort(N, len_N)

for i in range(N):
    print(str(len_N[i]), end='')
    if i == N-1:
        print('\n' + str(count))
        break
    else:
        print(' ', end='')
