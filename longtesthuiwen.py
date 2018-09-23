#coding=utf-8
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
#动态规划方法
#去除重复计算
#时间效率和上面的差不多
class Solution2(object):
    def longestPalindrome(self, s):
        temp=[[False for _ in xrange(len(s))] for _ in xrange(len(s))]
        if len(s)>0:
            maxs=s[0]
        else:
            maxs=""
        for j in xrange(1,len(s)):
            for i in xrange(0,j):
                if s[i]==s[j] and (j-i<=2 or temp[i+1][j-1]==True):
                    temp[i][j]=True
                    if j-i+1>len(maxs):
                        maxs=s[i:j+1]
        return maxs        
        

ob=Solution2()
print ob.longestPalindrome("cababad")




                
        
        