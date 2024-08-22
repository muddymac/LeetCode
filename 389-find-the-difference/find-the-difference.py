class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # t is the longer, s is the shorter
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for j in t:
            if j in t_dict:
                t_dict[j] += 1
            else:
                t_dict[j] = 1
        for letter in t_dict.keys():
            if t_dict[letter] != s_dict.get(letter):
                return letter