class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        freq = {}

        # Count characters of s
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Remove characters using t
        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False

        return True
        
        