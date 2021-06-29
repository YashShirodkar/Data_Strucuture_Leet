class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used=""
        max_len=0
        for c in (s):
            if c in used:
                max_len=max(len(used),max_len)
                used=used[used.index(c)+1:]
            used=used+c
        return max(max_len,len(used))