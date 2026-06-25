class Solution(object):
    def backspaceCompare(self, s, t):
       i = len(s) - 1
       j = len(t) - 1
       while i >= 0 or j >= 0:

        skips=0
        while i >= 0:
            if s[i] == '#':
                skips += 1
                i -= 1
            elif skips > 0:
                skips -= 1
                i -= 1
            else:
                break

        skipt =0
        while j >= 0:
            if t[j] == '#':
                skipt += 1
                j -= 1 
            elif skipt > 0:
                skipt -= 1
                j -= 1
            else:
                break

        if i >= 0 and j >= 0:
            if s[i] != t[j]:
              return False
        elif i >= 0 or j >= 0:
            return False

        i -= 1
        j -= 1
       return True
        