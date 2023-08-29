# categories: strings, stacks, two pointers

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2= list(t)

        s_stack = l1[::-1]
        t_stack = l2[::-1]

        
        s_index = len(s_stack) - 1
        t_index = len(t_stack) - 1
        while t_index > -1 and s_index > -1:
            if s_stack[s_index] == t_stack[t_index]:
                s_stack.pop()
                s_index-=1
            t_stack.pop()
            t_index-=1
        return len(s_stack) == 0