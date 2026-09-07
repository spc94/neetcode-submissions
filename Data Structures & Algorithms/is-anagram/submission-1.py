class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        j = len(t)-1
        i = 0
        if len(s) == len(t):
            s_list = list(s)
            s_list.sort()
            s_sorted = "".join(s_list)
            t_list = list(t)
            t_list.sort()
            t_sorted = "".join(t_list)
            #t_list = list(t).sort()
            #t_sorted = "".join(list(t).sort())
            if s_sorted == t_sorted:
                return True
        return False
        