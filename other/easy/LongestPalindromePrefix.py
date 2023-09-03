def solution(s):
    if s == "":
        return ""
    res = get_longest_prefix(s)
    while len(res) >= 2:
        s = s[len(res):]
        res = get_longest_prefix(s)
    return res

def get_longest_prefix(s):
    max_length = 0
    for i in range(1, len(s) + 1):
        temp = s[0:i]
        if is_palindrome(temp) and len(temp) > max_length:
            max_length = len(temp)
    return s[0:max_length]


def is_palindrome(s):
    str = s.lower()
    reverse = str[::-1]
    return str == reverse
