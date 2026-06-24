class Solution(object):
    def rotateString(self, s, goal):
       if len(s) != len(goal):
         return False
       
       
       str = s+s
       if goal in str:
            return True
        
       return False
