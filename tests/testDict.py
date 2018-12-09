"""
文法的测试
"""

g=dict()
g['S1']=['E']
g['E']=['aA',  'bB']
g['A']=['cA', 'd']
g['B']=['cB',  'd']

allValue=g.values()
#allValueList=list()
#allValueList=allValueList.add(i) for i in dict_values
allValueList=list(allValue)
print(allValueList)
l=len(allValueList)
print(l)
newList=list()
for i in range(l):
    newList+=allValueList[i]
print(newList)
print(len(newList))
