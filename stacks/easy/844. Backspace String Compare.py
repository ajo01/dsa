class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_backspaced = []
        t_backspaced = []

        for i in range(0, len(s)):
            if s[i] != '#':
                s_backspaced.append(s[i])
            elif s_backspaced:
                s_backspaced.pop()
        for i in range(0, len(t)):
            if t[i] != '#':
                t_backspaced.append(t[i])
            elif t_backspaced:
                t_backspaced.pop()
        return s_backspaced == t_backspaced
