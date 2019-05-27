
# longest substring without repeating characters

# algorithm
# pwwkew
# 

def length_of_longest_substring(s):
    letters = {}
    maxz = 0
    count = 0
    start_index = 0

    for l in range(0, len(s)):
        if s[l] not in letters:
            letters[s[l]] = l
            count += 1
        else:
            maxz = max(count, maxz)
            
            # check if repeated letter is part of current longest substring
            if (l - count) > (letters[s[l]] + 1):
                count += 1
                letters[s[l]] = l
                continue

            # get index of repeated letter
            r = letters[s[l]]

            # setting new count
            count -= (r - start_index) + 1
            count += 1
            
            # setting start index of current longest substring
            # we set it to the next letter, next to the repeated letter
            start_index = r + 1

            # del repeated letter
            del letters[s[l]]

            # adding new letter
            letters[s[l]] = l

    maxz = max(maxz, count)
    return maxz

print(length_of_longest_substring("aabaab!bb"))