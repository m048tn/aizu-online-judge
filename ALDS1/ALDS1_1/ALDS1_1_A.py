# Insertion Sort
# 挿入ソート
N = int(input())

len_N = list(map(int, input().split()))


def insertionSort(len_N, N):
    i = 1
    for i in range(N):
        v = len_N[i]
        j = i-1

        # 左側の値が大きかったら入れ替える
        while j >= 0 and len_N[j] > v:
            len_N[j+1] = len_N[j]
            j -= 1

        # jがあったところにvを代入する（値の入れ替え）
        len_N[j+1] = v
        for target_list in range(N):

            print(str(len_N[target_list]), end='')
            if target_list == N-1:
                print('')
                break
            else:
                print(' ', end='')

    return len_N


ans = insertionSort(len_N, N)
