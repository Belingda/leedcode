class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        
        left=1
        right=x
        while(right>1):
            num=(left+right)/2
            temp=num*num
            if temp<=x:
                if temp==x:
                    return num
                if pow(num+1,2)>x:
                    return num
                else:
                    left=num+1
            else:
                right=num-1

ob=Solution()
print(ob.mySqrt(9))
print(ob.mySqrt(4))
print(ob.mySqrt(2))
print(ob.mySqrt(36))
              
      