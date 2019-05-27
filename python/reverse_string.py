def reverse_string(s):
    s_arr = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        temp = s_arr[i]
        s_arr[i] = s_arr[j]
        s_arr[j] = temp
        i += 1
        j -= 1

    return ''.join(s_arr)

print(reverse_string('Jefferson Vivanco'))