class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted=''
        for char in s.lower():
            if ord(char) in range(97,123) or ord(char) in range(47,58):
                converted+=char
        n=len(converted)
        l,r=0,n-1
        for i in range(n//2):
            print("Entering Loop")
            if converted[l+i]!=converted[r-i]:
                print("Checking {} and {}".format(converted[l+i],converted[r-i]))
                return False
        return True
        