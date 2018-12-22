from dataStructure import Grammar
"""
先搭建一个基本框架
Author:Jipeng Zhang
Time:2018/12/9
"""

"""
2.产生式变项目：
只需保存点的位置即可
入口参数：一个文法对象，为dataStructure.py中实现的

思考如何保存出口参数：
对于文法:g['S']=['E']
g['E']=['aA', 'bB']
记录点的位置就是记录：'E',‘aA','bB'的长度
也是用词典保存,故出口参数为形如下述词典
dotLocation['S']={'E':1}
dotLocation['E']={'aA':2, 'bB':2}
"""
def grammarToItem(grammar):
    '''产生式变项目\n返回字典[leftS1:[rightS1:len,rightS2:len...], ...]'''
    dotLocation = grammar.g.fromkeys(grammar.g.keys())
    for eachGrammar in dotLocation.keys():
        d = dict.fromkeys(grammar.g[eachGrammar])
        for delem in d.keys():
            d[delem] = len(delem) 
    return dotLocation
    
"""
3.构造项目集规范族：
3.1求闭包
3.2保存GOTO函数
"""

"""
3.1构造闭包

入口参数：
1.一个文法对象grammar  
2.文法产生式左部：’S'，为一个String,长度为1
3.grammar[‘S']为一个list,此参数记录产生式右部在list中的下标，为一个int
4.项目中点的位置，为一个int
"""
def Closure(grammar,  leftString,  rightSubscript,  dotLocation):
    closure = list(grammar.g[leftString][rightSubscript])
    old = list()
    while old != closure:
        old = closure
        pass
    pass
    
"""
3.2Canonical Collection:项目集规范族
GOTO函数的产生在此过程中
入口参数：
1文法
2dotLocation
需要使用闭包函数
出口参数：
1一个集合，此集合的元素为各个状态
2一个词典，保存GOTO函数形如：Go['I0']={'E':'I1'}表示GO('T0', 'E')=I1

伪代码如下：
for set2 不为空：  这个就是判断是否构建完成的条件
    set1=set1并set2
    for i in set1:
        假设I0产生了3个状态：将他们保存到set2中
        假设I1产生了3个状态，也将其保存到set2中
        其中需要注意查重，不仅在set2中差也要在set1中查
最后的set1即为所有状态，不要忘记在其中保存GOTO
"""

def CanonicalCollection(grammar,  dotLocation):
    goto = dict()
    Closure(grammar,  'S',  0,  dotLocation)
    pass
    
"""
4.分析表的构造
出口参数：此出口参数也是前端需要显示的
考虑数据结构：
1.Action子表，形如：
Action[0]={'a':'si', 'b':xx, 'c':xx}
2.GoTo子表，形如：
GoTo[0]={'E':xx, 'A':xx}

入口参数：
1.文法
2.状态集合set1
3.GOTO词典
"""
def AnalyticalStatement(grammar,  set1,  goto):
    pass
    
"""
5.分析栈的形成
入口参数：
1.语法形如：abc
2.Action子表
3.GoTo子表
4.文法

出口参数：
1.状态栈所形成的记录，使用String保存
2.符号栈所形成的记录，使用String保存
3.输入串栈所形成的记录，使用String保存
均为了前端显示方便。
"""

def LRAnalysis(grammar):
    CanonicalCollection(grammar, grammarToItem(grammar))
    pass


if __name__=="__main__":
    g=Grammar("S-->E\n\
               E-->aA|bB\n\
               A-->cA|d\n\
               B-->cB|d\n")
    g.showGrammar()
    LRAnalysis(g)
