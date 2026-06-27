class Solution(object):
    def lengthOfLongestSubstring(self, s):
    #    ans = 0 
    #    for i in range (len(s)):
    #     seen = set()
    #     for j in range(i, len(s)):
    #         if s[j] not in seen:
    #             seen . add(s[j])
    #             ans = max(ans, len(seen))

    #         else:
    #             break
    #    return ans 
        seen = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            ans = max(ans, right - left + 1)

        return ans