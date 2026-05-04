def string_length(s):
    count = 0
    for _ in s:
        count = count + 1
    return count

def absolute(x):
    if x < 0:
        return -x
    return x

def solve(n, a, k):
    if k == 0:
        same = 1
        i = 1
        while i < n:
            if a[i] != a[0]:
                same = 0
            i = i + 1
        if same == 1:
            return 0
        return -1

    remainder = a[0] % k
    i = 1
    while i < n:
        if a[i] % k != remainder:
            return -1
        i = i + 1

    steps = []
    i = 0
    while i < n:
        steps = steps + [a[i] // k]
        i = i + 1

    i = 1
    while i < n:
        key = steps[i]
        j = i - 1
        while j >= 0 and steps[j] > key:
            steps[j + 1] = steps[j]
            j = j - 1
        steps[j + 1] = key
        i = i + 1

    median = steps[n // 2]

    total = 0
    i = 0
    while i < n:
        total = total + absolute(steps[i] - median)
        i = i + 1

    return total


# Driver
n = int(input("Enter N: "))

raw = input("Enter array: ")
a = []
num = 0
has_num = 0
i = 0
length = string_length(raw)
while i <= length:
    if i < length and raw[i] != ' ':
        num = num * 10 + int(raw[i])
        has_num = 1
    else:
        if has_num == 1:
            a = a + [num]
            num = 0
            has_num = 0
    i = i + 1

k = int(input("Enter K: "))

answer = solve(n, a, k)

if answer == -1:
    print("Output: -1")
else:
    digits = []
    tmp = answer
    if tmp == 0:
        digits = ['0']
    else:
        while tmp > 0:
            digits = [tmp % 10] + digits
            tmp = tmp // 10

    out = ''
    for d in digits:
        out = out + '0123456789'[d]

    print("Output:", out)