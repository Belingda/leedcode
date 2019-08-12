'''
有三个水杯 一个装满水的8品脱的水杯，一个装满5品脱的水杯，一个装满3品脱的水杯，问怎么才能让其中一个水杯
装4品脱的水
'''
import copy
class Cup(object):
	def __init__(self,cuplimit,water):
		self.__m_CupLimit = cuplimit # 只可定义1次 不可修改
		self.m_Water = water

	def GetCupLimit(self):
		return self.__m_CupLimit

class Node(object):
	def __init__(self,data):
		self.m_Data = data


def PourWater(cup1,cup2): # cup1向cup2倒水
	if cup1.m_Water == 0 or cup2.m_Water == cup2.GetCupLimit():# cup1水空或者cup2水满
		return
	tempwater1 = cup1.m_Water
	cup1.m_Water = max(0,cup1.m_Water - (cup2.GetCupLimit() - cup2.m_Water))
	# 8-(5-0) =3  8-3=5
	cup2.m_Water = cup2.m_Water + (tempwater1 - cup1.m_Water)
	# DebugPrint("PourWater (cup1.GetCupLimit()=%s,%s),(cup2.GetCupLimit()=%s,%s)"%
	#            (cup1.GetCupLimit(),cup1.m_Water,cup2.GetCupLimit(),cup2.m_Water))
	return cup1,cup2


class PourSolution(object):
	def __init__(self,aim):
		self.m_ResPossibles = [] # 本次倒水的结果
		self.m_LastPossibles = [] # 记录父结点 （上一次倒水的可能性）
		self.m_AimPinTuo = aim # 要求杯子里达到的水的品脱数

	def IsPourOk(self,cup):
		if cup.m_Water == self.m_AimPinTuo:
			DebugPrint("IsPourOk %s %s"%(cup.m_Water,cup.GetCupLimit()))
			return True
		return False

	def ListPossibleResOnce(self,acup, bcup, ccup):  # 列举单次倒水的可能性
		lst =  [(acup,bcup,ccup),(acup,ccup,bcup),(bcup,acup,ccup),(bcup,ccup,acup),(ccup,bcup,acup),(ccup,acup,bcup)]
		for cups in lst:
			cup1 = copy.deepcopy(cups[0])
			cup2 = copy.deepcopy(cups[1])
			res = PourWater(cup1, cup2)
			if res:
				if self.IsPourOk(cup1) or self.IsPourOk(cup2):
					self.ShowSuccessView(cup1,cup2,cups[2])
					return True
				self.m_ResPossibles.append((cup1, cup2, cups[2]))
				self.ShowView(cup1, cup2, cups[2])

	def ShowSuccessView(self,acup,bcup,ccup):
		print("success (limit=%s:%s),(limit=%s:%s),(limit=%s:%s)"% (acup.GetCupLimit(),acup.m_Water,
		                                                            bcup.GetCupLimit(),bcup.m_Water,
		                                                            ccup.GetCupLimit(),ccup.m_Water))

	def ShowFailView(self,):
		print("Fail")

	def ShowView(self,acup,bcup,ccup,tipmsg="ShowView"):
		print("%s:%s %s %s"%(tipmsg,acup.m_Water,bcup.m_Water,ccup.m_Water))

	def StartPour(self,acup,bcup,ccup):
		self.m_LastPossibles.append((acup,bcup,ccup))
		while len(self.m_LastPossibles)>0:
			possiblenum = len(self.m_LastPossibles)
			for i in range(possiblenum):
				res = self.m_LastPossibles.pop()
				cup1,cup2,cup3 = res
				success = self.ListPossibleResOnce(cup1,cup2,cup3)
				if success:
					return
			self.m_LastPossibles = copy.deepcopy(self.m_ResPossibles)
			self.m_ResPossibles = []
		self.ShowFailView()

def DebugPrint(msg):
	print(msg)


acup = Cup(8, 8)
bcup = Cup(5, 0)
ccup = Cup(3, 0)
solution = PourSolution(4)
solution.StartPour(acup,bcup,ccup)
# todo 用树建立找寻轨迹
# 解决的问题

