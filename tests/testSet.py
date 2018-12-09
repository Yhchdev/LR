"""
测试集合在不断更新时，如何进行有效的循环遍历
方案1：
set1=set([1, 2, 3])
print(set1)
for i in set1:
    print(i)
    set1.add(4)
这种方案不可行，会抛出异常

方案2：
子集合，然后并起来
好像可以
"""

#test1
set1=set([1, 2, 3])
print(set1)
for i in set1:
    print(i)
    #set1.add(4)
