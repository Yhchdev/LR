"""
Author:Jipeng Zhang
Time:2018/12/9
"""


"""
1.首先考虑文法保存方式：
基本思路为使用词典
考虑前端传过来什么数据？
s1-->E
E-->aA|bB
"""
import pprint


class Grammar():
    '''文法的数据结构
       形如“a->b|c”'''
    def __init__(self,  grammarText):
        """
        假设前端传来只有一个字符串，该字符串包含所有文法
        则：self.g中保存初步处理后的文法为dict()
        """
        self.g=dict()
        #需要去掉最后一个空行，所以[0:-1]
        grammars=list(grammarText.split("\n"))[0:-1]
        for eachGrammar in grammars:
            location=eachGrammar.find("-->")
            self.g[eachGrammar[0:location]]=list(eachGrammar[location+3:].split('|'))

    def showGrammar(self):
        print(self.g)

if __name__=="__main__":
    g=Grammar("S-->E\n\
               E-->aA|bB\n\
               A-->cA|d\n\
               B-->cB|d")
    g.showGrammar()
   #with open('tests/test1.txt',  'r') as f:
       #g=Grammar(f.read())
       #g.showGrammar()
