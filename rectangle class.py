#3.编程计算矩形的类，构造函数初始化矩形的长和宽，并使用方法计算面积和周长。通过对象调用。
#定义子类正方形，利用构造函数初始化正方形边长，并计算面积和周长
class Juxing():
    def __init__(self,chang,kuan):
        self.chang=chang
        self.kuan=kuan
    def zhouchang(self):
        return (self.chang+self.kuan)*2
    def mianji(self):
        return self.chang*self.kuan
class Square(Juxing):
    def __init__(self, side):
        super().__init__(side, side)
juxing=Juxing(4,5)
s=juxing.mianji()
c=juxing.zhouchang()
square=Square(5)
print(square.mianji())