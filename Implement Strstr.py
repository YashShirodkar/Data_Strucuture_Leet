class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1
        if not haystack or not needle: return 0
        
        j=0 
        
        while j< len(haystack)- len(needle)+1:

            if haystack[j: j+len(needle)] != needle[0:len(needle)]:
                j += 1
            else:
                return j
            
        return -1