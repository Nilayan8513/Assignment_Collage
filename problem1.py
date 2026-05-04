def char_value(c):
    table = {
        'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
        'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,
        't':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
    }
    return table[c]

def string_length(s):
    count = 0
    for _ in s:
        count = count + 1
    return count

def solve(s):
    n = string_length(s)

    doubled = []
    i = 0
    while i < n:
        doubled[i:i] = [s[i]]
        i = i + 1
    j = 0
    while j < n:
        doubled[n + j:n + j] = [s[j]]
        j = j + 1
    total_len = n + n

    freq = [0] * 26

    def char_index(c):
        return char_value(c) - 1

    left     = 0
    curr_sum = 0
    best     = 0
    best_l   = 0
    best_r   = -1

    right = 0
    while right < total_len:
        if right - left >= n:
            lc = doubled[left]
            freq[char_index(lc)] = freq[char_index(lc)] - 1
            curr_sum = curr_sum - char_value(lc)
            left = left + 1

        rc = doubled[right]
        ri = char_index(rc)
        freq[ri] = freq[ri] + 1
        curr_sum = curr_sum + char_value(rc)

        while freq[ri] > 1:
            lc = doubled[left]
            freq[char_index(lc)] = freq[char_index(lc)] - 1
            curr_sum = curr_sum - char_value(lc)
            left = left + 1

        if curr_sum > best:
            best   = curr_sum
            best_l = left
            best_r = right

        right = right + 1

    result_chars = []
    k = best_l
    while k <= best_r:
        result_chars = result_chars + [doubled[k]]
        k = k + 1

    return best, result_chars


s = input("Enter string: ")
answer, window = solve(s)

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