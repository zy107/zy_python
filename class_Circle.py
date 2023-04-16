class Circle:
    def __init__(self):
        self.center = (0, 0)
        self.radius = 0

    def SetCenter(self, x, y):
        self.center = (x, y)

    def SetRadius(self, r):
        self.radius = r

    def PrintInfo(self):
        x, y = self.center
        print('x=%.2f,y=%.2f,r=%.2f' % (x, y, self.radius))

    def GetArea(self):
        return 3.14 * self.radius ** 2

if __name__ == '__main__':
    c = Circle()  # 创建Circle类对象c
    x = eval(input())  # 输入圆心的x坐标
    y = eval(input())  # 输入圆心的y坐标
    r = eval(input())  # 输入半径
    c.SetCenter(x, y)  # 设置圆心
    c.SetRadius(r)  # 设置半径
    c.PrintInfo()  # 输出圆的圆心和半径信息（均保留2位小数）
    print('%.2f' % c.GetArea())  # 输出圆的面积（保留2位小数）