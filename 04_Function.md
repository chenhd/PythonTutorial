# Python Tutorial 4 函数

索引

1.[函数的作用](#函数的作用)  
2.[函数的交互](#函数的交互)  
3.[函数的调用](#函数的调用)  
4.[拓展_高阶函数](#拓展_高阶函数)  

## 函数的作用
我们时常会听到，某个成熟的软件项目代码行数达到了上百万的级别，如果这些代码全都在一个源文件之中，那人们每次对其进行编辑的时候光打开就需要消耗相当的时间。除了这个问题之外，还会出现其他更多的一些问题，比如：
+ 所有的逻辑代码混合在一起，可读性极差，每次阅读代码都会十分痛苦；
+ 各种各样的计算都需要用到大量的临时变量来存储，使得变量命名较为容易发生混乱；
+ 如果只有一份文件，那么多人进行协同开发听起来更像是天方夜谭；
+ 在进行debug调试的时候，如此巨大的代码量会让人无从下手。

所以，一种对代码进行抽象的封装技术便不可或缺了--函数。

首先，如果让我们打印一首辛弃疾的词，我们在学习完前面的内容之后可以这样：

~~~python
print "丑奴儿·书博山道中壁"
print "少年不识愁滋味，爱上层楼。"
print "爱上层楼，为赋新词强说愁。"
print "而今识尽愁滋味，欲说还休。"
print "欲说还休，却道天凉好个秋。"
~~~

那么，假如让我们打印两次的话，为了完成预期的目标我们可以对这5行代码进行Ctrl+c、Ctrl+v，但这样做的话或许会发现有的地方不对劲，上面这5行代码之间是各个独立的个体，写完之后，它们仍是互相独立，无任何关联，也就无法在第二个需要这段代码的地方方便地进行复用。如果说，一个工程中成千上万个重复的小功能每次编写都是重新地写代码、复制代码，这显然是不可接受的。

为了克服上述的困难，我们可以对这5行代码进行抽象，将其封装成一个函数，然后对该函数进行调用。这样一来，我们就实现了对代码块复用，并且，还可以看出来该程序对这整个代码块执行了2次，提高了代码的**可读性**：

~~~python
def print_XinQiji_SongPoems():
    print "丑奴儿·书博山道中壁"
    print "少年不识愁滋味，爱上层楼。"
    print "爱上层楼，为赋新词强说愁。"
    print "而今识尽愁滋味，欲说还休。"
    print "欲说还休，却道天凉好个秋。"

print_XinQiji_SongPoems()
print_XinQiji_SongPoems()
~~~

## 函数的交互
如果函数只是简单地对多行代码进行封装的话，那还不足以解决我们一开始提出的诸多问题，我们还需要与函数进行交互，这样才能够进行数据交换，从而进行一系列更加复杂的数据操作。

一般情况下，函数有任意数量的输入，称为函数参数，和一个输出，称为返回值。在进行函数调用的时候，外部通过传递参数给函数，函数执行完毕后返回一个返回值，至此完成函数的调用。

~~~python
# question: 计算两个数的平方和？

# 1.定义一个计算平方的函数
def square(num):
    tmp = num * num
    print "call square and in: ", num, " and out : ", tmp
    return tmp

# 2.计算两个数的平方和
def sum_of_square(a, b):
    sum = square(a) + square(b)
    print "call sum_of_square and in: ", a, b, " and out : ", sum
    return sum

sum_of_square(3, 4)
# call square and in:  3  and out :  9
# call square and in:  4  and out :  16
# call sum_of_square and in:  3 4  and out :  25
# 25
~~~

上述代码定义了一个sum_of_square函数并对其进行了调用，为了方便我们的理解，我们尝试使用一种“代换模型”来看看上述代码在去掉函数调用的结构是长什么样的，并且，还会去掉用于帮助理解的打印语句。

~~~python


# 原始
sum_of_square(a, b)

# 第一次代换
square(a) + square(b)

# 第二次代换
a*a + b*b

# 把a=3和b=4代换进去得出结果
# 9 + 16
25
~~~

需要特别说明的是，“代换模型”并不是实际计算机的工作方式，只是一种方便我们理解的模型，因为往往计算机会对代码进行复杂的优化步骤，经过优化之后的代码逻辑会与原先的有所不同，并且，我们会在后文讨论到代换还有一个地方无法直接代换--**递归函数**。

``
question:那么问题来了，第一节中的print_XinQiji_SongPoems函数并没有return一个值，这个属于什么情况？
``


## 函数的调用
我们在执行单个python脚本文件的时候，是按照先后顺序执行每一行代码，这个文件则被看作是一个模块，模块名为不带拓展名的文件名。

在定义顶层变量的同时，这些变量组成了一个上下文环境（context），由于python语言是跟进缩进层次来分辨层次，这里的顶层可以看成是没有任何缩进的定义语句，处在函数之中定义的变量不属于顶层变量。

我们定义一个变量的时候，程序会在context创建这个变量，当需要使用这个变量的时候，则会在context中进行查找，如果查找不到，便会出现变量未定义的运行时错误，所以，变量一定要**先定义，后使用**。

~~~python
a = 1
b = a
~~~
``
question:那么问题来了，上述代码中的两个a具体是指什么，第一个a跟第二个a是一个含义吗？请自行理解下左值与右值。
``

因为，函数也是一种对象，定义函数的时候就相当于定义了一个函数的变量，（注意这里用的是定义这个词，由于python是不用进行类型声明的，所以，声明与定义是同时发生的，声明了有这样的一个变量，这个变量的内容被定义成了什么。）我们无法在函数定义完成之前对其进行调用。在这里，函数跟数据之间的关系开始变得有点模糊了。

~~~python
a()
def a():
    pass

# NameError: name 'a' is not defined
~~~


接着，我们来考虑一种特殊一点的情况，函数间的互相调用：
~~~python
def a(a_num):
    if a_num == 3:
        return
    print a_num
    
    b(a_num)
    

def b(b_num):
    b_num += 1
    print b_num
    print '-' * 10
    
    a(b_num)

a(1)

# 1
# 2
# ----------
# 2
# 3
# ----------

# 接着还可以考虑下递归函数：函数在自己的定义过程中对自身进行了调用
def c(c_num):
    print c_num
    c(c_num+1)
c(c_num)
~~~

在上述代码中，a函数中调用了b函数，而在这行代码之前b函数还未进行定义，似乎与我们之前所说的有点矛盾。但这里其实是与函数的定义机制有关，当我们定义一个函数的时候，python会先声明有这样一个函数，此时并未完成定义，而是会在我们调用的动作实际发生之前完成其定义，这种机制类似于前向声明，指的是声明标识符的时候没有给出完整的定义。所以我们前面在函数定义之前直接调用该函数会出现错误，因为这是实实在在的调用，而函数定义的代码中的进行对其它函数进行调用，实际上还未发生。

而这种递归或互相调用的函数，并不能跟之前的代换模型所说的那样直接把代码代换进去，因为这会无穷无尽，所以需要一点修改，在代换的时候也把参数也一起代换进去。

``
tip:程序执行过程中，函数调用实际上通过一种程序栈的形式实现的，栈指的是一种模式，像汉诺塔那样，后进先出，最后放进来的盘子一定要最先拿出去，在层层连续的函数调用中，最后一个调用的函数一个要先返回，才会将控制权随着返回值回到上一层函数接着执行后续的指令，因为后进先出，所以调用下一个函数的时候，直接占用原先调用过的函数的地址，也就覆盖了上面的数据，因此函数中的数据就变成了临时的数据，也就解决了变量名混乱的问题，具体的内容请自行网上查找资料，此次不在赘述。
``


## 拓展_高阶函数
在程序设计过程中，如果将函数限制为只能以数值作为参数的化，那会严重地限制我们建立抽象的能力，经常有一些同样的程序设计模式能用于若干不同的过程，为了能把这种模式描述为相应的概念，我们需要构造一种将函数作为参数，或是以函数作为返回值的函数，这种能操作函数的函数称为高阶函数。

~~~python
# question:
# 数值：1 + 2
# 字符串："1" + "2"
# 罗马数值："I" + "II"

# 普通做法：
def add_num(a, b):
    return a+b
num_a = 1
num_b = 2
tmp = add_num(num_a, num_b)
print type(tmp), tmp


def add_str(a, b):
    return str(int(a)+int(b))
str_a = "1"
str_b = "2"
tmp = add_str(str_a, str_b)
print type(tmp), tmp


Roman2Int = {
             "I"   : 1,
             "II"  : 2,
             "III" : 3,
             }
Int2Roman = {
             1 : "I",
             2 : "II",
             3 : "III",
             }
def add_Roman(a, b):
    tmp = Roman2Int[a] + Roman2Int[b]
    return Int2Roman[tmp]
Roman_a = "I"
Roman_b = "II"
tmp = add_Roman(Roman_a, Roman_b)
if ord(tmp[0]) >= ord('0') and ord(tmp[0]) <= ord('9'):
    print type(tmp),
else:
    print "<type 'Roman'>",
print tmp



# 抽象做法：
# 我们先借助上面已实现好的具体的加法操作
def add_num(a, b):
    return a+b

def add_str(a, b):
    return str(int(a)+int(b))

Roman2Int = {
             "I"   : 1,
             "II"  : 2,
             "III" : 3,
             }
Int2Roman = {
             1 : "I",
             2 : "II",
             3 : "III",
             }
def add_Roman(a, b):
    tmp = Roman2Int[a] + Roman2Int[b]
    return Int2Roman[tmp]
# 构造一个通用接口，调用一个实施具体加法操作的高阶函数，方便提供给用户使用
def print_add_result(a, b):
    res = None
    res_type = None
    if type(a) == type(0):
        res = add(add_num, a, b)
        res_type = type(res)
    elif type(a) == type(''):
        if ord(a[0]) >= ord('0') and ord(a[0]) <= ord('9'):
            res = add(add_str, a, b)
            res_type = type(res)
        else:
            res = add(add_Roman, a, b)
            res_type = "<type 'Roman'>"
    
    print res_type, res
# 实际执行加法的高阶函数
def add(function, a, b):
    return function(a, b)

print_add_result(1, 2)
print_add_result("1", "2")
print_add_result("I", "II")
# <type 'int'> 3
# <type 'str'> 3
# <type 'Roman'> III

# 这样的做法方便用于对函数在不同层面的使用进行抽象，在用户使用接口的层面能够容易的进行新方式的加法功能的拓展，在具体实现的接口能够统一的为同一个操作（这里是加法这个操作）进行修改。

# 比如为加法功能添加一个log
def add(function, a, b):
    print a, "add", b, "produce", function(a, b)
    return function(a, b)
# 1 add 2 produce 3
# <type 'int'> 3
# 1 add 2 produce 3
# <type 'str'> 3
# I add II produce III
# <type 'Roman'> III

~~~


参考：SICP

end
