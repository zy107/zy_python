#五、多态：+单继承
#编写程序实现乐手弹奏乐器。乐手可以弹奏不同的乐器从而发出不同的声音。可以弹奏的乐器包括二胡、钢琴和琵琶。
# 实现思路及关键代码：
# 1)定义乐器类Instrument，包括makeSound()方法，此方法中乐器声音："乐器发出美妙的声音！"
# 2)定义乐器类的子类：二胡Erhu、钢琴Piano和小提琴Violin
#     二胡Erhu声音："二胡拉响人生"
#     钢琴Piano声音："钢琴美妙无比"
#     小提琴Violin声音："小提琴来啦"
# 3）用多态的方式对不同乐器进行切换
class yueqi:
    def fs(self):
        print("乐器发出美妙的声音")
class erhu(yueqi):
    def fs(self):
        print("二胡拉响人生")
class Piano(yueqi):
    def fs(self):
        print("钢琴美妙无比")
class Violin(yueqi):
    def fs(self):
        print("小提琴来啦")
def music(object):
    object.fs()
eh = erhu()
po = Piano()
vl = Violin()
music(vl)
music(po)
music(eh)
