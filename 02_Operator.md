# Python Tutorial 2 运算符

索引

1.[](#)


## 算术运算符
算术运算符包括：＋，－，＊，／，％（取模运算符）。整数除法会截断结果中的小数部分，取模运算符一般只用于正整数。

## 布尔类型
在讨论关系运算符之前，先来看看我们还尚未讨论的一种类型：bool（布尔类型），其实它就两个值，分别是**True**和**Fasle**（注意大小写）。

~~~python
if type(True) == type(False):
  print type(True)
# <type 'bool'>

print int(True)
print int(False)
# 1
# 0

print bool(1)
print bool(0)
print bool(-1)
# True
# False
# True

if 0:
  print 0
elif -1:
  print -1
# -1
# 我们从这可以看出，python将0看成False，其它值当成True，但我们一般不这样使用，建议直接使用True与Fasle。
~~~

## 关系运算符
算术运算符包括：>， >=， <， <=， ==和!=，分别的意思是大于，大于等于，小于，小于等于，等于和不等于。用关系运算符进行运算的表达式称为关系表达式，其结果为布尔值。

~~~python
print 1 > 1
# False
print 1 <= 1
# True
print 1001 == 1000+1
# True, 这里会将其当作数值来进行对比，而不是对象id
print 1 != 1001-1000
# False
~~~

## 逻辑运算符
逻辑运算符包括：and（与，C语言中的&&），or（或，C语言中的||），not（非，C语言中的！）。逻辑运算符是对布尔值进行运算，其结果也为布尔值。

~~~python
print True and True
# True, and要同时True其结果才为True
print True and False
# False
print False or False
# False, or要同时为False其结果才为False
print False or True
# True
print not True
# False
print not False
# True
~~~

接下来我们使用2个带有副作用的布尔值（借助尚未学到的函数来实现这个功能）来试验and与or的处理机制：

~~~python
# 定义两个函数，在取它返回值的时候，它会进行一个额外的操作，在这里我们暂时使用打印函数名这样的操作
def TrueMethod():
  print "TrueMethod"
  return True
def FalseMethod():
  print "FalseMethod"
  return False

print TrueMethod() and FalseMethod()
# TrueMethod
# FalseMethod
# False
print FalseMethod() and TrueMethod()
# FalseMethod
# False
# and 在判断第一个条件失败的时候就不继续进行后续判断了，俗称“短路与”

print FalseMethod() or TrueMethod()
# FalseMethod
# TrueMethod
# True
print TrueMethod() or FalseMethod()
# TrueMethod
# True
# or 在判断第一个条件成功时候就不继续进行后续判断了，俗称“短路或”
~~~

## 运算符优先级与小括号
所有的运算符，都有它各自的优先级，就拿处于同一级别的算术运算符加减乘除这几个操作来说，我们都知道在同时含有这几个运算符的时候，先算乘除，后算加减，同级的从左向右一次进行运算。而这些运算符的优先级与它本身的运算规则是比较相符的，比如同时含有关系运算符与算术运算符时，表达式看起来时长这样的：

~~~python
print 1 + 4 > 2 * 3
# False, 结果是布尔值说明关系运算符大于号是最后运算的

# 我们借助小括号来改变运算顺序来看看结果如何
print 1 + (4 > 2) * 3
# 4, 再次验证了我们上述的推测， 算术运算符的优先级是高于关系运算符的大于号（同级的运算符大多优先级差不多）

# 如果我们想提高可读性我们应该这样来写
print 1+4 > 2*3
# False
~~~

假如，我们在编程过程中，实在不清楚几个运算符的优先级，又懒得打开控制台去试验一下（当然我是非常不支持你去记的，日常使用中熟悉即可，不需强记），我们可以通过牺牲一点点的优雅来提高一点点可读性来解决这样的问题：

~~~python
print (1+4) > (2*3)
~~~

## 拓展_按位运算符
按位运算符包括：&（按位与），｜（按位或），^（按位异或）。与？或？听起来感觉与上面的逻辑运算符有些联系，事实上确实是有点点接近。你是否还记得第一章中的类型比较那里讲的一个字节是由8位（bit）组成，按位运算符的处理对象就是这些位上的数据，也就是0，1这2个值。一般情况下两个操作数为整数。
如果拿两个数值进行按位运算，那么其实是将这两个数值各个对应位（bit）上的值进行按位运算，然后再汇总结果。

~~~python
# 按位与：只有两个位上的值同为1结果的相应位上的值才为1
print bin(0b1010&0b1101)
# 0b1000

# 按位或：只有两个位上的值同为0结果的相应位上的值才为0
print bin(0b1010|0b1001)
# 0b1011

# 按位异或：只有两个位上的值异同结果的相应位上的值才为1
print bin(0b1010^0b1001)
# 0b11
~~~

除了上面的运算符之外，还有两个相对比较好理解的：<<（左移）， >>（右移）。换言之便是将所有位向一个方向移动一定位数，左移空出的位置补0，右移多余的位置舍去：
~~~python
print bin(0b11<<3) # 3 * 2^3 == 24
# 0b11000
print bin(0b11000>>4) # 24 / 2^4 == 1 (舍去一个1)
# 0b1
~~~

那么，这些操作符一般情况下是如何使用的呢？在一些资源很紧张的场景中（比如游戏服务器），存储一些可列举的情况（性别为男、女可占一位，年龄段分幼儿、青年、成年、老年可用两位表示，高矮一位，胖瘦一位等），在一个字节里就能存储不少于一个的信息，减少了数据占用（磁盘读写），带宽消耗（网络传输），起到了非常重要的作用。我们来看看在代码中该如何表示：
~~~python
# 一般用全大写字母表示一个常量，即这个名字就对应某个固定值，不会再更改了
SEX_FEMALE = 0b0   # 0, 女性
SEX_MALE   = 0b1   # 1, 男性
SEX_MASK   = 0b0001   # 性别掩码，用于识别性别这个属性是具体在哪个位置，这里便指明了在最后一位

AGE_CHILD  = 0b00  # 0, 幼儿
AGE_YOUNG  = 0b01  # 1, 青年
AGE_ADULT  = 0b10  # 2, 年长
AGE_OLDER  = 0b11  # 3, 老年
AGE_MASK   = 0b0110   # 年龄掩码

HEIGHT_TALL  = 0b0  # 0, 高
HEIGHT_SHORT = 0b1  # 1, 矮
HEIGHT_MASK  = 0b1000  # 身高掩码
# 常量定义完毕，我们这里暂时只用最后4位

person_attribute = 0 # 定义一个人物的属性值，在这里我们单单只抽出一个值出来，不分析其它上下文数据
# 定义一个矮的青年男生，用 按位或 来进行组合操作
person_attribute = person_attribute | (HEIGHT_SHORT<<3) | (AGE_YOUNG<<1) | (SEX_MALE<<0)
print bin(person_attribute)
# 0b1011

# 取值， 先进行掩码操作掩去多余的数据，然后在移位去掉多余的0，移位的多少可以参考掩码后面0的个数
# 性别
print bin((person_attribute & SEX_MASK) >> 0)
# 0b1， 男

# 年龄
print bin((person_attribute & AGE_MASK) >> 1)
# 0b1， 青年

# 身高
print bin((person_attribute & HEIGHT_MASK) >> 3)
# 0b1， 矮
~~~

``
那么问题来了，上面代码的右移位数是直接使用的常量，这样不利于理解与后期更新维护，要怎么将其封装才会比较好呢？
``

哦，我们好像还少了个按位异或操作符，这个是拿来做什么用的呢？

~~~python
# 不用第三个变量交互两个整数的值
x = 123
y = 456
x = x ^ y
y = x ^ y
x = x ^ y
print x, y
# 456 123

a = 123
b = 456
print a ^ b
# 435, 看不出什么意义

print a ^ b ^ b
# 123, 咦，变回a本身了，那么如果一个函数的功能是将一个值（不一定是单个字节的整数，也有可能是好几个字节的字符串数据）进行第一次异或，那么出来的数据谁都认不出来，等第二次调用同样的函数，它就恢复了原数据的样貌，这就实现了一个简陋的客户端、服务器公用的加密函数，加密过的数据在网络传输过程中即使被截取也不会造成内容泄露。如果要对该函数进行升级，可以根据每个不同位置的数据来对一个不同的值进行异或，这时候就需要一系列的用来被异或的数据；或者，在原来的数据上，加上一个固定的数值，比如1，再进行异或等等一系列的变化，有兴趣的同学请自行查阅资料。
~~~



end
