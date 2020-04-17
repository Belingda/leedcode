# -*- coding: gbk -*-
class Solution:
	def removeOuterParentheses(self, S: str) -> str:
		tempstack = []
		level = 0
		L=0
		popindexs = []
		for i,c in enumerate(S):
			if c == "(":
				if L == 0:
					popindexs.append(i)
				L += 1
			else:
				L -= 1
				if L == 0:
					popindexs.append(i)
		for index,c in enumerate(S):
			if index in popindexs:
				continue
			tempstack.append(c)
		return ''.join(tempstack)



class Solution2:
	def removeOuterParentheses(self, S: str) -> str:
		res = []
		L=0
		for i,c in enumerate(S):
			if c=="(":
				L+=1
				if L==1:    # 外层‘(’
					continue
			else:
				L-=1
			if L!=0: # 外层‘)’
				res.append(c)
		return ''.join(res)

ob = Solution2()
print(ob.removeOuterParentheses("(()())(())"))


