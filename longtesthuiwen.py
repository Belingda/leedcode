class Solution(object):
    def longestPalindrome(self, s):
        lst=list(s)
        length=len(lst)
        for i in xrange(length):
            lst.insert(2*i,'#')
        lst.append('#')
        s=''.join(lst)
        maxs=""
        for i in range(len(s)):
            temps=self.findPalindromeLen(s,i)
            if len(temps)>len(maxs):
                maxs=temps
            
        maxs=maxs.replace('#','')
        return maxs
    def findPalindromeLen(self,s,pos):
        if pos==0 or pos==len(s)-1:
            return ""
        start=pos-1
        end=pos+1
        for i in range(len(s)):
            if start<0 or end>=len(s):
                return s[start+1:end]
            if s[start]==s[end]:
                start-=1
                end+=1
            else:
                return s[start+1:end]

ob=Solution()
print ob.longestPalindrome("babad")



                
        
        