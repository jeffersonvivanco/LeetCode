import math

# uses dynamic programming, time complexity O(n^2), space complexity O(n^2)
def longest_palindrome(s):
    len_of_s = len(s)
    if len_of_s == 1:
        return s

    if s == s[::-1]:
        return s

    # grid
    cell = []
    l_p_s = ''
    index_to_pop = 0
    len_of_s_half = len_of_s / 2

    # temp store so its no computing values
    temp_store = {}

    for a in range(0, len_of_s):
        cell.append(list('' for b in s))

    for i in range(0, len_of_s):
        if i > 1:
            cell[index_to_pop] = None
            index_to_pop += 1
        should_break = False
        j_index = len_of_s - 1
        for j in range(0, len_of_s):
            if s[i] == s[j_index]:
                temp = cell[i-1][j-1]
                if i == 0 or j == 0:
                    temp = ''
                cell[i][j] = temp + s[i]
                found = cell[i][j]
                if found in temp_store:
                    j_index -= 1
                    continue
                temp_store[found] = found
                if len(l_p_s) < len(found) and found == found[::-1]:
                    l_p_s = found
                    if len(l_p_s) > len_of_s_half and len(l_p_s) > j:
                        should_break = True
            j_index -= 1
        if should_break:
            break

    return l_p_s

# uses technique expand around center, time complexity O(n^2), space complexity O(1)
def longest_palindrome2(s):
    len_of_s = len(s)
    if len_of_s == 1:
        return s

    if s == s[::-1]:
        return s

    start = 0
    end = 0
    for i in range(len_of_s):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > (end - start):
            start = int(i - math.floor((max_len - 1) / 2))
            end = int(i + (max_len / 2))
    return s[start:end + 1]

def expand_around_center(s, left, right):
    l = left
    r = right
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1
    
# uses Manacher's algorithm, time complexity O(n), space complexity O(n)
# summary of the algorithm
# if P[i'] <= R - i
# then P[i] <- P[i']
# else P[i] >= P[i'] (Which we have to expand past the right edge (R) to find P[i])
#
# if the palindrome centered at i does expand past R, we update C to i, (the center of
# this new palindrome), and extend R to the new palindrome's right edge 
def manacher_algorithm(s):
    len_of_s = len(s)
    if len_of_s == 1:
        return s

    if s == s[::-1]:
        return s

    # trasforming string s to another string by inserting '#' between the letters
    # adding chars @ and $ at the beginning and end to cover palindromes that might
    # extend towards the first or last letter in the string
    s = '@' + s.replace('', '#') + '$'
    p = list(0 for c in s)
    right = 0
    mirror = 0
    i = 0
    center = 0
    curr_max = 0
    curr_max_index = 0

    for i in range(len(s) - 1):
        mirror = 2 * center - i
        if right > i:
            p[i] = min(right - i, p[mirror])
        
        # Attempt to expand palindrome centered at i
        while s[i + (p[i] + 1)] == s[i - (1 + p[i])]:
            p[i] += 1
            
        # if palindrome centered at i expands past right,
        # adjust center based on expanded palindrome
        if i + p[i] > right:
            center = i
            right = i + p[i]
            if p[i] > curr_max:
                curr_max = p[i]
                curr_max_index = i

    return s[curr_max_index - curr_max:curr_max_index + curr_max].replace('#', '')


import unittest

class LongestPalindromeTest(unittest.TestCase):
    def test_longest_palindrome_1(self):
        l = longest_palindrome('babad')
        success = False
        if l == 'bab' or l == 'aba':
            success = True
        self.assertTrue(success)
    
    def test_longest_palindrome_2(self):
        l = longest_palindrome('cbbd')
        self.assertEqual(l, 'bb')

    def test_longest_palindrome_3(self):
        l = longest_palindrome('bb')
        self.assertEqual(l, 'bb')
    
    def test_longest_palindrome_4(self):
        l = longest_palindrome('abb')
        self.assertEqual(l, 'bb')

    def test_longest_palindrome_5(self):
        l = longest_palindrome('aacdefcaa')
        self.assertEqual(l, 'aa')

    def test_longest_palindrome_6(self):
        l = longest_palindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.assertEqual(l, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    def test_longest_palindrome_7(self):
        l = longest_palindrome('321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123')
        self.assertEqual(l, '321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123')

    def test_longest_palindrome_8(self):
        l = longest_palindrome('jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel')
        self.assertEqual(l, 'sknks')
    
    # -------------------------- Tests for longest_palindrome2() ---------------------- #
    def test_longest_palindrome_9(self):
        l = longest_palindrome2('babad')
        success = False
        if l == 'bab' or l == 'aba':
            success = True
        self.assertTrue(success)

    def test_longest_palindrome_10(self):
        l = longest_palindrome2('cbbd')
        self.assertEqual(l, 'bb')

    def test_longest_palindrome_10(self):
        l = longest_palindrome2('321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123')
        self.assertEqual(l, '321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123')

    def test_longest_palindrome_11(self):
        l = longest_palindrome2('jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel')
        self.assertEqual(l, 'sknks')

    # --------------------------- Tests for manacher's algorithm --------------------- #
    def test_longest_palindrome_11(self):
        l = manacher_algorithm('cbbd')
        self.assertEqual(l, 'bb')

    def test_longest_palindrome_12(self):
        l = manacher_algorithm('babad')
        success = False
        if l == 'bab' or l == 'aba':
            success = True
        print('l is: ' + l)
        self.assertTrue(success)

    def test_longest_palindrome_4(self):
        l = manacher_algorithm('abb')
        self.assertEqual(l, 'bb')

    def test_longest_palindrome_5(self):
        l = manacher_algorithm('aacdefcaa')
        self.assertEqual(l, 'aa')

    def test_longest_palindrome_13(self):
        l = manacher_algorithm('321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123')
        self.assertEqual(l, '321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123')

    def test_longest_palindrome_14(self):
        l = manacher_algorithm('jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel')
        self.assertEqual(l, 'sknks')

unittest.main()