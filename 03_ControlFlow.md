# Python Tutorial 3 控制流

索引

1.[](#)


## 跳转
#### if 语句
if语句有三部分组成，if关键字，用于进行判断的布尔值与一个普通的代码块，当布尔表达式的值为True时（如果你采用一个非0的数值，那么python会将其看成True），将执行该代码块。
~~~python
if 123 < 321:
  print "123 < 321 !"

if __name__ == '__main__': # 这是个含有特别意义功能的代码片段，有兴趣的同学自行理解
  print "hello world!"
~~~

#### else 语句
else语句与if语句有比较明显的一点不同的是，它不能单独使用，需要配合if语句一起使用，else语句由else关键字和一个普通的代码块组成。当if-else语句出现的时候，程序先对if的表达式进行判断，如果成功则执行if语句的代码块，否则则直接执行else语句的代码块。
~~~python
if 1+1 == 3:
  print "1+1 == 3"
  print "1+1 == 3, again!" # 通过缩进来区分是否属于同一代码块
else:
  print "1+1 != 3"
  print "1+1 != 3, again..."
~~~

#### 让我们来举个看起来简单的栗子
随机生成一个工作日，周一到周日，如果是周一的话打印"Monday", 周二的话打印"Tuesday",其余日前打印其普通数字即可，周日为0:
~~~python
import random

day = random.randint(0, 6) # 随机产生一个0-6的整数

if day == 1 or day == 2:
  if day == 1:
    print "Monday"
  else:
    print "Tuesday"
else:
  print day
~~~

这样的代码看起来似乎很正常，但好像又感觉哪里不对，因为周一与周二的判断多了一步，有一点重复的样子。

#### elif 语句
elif， 即else-if的意思，与else一样需要配合if一起使用，同一个if语句中允许出现多个。它有个一个跟if语句一样的逻辑表达式，用于判断逻辑是否为True来确定是否执行其代码块。
借助这个语句，我们来调整下上一小结的代码：
~~~python
import random

day = random.randint(0, 6)

if day == 1:
  print "Monday"
elif day == 2:
  print "Tuesday"
else:
  print day
~~~

#### pass 语句
pass语句即是空语句，因为python是通过缩进来区分代码块的，不像其它语言用大括号或分号，如果你在一个需要有代码块的地方不想执行任何操作，那就需要使用pass语句了。
我们来继续修改上述题目，加上一个“不打印周三的条件”：
~~~python
import random

day = random.randint(0, 6)

if day == 1:
  print "Monday"
elif day == 2:
  print "Tuesday"
elif day == 3:
  pass
else:
  print day
~~~

## 循环
#### while 循环
while语句与if语句相似，同一由三部分组成，while关键字，用于进行判断的布尔值与一个普通的代码块，当用于判断的表达式为True时，则执行代码块，然后再次重复对该表达式进行判断，否则则完全退出while循环。这里要注意的是，每次循环前都会对while语句的逻辑表达式进行判断，所以如果该表达式的结果是不变的，每次都是True的话，那么就进入了死循环，这时就得依赖其它语句来退出死循环了。

举个栗子：
~~~python
# 打印 5 次 “hello world”
count = 0
while count < 5: # 一个结果可变的表达式，当count为0，1，2，3，4时，表达式为True，当第六次对该表达式进行判断时，count已经等于5，则退出循环
  print "hello world!", count
  count += 1     # 更新计数以改变表达式的结果
print "hi"
~~~

#### break 语句
break语句可以直接结束当前循环，执行循环之后的语句：
~~~python
# 打印 5 次 “hello world”
count = 0
while count < 5:
  if count == 3:
    break     # 当循环执行到第4次的流程的时候，强制结束该循环
  print "hello world!", count
  count += 1
print "hi"
~~~

#### continue 语句
continue语句可以结束当前循环的当前执行流程，然后执行下一个流程：
~~~python
# 打印 5 次 “hello world”
count = 0
while count < 5:
  if count == 3:
    break     # 当循环执行到第4次的流程的时候，强制结束该循环
  elif count == 1:
    continue
  print "hello world!", count
  count += 1
print "hi"
~~~

``
运行上面的代码你有没有发现出现了什么问题，是不是卡住不会继续往下运行了？尝试下自行进行定位问题所在并进行修改。
``




end
