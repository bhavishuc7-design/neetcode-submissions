class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        res = ""
        for ch in s:
            if ch.isalnum():
                res+=ch.lower()
        n = len(res)
        left = 0
        right = n-1
        while left < right:
                if res[left]!=res[right]:
                    return False
                left+=1
                right-=1
        return True
        