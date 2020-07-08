
len_N = list(map(int, input().split()))

# プロセス数
n = len_N[0]

# クオンタム
q = len_N[1]

# 経過時間
elaps = 0

Q = []
head = 0
count = 0


def dequeue(head):
    x = Q[head]
    if head+1 == n-1:
        head = 0
    else:
        head += 1

    return x, head


def enqueue(len_Q):

    Q.append(len_Q)


def time(Q_time):
    time = q - Q_time

    return time


# プロセスの値を代入
for x in range(n):
    len_N = input().split()
    x = int(len_N[1])
    Q.append([len_N[0], x])

# プロセスが残ってる限り続く
while len(Q) != 0:
    # 要素を取り出す
    len_Q, head = dequeue(head)

    # もしプロセス＞クオンタムなら
    # 残りプロセス＝プロセス ー クオンタム
    if len_Q[1] > q:
        len_Q[1] -= q
        enqueue(len_Q)
    else:
        print(str(len_Q[0]) + ' ' + str(len_Q[1] + elaps))
        count += 1
        if(count == n):
            break

    elaps += x
