class Solution(object):
    def lengthOfLongestSubstring(self, s):
       ans = 0 
       for i in range (len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] not in seen:
                seen . add(s[j])
                ans = max(ans, len(seen))

            else:
                break
       return ans 
        