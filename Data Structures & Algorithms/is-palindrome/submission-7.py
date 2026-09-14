class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_len = len(s)
        l=0
        r= str_len -1

        while l<=r:
            if not s[l].isalnum() :
                l = l+1
            elif not s[r].isalnum():
                r -=1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False 
        return True
        